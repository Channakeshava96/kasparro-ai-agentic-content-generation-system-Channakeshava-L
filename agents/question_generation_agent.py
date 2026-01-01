from agents.base_agent import BaseAgent
from models.product import Product

class QuestionGenerationAgent(BaseAgent):
    """
    Agent responsible for generating categorized user questions
    based on product attributes.
    """

    def run(self, product: Product) -> dict:
        questions = {
            "Informational": [
                f"What is {product.name}?",
                f"What does {product.concentration} mean in this product?",
                "What are the key ingredients in this product?",
            ],
            "Usage": [
                "How should this product be applied?",
                "When should this product be used during the day?",
                "Can this product be used daily?",
            ],
            "Safety": [
                "Is this product suitable for sensitive skin?",
                "Are there any side effects?",
                "What should I do if irritation occurs?",
            ],
            "Purchase": [
                "What is the price of this product?",
                "Is this product affordable compared to similar serums?",
                "Who is this product best suited for?",
            ],
            "Comparison": [
                "How is this product different from other Vitamin C serums?",
                "How does this product compare in price to similar products?",
                "What makes this product unique?",
            ],
        }

        return questions
