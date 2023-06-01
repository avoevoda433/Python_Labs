access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

def generate_access_config(access):
    result = []
    for intf, vlan in access.items():
        result.append('interface ' + intf)
        for command in access_template:
            result.append('{} {}'.format(command, vlan if command.endswith('access vlan') else ''))

    return result
            

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

print(generate_access_config(access_dict))
