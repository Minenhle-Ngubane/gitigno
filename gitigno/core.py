import click

from .constants import (
    START_MESSAGE,
    ERROR_TEXT,
    ECHO_LABEL,
    VERSION,
    PROG_NAME,
)

from .utils import (
    display_text_block, 
    request_gitignore, 
    display_ascii_art, 
    display_available_templates_table,
    show_available_templates
)


@click.group()
@click.version_option(version=VERSION, prog_name=PROG_NAME)
@click.option(
    "--tnames", 
    is_flag=True, 
    callback=show_available_templates, 
    expose_value=False, 
    is_eager=True,
    help="Show a list of available templates in table form and exit."
)
@click.pass_context
def cli(ctx):
    subcommand = ctx.invoked_subcommand
    
    if subcommand == "create":
        click.echo("\033[H\033[J")
        display_ascii_art()
        display_text_block(START_MESSAGE)


@cli.command()
@click.option(
    "-t",
    "--template",
    prompt="Enter Template name(s) (Template names must be separated by commas)", 
    help="Name(s) used to generate the required .gitignore file",
)
def create(template):
    gitignore_content = request_gitignore(template.split(","))

    if gitignore_content:
        with open(".gitignore", "w") as f:
            f.write(gitignore_content)
            click.echo(ECHO_LABEL + "\033[1;32m \u2713\u2713 \U0001F600 \U0001F44D .gitignore file created successfully.\033[0m")
    
    else:
        click.echo(ECHO_LABEL + f"\033[1;31m \U00002716 \U00002716 \U0001F614 \U0001F44E Failed to generate .gitignore file for {template}.\033[0m")
        display_text_block(ERROR_TEXT)


if __name__ == "__main__":
    cli()