from app.agents.screening_agent import ScreeningAgent

phq9_agent = ScreeningAgent("data/questionnaires/phq9.json")

responses = {
    1: 2, 2: 2, 3: 1, 4: 2, 5: 1,
    6: 1, 7: 1, 8: 1, 9: 0
}

result = phq9_agent.run_screening(responses)
print(result)
