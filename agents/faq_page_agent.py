from agents.base_agent import BaseAgent
from templates.faq_template import FAQ_TEMPLATE
from logic_blocks.generate_safety_block import generate_safety_block
from logic_blocks.extract_usage_block import extract_usage_block

class FAQPageAgent(BaseAgent):
    """
    Assembles FAQ page content using questions and logic blocks.
    """

    def run(self, input_data: dict) -> dict:
        product = input_data["product"]
        questions = input_data["questions"]

        faq_items = []

        # Simple deterministic assembly
        for category, qs in questions.items():
            for q in qs:
                if len(faq_items) >= FAQ_TEMPLATE.rules["min_items"]:
                    break

                if category == "Safety":
                    answer = generate_safety_block(product)
                elif category == "Usage":
                    answer = extract_usage_block(product)[0]
                else:
                    answer = f"This information is based on the provided product details."

                faq_items.append({
                    "question": q,
                    "answer": answer,
                    "category": category
                })

        return {
            "page_type": "faq",
            "items": faq_items
        }
