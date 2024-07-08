import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'virtual_router.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def virtual_router():
    # Create a Mininet object
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add a remote controller
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add hosts and switch
    info('*** Adding hosts and switch\n')
    logging.info('Adding hosts and switch')
    h1 = net.addHost('h1', ip='10.0.1.1/24')
    h2 = net.addHost('h2', ip='10.0.2.1/24')
    h3 = net.addHost('h3', ip='10.0.3.1/24')
    h4 = net.addHost('h4', ip='10.0.4.1/24')
    r1 = net.addHost('r1')
    s1 = net.addSwitch('s1')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.addLink(r1, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure the router
    info('*** Configuring the router\n')
    logging.info('Configuring the router')
    r1.cmd('ifconfig r1-eth0 10.0.1.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1 10.0.2.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth2 10.0.3.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth3 10.0.4.254 netmask 255.255.255.0')
    r1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    h1.cmd('route add default gw 10.0.1.254')
    h2.cmd('route add default gw 10.0.2.254')
    h3.cmd('route add default gw 10.0.3.254')
    h4.cmd('route add default gw 10.0.4.254')

    # Test connectivity
    info('*** Testing connectivity\n')
    logging.info('Testing connectivity')
    result = net.pingAll()
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
    virtual_router()

