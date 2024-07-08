#!/bin/bash

# Update the system
echo "Updating the system..."
sudo apt-get update -y

# Install Mininet
echo "Installing Mininet..."
sudo apt-get install -y mininet

# Install Open vSwitch
echo "Installing Open vSwitch..."
sudo apt-get install -y openvswitch-switch

# Install additional dependencies
echo "Installing additional dependencies..."
sudo apt-get install -y python3 python3-pip

# Clean up
echo "Cleaning up..."
sudo apt-get clean

echo "Mininet setup is complete."

