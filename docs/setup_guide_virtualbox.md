# Setup Guide: Mininet on VirtualBox

This guide provides step-by-step instructions to set up Mininet in a VirtualBox virtual machine. This is ideal for testing and studying SDN in a controlled environment.

## Prerequisites

1. **VirtualBox**: Download and install VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads).
2. **Mininet VM Image**: Download the Mininet VM image from [here](https://github.com/mininet/releases/tag/2.3.0).

## Steps

### 1. Install VirtualBox

1. **Download VirtualBox**: Go to the [VirtualBox download page](https://www.virtualbox.org/wiki/Downloads) and select the appropriate version for your operating system (Windows, macOS, Linux).
2. **Install VirtualBox**: Run the downloaded installer and follow the on-screen instructions to install VirtualBox.

### 2. Import the Mininet VM

1. **Open VirtualBox**: Launch VirtualBox from your applications menu.
2. **Import Appliance**: Click on `File` in the menu bar and select `Import Appliance...`.
3. **Select Mininet VM Image**: In the `Appliance to Import` field, click the folder icon and navigate to the location where you downloaded the Mininet VM image (`.ova` file). Select the file and click `Open`.
4. **Proceed with Import**: Click `Next` to proceed. Review the settings and click `Import` to start the import process. This may take a few minutes.

### 3. Configure the Virtual Machine

1. **Select the VM**: Once the import is complete, you should see the Mininet VM listed in the VirtualBox Manager. Select the Mininet VM.
2. **Open Settings**: Click on the `Settings` icon.
3. **Adjust System Resources**:
    - **System**: Navigate to the `System` tab. Under `Motherboard`, allocate at least 2 GB of RAM (2048 MB). More is better if your host machine has sufficient memory.
    - **Processor**: Under the `Processor` tab, allocate at least 2 CPU cores.
4. **Network Settings**:
    - Navigate to the `Network` tab. Ensure that the first adapter is enabled and set to `NAT` mode. Optionally, you can add a second adapter and set it to `Host-only Adapter` if you need the VM to communicate with your host machine directly.
5. **Save Settings**: Click `OK` to save the settings.

### 4. Start the Virtual Machine

1. **Start the VM**: Select the Mininet VM and click the `Start` button.
2. **Login**: Once the VM boots up, you will see the login screen. Use the default credentials:
    - **Username**: `mininet`
    - **Password**: `mininet`

### 5. Update and Install Additional Tools

1. **Open Terminal**: Once logged in, open a terminal.
2. **Update Packages**: Run the following commands to update the package lists and upgrade existing packages:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```
3. **Install Additional Tools**: You might want to install some additional tools for convenience:
    ```bash
    sudo apt-get install git vim curl
    ```

### 6. Verify Mininet Installation

1. **Run a Simple Mininet Command**: To verify that Mininet is working correctly, run the following command:
    ```bash
    sudo mn --test pingall
    ```
    This should create a simple network topology and test connectivity between the hosts.

### 7. Save Your VM State

1. **Shutdown the VM**: After verifying Mininet, you can shut down the VM by running:
    ```bash
    sudo systemctl poweroff
    ```
2. **Save the State**: Alternatively, you can save the state of the VM from the VirtualBox Manager by right-clicking on the VM and selecting `Close` > `Save the Machine State`.

## Conclusion

You now have Mininet set up and running in a VirtualBox VM. You can start exploring SDN and running your tests. For more information on using Mininet, refer to the [Mininet Walkthrough](http://mininet.org/walkthrough/).


