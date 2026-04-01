import random
import string

"""
Lab Task: Implement a simple sanitization function to defend against jailbreaks!
Try to block phrases like "ignore previous instructions", "password", etc.
"""
def sanitize_input(user_input):

    blocked_words = ["secret"] # Add words to this list to block them!
    
    # Example defense:
    for word in blocked_words:
        if word.lower() in user_input.lower():
            return "[SYSTEM ALERT: Malicious input detected. Prompt blocked.]"
            
    return user_input

"""
Lab Task: Try to implement the three core Spotlighting techniques to defend against and Jailbreaks.
The three core techniques are:
- Delimiting
- Datamarking
- Encoding
"""
class SpotlightingDefense:

    @staticmethod
    def delimiting(untrusted_input: str) -> str:
        """
        Spotlighting via Delimiting:
        Encloses the untrusted input with unique, randomized boundary markers.
        """

        # TODO: pick a marker and write a secure prompt that encloses the untrusted input with this marker.

        #marker = ...
        
        secure_prompt = untrusted_input
        return secure_prompt

    @staticmethod
    def datamarking(untrusted_input: str) -> str:
        """
        Spotlighting via Datamarking:
        Interleaves a special token throughout the untrusted input (replacing spaces) 
        to provide a continuous signal of provenance.
        """

        # TODO: pick a marker and write a secure prompt that interleaves the untrusted input with this marker.

        #unique_marker = ...
        
        # Interleave the marker throughout the text
        #marked_input = ...
        
        secure_prompt = untrusted_input

        return secure_prompt

    @staticmethod
    def encoding(untrusted_input: str) -> str:
        """
        Spotlighting via Encoding:
        Encodes the untrusted input so it cannot be parsed as raw instructions 
        by the model until it is explicitly evaluated within the context of being data.
        """

        # TODO: pick any encoding and write a secure prompt that encodes the untrusted input with this encoding.
        # hint: you can use base64 for example.

        #encoded_input = ...
        
        secure_prompt = untrusted_input

        return secure_prompt

