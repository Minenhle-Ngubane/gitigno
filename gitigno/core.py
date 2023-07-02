import click

from constants import (
    START_MESSAGE,
    ERROR_MESSAGE,
    VERSION,
    PROG_NAME,
)

from utils import (
    fetch_templates, 
    display_ascii_art, 
    display_template_names_table
)


# Define the main command group for the CLI
@click.group()
@click.pass_context
@click.version_option(version=VERSION, prog_name=PROG_NAME)
@click.option(
    "--tnames", 
    is_flag=True, 
    callback=display_template_names_table, 
    expose_value=False, 
    is_eager=True,
    help="Show a list of available templates in table form and exit."
)
def cli(ctx):
    # Determine the subcommand that was invoked
    subcommand = ctx.invoked_subcommand
    
    # If the subcommand is 'create', display ASCII art and welcome text
    if subcommand == "create":
        click.clear() # Clear the console to start with a clean presentation
        display_ascii_art() # Display ASCII art representing the CLI
        click.echo(START_MESSAGE) # Display the welcome message


# Define the 'create' subcommand for the CLI
@cli.command()
@click.option(
    "-t",
    "--template",
    prompt="Enter Template name(s) (Template names must be separated by commas)", 
    help="Name(s) used to generate the required .gitignore file",
)
def create(template):
    # Request .gitignore content based on the given template names
    gitignore_content = fetch_templates(template.split(","))

    # If .gitignore content is generated successfully, write it to the file
    if gitignore_content:
        with open(".gitignore", "w") as f:
            f.write(gitignore_content)
            success_message = click.style(
                "\u2713\u2713 \U0001F600 \U0001F44D .gitignore file created successfully.",
                fg="green", 
                bold=True
            )
            click.echo(success_message)
    
    # If there's an error, display a failure message
    else:
        click.echo(ERROR_MESSAGE)


# Run the CLI if this script is executed directly
if __name__ == "__main__":
    cli()