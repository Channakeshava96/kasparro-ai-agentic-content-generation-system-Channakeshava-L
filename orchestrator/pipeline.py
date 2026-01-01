from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

from models.fictional_product import get_fictional_product_b


class ContentGenerationPipeline:
    """
    Orchestrates the full multi-agent content generation workflow.
    """

    def __init__(self):
        self.product_parser = ProductParserAgent()
        self.question_generator = QuestionGenerationAgent()
        self.faq_page_agent = FAQPageAgent()
        self.product_page_agent = ProductPageAgent()
        self.comparison_page_agent = ComparisonPageAgent()

    def run(self, raw_product_data: dict) -> dict:
        # Step 1: Parse product data
        product = self.product_parser.run(raw_product_data)

        # Step 2: Generate user questions
        questions = self.question_generator.run(product)

        # Step 3: Generate pages
        faq_page = self.faq_page_agent.run({
            "product": product,
            "questions": questions
        })

        product_page = self.product_page_agent.run(product)

        product_b = get_fictional_product_b()
        comparison_page = self.comparison_page_agent.run({
            "product_a": product,
            "product_b": product_b
        })

        return {
            "faq_page": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }
