import re

class NoteValidator:
    # Strictly required sections (critical for a valid note)
    CRITICAL_SECTIONS = [
        r"## .*Key Idea",
        r"## .*Approach",
        r"## .*Code"
    ]
    
    # Recommended sections (nice to have, but don't fail validation if missing)
    RECOMMENDED_SECTIONS = [
        r"## .*Pattern",
        r"## .*Dry Run",
        r"## .*Edge Cases",
        r"## .*Mistakes",
        r"## .*Complexity",
        r"## .*Difficulty",
        r"## .*Metadata & Placement Tags"
    ]

    @staticmethod
    def validate(content: str) -> tuple[bool, str]:
        # Count words (simple split)
        word_count = len(content.split())
        if word_count < 50:
            return False, f"Output too short ({word_count} words, minimum 50)."

        # Check for CRITICAL sections
        missing_critical = []
        for section in NoteValidator.CRITICAL_SECTIONS:
            # Clean up the regex for display in error message
            section_name = section.replace("## .*", "").replace("## ", "")
            if not re.search(section, content, re.IGNORECASE):
                missing_critical.append(section_name)
        
        if missing_critical:
            return False, f"Missing critical sections: {', '.join(missing_critical)}"

        # Check for RECOMMENDED sections (warn but don't fail)
        missing_recommended = []
        for section in NoteValidator.RECOMMENDED_SECTIONS:
            if not re.search(section, content, re.IGNORECASE):
                missing_recommended.append(section.replace("## .*", "").replace("## ", ""))
        
        if missing_recommended:
             # We just log this internally or append to message, but return True
             pass

        return True, "Valid"
