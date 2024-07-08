import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'vlan_isolation.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def vlan_isolation():
    # Create a Mininet object with a default controller
    net = Mininet(controller=Controller)

    # Add a default controller to the network
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0')

    # Add four hosts to the network
    info('*** Adding hosts\n')
    logging.info('Adding hosts')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Add two switches to the network
    info('*** Adding switches\n')
    logging.info('Adding switches')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Create links between the switches and the hosts
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure VLANs on the switches
    info('*** Configuring VLANs\n')
    logging.info('Configuring VLANs')
    s1.cmd('ovs-vsctl add-port s1 h1 -- set interface h1 type=internal')
    s1.cmd('ovs-vsctl add-port s1 h2 -- set interface h2 type=internal')
    s2.cmd('ovs-vsctl add-port s2 h3 -- set interface h3 type=internal')
    s2.cmd('ovs-vsctl add-port s2 h4 -- set interface h4 type=internal')

    # Set VLAN tags on the ports
    s1.cmd('ovs-vsctl set port h1 tag=10')
    s1.cmd('ovs-vsctl set port h2 tag=20')
    s2.cmd('ovs-vsctl set port h3 tag=10')
    s2.cmd('ovs-vsctl set port h4 tag=20')

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
    vlan_isolation()

