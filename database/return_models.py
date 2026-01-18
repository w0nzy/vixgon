from dataclasses import dataclass,field


@dataclass
class ShelfDataModel:
    shelf_name: str = field(default = "no_shelf")