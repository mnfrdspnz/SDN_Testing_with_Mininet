# Mininet CLI Help Guide

This guide provides step-by-step instructions on how to test your network configurations once you are in the Mininet CLI (`mininet>`). The commands and explanations are applicable to any scenario you might encounter while using Mininet.

## Common Mininet CLI Commands

### General Commands

- **help**
  - Displays a list of available CLI commands along with a brief description of each. Use this to get an overview of what you can do within the Mininet CLI.
  - Example:
    ```shell
    mininet> help
    ```

### Node Commands

- **nodes**
  - Lists all nodes in the network, including hosts, switches, and controllers.
  - Example:
    ```shell
    mininet> nodes
    ```

- **net**
  - Displays the network connections between nodes.
  - Example:
    ```shell
    mininet> net
    ```

- **dump**
  - Dumps detailed information about all nodes, including their interfaces and links. This is useful for getting a quick overview of the network topology and configuration.
  - Example:
    ```shell
    mininet> dump
    ```

### Host Commands

- **<host> <command>**
  - Runs a shell command on a specific host. Replace `<host>` with the host name (e.g., `h1`) and `<command>` with the shell command you want to execute.
  - Examples:
    ```shell
    mininet> h1 ifconfig
    mininet> h1 ping -c 3 h2
    mininet> h1 iperf -s  # Start an iperf server on h1
    mininet> h2 iperf -c 10.0.0.1  # Run an iperf client on h2 to connect to h1
    ```

### Link and Interface Commands

- **link <node1> <node2> {up|down}**
  - Changes the status of the link between two nodes. Use `up` to bring the link up and `down` to bring it down. This is useful for simulating link failures and recoveries.
  - Examples:
    ```shell
    mininet> link s1 s2 down
    mininet> link s1 s2 up
    ```

- **intfs**
  - Lists all interfaces in the network.
  - Example:
    ```shell
    mininet> intfs
    ```

### Network Performance Commands

- **iperf <node1> <node2>**
  - Runs an iperf bandwidth test between two nodes. This command measures the bandwidth between the nodes using the iperf tool. One node acts as the server, and the other acts as the client.
  - Example:
    ```shell
    mininet> iperf h1 h2
    ```

- **pingall**
  - Pings all hosts in the network from each other. This command is useful for testing overall network connectivity.
  - Example:
    ```shell
    mininet> pingall
    ```

- **pingpair**
  - Pings between each pair of hosts. This is useful for testing connectivity between specific pairs of hosts.
  - Example:
    ```shell
    mininet> pingpair
    ```

- **pingpairfull**
  - Pings between each pair of hosts and displays detailed results. This provides more comprehensive information about the connectivity and latency between host pairs.
  - Example:
    ```shell
    mininet> pingpairfull
    ```

### Network Management Commands

- **addlink <node1> <node2>**
  - Adds a link between two nodes. This command is useful for dynamically modifying the network topology.
  - Example:
    ```shell
    mininet> addlink s1 s3
    ```

- **dellink <node1> <node2>**
  - Deletes the link between two nodes.
  - Example:
    ```shell
    mininet> dellink s1 s3
    ```

- **addhost <host>**
  - Adds a new host to the network.
  - Example:
    ```shell
    mininet> addhost h3
    ```

- **delhost <host>**
  - Deletes a host from the network.
  - Example:
    ```shell
    mininet> delhost h3
    ```

- **switch <switch>**
  - Selects a switch to view its details and manage it.
  - Example:
    ```shell
    mininet> switch s1
    ```

### Utility Commands

- **sh <command>**
  - Runs a shell command in the Mininet CLI environment. This allows you to execute any Linux command from within Mininet.
  - Example:
    ```shell
    mininet> sh ls
    ```

- **xterm <node>**
  - Opens an xterm terminal window for the specified node. This is useful for running interactive commands on a node.
  - Example:
    ```shell
    mininet> xterm h1
    ```

### Controller Commands

- **controller <controller>**
  - Selects a controller to view its details and manage it.
  - Example:
    ```shell
    mininet> controller c0
    ```

### Exiting Mininet

- **exit**
  - Stops the Mininet network and exits the CLI. Use this command when you are done with your testing and want to shut down the network.
  - Example:
    ```shell
    mininet> exit
    ```

## Example Workflow in Mininet CLI

Here is an example of what you might do after the script starts and you're in the Mininet CLI:

1. **Ping Between Hosts**:
   ```shell
   mininet> h1 ping h2
   ```

2. **List Nodes**:
   ```shell
   mininet> nodes
   ```

3. **Dump Node Information**:
   ```shell
   mininet> dump
   ```

4. **Check Interfaces Details**:
   ```shell
   mininet> h1 ifconfig
   ```

5. **Test Bandwidth Between Hosts**:
   ```shell
   mininet> iperf h1 h2
   ```

6. **Exit the Mininet CLI**:
   ```shell
   mininet> exit
   ```
