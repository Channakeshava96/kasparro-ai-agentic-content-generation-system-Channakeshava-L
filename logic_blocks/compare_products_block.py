from models.product import Product

def compare_products_block(product_a: Product, product_b: Product) -> dict:
    """
    Compares two products on ingredients, benefits, and price.
    """

    return {
        "ingredients": {
            product_a.name: product_a.ingredients,
            product_b.name: product_b.ingredients,
        },
        "benefits": {
            product_a.name: product_a.benefits,
            product_b.name: product_b.benefits,
        },
        "price": {
            product_a.name: product_a.price,
            product_b.name: product_b.price,
        }
    }
