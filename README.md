# Mininet SDN Testing Repository

Welcome to the Mininet SDN Testing Repository! This project is designed for testing various Software-Defined Networking (SDN) environments using Mininet. It's a great resource for those preparing for certifications or simply exploring SDN.

## Getting Started

To get started, follow these steps:

### 1. Set Up Your Environment

First, set up Mininet. Here are detailed guides to help you:

- [Setting Up Mininet on VirtualBox](./docs/setup_guide_virtualbox.md)
- [Setting Up Mininet on a Linux Distribution](./docs/setup_guide_linux.md)

### 2. Learn Mininet CLI

Once you're in the Mininet CLI, you might need some guidance. Check out our [Mininet CLI Help Document](./docs/mininet_help.md) for detailed command usage.

### 3. Running Scripts

After setting up Mininet and familiarizing yourself with the CLI, you can start running the provided scripts. The scripts are categorized into various SDN topics and environments. Each environment has its own set of configuration files and scripts to run different tests.

The scripts can be found in the respective environment directories:

- [OpenFlow](./environments/openflow)
- [SDN Controllers](./environments/sdn_controllers)
- [NETCONF/YANG](./environments/netconf_yang)
- [REST APIs](./environments/rest_apis)
- [Overlay Networks](./environments/overlay_networks)
- [SFC](./environments/sfc)
- [Network Virtualization](./environments/network_virtualization)
- [Telemetry and Analytics](./environments/telemetry_analytics)

## Repository Structure

Here's a quick overview of the repository:

