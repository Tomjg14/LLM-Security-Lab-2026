def sanitize_input(user_input):
    """
    Lab Task: Implement defenses against prompt injection!
    Try to block phrases like "ignore previous instructions", "password", etc.
    """
    blocked_words = [] # Add words to this list to block them!
    
    # Example defense:
    for word in blocked_words:
        if word.lower() in user_input.lower():
            return "[SYSTEM ALERT: Malicious input detected. Prompt blocked.]"
            
    return user_input
