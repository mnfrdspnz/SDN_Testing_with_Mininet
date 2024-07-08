import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'virtual_firewall.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def virtual_firewall():
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
    firewall = net.addHost('firewall')
    s1 = net.addSwitch('s1')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(firewall, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure virtual firewall
    info('*** Configuring virtual firewall\n')
    logging.info('Configuring virtual firewall')
    firewall.cmd('ifconfig firewall-eth0 10.0.0.3 netmask 255.255.255.0')
    firewall.cmd('iptables -A FORWARD -i firewall-eth0 -j ACCEPT')
    firewall.cmd('iptables -A FORWARD -o firewall-eth0 -j ACCEPT')
    firewall.cmd('iptables -A FORWARD -p tcp --dport 80 -j DROP')
    firewall.cmd('iptables -A FORWARD -p icmp -j ACCEPT')
    h1.cmd('route add default gw 10.0.0.3')
    h2.cmd('route add default gw 10.0.0.3')

    # Test connectivity through firewall
    info('*** Testing connectivity through firewall\n')
    logging.info('Testing connectivity through firewall')
    result = net.ping([h1, h2])
    logging.info(f'Ping result: {result}')

    # Test HTTP access through firewall
    info('*** Testing HTTP access through firewall\n')
    logging.info('Testing HTTP access through firewall')
    http_result = h1.cmd('curl -I http://10.0.0.2')
    logging.info(f'HTTP access result: {http_result}')

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
    virtual_firewall()

