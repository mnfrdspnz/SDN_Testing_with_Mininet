import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'vxlan_basic.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def vxlan_basic():
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
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s2)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure VXLAN
    info('*** Configuring VXLAN\n')
    logging.info('Configuring VXLAN')
    s1.cmd('ovs-vsctl add-port s1 vxlan0 -- set interface vxlan0 type=vxlan options:remote_ip=flow options:key=flow')
    s2.cmd('ovs-vsctl add-port s2 vxlan0 -- set interface vxlan0 type=vxlan options:remote_ip=flow options:key=flow')

    # Set VXLAN flows
    s1.cmd('ovs-ofctl add-flow s1 "in_port=1,actions=set_tunnel:100,output:vxlan0"')
    s2.cmd('ovs-ofctl add-flow s2 "in_port=1,actions=set_tunnel:100,output:vxlan0"')
    s1.cmd('ovs-ofctl add-flow s1 "in_port=vxlan0,tunnel_id=100,actions=output:1"')
    s2.cmd('ovs-ofctl add-flow s2 "in_port=vxlan0,tunnel_id=100,actions=output:1"')

    # Test connectivity
    info('*** Testing connectivity\n')
    logging.info('Testing connectivity')
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
    vxlan_basic()

