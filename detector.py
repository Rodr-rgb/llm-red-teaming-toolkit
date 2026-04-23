from patterns import JAILBREAK_PATTERNS

def detect(prompt: str):
    matches = []

    for pattern in JAILBREAK_PATTERNS:
        if pattern in prompt.lower():
            matches.append(pattern)

    return {
        "risk": "HIGH" if len(matches) > 1 else "LOW",
        "matches": matches
    }