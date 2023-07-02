import click
import requests
from tabulate import tabulate


def fetch_templates(templates):
    try:
        url = f"https://www.toptal.com/developers/gitignore/api/{','.join(templates)}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful response status codes
        return response.text
    
    except (requests.exceptions.RequestException, IOError) as e:
        message = click.style(f"\U00002716 \U00002716 \U0001F614 \U0001F44E {str(e)}.", fg="red", bold=True)
        click.echo(message)
        return None
    

def display_template_names_table(ctx, param, value):
    if value and not ctx.resilient_parsing:
        generate_template_names_table()
        ctx.exit()


def generate_template_names_table():
    try:
        # Send GET request to gitignore.io API to fetch template names
        response = requests.get("https://www.gitignore.io/api/list?format=lines")
        response.raise_for_status()  # Raise an exception for unsuccessful response status codes
        template_names = response.text.splitlines()

        # Prepare table data
        table_data = []
        for i in range(0, len(template_names), 6):
            row = template_names[i:i + 6]
            table_data.append(row)

        # Generate and print the table
        table = tabulate(
            table_data, 
            headers=[
                "Template Name", 
                "Template Name",
                "Template Name",
                "Template Name",
                "Template Name",
                "Template Name"
            ], 
            tablefmt="fancy_grid"
        )
        click.clear()
        click.secho(table, fg="green")
        
    except (requests.exceptions.RequestException, IOError) as e:
        message = click.style(
            f"\U00002716 \U00002716 \U0001F614 \U0001F44E Error occurred while fetching template names.\n Details: {str(e)}",
            fg="red",
            bold=True
        )
        click.echo(message)
    
    
def display_ascii_art():
    art = """
    ░██████╗░██╗████████╗██╗░██████╗░███╗░░██╗░█████╗░
    ██╔════╝░██║╚══██╔══╝██║██╔════╝░████╗░██║██╔══██╗
    ██║░░██╗░██║░░░██║░░░██║██║░░██╗░██╔██╗██║██║░░██║
    ██║░░╚██╗██║░░░██║░░░██║██║░░╚██╗██║╚████║██║░░██║
    ╚██████╔╝██║░░░██║░░░██║╚██████╔╝██║░╚███║╚█████╔╝
    ░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░
    """

    click.secho(art, fg="green")