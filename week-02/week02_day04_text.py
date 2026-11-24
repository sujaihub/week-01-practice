import re
def clean_text(raw_text: str)-> str:
     """Remove outer spaces and make the text lower case.
    Why: page text often has extra spaces and mixed capitals."""
     return raw_text.strip().lower()
def texts_match(actual_text: str, expected_text: str)-> bool:
    """Check if two texts match, ignoring case and extra spaces.
    Why: page text often has extra spaces and mixed capitals."""
    return clean_text(actual_text) == clean_text(expected_text)
def contains_word(text: str, word: str) -> bool:
    """re.search returns a match or None. bool() turns it into True or False."""
    return bool(re.search(word, text))


# Given: five text values as the shop page shows them
page_title: str = "  Swag Labs  "
product_name: str = "Sauce Labs Backpack"
cart_badge: str = " 2 "
login_error: str = "Epic sadface: Username and password do not match any user in this service"
continue_button: str = "Continue Shopping"

# When: I clean and compare the texts
title_matches: bool = texts_match(page_title, "swag labs")
cart_matches: bool = texts_match(cart_badge, "2")
product_has_backpack: bool = "backpack" in clean_text(product_name)
error_words = login_error.split()
login_found: bool = contains_word(clean_text("  Login  "), "log")
shop_pattern = re.compile("shop")
shopping_found: bool = bool(shop_pattern.search(clean_text(continue_button)))

# Then: the results are what the shop test expects
print(f"Title matches: {title_matches}")
print(f"Cart count matches: {cart_matches}")
print(f"Product name has 'backpack': {product_has_backpack}")
print(f"Login error has {len(error_words)} words, first word: {error_words[0]}")
print(f"Word 'log' found in 'Login': {login_found}")
print(f"Pattern 'shop' found in button text: {shopping_found}")
print(f"Missing word found: {contains_word(clean_text(product_name), 'cart')}")