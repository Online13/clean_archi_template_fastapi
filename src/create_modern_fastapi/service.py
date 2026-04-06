from create_modern_fastapi.commands.add import registry
from create_modern_fastapi.commands.create import create_folder, create_template
from create_modern_fastapi.domain import EntityType


def create_project(
    project_folder_path: str,
    project_description: str,
    init_git: bool = True,
) -> None:
    target_path = create_folder(project_folder_path)
    create_template(target_path, project_description, init_git=init_git)


def add_entity(type: EntityType) -> None:
    action = registry.get(type)
    action()
