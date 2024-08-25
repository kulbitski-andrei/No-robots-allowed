"""SERVICE METHODS"""

import random
import string


def generate_random_email():
    """
    Generate a random email address.

    This function creates a random email address by generating
    a random username consisting of 10 lowercase letters and appending it
    to a randomly selected domain from a predefined list.

    Returns:
        str: A randomly generated email address.
    """

    random_char = ''.join(random.choice(string.ascii_letters)
                          for _ in range(10))
    email = random_char + "@gmail.com"
    print(email)
    return email
