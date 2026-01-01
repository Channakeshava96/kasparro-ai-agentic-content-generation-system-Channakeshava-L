from models.product import Product

def test_product_model_creation():
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

    assert product.name == "GlowBoost Vitamin C Serum"
    assert "Vitamin C" in product.ingredients
