def parse_input(input_str: str):
    """
    Parses "problem name | mistake" or "problem name - mistake" input string.
    Returns: (problem_name, mistake)
    """
    # Prefer pipe separator
    if "|" in input_str:
        parts = [p.strip() for p in input_str.split("|", 1)]
        return parts[0], parts[1]
    
    # Try dash if pipe is missing but only if there's enough space
    if " - " in input_str:
        parts = [p.strip() for p in input_str.split(" - ", 1)]
        return parts[0], parts[1]
    
    return input_str.strip(), "No specific mistake mentioned."
