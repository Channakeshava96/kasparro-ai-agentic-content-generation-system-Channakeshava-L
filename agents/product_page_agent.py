from agents.base_agent import BaseAgent
from templates.product_page_template import PRODUCT_PAGE_TEMPLATE
from logic_blocks.generate_benefits_block import generate_benefits_block
from logic_blocks.extract_usage_block import extract_usage_block

class ProductPageAgent(BaseAgent):
    """
    Assembles product description page.
    """

    def run(self, product) -> dict:
        return {
            "page_type": "product_page",
            "data": {
                "name": product.name,
                "concentration": product.concentration,
                "benefits": generate_benefits_block(product),
                "usage": extract_usage_block(product),
                "price": product.price
            }
        }
