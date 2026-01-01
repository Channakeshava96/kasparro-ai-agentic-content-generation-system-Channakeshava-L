from models.product import Product

def generate_safety_block(product: Product) -> str:
    """
    Generates safety-related information.
    """
    return product.side_effects
