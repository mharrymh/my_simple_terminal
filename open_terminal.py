import tkinter as tk
import executer


# Create the main window
window = tk.Tk()
window.title('My terminal')
window.geometry('600x400')
window.iconbitmap('resources/terminal_icon.ico')  # Set window icon
window.config(bg='black')  # Set background color

# Create the text widget with a terminal-like appearance
text = tk.Text(window, bg='black', fg='white', insertbackground='white', font=('Consolas', 12), wrap='none')
text.pack(expand=True, fill='both')

def insert_prompt(prompt: str = 'Write your commands here>>> '):
    """Insert the prompt and mark its end to prevent deletion."""
    text.insert('end', prompt)
    text.mark_set('prompt_end', 'end-2c')  # Mark the end of the prompt
    text.mark_gravity('prompt_end', 'left')  # Keep prompt mark in place
    text.mark_set('insert', 'end')  # Move cursor to the end

def block_delete(event):
    """Block deletion if cursor is before the prompt."""
    if text.compare("insert", "<=", "prompt_end"):
        return "break"  # Prevent backspace if before prompt

def prevent_cursor_move(event):
    """Prevent cursor from moving before the prompt."""
    if text.compare("insert", "<", "prompt_end"):
        text.mark_set("insert", "end")  # Keep cursor after prompt
        return "break"


def execute(event):
    '''Execute the user input'''
    user_input = text.get('prompt_end', 'end')
    executer.run(user_input, insert_prompt)
    #Handle exit logic
    if 'Exiting!!' in text.get('1.0', 'end-1c'):
        window.destroy()
        return
    text.insert('end','\n') #Add a new line
    insert_prompt()
    
    return 'break' #Avoid adding a new line after 'Enter' is pressed

# Initialize the prompt
insert_prompt()

# Bind events to protect prompt area
text.bind('<BackSpace>', block_delete)  # Block backspace before prompt
text.bind("<KeyRelease>", prevent_cursor_move)  # Prevent moving cursor before prompt
text.bind("<Key>", prevent_cursor_move)
text.bind("<ButtonRelease-1>", prevent_cursor_move)  # Prevent mouse click before prompt

text.bind('<Return>', execute)

window.mainloop()
