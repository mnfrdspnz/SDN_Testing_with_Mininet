# Setup Guide: Mininet on Linux (RedHat or Ubuntu)

This guide provides step-by-step instructions to set up Mininet on a Linux machine running either RedHat (minimal installation) or Ubuntu Server. This setup is ideal for testing and studying SDN in a native Linux environment.

## Prerequisites

1. **A Linux machine**: Ensure you have a running instance of either RedHat (minimal installation) or Ubuntu Server.
2. **Internet access**: To download and install the necessary packages.

## Steps

### 1. Update Your System

#### RedHat
1. **Update Package List**:
    ```bash
    sudo yum update
    ```

#### Ubuntu
1. **Update Package List**:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

### 2. Install Required Dependencies

#### RedHat
1. **Enable EPEL Repository**:
    ```bash
    sudo yum install epel-release
    ```
2. **Install Dependencies**:
    ```bash
    sudo yum install git vim wget curl net-tools
    ```

#### Ubuntu
1. **Install Dependencies**:
    ```bash
    sudo apt-get install git vim wget curl net-tools
    ```

### 3. Install Mininet

#### RedHat
1. **Clone Mininet Repository**:
    ```bash
    git clone git://github.com/mininet/mininet
    cd mininet
    ```
2. **Install Mininet**:
    ```bash
    sudo ./util/install.sh -a
    ```

#### Ubuntu
1. **Clone Mininet Repository**:
    ```bash
    git clone git://github.com/mininet/mininet
    cd mininet
    ```
2. **Install Mininet**:
    ```bash
    sudo ./util/install.sh -a
    ```

### 4. Verify Mininet Installation

1. **Run a Simple Mininet Command**:
    ```bash
    sudo mn --test pingall
    ```
    This should create a simple network topology and test connectivity between the hosts.

### 5. Install Open vSwitch (Optional, for advanced SDN testing)

#### RedHat
1. **Install Open vSwitch**:
    ```bash
    sudo yum install openvswitch
    sudo systemctl start openvswitch
    sudo systemctl enable openvswitch
    ```

#### Ubuntu
1. **Install Open vSwitch**:
    ```bash
    sudo apt-get install openvswitch-switch
    sudo service openvswitch-switch start
    ```

### 6. Install Additional Tools (Optional)

1. **Wireshark** (for packet analysis):
    ```bash
    sudo yum install wireshark  # RedHat
    sudo apt-get install wireshark  # Ubuntu
    ```

2. **TCPDump** (for packet capturing):
    ```bash
    sudo yum install tcpdump  # RedHat
    sudo apt-get install tcpdump  # Ubuntu
    ```

### 7. Network Configuration (Optional)

#### RedHat
1. **Edit Network Configuration Files**:
    ```bash
    sudo vim /etc/sysconfig/network-scripts/ifcfg-eth0
    ```
    Configure the network interface as needed.

#### Ubuntu
1. **Edit Network Configuration Files**:
    ```bash
    sudo vim /etc/network/interfaces
    ```
    Configure the network interface as needed.

### Conclusion

You now have Mininet set up and running on your Linux machine. You can start exploring SDN and running your tests. For more information on using Mininet, refer to the [Mininet Walkthrough](http://mininet.org/walkthrough/).


