access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

port_security = ['switchport port-security maximum 2',
                 'switchport port-security violation restrict',
                 'switchport port-security']

def generate_access_config(access, psecurity=False):
    result = dict.fromkeys([intf for intf in access], [])
    for intf, vlan in access.items():
        preres = []
        preres.append('interface ' + intf)
        for command in access_template:
            preres.append('{} {}'.format(command, vlan if command.endswith('access vlan') else ''))
        if psecurity:
            for command in port_security:
                preres.append('{}'.format(command))
        result[intf] = preres

    return result
            

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

print(generate_access_config(access_dict))