from abc import ABC


class Error(ABC):
    def __init__(self, message):
        # Inicializar el atributo de instancia message
        self.message = message

    def display(self):
        from open_terminal import insert_prompt
        insert_prompt(self.message)

class SyntaxError(Error):
    def __init__(self, message):
        super().__init__('SyntaxError: ' + message)

class ParsingError(Error):
    def __init__(self, message):
        super().__init__('ParsingError: ' + message)

class ExecutionError(Error):
    def __init__(self, message):
        super().__init__('ExecutionError: ' + message)

