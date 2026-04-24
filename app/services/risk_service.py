from app.core.detector import PromptDetector

detector = PromptDetector()

def analyze_prompt(prompt: str):
    result = detector.detect(prompt)

    return {
        **result,
        "action": "BLOCK" if result["risk_score"] > 1 else "ALLOW"
    }