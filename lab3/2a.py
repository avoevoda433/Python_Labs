trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']


def generate_trunk_config(trunk):
    result = dict.fromkeys([intf for intf in trunk], [])
    for intf, vlans in trunk.items():
        preres = []
        preres.append('interface ' + intf)
        for command in trunk_template:
            preres.append('{} {}'.format(command, ','.join([str(vlan) for vlan in vlans]) if command.endswith('allowed vlan') else ''))
        result[intf] = preres

    return result
            

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }


print(generate_trunk_config(trunk_dict))