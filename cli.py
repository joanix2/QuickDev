import os
import click
from gpt.ask import poser_question
from gpt.gpt import create_graphql_schema
from make.build import build_app
from make.clean import clean_app
from make.run import run_app

@click.group()
def cli():
    """Simple CLI for project management."""
    pass

@cli.command()
@click.option('--path', default=os.getcwd(), type=click.Path(), help="Path to save the schema (default: current directory).")
@click.option('--model', default="gpt-4", type=str, help="Model to use for schema generation (default: gpt-4).")
def create_schema(path, model):
    """Create the GraphQL schema."""
    click.echo(f"Generating GraphQL schema using model '{model}'...")
    create_graphql_schema(path=path, model=model)

@cli.command()
@click.option('--name', required=True, type=str, help="Name of the application to build.")
def build(name):
    """Build the project."""
    click.echo(f"Building the project with name '{name}'...")
    build_app(name=name)
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
