"""
Guardrails to prevent hallucinations and unsafe responses
for a mental health support chatbot.
"""


class ContextGuardrail:
    """
    Ensures the chatbot answers only when reliable context
    is retrieved from the knowledge base.
    """

    def validate(self, retrieved_docs) -> bool:
        return retrieved_docs is not None and len(retrieved_docs) > 0


class MedicalSafetyGuardrail:
    """
    Prevents medical diagnosis, prescriptions, or clinical claims.
    """

    BLOCKED_PHRASES = [
        "you have depression",
        "you are depressed",
        "you have anxiety",
        "diagnosis",
        "medication",
        "treatment",
        "prescribe",
        "disorder"
    ]

    def filter(self, response: str) -> str:
        lowered = response.lower()
        for phrase in self.BLOCKED_PHRASES:
            if phrase in lowered:
                return (
                    "I can’t provide medical diagnoses or treatment advice. "
                    "I can share general, supportive information instead."
                )
        return response


class ConfidenceGuardrail:
    """
    Handles low-confidence situations when retrieval context is limited.
    """

    def is_confident(self, retrieved_docs) -> bool:
        return len(retrieved_docs) >= 2


def add_disclaimer(response: str) -> str:
    """
    Appends a mandatory healthcare disclaimer.
    """
    disclaimer = (
        "\n\nNote: This chatbot provides general supportive information only "
        "and is not a substitute for professional medical advice."
    )
    return response + disclaimer


class GuardrailPipeline:
    """
    Orchestrates all guardrails in a single pipeline.
    """

    def __init__(self):
        self.context_guardrail = ContextGuardrail()
        self.medical_guardrail = MedicalSafetyGuardrail()
        self.confidence_guardrail = ConfidenceGuardrail()

    def apply(self, retrieved_docs, response: str) -> str:
        # Guardrail 1: Context availability
        if not self.context_guardrail.validate(retrieved_docs):
            return (
                "I don’t have enough reliable information to answer this safely. "
                "Please consider rephrasing your question."
            )

        # Guardrail 2: Medical safety
        response = self.medical_guardrail.filter(response)

        # Guardrail 3: Low confidence handling
        if not self.confidence_guardrail.is_confident(retrieved_docs):
            response += (
                "\n\nThis response is based on limited information and may not fully "
                "match your situation."
            )

        # Guardrail 4: Mandatory disclaimer
        response = add_disclaimer(response)

        return response
