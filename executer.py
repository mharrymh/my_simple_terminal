from saved_commands import save_commands as save 
from saved_commands import load_commands as commands 
from errors_manager import SyntaxError , ParsingError, ExecutionError
import os

def run(user_input:str)->None:
    tokens:list = user_input.split() #Remove special characters and return a list
    if (len(tokens) == 0 or not parse(tokens[:])):
        return
    execute(tokens)

def parse(tokens:list)->bool:
    token = tokens.pop(0)
    if token == 'add':
        return parse_add_expr(tokens)
    elif token == 'rm':
        return parse_rm_expr(tokens)
    elif token == 'ls' or token == 'exit':
        if len(tokens) != 0:
            error = ParsingError(f'"{tokens[0]}" is not an accepted command after "{token}".\nTry with only "{token}" next time.')
            error.display()
            return False
    else:
        if not token in commands():
            error = ParsingError(f'"{token}" is not an existing command.\nTry with "ls" to see available commands.\nTry with "add [command] [path]" to add a new command')
            error.display()
            return False
        elif len(tokens) != 0:
            error = SyntaxError(f'"{tokens[0]}" not valid after: "{token}"')
            error.display()
            return False
    return True
        

def parse_add_expr(tokens:list)->bool:
    if len(tokens) != 2:
        error = ParsingError(f'"add" command only accepts two arguments.\nTry with "add [command] [path]"')
        error.display()
        return False
    return True


def parse_rm_expr(tokens:list)->bool:
    if len(tokens) != 1:
        error = ParsingError(f'"rm" command only accepts one argument.\nTry with "rm [command]"')
        error.display()
        return False
    elif tokens[0] not in commands():
        error = ParsingError(f'"{tokens[0]}" is not an existing command.')
        error.display()
        return False
    return True

def ls(orders, display):
    message = " ".join(commands().keys())
    display(message)

def exit(orders, display):
    from open_terminal import window
    window.destroy()

def add(orders, display):
    command, path = tuple(orders)
    if os.path.isfile(path):
        save({command : path})
        display(f'Your command {command} was added successfully!')
    else:
        error = ExecutionError(f'{path} is not a valid path.\nTry again!')
        error.display()

def rm(orders, display):
    command = orders[0]
    saved_commands = commands()
    saved_commands.remove(command)
    save(saved_commands, overwrite=True)
    display(f'Your command {command} was removed successfully!')


def execute_command(command):
    saved_commands = commands()
    path = saved_commands[command]

    try:
        os.startfile(path)  # Only in windows
    except Exception as e:
        error = ExecutionError(f"Error opening the file: {e}")



execution_dict = {
    'ls' : ls,
    'exit' : exit,
    'add' : add,
    'rm' : rm
}

def execute(tokens:list)->None:
    token = tokens.pop(0)
    if token in execution_dict:
        from open_terminal import insert_prompt
        execution_dict[token](tokens, insert_prompt)
    else:
        execute_command(token)


