from saved_commands import save_commands , load_commands as save , commands
import errors_manager

def run(user_input:str)->None:
    tokens:list = user_input.split() #Remove special characters and return a list
    parse(tokens[:])
    # execute(tokens)

def parse(tokens:list)->None:
    token = list.pop(0)
    if token == 'add':
        parse_add_expr(tokens)
    elif token == 'rm':
        parse_rm_expr(tokens)
    elif token == 'ls' or token == 'exit':
        if len(tokens) != 0:
            #TODO: LANZA ERROR
            return
    else:
        if not token in commands():
            #TODO: Lanza error
            return
        elif len(tokens) != 0:
            #TODO: Lanza error
            return
        

def parse_add_expr(tokens:list)->None:
    if len(tokens) != 2:
        #TODO: Lanza error
        return


def parse_rm_expr(tokens:list)->None:
    if len(tokens) != 1:
        #TODO: Lanza error
        return
    elif tokens[0] not in commands():
        #TODO: Lanza error
        return




