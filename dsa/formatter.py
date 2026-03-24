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
    
    # Normalize multiple newlines between sections to exactly 2 newlines (one blank line)
    clean = re.sub(r'\n{3,}', '\n\n', clean)
    
    # Move Metadata section to the bottom if it exists
    # Matches "## ... Metadata & Placement Tags" and everything after it
    metadata_pattern = re.compile(r"(## .*Metadata & Placement Tags.*)", re.DOTALL | re.IGNORECASE)
    match = metadata_pattern.search(clean)
    
    if match:
        metadata_section = match.group(1).strip()
        # Remove the section from its current position
        clean_without_metadata = metadata_pattern.sub("", clean).strip()
        # Append it to the end
        clean = f"{clean_without_metadata}\n\n{metadata_section}"

    return clean
