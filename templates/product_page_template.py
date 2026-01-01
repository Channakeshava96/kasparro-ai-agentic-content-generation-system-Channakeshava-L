from templates.base_template import BaseTemplate

PRODUCT_PAGE_TEMPLATE = BaseTemplate(
    page_type="product_page",
    required_blocks=[
        "generate_benefits_block",
        "extract_usage_block"
    ],
    rules={
        "sections": [
            "overview",
            "benefits",
            "usage",
            "price"
        ]
    }
)
