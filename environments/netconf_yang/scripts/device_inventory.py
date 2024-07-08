import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from ncclient import manager

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'device_inventory.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def device_inventory():
    # Create a Mininet object
    net = Mininet()

    # Add multiple devices
    info('*** Adding devices\n')
    logging.info('Adding devices')
    d1 = net.addHost('d1')
    d2 = net.addHost('d2')

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Connect to the devices using NETCONF
    info('*** Connecting to devices using NETCONF\n')
    logging.info('Connecting to devices using NETCONF')
    
    devices = ['127.0.0.1', '127.0.0.2']
    for device in devices:
        with manager.connect(host=device, port=830, username='admin', password='admin', hostkey_verify=False) as m:
            # Retrieve and log the device inventory
            info(f'*** Retrieving inventory for device {device}\n')
            logging.info(f'Retrieving inventory for device {device}')
            inventory = m.get_config(source='running').data_xml
            logging.info(f'Device {device} inventory: {inventory}')

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
    device_inventory()

