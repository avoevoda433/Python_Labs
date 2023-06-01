ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    ignore_command = False
    for word in ignore:
        if word in command:
            return True
    return ignore_command

def config_to_dict(config):
    try:
        config_file = open(config, 'r')
    except FileNotFoundError:
        print(f"File {config} is not found!")
        return False

    commands = {}
    command = ""
    subcommand = ""
    subcommands = {}
    subsubcommands = []
    isthreeLevel = False

    for line in config_file:
        try:
            line_list = line.split(" ")
            if (not ignore_command(line_list,ignore) and not("!" in "".join(line_list[0:2])) and not("\n" in line_list[0])):
                if (("" == line_list[0])):
                    if (("" == line_list[1])):
                        subsubcommands.append(line[2:-1])
                        isthreeLevel = True
                    else:
                        subcommand = line[1:-1]
                        subcommands.update({subcommand: subsubcommands})
                        subsubcommands = []
                else:
                    if(not isthreeLevel):
                        subcommands = [subcommand for subcommand in list(subcommands.keys())]
                    else:
                        subcommands[subcommand] = [subsubcommand for subsubcommand in subsubcommands]
                        isthreeLevel = False
                    commands.update({command: subcommands})
                    command = line[:-1]
                    subcommands = {}
            else:
                continue
            
        except(IndexError):
            continue
        isInterface = False

    commands.pop("")

    return commands


result = config_to_dict("config_r1.txt")

for command, subcommands in result.items():
    print(command)
    try:
        subcom = subcommands.items()
        print("{")
        for subcommand, subsubcommands in subcom:
            print(f"\t{subcommand}")
            if (len(subsubcommands) > 0):
                print("\t[")
                for subsubcommand in subsubcommands:
                    print(f"\t\t{subsubcommand}")
                print("\t]")
        print("}")
    except(AttributeError):
        if subcommands != []:
            print("[")
            for subcommand in subcommands:
                print(f"\t{subcommand}")
            print("]")