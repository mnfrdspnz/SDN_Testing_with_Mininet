import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'multi_controller.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def multi_controller():
    # Create a Mininet object with multiple remote controllers
    net = Mininet(controller=RemoteController)

    # Add multiple remote controllers with IP 127.0.0.1 and different ports
    info('*** Adding controllers\n')
    logging.info('Adding controllers')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6654)
    net.addController('c2', controller=RemoteController, ip='127.0.0.1', port=6655)

    # Add hosts to the network
    info('*** Adding hosts\n')
    logging.info('Adding hosts')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Add switches to the network
    info('*** Adding switches\n')
    logging.info('Adding switches')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    # Create links between the switches and the hosts
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s3)
    net.addLink(s1, s2)
    net.addLink(s2, s3)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Test connectivity between the hosts
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
    multi_controller()

