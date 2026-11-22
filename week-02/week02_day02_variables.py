# week02_day02_variables.py
# Scenario: describe one test case with 5 typed variables and print each type.

# Given a test case for the saucedemo.com cart
# BASE_URL is written in CAPITAL letters: a habit for a value that must not change.
# Python has no const, so nothing stops a later change.
BASE_URL: str = "https://www.saucedemo.com"
test_name: str = "add backpack to cart" 
product_price: float = 29.99
expected_cart_count: int = 1
is_smoke_test: bool = True
# When I print each value with its type
print("BASE_URL:", BASE_URL, "Type:", type(BASE_URL))
print("Test Name:", test_name, "Type:", type(test_name))
print("Product Price:", product_price, "Type:", type(product_price))
print("Expected Cart Count:", expected_cart_count, "Type:", type(expected_cart_count))
print("Is Smoke Test:", is_smoke_test, "Type:", type(is_smoke_test))

wrong_example:int= "one"
print("Wrong Example:", wrong_example, "Type:", type(wrong_example))


