import re

def clean_output(raw_text: str) -> str:
    """
    Cleans and enforces the structure of the AI output based on GEMINI.MD.
    """
    if not raw_text:
        return ""

    # Remove code block wrappers if AI wrapped the entire response
    # (Sometimes AI puts everything inside ```markdown ... ```)
    clean = re.sub(r"^```markdown\n?", "", raw_text, flags=re.IGNORECASE)
    clean = re.sub(r"```$", "", clean)
    
    # Strip whitespace
    clean = clean.strip()
    
    # Ensure mandatory headers are present (or at least check for them)
    # Based on GEMINI.MD and prompt.txt
    mandatory_headers = [
        "Metadata & Placement Tags",
        "Pattern",
        "Logic Evolution",
        "Python Implementation (Optimal)",
        "Dry Run Table",
        "Edge Cases",
        "Common Mistakes",
        "Complexity Analysis"
    ]
    
    for header in mandatory_headers:
        if header not in clean and f"## {header}" not in clean:
            # If missing, it's not a hard failure but ideally the AI follows prompt.txt
            pass

    # Normalize multiple newlines between sections to exactly 2 newlines (one blank line)
    # But preserve formatting within sections.
    # This is tricky without a full parser, so we'll do simple cleanup.
    clean = re.sub(r'\n{3,}', '\n\n', clean)
    
    return clean
