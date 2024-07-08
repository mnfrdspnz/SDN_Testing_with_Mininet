import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'authentication.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def authentication():
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

    # Perform a POST request to authenticate
    info('*** Authenticating using REST API\n')
    logging.info('Authenticating using REST API')
    url = "http://127.0.0.1:5000/api/auth"
    auth_data = {
        "username": "admin",
        "password": "password"
    }
    try:
        response = requests.post(url, json=auth_data)
        response.raise_for_status()
        auth_result = response.json()
        logging.info(f'Authentication response: {auth_result}')
        print(f'Authentication Response: {auth_result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error during authentication: {e}')
        print(f'Error during authentication: {e}\n')

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
    authentication()

