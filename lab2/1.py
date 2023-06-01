ip_address_str = input("Введите IP-адрес в формате 10.0.1.1: ")
ip_address_list = list(map(int,ip_address_str.split('.')))

if ip_address_list[0] >= 1 and ip_address_list[0] < 128 :
    class_of_address = 'A'
elif ip_address_list[0] >= 128 and ip_address_list[0] < 192 :
    class_of_address = 'B'
elif ip_address_list[0] >= 192 and ip_address_list[0] < 224 :
    class_of_address = 'C'
else:
    class_of_address = 'D'

if ip_address_str == "255.255.255.255" :
    print("local broadcast")
elif ip_address_str == "0.0.0.0" :
    print("unassigned")
elif class_of_address in 'ABC' :
    print("unicast")
elif class_of_address == 'D' :
    print("multicast")
else:
    print("unused")
