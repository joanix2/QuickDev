import os
import click
from cli.init import init_app
from compiler.parser import parse_xml_to_app
from gpt.gpt import create_graphql_schema
from cli.build import build_app
from cli.clean import clean_app
from cli.run import run_app
from utils.template import load_file

@click.group()
def cli():
    """Simple CLI for project management."""
    pass

@cli.command()
def init():
    """
    Create init file
    """
    click.echo("creating new project")
    init_app()

@cli.command()
@click.option('--path', default=os.getcwd(), type=click.Path(), help="Path to save the schema (default: current directory).")
@click.option('--model', default="gpt-4", type=str, help="Model to use for schema generation (default: gpt-4).")
def create_schema(path, model):
    """Create the GraphQL schema."""
    click.echo(f"Generating GraphQL schema using model '{model}'...")
    create_graphql_schema(path=path, model=model)

@cli.command()
@click.option('--input', required=True, type=click.Path(), help="Input dsl file")
@click.option('--output', default=os.getcwd(), type=click.Path(), help="Path to save the app (default: current directory).")
def build(input, output):
    """Build the project."""
    click.echo(f"Reading config file '{input}'...")
    app = parse_xml_to_app(load_file(input))
    click.echo(f"Building the project with name '{app.name}'...")
    build_app(path=output, app=app)
    click.echo("Build complete.")

@cli.command()
def clean():
    """Clean the build directory."""
    click.echo("Cleaning the build directory...")
    clean_app()

@cli.command()
def run():
    """Run the main script."""
    click.echo("Running the project...")
    run_app()

if __name__ == "__main__":
    cli()
