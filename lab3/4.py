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
    subcommands = []

    isInterface = False
    for line in config_file:
        try:
            line_list = line.split(" ")

            if (not ignore_command(line_list,ignore) and not("!" in line_list[0]) and not("\n" in line_list[0])):
                if (not("" == line_list[0])):
                    commands.update({command: subcommands})
                    subcommands = []
                    command = line.replace("\n","")
                else:
                    subcommands.append(line[1:].replace("\n",""))

            else:
                continue
            
        except(IndexError):
            continue
        isInterface = False

    commands.pop("")

    return commands


result = config_to_dict("config_sw1.txt")

for command, subcommands in result.items():
        print(command)
        if subcommands != []:
            for subcommand in subcommands:
                print(f"\t{subcommand}")
