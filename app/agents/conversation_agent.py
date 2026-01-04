from app.agents.guardrails import GuardrailPipeline


class ConversationAgent:
    """
    Generates supportive responses based on retrieved context.
    """

    def __init__(self):
        self.guardrails = GuardrailPipeline()

    def generate(self, retrieved_docs):
        # Convert retrieved documents into text context
        context = "\n".join([doc.page_content for doc in retrieved_docs])

        # Simple response generation logic (safe & hackathon-ready)
        raw_response = (
            "Based on what you shared, it sounds like you may be experiencing some "
            "emotional strain. Some people find it helpful to practice grounding "
            "exercises, maintain daily routines, and take small breaks when feeling overwhelmed."
        )

        # Apply guardrails BEFORE returning response
        final_response = self.guardrails.apply(retrieved_docs, raw_response)

        return final_response
