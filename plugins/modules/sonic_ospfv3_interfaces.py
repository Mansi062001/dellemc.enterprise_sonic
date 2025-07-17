#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


"""
The module file for sonic_ospfv3_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_ospfv3_interfaces
version_added: '3.1.0'
notes:
  - Supports C(check_mode).
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
short_description: Configure OSPFv3 interface mode protocol settings on SONiC.
description:
  - This module provides configuration management of OSPFv3 interface mode parameters on devices running SONiC.
  - Configure VRF instance before configuring OSPFv3 in a VRF.
  - Configure OSPFv3 instance before configuring OSPFv3 in interfaces.
author: "Mansi Jharia (@Mansi062001)"
options:
      config:
        description:
          - Specifies the OSPFv3 interface mode related configuration.
        type: list
        elements: dict
        suboptions:
          name:
            required: True
            type: str
            description:
              - Full name of the interface, i.e. Ethernet1.
          advertise:
            description:
              - Enable OSPFv3 interface advertise.
              - expects name of a prefix list.
            type: str
          area_id:
            description:
              - OSPFv3 Area ID of the network (A.B.C.D or 0 to 4294967295).
            type: str
          bfd:
            description:
              - Configure OSPFv3 interface BFD.
            type: dict
            suboptions:
              enable:
                description:
                  - Enable BFD support for OSPFv3.
                type: bool
                required: true
              bfd_profile:
                description:
                  - Configure BFD profile.
                type: str
          cost:
            description:
              - Configure OSPFv3 interface cost (1 to 65535).
            type: int
          dead_interval:
            description:
              - Configure OSPFv3 adjacency dead interval (1 to 65535).
            type: int
          hello_interval:
            description:
              - Configure OSPFv3 neighbour hello interval (1 to 65535).
            type: int
          mtu_ignore:
            description:
              - Disable OSPFv3 MTU mismatch detection.
            type: bool
          network:
            description:
              - Configure OSPFv3 interface network type
            type: str
            choices:
              - broadcast
              - point_to_point
          passive:
            description:
              - Configure ospfv3 interface as passive.
            type: bool
          priority:
            description:
              - Configure OSPFv3 adjacency router priority (0 to 255).
            type: int
          retransmit_interval:
            description:
              - Configure OSPFv3 retransmit interval (2 to 65535).
            type: int
          transmit_delay:
            description:
              - Configure OSPFv3 transmit delay (1 to 65535).
            type: int
          ospfv3ipsec:
            description:
              - Configure OSPFv3 IPsec on interfaces.
              - I(authentication) and I(encryption) are mutually exclusive.
            type: dict
            suboptions:
              authentication:
                description:
                  -  Configure OSPFv3 IPsec authentication.
                type: dict
                suboptions:
                  spi_value:
                    description:
                      - Configure a unique security policy index (SPI) value, from 256 to 4294967295.
                    type: int
                    required: true
                  authentication_type:
                    description:
                      - Configure OSPFv3 IPsec authentication type.
                    type: str
                    required: true
                    choices:
                      - IPSEC
                  authentication_algorithm:
                    description:
                      - Configure OSPFv3 IPsec authentication algorithm
                      - C(MD5) - Enable message digest 5 (MD5) authentication.
                      - C(SHA1) - Enable secure hash algorithm 1 (SHA-1) authentication.
                      - C(SHA256) - Enable secure hash algorithm 256 (SHA-256) authentication.
                    type: str
                    required: true
                    choices:
                      - MD5
                      - SHA1
                      - SHA256
                  authentication_key:
                    description:
                      - Configure OSPFv3 IPsec authentication key.
                      - Authentication key can be 32 ,40 or 64character long depending upon authentication type.
                      - Authentication key will be 32 character long hexstring for MD5 authentication type.
                      - Authentication key will be 40 character long hexstring for SHA1 authentication type.
                      - Authentication key will be 64 character long hexstring for SHA256 authentication type.
                    type: str
                    required: true
                  authentication_key_encrypted:
                    description:
                      - Indicates whether the authentication key is encrypted text.
                    type: bool
                    required: true
              encryption:
                description:
                  - Configure OSPFv3 IPsec encryption.
                type: dict
                suboptions:
                  spi_value:
                    description:
                      - Configure a unique security policy index (SPI) value, from 256 to 4294967295.
                    type: int
                    required: true
                  encryption_type:
                    description:
                      - Configure OSPFv3 IPsec encryption type.
                    type: str
                    required: true
                    choices:
                      - IPSEC
                  encryption_algorithm:
                    description:
                      - Configure OSPFv3 IPsec encryption algorithm.
                      - C(3DES) - Enable triple DES encryption.
                      - C(DES) - Enable DES encryption.
                      - C(AES_CBC_128) - Enable AES-CBC-128 encryption.
                      - C(AES_CBC_192) - Enable AES-CBC-192 encryption.
                      - C(NULL) - NULL encryption
                    type: str
                    required: true
                    choices:
                      - 'DES'
                      - '3DES'
                      - 'AES_CBC_128'
                      - 'AES_CBC_192'
                      - 'NULL'
                  encryption_key:
                    description:
                      - Encryption key can be of varied length depending upon the encryption algorithm.
                      - Encryption key will be 48 character long hexstring for 3DES encryption algorithm.
                      - Encryption key will be 16 character long hexstring for DES encryption algorithm.
                      - Encryption key will be 32 character long hexstring for AES-CBC-128 encryption algorithm.
                      - Encryption key will be 48 character long hexstring for AES-CBC-192 encryption algorithm.
                      - Encryption key is not required for NULL is specified as  encryption algorithm.
                    type: str
                  encryption_key_encrypted:
                    description:
                      - Indicates whether the encryption key is encrypted text.
                    type: bool
                  authentication_algorithm:
                    description:
                      - Configure OSPFv3 IPsec authentication algorithm
                      - C(MD5) - Enable message digest 5 (MD5) authentication.
                      - C(SHA1) - Enable secure hash algorithm 1 (SHA-1) authentication.
                      - C(SHA256) - Enable secure hash algorithm 256 (SHA-256) authentication.
                    type: str
                    required: true
                    choices:
                      - MD5
                      - SHA1
                      - SHA256
                  authentication_key:
                    description:
                      - Configure OSPFv3 IPsec authentication key.
                      - Authentication key can be 32, 40 or 64 character long depending upon authentication type.
                      - Authentication key will be 32 character long hexstring for MD5 authentication type.
                      - Authentication key will be 40 character long hexstring for SHA1 authentication type.
                      - Authentication key will be 64 character long hexstring for SHA256 authentication type.
                    type: str
                    required: true
                  authentication_key_encrypted:
                    description:
                      - Indicates whether the authentication key is encrypted text.
                    type: bool
                    required: true
      state:
        description:
          - Specifies the operation to be performed on the OSPFv3 interfaces configured on the device.
          - In case of merged, the input configuration will be merged with the existing OSPFv3 interfaces configuration on the device.
          - In case of deleted, the existing OSPFv3 interfaces configuration will be removed from the device.
          - In case of overridden, all the existing OSPFv3 interfaces configuration will be deleted and the specified input
            configuration will be installed.
          - In case of replaced, the existing OSPFv3 interface configuration on the device will be replaced by the configuration in the
            playbook for each interface group configured by the playbook.
        type: str
        default: merged
        choices: ['merged', 'deleted', 'replaced', 'overridden']

"""
EXAMPLES = """
# Using deleted

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile2
# ipv6 ospfv3 cost 30
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 passive
# ipv6 ospfv3 authentication ipsec spi 276 md5
# U2FsdGVkX18YF7GTSaFz25cM142ikx3vdltAb+ryG4cJe8PAVmn4lgZq8TDX9TDvsKMFogC+JaumKItGAR28lA== authentication-key-encrypted
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 encryption ipsec spi 9999 esp des U2FsdGVkX1+a0nn/SRCog1Gad6cE9qvAR6rgrDE0DAyLl8XbqkVh3DkHqhnxlSZO encryption-key-encrypted
# md5 U2FsdGVkX18O/Jz5opNz/SLjwq9+UaXnWiItWLtsgPaCxbp+J7TO6+MPb1hx/idGWjJ/QpAjiHVButAUwEjHbA== authentication-key-encrypted

# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# ipv6 ospfv3 encryption ipsec spi 555 esp null sha1
# U2FsdGVkX18CeqRGe0yw9MYx7auhvoudMpnTkBjQhMzJs/4VGMQnlhCndvFdoJHe2GmMEPiqjxp940cOKrogdQ== authentication-key-encrypted
# !
# sonic#

- name: Delete the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/1'
        area_id: '2.2.2.2'
        cost: 30
        priority: 20
        hello_interval: 10
        dead_interval: 40
        mtu_ignore: true
        bfd:
          enable: true
          bfd_profile: 'profile2'
        network: point_to_point
        ospfv3ipsec:
          authentication:
            spi_value: 276
            authentication_type: 'IPSEC'
            authentication_algorithm: 'MD5'
            authentication_key: 'U2FsdGVkX18YF7GTSaFz25cM142ikx3vdltAb+ryG4cJe8PAVmn4lgZq8TDX9TDvsKMFogC+JaumKItGAR28lA=='
            authentication_key_encrypted: true
      - name: 'Eth1/2'
        bfd:
          enable: true
        ospfv3ipsec:
          encryption:
            spi_value: 9999
            encryption_type: 'IPSEC'
            encryption_algorithm: 'DES'
            encryption_key: 'U2FsdGVkX1+a0nn/SRCog1Gad6cE9qvAR6rgrDE0DAyLl8XbqkVh3DkHqhnxlSZO'
            encryption_key_encrypted: true
            authentication_algorithm: 'MD5'
            authentication_key: 'U2FsdGVkX18O/Jz5opNz/SLjwq9+UaXnWiItWLtsgPaCxbp+J7TO6+MPb1hx/idGWjJ/QpAjiHVButAUwEjHbA=='
            authentication_key_encrypted: true
      - name: 'Eth1/3'
        ospfv3ipsec:
          encryption:
            spi_value: 555
            encryption_type: 'IPSEC'
            encryption_algorithm: 'NULL'
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX18CeqRGe0yw9MYx7auhvoudMpnTkBjQhMzJs/4VGMQnlhCndvFdoJHe2GmMEPiqjxp940cOKrogdQ=='
            authentication_key_encrypted: true
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 passive
# !
# interface Eth1/2
# ipv6 ospfv3 network point-to-point
# !
# interface Eth1/3
# !
# sonic#


# Using deleted

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile2
# ipv6 ospfv3 cost 30
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 passive
# ipv6 ospfv3 authentication ipsec spi 388 sha1
# U2FsdGVkX18gierkTwkumRf/3zPOdum+4LZd9RIii5Sr12S5R4oEZY/a98VIfiWkEnXlEqGl0NQei1FVnk0Qvg== authentication-key-encrypted
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 authentication ipsec spi 484
# md5 U2FsdGVkX1/VZuJrAQKgRuitc4xDJYAfUUDA6ADg8U1N9PUL3dUXn1FajshSgcuuGMvvjCemkdqldqLsteyGjg== authentication-key-encrypted
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# !
# sonic#

- name: Delete the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/1'
        ospfv3ipsec:
          authentication:
            spi_value: 388
            authentication_type: 'IPSEC'
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX18gierkTwkumRf/3zPOdum+4LZd9RIii5Sr12S5R4oEZY/a98VIfiWkEnXlEqGl0NQei1FVnk0Qvg=='
            authentication_key_encrypted: true
      - name: 'Eth1/2'
        bfd:
          enable: true
        ospfv3ipsec:
          authentication:
            spi_value: 484
            authentication_type: 'IPSEC'
            authentication_algorithm: 'MD5'
            authentication_key: 'U2FsdGVkX1/VZuJrAQKgRuitc4xDJYAfUUDA6ADg8U1N9PUL3dUXn1FajshSgcuuGMvvjCemkdqldqLsteyGjg=='
            authentication_key_encrypted: true

      - name: 'Eth1/3'
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# !
# interface Eth1/2
# ipv6 ospfv3 network point-to-point
# !
# interface Eth1/3
# !
# sonic#


# Using merged

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# !
# interface Eth1/2
# !
# interface Eth1/3
# !
# sonic#

- name: Add the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/1'
        advertise: 'test1'
        area_id: '2.2.2.2'
        cost: 20
        passive: true
        priority: 20
        hello_interval: 10
        dead_interval: 40
        mtu_ignore: true
        hello_multiplier: 5
        bfd:
          enable: true
          bfd_profile: 'profile1'
        ospfv3ipsec:
          encryption:
            spi_value: 9999
            encryption_type: 'IPSEC'
            encryption_algorithm: 'AES_CBC_128'
            encryption_key: 'U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg=='
            encryption_key_encrypted: true
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw=='
            authentication_key_encrypted: true
        network: broadcast
      - name: 'Eth1/3'
        area_id: '3.3.3.3'
        hello_multiplier: 5
        bfd:
          enable: true
        network: point_to_point
    state: merged

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile1
# ipv6 ospfv3 cost 20
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 9999 esp aes-cbc-128
# U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg== encryption-key-encrypted
# U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw== authentication-key-encrypted
# !
# interface Eth1/2
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# !
# sonic#

# Using merged

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile1
# ipv6 ospfv3 cost 20
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 9999 esp
# aes-cbc-128 U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg== encryption-key-encrypted
# U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw== authentication-key-encrypted
# !
# interface Eth1/2
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# !
# sonic#

- name: Add the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/1'
        area_id: '2.2.2.2'
        cost: 30
        passive: true
        priority: 20
        hello_interval: 10
        dead_interval: 40
        mtu_ignore: true
        bfd:
          enable: true
          bfd_profile: 'profile2'
        network: point_to_point
        ospfv3ipsec:
          encryption:
            spi_value: 9999
            encryption_type: 'IPSEC'
            encryption_algorithm: 'AES_CBC_128'
            encryption_key: 'U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg=='
            encryption_key_encrypted: true
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw=='
            authentication_key_encrypted: true
      - name: 'Eth1/2'
        bfd:
          enable: true
        network: point_to_point
        ospfv3ipsec:
          authentication:
            spi_value: 566
            encryption_key: 'IPSEC'
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX18Dmg2PY5pefS+Px6uf3eusD3/p7geRI+CKbEhhu6dCz0LjkFfHpo30xkotd2RGEEbu3O8H1u/Hst8Em8ijgBzSVvXOiD9QbTQ='
            authentication_key_encrypted: true
      - name: 'Eth1/3'
        ospfv3ipsec:
          encryption:
            spi_value: 555
            encryption_type: 'IPSEC'
            encryption_algorithm: 'DES'
            encryption_key: 'U2FsdGVkX1+qamfn+ogyJoO9b3jo6ooYihCH/Tlvg2LMZFYRUEXhLeo//2wQx56A'
            encryption_key_encrypted: true
            authentication_algorithm: 'SHA256'
            authentication_key: 'U2FsdGVkX18peEBfs0HBZvbjnrpO9HEqGw0cHkRbRmS+H1AZtBYsRZZAVHb1VAVKv/vlQP5xsJZEDVX2NbqPl8gh8f8QGoR1gC2bpPAw6Q3pFhxEhgmOIunFf9bwm
                                 JsJ'
            authentication_key_encrypted: true
    state: merged

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile2
# ipv6 ospfv3 cost 30
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 9999 esp
# aes-cbc-128 U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg== encryption-key-encrypted
# U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw== authentication-key-encrypted
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 authentication ipsec spi 566 sha1
# U2FsdGVkX18Dmg2PY5pefS+Px6uf3eusD3/p7geRI+CKbEhhu6dCz0LjkFfHpo30xkotd2RGEEbu3O8H1u/Hst8Em8ijgBzSVvXOiD9QbTQ= authentication-key-encrypted
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# ipv6 ospfv3 encryption ipsec spi 555 esp des U2FsdGVkX1+qamfn+ogyJoO9b3jo6ooYihCH/Tlvg2LMZFYRUEXhLeo//2wQx56A encryption-key-encrypted
# sha256
# U2FsdGVkX18peEBfs0HBZvbjnrpO9HEqGw0cHkRbRmS+H1AZtBYsRZZAVHb1VAVKv/vlQP5xsJZEDVX2NbqPl8gh8f8QGoR1gC2bpPAw6Q3pFhxEhgmOIunFf9bwmJsJ authentication-key-encrypted
# !
# sonic#


# Using replaced

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile1
# ipv6 ospfv3 cost 20
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 9999 esp aes-cbc-128
# U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg== encryption-key-encrypted
# U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw== authentication-key-encrypted
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 authentication ipsec spi 566 sha1
# U2FsdGVkX18Dmg2PY5pefS+Px6uf3eusD3/p7geRI+CKbEhhu6dCz0LjkFfHpo30xkotd2RGEEbu3O8H1u/Hst8Em8ijgBzSVvXOiD9QbTQ= authentication-key-encrypted
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# ipv6 ospfv3 encryption ipsec spi 555 esp des U2FsdGVkX1+qamfn+ogyJoO9b3jo6ooYihCH/Tlvg2LMZFYRUEXhLeo//2wQx56A encryption-key-encrypted
# sha256
# U2FsdGVkX18peEBfs0HBZvbjnrpO9HEqGw0cHkRbRmS+H1AZtBYsRZZAVHb1VAVKv/vlQP5xsJZEDVX2NbqPl8gh8f8QGoR1gC2bpPAw6Q3pFhxEhgmOIunFf9bwmJsJ authentication-key-encrypted
# !
# sonic#


- name: Replace the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/3'
        area_id: '2.2.2.2'
        cost: 30
        passive: true
        priority: 20
        hello_interval: 10
        dead_interval: 40
        mtu_ignore: true
        bfd:
          enable: true
          bfd_profile: 'profile2'
        network: broadcast
        ospfv3ipsec:
          encrypption:
            spi_value: 444
            encryption_type: 'IPSEC'
            encryption_algorithm: 'NULL'
            authentication_algorithm: 'SHA1'
            authentication_key: 'U2FsdGVkX1/TRX7fZMWcSi4IqDpv+JEkvzsOC8wKb4rOw5a+DiQyDcsZj8nQTaP5C6ydcL/IHoB9lSa0djS6KQ=='
            authentication_key_encrypted: true

    state: replaced

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile1
# ipv6 ospfv3 cost 20
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 9999 esp esp aes-cbc-128
# U2FsdGVkX1+RVU8e/t9tl/WgxdwLqE5ItVx3qyiviwc2jm5SvfH64yALBdASkG+piHyxZHn0JZGGQAb6Z6YnQg== encryption-key-encrypted
# U2FsdGVkX1+KgS+cZFc26KNss7416P1ocgpNdWKP6hu/u42uVzR+Rt1uYVEbV5jThz4r8Ju2/rC19r2rqCc8Aw== authentication-key-encrypted
#
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 authentication ipsec spi 566 sha1
# U2FsdGVkX18Dmg2PY5pefS+Px6uf3eusD3/p7geRI+CKbEhhu6dCz0LjkFfHpo30xkotd2RGEEbu3O8H1u/Hst8Em8ijgBzSVvXOiD9QbTQ= authentication-key-encrypted
# !
# interface Eth1/3
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile2
# ipv6 ospfv3 cost 30
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 encryption ipsec spi 444 esp null
# sha1 U2FsdGVkX1/TRX7fZMWcSi4IqDpv+JEkvzsOC8wKb4rOw5a+DiQyDcsZj8nQTaP5C6ydcL/IHoB9lSa0djS6KQ== encryption-key-encrypted
# !
# sonic#


# Using overridden

# Before state:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile1
# ipv6 ospfv3 cost 20
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 priority 20
# !
# interface Eth1/2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 authentication ipsec spi 566 sha1
# U2FsdGVkX18Dmg2PY5pefS+Px6uf3eusD3/p7geRI+CKbEhhu6dCz0LjkFfHpo30xkotd2RGEEbu3O8H1u/Hst8Em8ijgBzSVvXOiD9QbTQ= authentication-key-encrypted
# !
# interface Eth1/3
# ipv6 ospfv3 bfd
# ipv6 ospfv3 network point-to-point
# ipv6 ospfv3 area 3.3.3.3
# ipv6 ospfv3 encryption ipsec spi 444 esp null
# sha1 U2FsdGVkX1/TRX7fZMWcSi4IqDpv+JEkvzsOC8wKb4rOw5a+DiQyDcsZj8nQTaP5C6ydcL/IHoB9lSa0djS6KQ== encryption-key-encrypted
# !
# sonic#

- name: Override the OSPFv3_interface configurations
  sonic_ospfv3_interfaces:
    config:
      - name: 'Eth1/3'
        advertise: 'test1'
        area_id: '2.2.2.2'
        cost: 30
        passive: true
        priority: 20
        hello_interval: 10
        dead_interval: 40
        mtu_ignore: true
        bfd:
          enable: true
          bfd_profile: 'profile2'
        network: broadcast
        ospfv3ipsec:
          authentication:
            spi_value: 888
            authentication_type: 'IPSEC'
            authentication_algorithm: 'MD5'
            authentication_key: 'U2FsdGVkX1/zmIu9qjNBGjK+itJO2cU/4EES17fBhljI3Jy4HkHCBHYQyY2WQbg3/BQu9Wv6ZbUMQoV1G9DqVQ=='
            authentication_key_encrypted: true
    state: overridden

# After state:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
# !
# interface Eth1/2
# !
# interface Eth1/3
# ipv6 ospfv3 advertise prefix-list test1
# ipv6 ospfv3 area 2.2.2.2
# ipv6 ospfv3 bfd
# ipv6 ospfv3 bfd profile profile2
# ipv6 ospfv3 cost 30
# ipv6 ospfv3 dead-interval 40
# ipv6 ospfv3 hello-interval 10
# ipv6 ospfv3 mtu-ignore
# ipv6 ospfv3 network broadcast
# ipv6 ospfv3 passive
# ipv6 ospfv3 priority 20
# ipv6 ospfv3 authentication ipsec spi 888
# md5 U2FsdGVkX1/zmIu9qjNBGjK+itJO2cU/4EES17fBhljI3Jy4HkHCBHYQyY2WQbg3/BQu9Wv6ZbUMQoV1G9DqVQ== authentication_key_encrypted
# !
# sonic#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after(generated):
  description: The generated configuration model invocation.
  returned: when C(check_mode)
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.ospfv3_interfaces.ospfv3_interfaces import Ospfv3_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.ospfv3_interfaces.ospfv3_interfaces import Ospfv3_interfaces


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Ospfv3_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Ospfv3_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
