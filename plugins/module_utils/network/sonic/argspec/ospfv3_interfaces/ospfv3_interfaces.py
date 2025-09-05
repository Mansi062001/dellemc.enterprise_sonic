from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Ospfv3_interfacesArgs(object):
    """The arg spec for the sonic_ospfv3_interfaces module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'bfd': {
                    'options': {
                        'bfd_profile': {'type': 'str'},
                        'enable': {'required': True, 'type': 'bool'}
                    },
                    'type': 'dict'
                },
                'name': {'required': True, 'type': 'str'},
                'network': {
                    'choices': ['broadcast', 'point_to_point'],
                    'type': 'str'
                },
                'area_id': {'type': 'str'},
                'cost': {'type': 'int'},
                'dead_interval': {'type': 'int'},
                'hello_interval': {'type': 'int'},
                'mtu_ignore': {'type': 'bool'},
                'priority': {'type': 'int'},
                'retransmit_interval': {'type': 'int'},
                'transmit_delay': {'type': 'int'},
                'passive': {'type': 'bool'},
                'advertise': {'type': 'str'},
                'ospfv3ipsec': {
                    'type': 'dict',
                    'mutually_exclusive': [['authentication', 'encryption']],
                    'options': {
                        'authentication': {
                            'type': 'dict',
                            'options': {
                                'authentication_algorithm': {'type': 'str', 'required': True, 'choices': ['MD5', 'SHA1', 'SHA256']},
                                'authentication_key': {'type': 'str', 'no_log': True, 'required': True},
                                'authentication_key_encrypted': {'type': 'bool', 'required': True},
                                'authentication_type': {'type': 'str', 'required': True, 'choices': ['IPSEC']},
                                'spi_value': {'type': 'int', 'required': True}
                            }
                        },
                        'encryption': {
                            'type': 'dict',
                            'options': {
                                'encryption_type': {'type': 'str', 'required': True, 'choices': ['IPSEC']},
                                'encryption_algorithm': {'type': 'str', 'required': True, 'choices': ['3DES', 'DES', 'AES_CBC_128', 'AES_CBC_192', 'NULL']},
                                'encryption_key': {'type': 'str', 'no_log': True},
                                'encryption_key_encrypted': {'type': 'bool'},
                                'authentication_algorithm': {'type': 'str', 'required': True, 'choices': ['MD5', 'SHA1', 'SHA256']},
                                'authentication_key': {'type': 'str', 'required': True, 'no_log': True},
                                'authentication_key_encrypted': {'type': 'bool', 'required': True},
                                'spi_value': {'type': 'int', 'required': True}
                            }
                        }
                    }
                }
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged',
            'type': 'str'
        }
    }
