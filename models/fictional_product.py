from models.product import Product

def get_fictional_product_b() -> Product:
    """
    Returns a fictional competitor product.
    Used only for comparison purposes.
    """

    return Product(
        name="RadiancePlus Vitamin C Serum",
        concentration="8% Vitamin C",
        skin_type=["Normal", "Combination"],
        ingredients=["Vitamin C", "Niacinamide"],
        benefits=["Brightening"],
        how_to_use="Apply once daily",
        side_effects="No major side effects reported",
        price="₹899"
    )
