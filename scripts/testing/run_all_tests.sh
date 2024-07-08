#!/bin/bash

# Define the list of scripts to run
scripts=(
    "environments/openflow/scripts/simple_switch.py"
    "environments/openflow/scripts/vlan_isolation.py"
    "environments/openflow/scripts/load_balancing.py"
    "environments/openflow/scripts/flow_timeout.py"
    "environments/openflow/scripts/flow_modification.py"
    "environments/openflow/scripts/topology_change.py"
    "environments/openflow/scripts/multipath_routing.py"
    "environments/openflow/scripts/qos_management.py"
    "environments/openflow/scripts/link_failure.py"
    "environments/openflow/scripts/port_mirroring.py"
    # Add other scripts from different environments here
)

# Run each script
for script in "${scripts[@]}"; do
    echo "Running $script..."
    python3 "$script"
done

echo "All tests completed."

