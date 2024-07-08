import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'vnf_integration.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def vnf_integration():
    # Create a Mininet object
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add a remote controller
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add hosts and switch
    info('*** Adding hosts and switch\n')
    logging.info('Adding hosts and switch')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    vnf1 = net.addHost('vnf1')
    s1 = net.addSwitch('s1')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(vnf1, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure VNF integration
    info('*** Configuring VNF integration\n')
    logging.info('Configuring VNF integration')
    vnf1.cmd('ifconfig vnf1-eth0 10.0.0.3 netmask 255.255.255.0')
    h1.cmd('route add default gw 10.0.0.3')
    h2.cmd('route add default gw 10.0.0.3')
    vnf1.cmd('iptables -t nat -A POSTROUTING -o vnf1-eth0 -j MASQUERADE')
    vnf1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    # Test connectivity through VNF
    info('*** Testing connectivity through VNF\n')
    logging.info('Testing connectivity through VNF')
    result = net.ping([h1, h2])
    logging.info(f'Ping result: {result}')

    # Open the Mininet CLI for interactive commands
    info('*** Running CLI\n')
    CLI(net)

    # Stop the network
    info('*** Stopping network\n')
    logging.info('Stopping network')
    net.stop()

if __name__ == '__main__':
    # Set the logging level to 'info' and run the script
    setLogLevel('info')
    vnf_integration()

