from agents.faq_page_agent import FAQPageAgent
from models.product import Product

def test_faq_page_agent():
    product = Product(
        name="GlowBoost Vitamin C Serum",
        concentration="10% Vitamin C",
        skin_type=["Oily", "Combination"],
        ingredients=["Vitamin C", "Hyaluronic Acid"],
        benefits=["Brightening", "Fades dark spots"],
        how_to_use="Apply 2–3 drops in the morning before sunscreen",
        side_effects="Mild tingling for sensitive skin",
        price="₹699"
    )

    questions = {
        "Safety": ["Is this safe?"],
        "Usage": ["How do I use it?"],
        "Informational": ["What is this product?"]
    }

    agent = FAQPageAgent()
    output = agent.run({
        "product": product,
        "questions": questions
    })

    assert output["page_type"] == "faq"
    assert len(output["items"]) >= 1
    assert "question" in output["items"][0]
    assert "answer" in output["items"][0]
