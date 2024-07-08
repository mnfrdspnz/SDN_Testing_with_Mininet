import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'delete_resources.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def delete_resources():
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

    # Perform a DELETE request to remove resources
    info('*** Deleting resources using REST API\n')
    logging.info('Deleting resources using REST API')
    url = "http://127.0.0.1:5000/api/resource"
    resource_id = "eth1"
    try:
        response = requests.delete(f"{url}/{resource_id}")
        response.raise_for_status()
        result = response.json()
        logging.info(f'Delete response: {result}')
        print(f'Delete Response: {result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error deleting resources: {e}')
        print(f'Error deleting resources: {e}\n')

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
    delete_resources()

