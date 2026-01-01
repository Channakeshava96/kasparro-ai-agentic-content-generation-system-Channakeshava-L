from templates.base_template import BaseTemplate

COMPARISON_PAGE_TEMPLATE = BaseTemplate(
    page_type="comparison_page",
    required_blocks=[
        "compare_ingredients_block",
        "generate_benefits_block"
    ],
    rules={
        "comparison_fields": [
            "ingredients",
            "benefits",
            "price"
        ]
    }
)
