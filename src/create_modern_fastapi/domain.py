from enum import Enum


class EntityType(str, Enum):
    Migration = "migration"
    Module = "module"
    Service = "service"
    UseCase = "use_case"


Entities = [e.value for e in EntityType]
