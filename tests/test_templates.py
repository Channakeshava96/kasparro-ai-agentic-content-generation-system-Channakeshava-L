from templates.faq_template import FAQ_TEMPLATE
from templates.product_page_template import PRODUCT_PAGE_TEMPLATE
from templates.comparison_page_template import COMPARISON_PAGE_TEMPLATE

def test_templates_exist():
    assert FAQ_TEMPLATE.page_type == "faq"
    assert "min_items" in FAQ_TEMPLATE.rules

    assert PRODUCT_PAGE_TEMPLATE.page_type == "product_page"
    assert "sections" in PRODUCT_PAGE_TEMPLATE.rules

    assert COMPARISON_PAGE_TEMPLATE.page_type == "comparison_page"
    assert "comparison_fields" in COMPARISON_PAGE_TEMPLATE.rules
