import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from ncclient import manager

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'qos_config.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def qos_config():
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
        # Configure QoS
        config = """
        <config>
            <qos xmlns="urn:ietf:params:xml:ns:yang:ietf-qos">
                <policy>
                    <name>qos1</name>
                    <description>Basic QoS policy</description>
                    <class-maps>
                        <class-map>
                            <name>class1</name>
                            <match>
                                <ip-dscp>46</ip-dscp>
                            </match>
                            <action>
                                <queue>high-priority</queue>
                            </action>
                        </class-map>
                    </class-maps>
                </policy>
            </qos>
        </config>
        """
        m.edit_config(target='running', config=config)
        logging.info('QoS configured')

        # Retrieve and log the QoS configuration
        info('*** Retrieving QoS configuration\n')
        logging.info('Retrieving QoS configuration')
        qos = m.get_config(source='running').data_xml
        logging.info(f'QoS configuration: {qos}')

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
    qos_config()

