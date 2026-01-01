from models.product import Product

def generate_benefits_block(product: Product) -> list[str]:
    """
    Generates benefit statements based on product benefits.
    """
    return [
        f"This product helps with {benefit.lower()}."
        for benefit in product.benefits
    ]
