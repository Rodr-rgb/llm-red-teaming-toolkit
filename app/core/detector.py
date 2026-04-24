from app.core.patterns import JAILBREAK_PATTERNS

class PromptDetector:
    def detect(self, prompt: str):
        matches = [
            p for p in JAILBREAK_PATTERNS
            if p in prompt.lower()
        ]

        return {
            "risk_score": len(matches),
            "risk_level": self._classify(len(matches)),
            "matches": matches
        }

    def _classify(self, score: int):
        if score >= 2:
            return "HIGH"
        elif score == 1:
            return "MEDIUM"
        return "LOW"