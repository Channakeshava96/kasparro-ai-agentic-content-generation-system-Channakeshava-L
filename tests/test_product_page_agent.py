from agents.product_page_agent import ProductPageAgent
from models.product import Product

def test_product_page_agent():
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

    agent = ProductPageAgent()
    output = agent.run(product)

    assert output["page_type"] == "product_page"
    assert "benefits" in output["data"]
    assert output["data"]["price"] == "₹699"
