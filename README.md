# My Terminal Emulator

Este proyecto simula un terminal básico utilizando **Tkinter** en Python, que permite al usuario ejecutar comandos personalizados y gestionar sus propios comandos. Está diseñado para ser fácilmente extensible y manejable, con módulos dedicados para la ejecución de comandos, manejo de errores y persistencia de datos.

## Características

- **Interfaz gráfica** simulada de terminal con Tkinter.
- **Manejo de comandos personalizados**: Los usuarios pueden agregar, eliminar y ejecutar comandos.
- **Soporte para archivos y carpetas**: Los comandos pueden abrir archivos y directorios.
- **Persistencia de comandos**: Los comandos personalizados se guardan y cargan automáticamente usando archivos JSON.
- **Manejo de errores**: El sistema captura y reporta errores comunes como errores de sintaxis, parseo y ejecución.

## Requisitos

- Python 3.x
- Tkinter (parte del estándar de Python en la mayoría de distribuciones)
- `json` (biblioteca estándar en Python)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

2. Asegúrate de tener **Tkinter** instalado en tu sistema:

```bash
# En distribuciones basadas en Debian/Ubuntu
sudo apt-get install python3-tk

# En distribuciones basadas en Red Hat/Fedora
sudo dnf install python3-tkinter
```

3. Navega a la carpeta del proyecto:

```bash
cd tu_repositorio
```

## Uso

Ejecuta el archivo `open_terminal.py` para abrir la interfaz del terminal:

```bash
python open_terminal.py
```

### Comandos disponibles

- `add <comando> <ruta>`: Agrega un nuevo comando con la ruta al archivo o aplicación que se ejecutará.
  ```bash
  add mycommand "C:/Program Files/My App/app.exe"
  ```

- `rm <comando>`: Elimina un comando existente.
  ```bash
  rm mycommand
  ```

- `<comando>`: Abre un archivo o carpeta en el sistema operativo.
  ```bash
  mycommand
  ```

- `exit`: Cierra la consola.
  ```bash
  exit
  ```

- `ls`: Lista todos los comandos disponibles.
  ```bash
  comando_1
  comando_2
  ...
  comando_n
  ```

### Estructura del proyecto

- **`open_terminal.py`**: Controla la interfaz gráfica de Tkinter.
- **`executer.py`**: Recibe, parsea y ejecuta los comandos que el usuario ingresa, llamando las funciones apropiadas dependiendo del comando.
- **`saved_commands.py`**: Permite guardar y cargar comandos en un archivo JSON para que sean persistentes entre ejecuciones.
- **`errors_manager.py`**: Maneja errores específicos como errores de sintaxis, parseo o ejecución mediante clases de errores personalizadas.

