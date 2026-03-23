import re

class NoteValidator:
    REQUIRED_SECTIONS = [
        r"## Pattern",
        r"## Key Idea",
        r"## Approach",
        r"## Code",
        r"## Dry Run",
        r"## Edge Cases",
        r"## Mistakes",
        r"## Complexity",
        r"## Difficulty",
        r"## Metadata & Placement Tags"
    ]

    @staticmethod
    def validate(content: str) -> tuple[bool, str]:
        # Count words (simple split)
        word_count = len(content.split())
        if word_count < 200:
            return False, f"Output too short ({word_count} words, minimum 200)."

        # Check for required sections
        missing_sections = []
        for section in NoteValidator.REQUIRED_SECTIONS:
            if not re.search(section, content, re.IGNORECASE):
                missing_sections.append(section.replace("## ", ""))
        
        if missing_sections:
            return False, f"Missing sections: {', '.join(missing_sections)}"

        # Validate Dry Run length (at least 2 data rows in table)
        dry_run_match = re.search(r"## Dry Run(.*?)(?=\n##|$)", content, re.DOTALL | re.IGNORECASE)
        if dry_run_match:
            section_text = dry_run_match.group(1)
            rows = [row for row in section_text.split('\n') if '|' in row]
            if len(rows) < 4:  # Header + separator + at least 2 data rows
                return False, f"Dry run table too short ({len(rows)} rows found, need at least 4)."
        else:
            return False, "Dry run section not found."

        # Validate complexity explanation
        complexity_match = re.search(r"## Complexity(.*?)(?=\n##|$)", content, re.DOTALL | re.IGNORECASE)
        if complexity_match:
            explanation = complexity_match.group(1).strip()
            if len(explanation.split()) < 10:
                return False, "Complexity analysis lacks sufficient explanation."
        else:
            return False, "Complexity section not found."

        # Ensure Metadata is at the bottom (after Code/Complexity)
        meta_pos = content.find("## Metadata & Placement Tags")
        code_pos = content.find("## Code")
        if meta_pos < code_pos:
            return False, "Metadata tags must be at the bottom of the note."

        return True, "Valid"
