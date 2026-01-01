import json
import os
from orchestrator.pipeline import ContentGenerationPipeline


def main():
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

    os.makedirs("output", exist_ok=True)

    pipeline = ContentGenerationPipeline()
    output = pipeline.run(raw_product_data)

    with open("output/faq.json", "w", encoding="utf-8") as f:
        json.dump(output["faq_page"], f, indent=2)

    with open("output/product_page.json", "w", encoding="utf-8") as f:
        json.dump(output["product_page"], f, indent=2)

    with open("output/comparison_page.json", "w", encoding="utf-8") as f:
        json.dump(output["comparison_page"], f, indent=2)

    print("✅ Content generation completed. JSON files written to /output")


if __name__ == "__main__":
    main()
