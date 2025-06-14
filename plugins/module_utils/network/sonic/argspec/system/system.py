#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the sonic_system module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class SystemArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_system module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'anycast_address': {
                    'options': {
                        'ipv4': {'type': 'bool'},
                        'ipv6': {'type': 'bool'},
                        'mac_address': {'type': 'str'}
                    },
                    'type': 'dict'
                },
                'hostname': {'type': 'str'},
                'audit_rules': {
                    'choices': ['BASIC', 'DETAIL', 'CUSTOM', 'NONE'],
                    'type': 'str'
                },
                'interface_naming': {
                    'choices': ['standard', 'standard_extended', 'native'],
                    'type': 'str'
                },
                'auto_breakout': {
                    'choices': ['ENABLE', 'DISABLE'],
                    'type': 'str'
                },
                'load_share_hash_algo': {
                    'choices': ['CRC', 'XOR', 'CRC_32LO', 'CRC_32HI', 'CRC_CCITT', 'CRC_XOR', 'JENKINS_HASH_LO', 'JENKINS_HASH_HI'],
                    'type': 'str'
                },
                'password_complexity': {
                    'options': {
                        'min_length': {'type': 'int'},
                        'min_lower_case': {'type': 'int'},
                        'min_numerals': {'type': 'int'},
                        'min_spl_char': {'type': 'int'},
                        'min_upper_case': {'type': 'int'}
                    },
                    'type': 'dict',
                    'no_log': False
                },
                'concurrent_session_limit': {'type': 'int'},
                'adjust_txrx_clock_freq': {'type': 'bool'},
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'replaced', 'overridden', 'deleted'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
