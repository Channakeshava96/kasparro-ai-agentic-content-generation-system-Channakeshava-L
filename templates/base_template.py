class BaseTemplate:
    """
    Base template definition.
    Templates define structure, rules, and required logic blocks.
    """

    def __init__(self, page_type: str, required_blocks: list, rules: dict):
        self.page_type = page_type
        self.required_blocks = required_blocks
        self.rules = rules
