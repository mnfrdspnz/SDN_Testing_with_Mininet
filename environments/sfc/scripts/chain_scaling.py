import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'chain_scaling.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def chain_scaling():
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
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Create links
    info('*** Creating links\n')
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, h2)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure initial service function chain
    info('*** Configuring initial service function chain\n')
    logging.info('Configuring initial service function chain')
    s1.cmd('ovs-vsctl add-port s1 chain0 -- set interface chain0 type=patch options:peer=chain1')
    s2.cmd('ovs-vsctl add-port s2 chain1 -- set interface chain1 type=patch options:peer=chain0')
    s2.cmd('ovs-vsctl add-port s2 chain2 -- set interface chain2 type=patch options:peer=chain3')
    s3.cmd('ovs-vsctl add-port s3 chain3 -- set interface chain3 type=patch options:peer=chain2')
    s3.cmd('ovs-vsctl add-port s3 chain4 -- set interface chain4 type=patch options:peer=chain5')
    s4.cmd('ovs-vsctl add-port s4 chain5 -- set interface chain5 type=patch options:peer=chain4')

    # Set initial flows for service function chain
    s1.cmd('ovs-ofctl add-flow s1 "in_port=1,actions=output:chain0"')
    s2.cmd('ovs-ofctl add-flow s2 "in_port=chain1,actions=output:chain2"')
    s3.cmd('ovs-ofctl add-flow s3 "in_port=chain3,actions=output:chain4"')
    s4.cmd('ovs-ofctl add-flow s4 "in_port=chain5,actions=output:1"')

    # Scale up the service function chain
    info('*** Scaling up the service function chain\n')
    logging.info('Scaling up the service function chain')
    s4.cmd('ovs-vsctl add-port s4 chain6 -- set interface chain6 type=patch options:peer=chain7')
    s3.cmd('ovs-vsctl add-port s3 chain7 -- set interface chain7 type=patch options:peer=chain6')
    s3.cmd('ovs-ofctl add-flow s3 "in_port=chain4,actions=output:chain7"')
    s4.cmd('ovs-ofctl add-flow s4 "in_port=chain6,actions=output:chain5"')

    # Test connectivity
    info('*** Testing connectivity\n')
    logging.info('Testing connectivity')
    result = net.ping([h1, h2])
    logging.info(f'Ping result: {result}')

    # Scale down the service function chain
    info('*** Scaling down the service function chain\n')
    logging.info('Scaling down the service function chain')
    s3.cmd('ovs-ofctl del-flows s3 "in_port=chain4,actions=output:chain7"')
    s4.cmd('ovs-ofctl del-flows s4 "in_port=chain6,actions=output:chain5"')
    s3.cmd('ovs-vsctl del-port s3 chain7')
    s4.cmd('ovs-vsctl del-port s4 chain6')

    # Test connectivity after scaling down
    info('*** Testing connectivity after scaling down\n')
    logging.info('Testing connectivity after scaling down')
    result = net.ping([h1, h2])
    logging.info(f'Ping result after scaling down: {result}')

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
    chain_scaling()

