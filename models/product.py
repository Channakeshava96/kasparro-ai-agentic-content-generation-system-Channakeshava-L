from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    concentration: str
    skin_type: List[str]
    ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str
