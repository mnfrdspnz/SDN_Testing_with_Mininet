import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'error_handling.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def error_handling():
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

    # Perform a GET request to trigger an error
    info('*** Triggering error using REST API\n')
    logging.info('Triggering error using REST API')
    url = "http://127.0.0.1:5000/api/error"
    try:
        response = requests.get(url)
        response.raise_for_status()
        error_result = response.json()
        logging.info(f'Error response: {error_result}')
        print(f'Error Response: {error_result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error response: {e}')
        print(f'Error response: {e}\n')

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
    error_handling()

