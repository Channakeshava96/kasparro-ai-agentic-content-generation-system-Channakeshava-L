from agents.product_parser_agent import ProductParserAgent
from models.product import Product

def test_product_parser_agent():
    raw_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": "Oily, Combination",
        "Key Ingredients": "Vitamin C, Hyaluronic Acid",
        "Benefits": "Brightening, Fades dark spots",
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": "₹699",
    }

    agent = ProductParserAgent()
    product = agent.run(raw_data)

    assert isinstance(product, Product)
    assert product.name == "GlowBoost Vitamin C Serum"
    assert product.skin_type == ["Oily", "Combination"]
    assert "Vitamin C" in product.ingredients
    assert product.price == "₹699"
