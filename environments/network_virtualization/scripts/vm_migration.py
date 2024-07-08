import logging
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'vm_migration.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def vm_migration():
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
    h4 = net.addHost('h4', ip='10.0.0.4/24')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Create links
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

    # Configure live migration of virtual machines
    info('*** Configuring live migration of virtual machines\n')
    logging.info('Configuring live migration of virtual machines')
    h1.cmd('ifconfig h1-eth0 10.0.0.1/24')
    h2.cmd('ifconfig h2-eth0 10.0.0.2/24')
    h3.cmd('ifconfig h3-eth0 10.0.0.3/24')
    h4.cmd('ifconfig h4-eth0 10.0.0.4/24')

    # Test connectivity before migration
    info('*** Testing connectivity before migration\n')
    logging.info('Testing connectivity before migration')
    result = net.ping([h1, h2, h3, h4])
    logging.info(f'Ping result before migration: {result}')

    # Perform live migration
    info('*** Performing live migration\n')
    logging.info('Performing live migration')
    h1.cmd('ifconfig h1-eth0 down')
    s1.cmd('ovs-vsctl del-port s1 h1-eth0')
    s2.cmd('ovs-vsctl add-port s2 h1-eth0')
    h1.cmd('ifconfig h1-eth0 10.0.0.1/24 up')

    # Test connectivity after migration
    info('*** Testing connectivity after migration\n')
    logging.info('Testing connectivity after migration')
    result = net.ping([h1, h2, h3, h4])
    logging.info(f'Ping result after migration: {result}')

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
    vm_migration()