```plaintext
├── docs/
│   ├── setup_guide_virtualbox.md
│   ├── setup_guide_linux.md
│   └── mininet_help.md
├── environments/
│   ├── openflow/
│   │   ├── configs/
│   │   │   ├── simple_switch.txt
│   │   │   ├── vlan_isolation.txt
│   │   │   ├── load_balancing.txt
│   │   │   ├── flow_timeout.txt
│   │   │   ├── flow_modification.txt
│   │   │   ├── topology_change.txt
│   │   │   ├── multipath_routing.txt
│   │   │   ├── qos_management.txt
│   │   │   ├── link_failure.txt
│   │   │   └── port_mirroring.txt
│   │   ├── scripts/
│   │   │   ├── simple_switch.py
│   │   │   ├── vlan_isolation.py
│   │   │   ├── load_balancing.py
│   │   │   ├── flow_timeout.py
│   │   │   ├── flow_modification.py
│   │   │   ├── topology_change.py
│   │   │   ├── multipath_routing.py
│   │   │   ├── qos_management.py
│   │   │   ├── link_failure.py
│   │   │   └── port_mirroring.py
│   ├── sdn_controllers/
│   │   ├── configs/
│   │   │   ├── ryu_basic.txt
│   │   │   ├── opendaylight_basic.txt
│   │   │   ├── floodlight_basic.txt
│   │   │   ├── onos_basic.txt
│   │   │   ├── controller_failover.txt
│   │   │   ├── multi_controller.txt
│   │   │   ├── northbound_api.txt
│   │   │   ├── southbound_api.txt
│   │   │   ├── custom_app.txt
│   │   │   └── security_policy.txt
│   │   ├── scripts/
│   │   │   ├── ryu_basic.py
│   │   │   ├── opendaylight_basic.py
│   │   │   ├── floodlight_basic.py
│   │   │   ├── onos_basic.py
│   │   │   ├── controller_failover.py
│   │   │   ├── multi_controller.py
│   │   │   ├── northbound_api.py
│   │   │   ├── southbound_api.py
│   │   │   ├── custom_app.py
│   │   │   └── security_policy.py
│   ├── netconf_yang/
│   │   ├── configs/
│   │   │   ├── basic_config.txt
│   │   │   ├── interface_management.txt
│   │   │   ├── device_inventory.txt
│   │   │   ├── policy_enforcement.txt
│   │   │   ├── acl_management.txt
│   │   │   ├── qos_config.txt
│   │   │   ├── telemetry.txt
│   │   │   ├── configuration_backup.txt
│   │   │   ├── rollback.txt
│   │   │   └── schema_validation.txt
│   │   ├── scripts/
│   │   │   ├── basic_config.py
│   │   │   ├── interface_management.py
│   │   │   ├── device_inventory.py
│   │   │   ├── policy_enforcement.py
│   │   │   ├── acl_management.py
│   │   │   ├── qos_config.py
│   │   │   ├── telemetry.py
│   │   │   ├── configuration_backup.py
│   │   │   ├── rollback.py
│   │   │   └── schema_validation.py
│   ├── rest_apis/
│   │   ├── configs/
│   │   │   ├── get_device_info.txt
│   │   │   ├── post_configuration.txt
│   │   │   ├── put_updates.txt
│   │   │   ├── delete_resources.txt
│   │   │   ├── authentication.txt
│   │   │   ├── rate_limiting.txt
│   │   │   ├── api_gateway.txt
│   │   │   ├── versioning.txt
│   │   │   ├── monitoring.txt
│   │   │   └── error_handling.txt
│   │   ├── scripts/
│   │   │   ├── get_device_info.py
│   │   │   ├── post_configuration.py
│   │   │   ├── put_updates.py
│   │   │   ├── delete_resources.py
│   │   │   ├── authentication.py
│   │   │   ├── rate_limiting.py
│   │   │   ├── api_gateway.py
│   │   │   ├── versioning.py
│   │   │   ├── monitoring.py
│   │   │   └── error_handling.py
│   ├── overlay_networks/
│   │   ├── configs/
│   │   │   ├── vxlan_basic.txt
│   │   │   ├── gre_tunnel.txt
│   │   │   ├── nvgre_basic.txt
│   │   │   ├── overlay_qos.txt
│   │   │   ├── multi_tenant.txt
│   │   │   ├── dynamic_tunnels.txt
│   │   │   ├── encryption.txt
│   │   │   ├── tunnel_monitoring.txt
│   │   │   ├── bandwidth_management.txt
│   │   │   └── tunnel_failover.txt
│   │   ├── scripts/
│   │   │   ├── vxlan_basic.py
│   │   │   ├── gre_tunnel.py
│   │   │   ├── nvgre_basic.py
│   │   │   ├── overlay_qos.py
│   │   │   ├── multi_tenant.py
│   │   │   ├── dynamic_tunnels.py
│   │   │   ├── encryption.py
│   │   │   ├── tunnel_monitoring.py
│   │   │   ├── bandwidth_management.py
│   │   │   └── tunnel_failover.py
│   ├── sfc/
│   │   ├── configs/
│   │   │   ├── basic_chain.txt
│   │   │   ├── dynamic_chaining.txt
│   │   │   ├── chain_scaling.txt
│   │   │   ├── service_insertion.txt
│   │   │   ├── service_removal.txt
│   │   │   ├── chain_monitoring.txt
│   │   │   ├── traffic_steering.txt
│   │   │   ├── policy_enforcement.txt
│   │   │   ├── chain_failover.txt
│   │   │   └── service_dependency.txt
│   │   ├── scripts/
│   │   │   ├── basic_chain.py
│   │   │   ├── dynamic_chaining.py
│   │   │   ├── chain_scaling.py
│   │   │   ├── service_insertion.py
│   │   │   ├── service_removal.py
│   │   │   ├── chain_monitoring.py
│   │   │   ├── traffic_steering.py
│   │   │   ├── policy_enforcement.py
│   │   │   ├── chain_failover.py
│   │   │   └── service_dependency.py
│   ├── network_virtualization/
│   │   ├── configs/
│   │   │   ├── virtual_switch.txt
│   │   │   ├── virtual_router.txt
│   │   │   ├── network_segmentation.txt
│   │   │   ├── vnf_integration.txt
│   │   │   ├── virtual_firewall.txt
│   │   │   ├── virtual_lb.txt
│   │   │   ├── vm_migration.txt
│   │   │   ├── hybrid_network.txt
│   │   │   ├── resource_allocation.txt
│   │   │   └── performance_monitoring.txt
│   │   ├── scripts/
│   │   │   ├── virtual_switch.py
│   │   │   ├── virtual_router.py
│   │   │   ├── network_segmentation.py
│   │   │   ├── vnf_integration.py
│   │   │   ├── virtual_firewall.py
│   │   │   ├── virtual_lb.py
│   │   │   ├── vm_migration.py
│   │   │   ├── hybrid_network.py
│   │   │   ├── resource_allocation.py
│   │   │   └── performance_monitoring.py
│   ├── telemetry_analytics/
│   │   ├── configs/
│   │   │   ├── basic_telemetry.txt
│   │   │   ├── flow_statistics.txt
│   │   │   ├── device_health.txt
│   │   │   ├── anomaly_detection.txt
│   │   │   ├── traffic_analysis.txt
│   │   │   ├── alerting.txt
│   │   │   ├── visualization.txt
│   │   │   ├── historical_data.txt
│   │   │   ├── predictive_analytics.txt
│   │   │   └── custom_metrics.txt
│   │   ├── scripts/
│   │   │   ├── basic_telemetry.py
│   │   │   ├── flow_statistics.py
│   │   │   ├── device_health.py
│   │   │   ├── anomaly_detection.py
│   │   │   ├── traffic_analysis.py
│   │   │   ├── alerting.py
│   │   │   ├── visualization.py
│   │   │   ├── historical_data.py
│   │   │   ├── predictive_analytics.py
│   │   │   └── custom_metrics.py
├── scripts/
│   ├── common/
│   │   ├── setup_mininet.sh
│   │   └── utils.py
│   └── testing/
│       ├── run_all_tests.sh
│       └── generate_reports.py

