ECHO_LABEL = "\033[1;36m[gitino]\033[0m"


VERSION = "0.0.3"


PROG_NAME = "Gitigno"


START_MESSAGE = f"""
\033[0;30;42m {PROG_NAME.lower()} \033[0;32m {VERSION} \033[0m \n
\u2592 Generate a .gitignore template for your project. \033[0;36mThe file will be created on the current directory\033[0m
\u2592 This package uses the gitignore.io API. For more info visit the docs at \033[0;36mhttps://docs.gitignore.io/use/api \033[0m
\u2592 Author:  \033[1;35m Minenhle Ngubane (https://minenhlengubane.com)\033[0m
"""

ERROR_TEXT = """
\033[1;33m Check the following:\033[0m
\033[0;37m 1. Make sure your spelling is correct for every template name.\033[0m
\033[0;37m 2. Check if you entered an existing template name. Try \033[1;36m"python gitigno --tnames"\033[0m to see available templates
\033[0;37m 3. Check your internet connection.\033[0m
"""

