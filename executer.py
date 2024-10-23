from saved_commands import save_commands as save 
from saved_commands import load_commands as commands 
from errors_manager import SyntaxError , ParsingError, ExecutionError
import os

def run(user_input:str, display_message)->None:
    tokens:list = user_input.split() #Remove special characters and return a list
    if (len(tokens) == 0 or not parse(tokens[:], display_message)):
        return
    execute(tokens, display_message)

def parse(tokens:list, display_message)->bool:
    print(tokens)
    token = tokens.pop(0)
    print(tokens)
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

def add(orders, display):
    command, path = tuple(orders)
    if os.path.isfile(path):
        save({command : path})
        display(f'Your command {command} was added successfully!')
    else:
        error = ExecutionError(f'{path} is not a valid path.\nTry again!', display)
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
        os.startfile(path)  # Only in windows
    except Exception as e:
        error = ExecutionError(f"Error opening the file: {e}")
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
