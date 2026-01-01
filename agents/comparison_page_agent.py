from agents.base_agent import BaseAgent
from logic_blocks.compare_products_block import compare_products_block

class ComparisonPageAgent(BaseAgent):
    """
    Assembles comparison page between two products.
    """

    def run(self, input_data: dict) -> dict:
        product_a = input_data["product_a"]
        product_b = input_data["product_b"]

        comparison_data = compare_products_block(product_a, product_b)

        return {
            "page_type": "comparison_page",
            "comparison": comparison_data
        }
