import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'flow_modification.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def flow_modification():
    # Create a Mininet object with a default controller
    net = Mininet(controller=Controller)

    # Add a default controller to the network
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0')

    # Add two hosts to the network
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

    # Add an initial flow to the switch
    info('*** Adding initial flow\n')
    logging.info('Adding initial flow')
    s1.cmd('ovs-ofctl add-flow s1 "priority=1,actions=normal"')

    # Modify the flow to drop packets
    info('*** Modifying flow\n')
    logging.info('Modifying flow')
    s1.cmd('ovs-ofctl mod-flows s1 "priority=1,actions=drop"')

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
    flow_modification()

