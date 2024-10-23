import json

#File where commands will be saved
COMMANDS_JSON = 'commands.json'

def save_commands(commands:dict, overwrite:bool = False)->None:
    """Update and save commands in a json file"""
    if not overwrite:
        commands = load_commands() | commands
    with open(COMMANDS_JSON, 'w') as file:
        json.dump(commands, file)


def load_commands()->dict:
    '''Load commands from the json file'''
    try:
        with open(COMMANDS_JSON, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

