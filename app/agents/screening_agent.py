import json
from typing import Dict


class ScreeningAgent:
    """
    ScreeningAgent performs mental health risk screening using
    standardized questionnaires (PHQ-9 and GAD-7).

    IMPORTANT:
    - This agent does NOT diagnose medical conditions.
    - Outputs indicate risk levels only.
    - Results are meant for awareness and support.
    """

    def __init__(self, questionnaire_path: str):
        with open(questionnaire_path, "r") as f:
            self.questionnaire = json.load(f)

    def calculate_score(self, responses: Dict[int, int]) -> int:
        """
        Calculate total score from questionnaire responses.

        responses: {question_id: selected_option_value}
        """
        return sum(responses.values())

    def categorize_phq9(self, score: int) -> Dict:
        if score <= 4:
            level = "Minimal"
            interpretation = "Minimal depressive symptoms"
        elif score <= 9:
            level = "Mild"
            interpretation = "Mild depressive symptoms"
        elif score <= 14:
            level = "Moderate"
            interpretation = "Elevated depressive symptoms"
        elif score <= 19:
            level = "Moderately Severe"
            interpretation = "High depressive symptom burden"
        else:
            level = "Severe"
            interpretation = "Very high depressive symptom burden"

        return {
            "tool": "PHQ-9",
            "score": score,
            "risk_level": level,
            "interpretation": interpretation,
            "note": "This is a screening result, not a medical diagnosis."
        }

    def categorize_gad7(self, score: int) -> Dict:
        if score <= 4:
            level = "Minimal"
            interpretation = "Minimal anxiety symptoms"
        elif score <= 9:
            level = "Mild"
            interpretation = "Mild anxiety symptoms"
        elif score <= 14:
            level = "Moderate"
            interpretation = "Elevated anxiety symptoms"
        else:
            level = "Severe"
            interpretation = "High anxiety symptom burden"

        return {
            "tool": "GAD-7",
            "score": score,
            "risk_level": level,
            "interpretation": interpretation,
            "note": "This is a screening result, not a medical diagnosis."
        }

    def run_screening(self, responses: Dict[int, int]) -> Dict:
        """
        Main entry point for screening.
        Automatically determines questionnaire type.
        """
        score = self.calculate_score(responses)

        if self.questionnaire["name"] == "PHQ-9":
            return self.categorize_phq9(score)
        elif self.questionnaire["name"] == "GAD-7":
            return self.categorize_gad7(score)
        else:
            raise ValueError("Unsupported questionnaire")
