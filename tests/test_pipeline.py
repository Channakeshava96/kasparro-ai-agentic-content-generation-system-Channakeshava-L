from orchestrator.pipeline import ContentGenerationPipeline

def test_full_pipeline():
    raw_product_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": "Oily, Combination",
        "Key Ingredients": "Vitamin C, Hyaluronic Acid",
        "Benefits": "Brightening, Fades dark spots",
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": "₹699",
    }

    pipeline = ContentGenerationPipeline()
    output = pipeline.run(raw_product_data)

    assert "faq_page" in output
    assert "product_page" in output
    assert "comparison_page" in output

    assert output["product_page"]["data"]["name"] == "GlowBoost Vitamin C Serum"
