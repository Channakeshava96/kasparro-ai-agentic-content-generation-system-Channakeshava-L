from agents.question_generation_agent import QuestionGenerationAgent
from models.product import Product

def test_question_generation_agent():
    product = Product(
        name="GlowBoost Vitamin C Serum",
        concentration="10% Vitamin C",
        skin_type=["Oily", "Combination"],
        ingredients=["Vitamin C", "Hyaluronic Acid"],
        benefits=["Brightening", "Fades dark spots"],
        how_to_use="Apply 2–3 drops in the morning before sunscreen",
        side_effects="Mild tingling for sensitive skin",
        price="₹699"
    )

    agent = QuestionGenerationAgent()
    questions = agent.run(product)

    assert isinstance(questions, dict)
    assert len(questions.keys()) >= 5

    total_questions = sum(len(v) for v in questions.values())
    assert total_questions >= 15

    assert "Safety" in questions
    assert len(questions["Safety"]) >= 3
