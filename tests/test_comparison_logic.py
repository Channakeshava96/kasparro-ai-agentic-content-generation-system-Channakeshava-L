from models.product import Product
from models.fictional_product import get_fictional_product_b
from logic_blocks.compare_products_block import compare_products_block

def test_compare_products_block():
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

    comparison = compare_products_block(product_a, product_b)

    assert "ingredients" in comparison
    assert product_a.name in comparison["ingredients"]
    assert product_b.name in comparison["ingredients"]
    assert comparison["price"][product_b.name] == "₹899"
