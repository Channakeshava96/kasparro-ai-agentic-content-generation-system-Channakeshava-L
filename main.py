import json
import os
from orchestrator.pipeline import ContentGenerationPipeline


def main():
    with open("input/product_data.json", "r", encoding="utf-8") as f:
        raw_product_data = json.load(f)

    os.makedirs("output", exist_ok=True)

    pipeline = ContentGenerationPipeline()
    output = pipeline.run(raw_product_data)

    with open("output/faq.json", "w", encoding="utf-8") as f:
        json.dump(output["faq_page"], f, indent=2)

    with open("output/product_page.json", "w", encoding="utf-8") as f:
        json.dump(output["product_page"], f, indent=2)

    with open("output/comparison_page.json", "w", encoding="utf-8") as f:
        json.dump(output["comparison_page"], f, indent=2)

    print("Content generation completed. JSON files written to /output")


if __name__ == "__main__":
    main()
