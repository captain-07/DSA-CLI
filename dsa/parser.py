import re

def parse_input(raw_input: str) -> tuple[str, str]:
    """
    Parses 'Problem Name | Optional Note' and beautifies the name.
    Example: 'two sum | check map' -> ('Two Sum', 'check map')
    """
    if "|" in raw_input:
        parts = raw_input.split("|", 1)
        name = parts[0].strip()
        note = parts[1].strip()
    else:
        name = raw_input.strip()
        note = "No specific note provided."

    # Beautify the problem name: Title Case (e.g., 'two sum' -> 'Two Sum')
    # We use a regex to handle cases like '3sum' -> '3Sum' or 're-order' -> 'Re-Order'
    beautified_name = re.sub(r"[a-zA-Z0-9]+", lambda m: m.group(0).capitalize(), name)
    
    return beautified_name, note
