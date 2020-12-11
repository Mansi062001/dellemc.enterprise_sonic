Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies
=================================================================================

This collection includes Ansible core modules, network resource modules, and plugins needed to provision and manage Dell EMC PowerSwitch platforms running Enterprise SONiC Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collection can be used.

Supported connections
---------------------
The SONiC Ansible collection supports network_cli and httpapi connections.

Plugins
--------
**CLICONF plugin**

Name | Description
--- | ---
[network_cli](https://github.com/ansible-collections/dellemc.enterprise_sonic)|Use Ansible CLICONF to run commands on Enterprise SONiC

**HTTPAPI plugin**

Name | Description
--- | ---
[httpapi](https://github.com/ansible-collections/dellemc.enterprise_sonic)|Use Ansible HTTPAPI to run commands on Enterprise SONiC

Collection core modules
------------------------
Name | Description | Connection type
--- | --- | ---
[**sonic_command**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_command.py)|Run commands through the Management Framework CLI|network_cli
[**sonic_config**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_config.py)|Manage configuration through the Management Framework CLI|network_cli
[**sonic_api**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_api.py)|Perform REST operations through the Management Framework REST API|httpapi

Collection network resource modules
-----------------------------------
Listed are the SONiC Ansible network resource modules which need ***httpapi*** as the connection type. Supported operations are ***merged*** and ***deleted***.

| **Interfaces** | **BGP** | **VRF** |
| -------------- | ------- | ------- | 
| [**sonic_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_interfaces.py)|[**sonic_bgp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp.py)| [**sonic_vrfs**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vrfs.py)|
| [**sonic_l2_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_l2_interfaces.py)| [**sonic_bgp_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_af.py)| **MCLAG** |
| [**sonic_l3_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_l3_interfaces.py) |[**sonic_bgp_as_paths**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_as_paths.py)| [**sonic_mclag**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_mclag.py)|
|**Port channel**|[**sonic_bgp_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_communities.py)| **VxLANs** |
|[**sonic_lag_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_lag_interfaces.py)|[**sonic_bgp_ext_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_ext_communities.py)| [**sonic_vxlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vxlans.py)|
|**VLANs**|[**sonic_bgp_neighbors**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_neighbors.py)| - |
|[**sonic_vlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vlans.py)|[**sonic_bgp_neighbors_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_neighbors_af.py)|- |

Sample use case playbooks
-------------------------
The playbooks directory includes this sample playbook that show end-to-end use cases.

Name | Description
--- | ---
[**BGP Layer 3 fabric**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/playbooks/bgp_l3_fabric)|Example playbook to build a Layer 3 leaf-spine fabric

Version compatibility
----------------------
* Recommended Ansible version 2.10 or higher
* Enterprise SONiC Distribution by Dell Technologies version 3.1 or higher
* Recommended Python 3.5 or higher, or Python 2.7


> **NOTE**: Community SONiC versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated 
        with community versions and is not supported.

Installation of Ansible 2.10+
-----------------------------
##### Dependencies for Ansible Enterprise SONiC collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible-base
      
      
Installation of Ansible 2.9
---------------------------
##### Dependencies for Ansible Enterprise SONiC collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible
      
##### Setting Enviroment Varibles

To use the Enterprise SONiC collection in Ansible 2.9, it is required to add one of the two available environment variables.

Option 1: Add the environment variable while running the playbook.


      ANSIBLE_NETWORK_GROUP_MODULES=sonic ansible-playbook sample_playbook.yaml -i inventory.yaml
      
      
Option 2: Add the environment variable in user profile.


      ANSIBLE_NETWORK_GROUP_MODULES=sonic
      

Installation of Enterprise SONiC collection from Ansible Galaxy
---------------------------------------------------------------

Install the latest version of the Enterprise SONiC collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.enterprise_sonic

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

      ansible-galaxy collection install 'dellemc.enterprise_sonic:>=1.0.0,<2.0.0'


Sample playbooks
-----------------
**VLAN configuration using CLICONF**

***sonic_network_cli.yaml***

    ---

    - name: SONiC Management Framework CLI configuration examples
      hosts: sonic_switches
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc.enterprise_sonic
      tasks:
        - name: Add VLAN entry
          sonic_config:
            commands: ['interface Vlan 700','exit']
            save: yes
          register: config_op
        - name: Test SONiC single command
          sonic_command:
            commands: 'show vlan'
          register: cmd_op

**VLAN configuration using HTTPAPI**

***sonic_httpapi.yaml***

    ---

    - name: SONiC Management Framework REST API examples
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.enterprise_sonic
      tasks:
        - name: Perform PUT operation to add a VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "PUT"
            body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
            status_code: 204
        - name: Perform GET operation to view VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "GET"
            status_code: 200
          register: api_op

**Configuration using network resource modules**

***sonic_resource_modules.yaml***

    ---

    - name: VLANs, Layer 2 and Layer 3 interfaces configuration using Enterprise SONiC resource modules
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.enterprise_sonic
      tasks:
       - name: Configure VLANs
         sonic_vlans:
            config:
             - vlan_id: 701
             - vlan_id: 702
             - vlan_id: 703
             - vlan_id: 704
            state: merged
         register: sonic_vlans_output
       - name: Configure Layer 2 interfaces
         sonic_l2_interfaces:
            config:
            - name: Eth1/2
              access:
                vlan: 701
              trunk:
                allowed_vlans:
                  - vlan: 702
                  - vlan: 703
            state: merged
         register: sonic_l2_interfaces_output
       - name: Configure Layer 3 interfaces
         sonic_l3_interfaces:
           config:
            - name: Eth1/3
              ipv4:
                - address: 8.1.1.1/16
              ipv6:
                - address: 3333::1/16
           state: merged
         register: sonic_l3_interfaces_output

***host_vars/sonic_sw1.yaml***

    hostname: sonic_sw1

    # Common parameters for connection type httpapi or network_cli:
    ansible_user: xxxx
    ansible_pass: xxxx
    ansible_network_os: dellemc.enterprise_sonic.sonic

    # Additional parameters for connection type httpapi:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false

***inventory.yaml***

    [sonic_sw1]
    sonic_sw1 ansible_host=100.104.28.119

    [sonic_sw2]
    sonic_sw2 ansible_host=100.104.28.120

    [sonic_switches:children]
    sonic_sw1
    sonic_sw2


(c) 2020 Dell Inc. or its subsidiaries. All rights reserved.
