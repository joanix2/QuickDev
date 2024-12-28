import os
import click
from compiler.parser import parse_yaml_with_checks
from gpt.ask import poser_question
from gpt.gpt import create_graphql_schema
from cli.build import build_app
from cli.clean import clean_app
from cli.run import run_app

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
@click.option('--config', required=True, type=click.Path(), help="Path to get the app config")
@click.option('--path', default=os.getcwd(), type=click.Path(), help="Path to save the app (default: current directory).")
def build(name, config, path):
    """Build the project."""
    click.echo(f"Reading config file '{config}'...")
    db, api, front = parse_yaml_with_checks(config)
    click.echo(f"Building the project with name '{name}'...")
    build_app(path=path, name=name, db=db, api=api, front=front)
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
