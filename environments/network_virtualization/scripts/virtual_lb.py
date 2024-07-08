import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'virtual_lb.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def virtual_lb():
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
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    lb = net.addHost('lb')
    s1 = net.addSwitch('s1')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(lb, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure virtual load balancer
    info('*** Configuring virtual load balancer\n')
    logging.info('Configuring virtual load balancer')
    lb.cmd('ifconfig lb-eth0 10.0.0.254 netmask 255.255.255.0')
    lb.cmd('iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.2:80')
    lb.cmd('iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.3:80')
    lb.cmd('iptables -t nat -A POSTROUTING -j MASQUERADE')

    # Test connectivity through load balancer
    info('*** Testing connectivity through load balancer\n')
    logging.info('Testing connectivity through load balancer')
    result = net.ping([h1, h2, h3])
    logging.info(f'Ping result: {result}')

    # Test load balancing
    info('*** Testing load balancing\n')
    logging.info('Testing load balancing')
    http_result_1 = h1.cmd('curl -I http://10.0.0.254')
    http_result_2 = h1.cmd('curl -I http://10.0.0.254')
    logging.info(f'Load balancing test result 1: {http_result_1}')
    logging.info(f'Load balancing test result 2: {http_result_2}')

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
    virtual_lb()

