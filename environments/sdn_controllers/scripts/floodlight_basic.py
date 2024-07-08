import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'floodlight_basic.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def floodlight_basic():
    # Create a Mininet object with a remote controller
    net = Mininet(controller=RemoteController)

    # Add a remote controller with IP 127.0.0.1 and default port 6653
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add hosts to the network
    info('*** Adding hosts\n')
    logging.info('Adding hosts')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # Add a switch to the network
    info('*** Adding switch\n')
    logging.info('Adding switch')
    s1 = net.addSwitch('s1')

    # Create links between the switch and the hosts
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

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
    floodlight_basic()

