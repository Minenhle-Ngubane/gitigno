import click
import requests


def request_gitignore(templates):
    url = f"https://www.toptal.com/developers/gitignore/api/{','.join(templates)}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None
    

def show_available_templates(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("    The following table only contains some of the available templates.\033[1;36m Go to https://github.io for the full list\033[0m")
    display_available_templates_table()
    ctx.exit()

    
def display_text_block(text):
    lines = text.split("\n")
    indented_lines = ["    " + line for line in lines]
    block_text = "\n".join(indented_lines)
    click.echo(block_text)

    
def display_ascii_art():
    art = r"""""""""
    
    ░██████╗░██╗████████╗██╗░██████╗░███╗░░██╗░█████╗░
    ██╔════╝░██║╚══██╔══╝██║██╔════╝░████╗░██║██╔══██╗
    ██║░░██╗░██║░░░██║░░░██║██║░░██╗░██╔██╗██║██║░░██║
    ██║░░╚██╗██║░░░██║░░░██║██║░░╚██╗██║╚████║██║░░██║
    ╚██████╔╝██║░░░██║░░░██║╚██████╔╝██║░╚███║╚█████╔╝
    ░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░                            
    """""""""""
    
    click.echo("\033[32m" + art + "\033[0m")


def display_available_templates_table():
    table = r"""
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗  
    ║   adobe                  advancedinstaller   c                   c++                 elisp               elixir         ║ 
    ║   adventuregamestudio    agda                codekit             codesniffer         elm                 emacs          ║ 
    ║   alteraquartusii        altium              codeio              coffeescript        ember               ensime         ║ 
    ║   amplify                android             commonlisp          compodoc            erlang              espresso       ║
    ║   androidstudio          angular             composer            compressed          executable          exercism       ║
    ║   anjuta                 ansible             compressedarchive   compression         expressionengine    extjs          ║
    ║   ansibletower           apachecordova       conan               concrete5           git                 gitbook        ║
    ║   apachehadoop           appbuilder          coq                 cordova             go                  goland         ║
    ║   appcode                appcode+all         craftcms            crashlytics         goland+all          goland+iml     ║
    ║   appcode+iml            appengine           diff                diskimage           godot               goodsync       ║
    ║   appceleratortitanium   aptanastudio        django              docfx               gradle              grails         ║
    ║   assembler              astro               dotfilessh          dotnetcore          helm                hexo           ║
    ║   atmelstudio            audio               dreamweaver         dropbox             redis               remix          ║
    ║   autohotkey             automationstudio    drupal              drupal7             vue                 vuejs          ║
    ║   autotools              autotools+strict    drupal8             episerver           visualstudiocode    vivado         ║
    ║   azurefunctions         azurite             eagle               eclipse             visualbasic         visualstudio   ║
    ║   backup                 ballerina           eiffelstudio        elasticbeanstalk    virtualenv          virtuoso       ║             
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝                      
    """
    
    click.echo("\033[32m" + table + "\033[0m")
    