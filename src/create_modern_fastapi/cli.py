import click
import questionary
from importlib.metadata import version
from create_modern_fastapi import service
from create_modern_fastapi.domain import Entities, EntityType


@click.group(invoke_without_command=True)
@click.version_option(version("create-modern-fastapi"), "-v", "--version")
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        option = questionary.select(
            "Select an action:", choices=["Create a new project", "Add a new entity"]
        ).ask()
        if option == "Create a new project":
            ctx.invoke(create)
        elif option == "Add a new entity":
            ctx.invoke(add)


@main.command()
@click.argument("project_folder_path", required=False)
@click.option("--no-git", is_flag=True, default=False, help="Do not initialize a git repository.")
def create(project_folder_path: str | None, no_git: bool) -> None:
    if project_folder_path:
        resolved_project_folder_path = project_folder_path
    else:
        project_name = questionary.text("What is the project name?").ask()
        if not project_name:
            raise click.BadParameter("Project name cannot be empty")
        resolved_project_folder_path = project_name.strip()

    project_description = questionary.text("Project description (optional):").ask()
    service.create_project(
        resolved_project_folder_path,
        project_description,
        init_git=not no_git,
    )


@main.command()
@click.argument("entity_type", type=click.Choice(Entities), required=False)
def add(entity_type: str):
    entity = entity_type
    if not entity:
        entity = questionary.select(
            "Select entity type to add :", choices=Entities
        ).ask()
        if not entity:
            raise click.BadParameter("Entity type cannot be empty")
    service.add_entity(EntityType(entity))
