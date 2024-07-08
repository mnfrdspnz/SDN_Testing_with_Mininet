import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'rate_limiting.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def rate_limiting():
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

    # Perform a GET request to retrieve rate limiting status
    info('*** Retrieving rate limiting status using REST API\n')
    logging.info('Retrieving rate limiting status using REST API')
    url = "http://127.0.0.1:5000/api/rate_limit"
    try:
        response = requests.get(url)
        response.raise_for_status()
        rate_limit_status = response.json()
        logging.info(f'Rate limiting status: {rate_limit_status}')
        print(f'Rate Limiting Status: {rate_limit_status}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error retrieving rate limiting status: {e}')
        print(f'Error retrieving rate limiting status: {e}\n')

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
    rate_limiting()

