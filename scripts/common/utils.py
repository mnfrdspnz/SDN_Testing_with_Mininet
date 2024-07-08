import logging
import os

def setup_logging(script_name):
    """Setup logging configuration."""
    script_dir = os.path.dirname(__file__)
    log_file = os.path.join(script_dir, f'{script_name}.log')
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info(f'Logging setup for {script_name}')

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f'Directory created: {path}')
    else:
        logging.info(f'Directory already exists: {path}')

