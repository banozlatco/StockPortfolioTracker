# url_shortener.py

import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url, length=6):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(length))

        self.url_map[short_url] = long_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_map.get(short_url)

# Usage example
shortener = URLShortener()

long_url = input("Enter the long URL: ")
short_url = shortener.shorten_url(long_url)
print("Shortened URL:", short_url)

retrieved_url = shortener.get_original_url(short_url)
print("Retrieved Original URL:", retrieved_url)
