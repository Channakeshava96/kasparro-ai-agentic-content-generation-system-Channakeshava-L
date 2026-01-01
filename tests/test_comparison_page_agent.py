from agents.comparison_page_agent import ComparisonPageAgent
from models.product import Product
from models.fictional_product import get_fictional_product_b

def test_comparison_page_agent():
    product_a = Product(
        name="GlowBoost Vitamin C Serum",
        concentration="10% Vitamin C",
        skin_type=["Oily", "Combination"],
        ingredients=["Vitamin C", "Hyaluronic Acid"],
        benefits=["Brightening", "Fades dark spots"],
        how_to_use="Apply 2–3 drops in the morning before sunscreen",
        side_effects="Mild tingling for sensitive skin",
        price="₹699"
    )

    product_b = get_fictional_product_b()

    agent = ComparisonPageAgent()
    output = agent.run({
        "product_a": product_a,
        "product_b": product_b
    })

    assert output["page_type"] == "comparison_page"
    assert "comparison" in output
    assert product_a.name in output["comparison"]["price"]
    assert product_b.name in output["comparison"]["price"]
