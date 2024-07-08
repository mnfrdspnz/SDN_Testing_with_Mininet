import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from ncclient import manager

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'basic_config.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def basic_config():
    # Create a Mininet object
    net = Mininet()

    # Add a single device
    info('*** Adding device\n')
    logging.info('Adding device')
    d1 = net.addHost('d1')

    # Start the network
    info('*** Starting network\n')
    logging.info('Starting network')
    net.start()

    # Connect to the device using NETCONF
    info('*** Connecting to device using NETCONF\n')
    logging.info('Connecting to device using NETCONF')
    with manager.connect(host='127.0.0.1', port=830, username='admin', password='admin', hostkey_verify=False) as m:
        # Configure the device
        config = """
        <config>
            <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
                <hostname>mininet-device</hostname>
            </system>
        </config>
        """
        m.edit_config(target='running', config=config)
        logging.info('Device configured with basic settings')
        
        # Retrieve and log the device configuration
        info('*** Retrieving device configuration\n')
        logging.info('Retrieving device configuration')
        config = m.get_config(source='running').data_xml
        logging.info(f'Device configuration: {config}')

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
    basic_config()

