import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'post_configuration.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def post_configuration():
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

    # Perform a POST request to apply configuration
    info('*** Applying configuration using REST API\n')
    logging.info('Applying configuration using REST API')
    url = "http://127.0.0.1:5000/api/config"
    config_data = {
        "hostname": "mininet-device",
        "interfaces": {
            "eth0": {
                "description": "Uplink interface",
                "enabled": True
            },
            "eth1": {
                "description": "Downlink interface",
                "enabled": True
            }
        }
    }
    try:
        response = requests.post(url, json=config_data)
        response.raise_for_status()
        result = response.json()
        logging.info(f'Configuration response: {result}')
        print(f'Configuration Response: {result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error applying configuration: {e}')
        print(f'Error applying configuration: {e}\n')

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
    post_configuration()

