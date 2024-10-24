from saved_commands import save_commands as save 
from saved_commands import load_commands as commands 
from errors_manager import SyntaxError , ParsingError, ExecutionError
import os
import shlex
import webbrowser
import requests

def run(user_input:str, display_message)->None:
    tokens:list = shlex.split(user_input) #Remove special characters and return a list
    if (len(tokens) == 0 or not parse(tokens[:], display_message)):
        return
    execute(tokens, display_message)

def parse(tokens:list, display_message)->bool:
    token = tokens.pop(0)
    if token == 'add':
        return parse_add_expr(tokens, display_message)
    elif token == 'rm':
        return parse_rm_expr(tokens, display_message)
    elif token == 'ls' or token == 'exit':
        if len(tokens) != 0:
            error = ParsingError(f'"{tokens[0]}" is not an accepted command after "{token}".\nTry with only "{token}" next time.', display_message)
            error.display()
            return False
    else:
        if not token in commands():
            error = ParsingError(f'"{token}" is not an existing command.\nTry with "ls" to see available commands.\nTry with "add [command] [path]" to add a new command', display_message)
            error.display()
            return False
        elif len(tokens) != 0:
            error = SyntaxError(f'"{tokens[0]}" not valid after: "{token}"', display_message)
            error.display()
            return False
    return True
        

def parse_add_expr(tokens:list, display_message)->bool:
    if len(tokens) != 2:
        error = ParsingError(f'"add" command only accepts two arguments.\nTry with "add [command] [path]"', display_message)
        error.display()
        return False
    return True


def parse_rm_expr(tokens:list, display_message)->bool:
    if len(tokens) != 1:
        error = ParsingError(f'"rm" command only accepts one argument.\nTry with "rm [command]"', display_message)
        error.display()
        return False
    elif tokens[0] not in commands():
        error = ParsingError(f'"{tokens[0]}" is not an existing command.', display_message)
        error.display()
        return False
    return True

def ls(orders, display):
    commands_names = commands().keys()
    if len(commands_names) == 0:
        display('\nNot available commands!\nTry adding some with "add [command] [path]"')
        return
    for c in commands_names:
        display('\n' + c)

def exit(orders, display):
    display('\nExiting!!')

def is_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        # Check if the response code is in the 200 range
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        # If there was an issue with the request (e.g., invalid URL format), return False
        return False

def add(orders, display):
    command, path = tuple(orders)
    if os.path.isfile(path) or os.path.isdir(path) or is_url(path):
        save({command : path})
        display(f'\nYour command {command} was added successfully!')
    else:
        error = ExecutionError(f'{path} is not a valid path or url.\nTry again!\nNote: The path has to be inside quotation marks', display)
        error.display()

def rm(orders, display):
    command = orders[0]
    saved_commands = commands()
    saved_commands.pop(command)
    save(saved_commands, overwrite=True)
    display(f'\nYour command {command} was removed successfully!')


def execute_command(command):
    saved_commands = commands()
    path = saved_commands[command]

    try:
        if os.path.isfile(path) or os.path.isdir(path):
            os.startfile(path) # Only in windows
        else: #is a url
            webbrowser.open(path)
    except Exception as e:
        error = ExecutionError(f"Error opening: {e}")
        error.display()



execution_dict = {
    'ls' : ls,
    'exit' : exit,
    'add' : add,
    'rm' : rm
}

def execute(tokens:list, display_message)->None:
    token = tokens.pop(0)
    if token in execution_dict:
        execution_dict[token](tokens, display_message)
    else:
        execute_command(token)
