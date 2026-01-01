from models.product import Product
from logic_blocks.generate_benefits_block import generate_benefits_block
from logic_blocks.extract_usage_block import extract_usage_block
from logic_blocks.generate_safety_block import generate_safety_block

def test_logic_blocks():
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

    benefits = generate_benefits_block(product)
    usage = extract_usage_block(product)
    safety = generate_safety_block(product)

    assert isinstance(benefits, list)
    assert len(benefits) == 2
    assert "brightening" in benefits[0].lower()

    assert isinstance(usage, list)
    assert "Apply" in usage[0]

    assert safety == "Mild tingling for sensitive skin"
