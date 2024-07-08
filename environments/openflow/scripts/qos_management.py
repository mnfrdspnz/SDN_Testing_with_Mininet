import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'qos_management.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def qos_management():
    # Create a Mininet object with a default controller
    net = Mininet(controller=Controller)

    # Add a default controller to the network
    info('*** Adding controller\n')
    logging.info('Adding controller')
    net.addController('c0')

    # Add three hosts to the network
    info('*** Adding hosts\n')
    logging.info('Adding hosts')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')

    # Add a switch to the network
    info('*** Adding switch\n')
    logging.info('Adding switch')
    s1 = net.addSwitch('s1')

    # Create links between the switch and the hosts
    logging.info('Creating links')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Configure QoS on the switch ports
    info('*** Configuring QoS\n')
    logging.info('Configuring QoS')
    s1.cmd('ovs-vsctl set port s1-eth1 qos=@newqos -- \
            --id=@newqos create qos type=linux-htb other-config:max-rate=1000000000 queues:0=@q0 \
            --id=@q0 create queue other-config:min-rate=500000000 other-config:max-rate=1000000000')
    s1.cmd('ovs-vsctl set port s1-eth2 qos=@newqos -- \
            --id=@newqos create qos type=linux-htb other-config:max-rate=1000000000 queues:0=@q0 \
            --id=@q0 create queue other-config:min-rate=500000000 other-config:max-rate=1000000000')
    s1.cmd('ovs-vsctl set port s1-eth3 qos=@newqos -- \
            --id=@newqos create qos type=linux-htb other-config:max-rate=1000000000 queues:0=@q0 \
            --id=@q0 create queue other-config:min-rate=500000000 other-config:max-rate=1000000000')

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
    qos_management()

