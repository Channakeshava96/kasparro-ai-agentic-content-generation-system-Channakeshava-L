from models.product import Product

def extract_usage_block(product: Product) -> list[str]:
    """
    Extracts standardized usage instructions.
    """
    return [
        product.how_to_use
    ]
