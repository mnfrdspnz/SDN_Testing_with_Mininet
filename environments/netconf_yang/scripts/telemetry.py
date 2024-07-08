import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from ncclient import manager

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'telemetry.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def telemetry():
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
        # Collect telemetry data
        config = """
        <config>
            <telemetry xmlns="urn:ietf:params:xml:ns:yang:ietf-telemetry">
                <sensor>
                    <name>cpu_usage</name>
                    <description>CPU usage sensor</description>
                    <interval>10</interval>
                </sensor>
            </telemetry>
        </config>
        """
        m.edit_config(target='running', config=config)
        logging.info('Telemetry data collection configured')

        # Retrieve and log the telemetry data
        info('*** Retrieving telemetry data\n')
        logging.info('Retrieving telemetry data')
        telemetry_data = m.get_config(source='running').data_xml
        logging.info(f'Telemetry data: {telemetry_data}')

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
    telemetry()

