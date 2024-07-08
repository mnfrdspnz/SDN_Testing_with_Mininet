import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'network_segmentation.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def network_segmentation():
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
    h3 = net.addHost('h3', ip='10.0.1.1/24')
    h4 = net.addHost('h4', ip='10.0.1.2/24')
    s1 = net.addSwitch('s1')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure network segmentation using VLANs
    info('*** Configuring network segmentation using VLANs\n')
    logging.info('Configuring network segmentation using VLANs')
    s1.cmd('ovs-vsctl add-port s1 vlan10 tag=10 -- set interface vlan10 type=internal')
    s1.cmd('ovs-vsctl add-port s1 vlan20 tag=20 -- set interface vlan20 type=internal')
    h1.cmd('ip link add link h1-eth0 name h1-eth0.10 type vlan id 10')
    h2.cmd('ip link add link h2-eth0 name h2-eth0.10 type vlan id 10')
    h3.cmd('ip link add link h3-eth0 name h3-eth0.20 type vlan id 20')
    h4.cmd('ip link add link h4-eth0 name h4-eth0.20 type vlan id 20')
    h1.cmd('ifconfig h1-eth0.10 10.0.0.1/24')
    h2.cmd('ifconfig h2-eth0.10 10.0.0.2/24')
    h3.cmd('ifconfig h3-eth0.20 10.0.1.1/24')
    h4.cmd('ifconfig h4-eth0.20 10.0.1.2/24')

    # Test connectivity
    info('*** Testing connectivity\n')
    logging.info('Testing connectivity')
    result = net.ping([h1, h2])
    logging.info(f'Ping result within VLAN 10: {result}')
    result = net.ping([h3, h4])
    logging.info(f'Ping result within VLAN 20: {result}')

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
    network_segmentation()

