isCurrent = False

while isCurrent == False:
    ip_address_str = input("Введите IP-адрес в формате 10.0.1.1: ")
    isCurrent = True
    try:
        ip_address_list = list(map(int, ip_address_str.split('.')))
    except ValueError:
        isCurrent = False
    if isCurrent and len(ip_address_list) <= 4:
        for num in ip_address_list:
            if num >= 0 and num <= 255:
                isCurrent = True
            else:
                isCurrent = False
                break
    else:
        isCurrent = False
    if isCurrent == False:
        print("Incorrect IPv4 address")

if ip_address_list[0] >= 1 and ip_address_list[0] < 128:
    class_of_address = 'A'
elif ip_address_list[0] >= 128 and ip_address_list[0] < 192:
    class_of_address = 'B'
elif ip_address_list[0] >= 192 and ip_address_list[0] < 224:
    class_of_address = 'C'
else:
    class_of_address = 'D'

if ip_address_str == "255.255.255.255":
    print("local broadcast")
elif ip_address_str == "0.0.0.0":
    print("unassigned")
elif class_of_address in 'ABC':
    print("unicast")
elif class_of_address == 'D':
    print("multicast")
else:
    print("unused")
