
from create_modern_fastapi.commands.add.add_module import add_module
from create_modern_fastapi.commands.add.add_migration import add_migration
from create_modern_fastapi.commands.add.add_service import add_service
from create_modern_fastapi.commands.add.add_use_case import add_use_case
from create_modern_fastapi.domain import EntityType


registry = {
    EntityType.Module: add_module,
    EntityType.Service: add_service,
    EntityType.UseCase: add_use_case,
    EntityType.Migration: add_migration,
}

def get(type: EntityType):
    action = registry.get(type)
    if not action:
        raise ValueError(f"No action found for entity type: {type}")
    return action