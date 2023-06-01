def get_int_vlan_map(file_name):
    try:
        config_file = open(file_name, 'r')
    except FileNotFoundError:
        print(f"File {file_name} is not found!")
        return False

    access_dict = {}
    trunk_dict = {}

    isInterface = False
    for line in config_file:
        try:
            line_list = line.split()
            if ("interface" in line_list and "Ethernet" in line_list[1]):
                isInterface = True
                int = line_list[1]
                continue
            if (isInterface and "switchport" in line_list):
                if "vlan" in line_list:
                    if "trunk" in line_list:
                        trunk_dict.update({int: line_list[-1].split(',')})
                    else:
                        access_dict.update({int: line_list[-1]})
                else:
                    continue
        except(IndexError):
            continue
        isInterface = False

    return access_dict, trunk_dict
    
file = 'config_sw1.txt'
print(get_int_vlan_map(file))
