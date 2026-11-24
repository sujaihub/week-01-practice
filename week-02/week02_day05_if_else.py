def get_test_result(actual: str, expected: str) -> str:
    """Return "PASS" when expected and actual are equal, otherwise "FAIL"."""
    # An empty actual value means the test read nothing from the page.
    # Return FAIL first, so an empty value can never give a false PASS.
    if actual == "":
        return "FAIL"
    elif expected == actual:
        return "PASS"
    else:
        return "FAIL"
def get_cart_label(cart_count: int) -> str:
    if cart_count == 0:
        return "Cart is empty"
    elif cart_count == 1:
        return "1 item in cart"
    elif cart_count > 1:
        return f"{cart_count} items in cart"
    else:
        return "Invalid cart count"
def can_log_in(username: str, password: str, is_locked_out: bool) -> bool:
    """Allow login only for a known user with the right password and an open account."""
    # or: at least one side must be True.
    is_known_user = username == "standard_user" or username == "problem_user"
    # and: all three parts must be True.
    # not: flips is_locked_out, so "not locked" means the account is open.
    if is_known_user and password == "secret_sauce" and not is_locked_out:
        return True
    else:
        return False

# ---------- Scenario 1: Cart count matches the expected count ----------
# Given the expected cart count is "2"
expected_cart_count = "2"
# And the actual cart count is "2"
actual_cart_count = "2"
# When I compare the actual and expected cart counts
cart_count_result = get_test_result(actual_cart_count, expected_cart_count)
# Then the result is "PASS"
print(f"Scenario 1 | expected: '{expected_cart_count}|actual: '{actual_cart_count}' | result:{cart_count_result} {cart_count_result}")
   
# ---------- Scenario 2: Product name differs from the expected name ----------
# Given the expected product name is "Sauce Labs Backpack"
expected_product_name = "Sauce Labs Backpack"
# And the actual product name is "Sauce Labs Bike Light"
actual_product_name = "Sauce Labs Bike Light"
# When I compare both values
product_name_result = get_test_result(expected_product_name, actual_product_name)
# Then the result is "FAIL"
print(f"Scenario 2 | expected: '{expected_product_name}' | actual: '{actual_product_name}' | result: {product_name_result}")

# ---------- Scenario 3: Actual value is empty ----------
# Given the expected price is "$29.99"
expected_price = "$29.99"
# And the actual price is empty
actual_price = ""
# When I compare both values
price_result = get_test_result(expected_price, actual_price)
# Then the result is "FAIL"
print(f"Scenario 3 | expected: '{expected_price}' | actual: '{actual_price}' | result: {price_result}")

# ---------- Scenario 4: Cart label names the cart state ----------
# Given the cart count is 0, 1, 2 and 7
# When I ask for the cart label
# Then the labels are EMPTY, ONE ITEM, TWO ITEMS and UNEXPECTED COUNT
print(f"Scenario 4 | cart count: 0 | label: {get_cart_label(0)}")
print(f"Scenario 4 | cart count: 1 | label: {get_cart_label(1)}")
print(f"Scenario 4 | cart count: 2 | label: {get_cart_label(2)}")
print(f"Scenario 4 | cart count: 7 | label: {get_cart_label(7)}")

# ---------- Scenario 5: Standard user may log in ----------
# Given the username is "standard_user" and the password is "secret_sauce"
standard_username = "standard_user"
standard_password = "secret_sauce"
# And the account is not locked
standard_is_locked_out = False
# When I check the login rules
standard_login_allowed = can_log_in(standard_username, standard_password, standard_is_locked_out)
# Then login is allowed
print(f"Scenario 5 | username: {standard_username} | allowed: {standard_login_allowed}")

# ---------- Scenario 6: Locked-out user may not log in ----------
# Given the username is "locked_out_user" and the password is "secret_sauce"
locked_username = "locked_out_user"
locked_password = "secret_sauce"
# And the account is locked
locked_is_locked_out = True
# When I check the login rules
locked_login_allowed = can_log_in(locked_username, locked_password, locked_is_locked_out)
# Then login is not allowed
print(f"Scenario 6 | username: {locked_username} | allowed: {locked_login_allowed}")

# ---------- Done-when check ----------
# and: both results must be as expected.
if cart_count_result == "PASS" and product_name_result == "FAIL" and price_result == "FAIL":
    print("Done-when check: OK, the function returns PASS and FAIL as expected")
else:
    print("Done-when check: NOT OK, read the results above")