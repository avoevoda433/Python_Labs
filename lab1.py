# Ex. 3.1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(f"\nEx. 3.1\n{NAT.replace('Fast', 'Gigabit')}")


# Ex. 3.2
MAC = 'AAAA:BBBB:CCCC'
print(f"\nEx. 3.2\n{MAC.replace(':', '.')}")


# Ex. 3.3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(f"\nEx. 3.3\n{CONFIG.split()[-1].split(',')}")


# Ex. 3.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
print(f"\nEx. 3.4\n{list(map(int, set(command1.split()[-1].split(',')) & set(command2.split()[-1].split(','))))}")


# Ex. 3.5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(f"\nEx. 3.5\n{sorted(set(VLANS))}")


# Ex. 3.6
labels = ('Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface')
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace(',', '').split()
ospf_route[2] = ospf_route[2][1:-1]
ospf_route.remove('via')

print(f"\nEx. 3.6\n"
	  f"{labels[0]}:{' '*(25-len(labels[0]))}{ospf_route[0]}\n"
	  f"{labels[1]}:{' '*(25-len(labels[1]))}{ospf_route[1]}\n"
	  f"{labels[2]}:{' '*(25-len(labels[2]))}{ospf_route[2]}\n"
	  f"{labels[3]}:{' '*(25-len(labels[3]))}{ospf_route[3]}\n"
	  f"{labels[4]}:{' '*(25-len(labels[4]))}{ospf_route[4]}\n"
	  f"{labels[5]}:{' '*(25-len(labels[5]))}{ospf_route[5]}")


# Ex. 3.7
MAC = 'AAAA:BBBB:CCCC'
bin_mac = '0x'+MAC.replace(':', '')
print(f"\nEx. 3.7\n{bin(int(bin_mac, 16))}")


# Ex. 3.8
IP = '192.168.3.1'.split('.')
bin_ip = [format(number, 'b') for number in map(int, IP)]
print(f"\nEx. 3.8\n"
	  f"{IP[0]+' '*(10-len(IP[0]))}"
	  f"{IP[1]+' '*(10-len(IP[1]))}"
	  f"{IP[2]+' '*(10-len(IP[2]))}"
	  f"{IP[3]+' '*(10-len(IP[3]))}\n"
	  f"{'0'*(8-len(bin_ip[0]))+bin_ip[0]}  "
	  f"{'0'*(8-len(bin_ip[1]))+bin_ip[1]}  "
	  f"{'0'*(8-len(bin_ip[2]))+bin_ip[2]}  "  
	  f"{'0'*(8-len(bin_ip[3]))+bin_ip[3]}  ")

# Ex. 3.9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

elem = 'ruby'
use_list = word_list

print(f"\nEx. 3.9\n{len(use_list)-use_list[::-1].index(elem)-1}")
