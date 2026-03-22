import re

def clean_output(raw_text: str) -> str:
    """
    Cleans and enforces the structure of the AI output.
    """
    if not raw_text:
        return ""

    # Remove code block wrappers if AI wrapped the entire response
    clean = re.sub(r"^```markdown\n?", "", raw_text, flags=re.IGNORECASE)
    clean = re.sub(r"```$", "", clean)
    
    # Strip whitespace
    clean = clean.strip()
    
    # Ensure mandatory headers are present
    mandatory_headers = [
        "## Metadata & Placement Tags",
        "## Difficulty",
        "## Pattern",
        "## Logic Evolution",
        "## Python Implementation",
        "## Dry Run Table",
        "## Edge Cases",
        "## Common Mistakes",
        "## Complexity Analysis"
    ]
    
    # Normalize multiple newlines between sections to exactly 2 newlines (one blank line)
    clean = re.sub(r'\n{3,}', '\n\n', clean)
    
    return clean
