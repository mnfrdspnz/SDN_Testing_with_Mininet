import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'hybrid_network.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def hybrid_network():
    # Create a Mininet object
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add a remote controller
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add hosts and switches
    info('*** Adding hosts and switches\n')
    logging.info('Adding hosts and switches')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.1.1/24')
    h4 = net.addHost('h4', ip='10.0.1.2/24')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s3)
    net.addLink(s2, s3)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure hybrid network
    info('*** Configuring hybrid network\n')
    logging.info('Configuring hybrid network')
    s3.cmd('ovs-vsctl add-port s3 patch1 -- set interface patch1 type=patch options:peer=patch2')
    s1.cmd('ovs-vsctl add-port s1 patch2 -- set interface patch2 type=patch options:peer=patch1')

    # Test connectivity
    info('*** Testing connectivity\n')
    logging.info('Testing connectivity')
    result = net.ping([h1, h2, h3, h4])
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
    hybrid_network()

