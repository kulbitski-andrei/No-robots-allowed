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


def add_arguments(options):
    options.add_argument('--start-maximized')
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=MetricsInterceptor')
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    return options
