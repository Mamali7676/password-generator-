import random
import string

def generate_password(length=8):
    """Generate a random password containing letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
