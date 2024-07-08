import logging
import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from ncclient import manager

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'acl_management.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def acl_management():
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
        # Manage ACLs
        config = """
        <config>
            <access-lists xmlns="urn:ietf:params:xml:ns:yang:ietf-acl">
                <acl>
                    <name>acl1</name>
                    <acl-entries>
                        <acl-entry>
                            <sequence-number>10</sequence-number>
                            <matches>
                                <source-ip>192.168.1.0/24</source-ip>
                            </matches>
                            <actions>
                                <forwarding-action>accept</forwarding-action>
                            </actions>
                        </acl-entry>
                    </acl-entries>
                </acl>
            </access-lists>
        </config>
        """
        m.edit_config(target='running', config=config)
        logging.info('ACLs managed and configured')

        # Retrieve and log the ACL configuration
        info('*** Retrieving ACL configuration\n')
        logging.info('Retrieving ACL configuration')
        acls = m.get_config(source='running').data_xml
        logging.info(f'ACL configuration: {acls}')

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
    acl_management()

