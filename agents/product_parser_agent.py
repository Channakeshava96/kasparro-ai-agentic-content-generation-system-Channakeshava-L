from agents.base_agent import BaseAgent
from models.product import Product

class ProductParserAgent(BaseAgent):
    """
    Agent responsible for converting raw product input data
    into a clean internal Product model.
    """

    def run(self, input_data: dict) -> Product:
        return Product(
            name=input_data["Product Name"],
            concentration=input_data["Concentration"],
            skin_type=input_data["Skin Type"].split(", "),
            ingredients=input_data["Key Ingredients"].split(", "),
            benefits=input_data["Benefits"].split(", "),
            how_to_use=input_data["How to Use"],
            side_effects=input_data["Side Effects"],
            price=input_data["Price"],
        )
