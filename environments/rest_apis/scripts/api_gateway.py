import logging
import os
import requests
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Set up logging
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, 'api_gateway.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def api_gateway():
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

    # Perform API Gateway configuration
    info('*** Configuring API Gateway using REST API\n')
    logging.info('Configuring API Gateway using REST API')
    url = "http://127.0.0.1:5000/api/gateway"
    gateway_config = {
        "gateway_name": "api-gateway",
        "routes": [
            {
                "path": "/api/device",
                "destination": "http://127.0.0.1:5000/device"
            },
            {
                "path": "/api/config",
                "destination": "http://127.0.0.1:5000/config"
            }
        ]
    }
    try:
        response = requests.post(url, json=gateway_config)
        response.raise_for_status()
        result = response.json()
        logging.info(f'API Gateway configuration response: {result}')
        print(f'API Gateway Configuration Response: {result}\n')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error configuring API Gateway: {e}')
        print(f'Error configuring API Gateway: {e}\n')

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
    api_gateway()

