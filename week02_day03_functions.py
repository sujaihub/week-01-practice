# week02_day03_functions.py
# Day 9: functions with def, typed inputs and a return type.
# No if/else, loops or f-strings yet: those come on Days 10-14.

def build_test_title(feature: str, scenario: str)-> str:
        # return sends the text back to the caller. print would only show it.
        return feature + ": " + scenario
def calculate_line_total(unit_price: float, quantity: int) -> float:
    # A line total is price times quantity, as in a shop cart.
    return unit_price * quantity


def calculate_cart_count(items_in_cart: int, items_added: int) -> int:
    # The cart badge number after adding items.
    return items_in_cart + items_added


def build_status_message(status_code: int) -> str:
    # str() turns the number into text so + can join it to other text.
    return "HTTP status " + str(status_code)


# Given
feature_name: str = "Login"
scenario_name: str = "Valid login shows products page"
unit_price: float = 29.99
quantity: int = 2
items_in_cart: int = 1
items_added: int = 2
status_code: int = 404

# When
test_title: str = build_test_title(feature_name, scenario_name)
line_total: float = calculate_line_total(unit_price, quantity)
cart_count: int = calculate_cart_count(items_in_cart, items_added)
status_message: str = build_status_message(status_code)

# Then
print("Test title:", test_title)
print("Line total:", line_total)
print("Cart count:", cart_count)
print("Status message:", status_message)
# 1. Positional: the order must match the parameters.
build_test_title("Login", "Valid login shows products page")

# 2. Keyword: the order does not matter, and the call is easier to read.
build_test_title(scenario="Valid login shows products page", feature="Login")

# 3. Inside print: no variable needed when you only want to see the result.
print(build_test_title("Login", "Valid login shows products page"))
