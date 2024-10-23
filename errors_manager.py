from abc import ABC


class Error(ABC):
    def __init__(self, message, display):
        # Inicializar el atributo de instancia message
        self.message = message
        self.display_function = display

    def display(self):
        self.display_function(self.message)

class SyntaxError(Error):
    def __init__(self, message, display):
        super().__init__('\nSyntaxError: ' + message, display)

class ParsingError(Error):
    def __init__(self, message, display):
        super().__init__('\nParsingError: ' + message, display)

class ExecutionError(Error):
    def __init__(self, message, display):
        super().__init__('\nExecutionError: ' + message, display)

