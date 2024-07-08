import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'put_updates.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def put_updates():
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

    # Perform a PUT request to update device settings
    info('*** Updating device settings using REST API\n')
    logging.info('Updating device settings using REST API')
    url = "http://127.0.0.1:5000/api/update"
    update_data = {
        "hostname": "mininet-device-updated",
        "interfaces": {
            "eth0": {
                "description": "Uplink interface - updated",
                "enabled": True
            }
        }
    }
    try:
        response = requests.put(url, json=update_data)
        response.raise_for_status()
        result = response.json()
        logging.info(f'Update response: {result}')
        print(f'Update Response: {result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error updating settings: {e}')
        print(f'Error updating settings: {e}\n')

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
    put_updates()

