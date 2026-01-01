from templates.base_template import BaseTemplate

FAQ_TEMPLATE = BaseTemplate(
    page_type="faq",
    required_blocks=[
        "question_generation",
        "generate_safety_block",
        "extract_usage_block"
    ],
    rules={
        "min_items": 5,
        "allowed_categories": [
            "Informational",
            "Usage",
            "Safety",
            "Purchase",
            "Comparison"
        ]
    }
)
