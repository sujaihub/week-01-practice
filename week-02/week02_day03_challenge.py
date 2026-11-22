def calculate_cart_total(subtotal: float, tax: float) -> float:
    # A cart total is subtotal plus tax, as in a shop cart.
    return subtotal + tax
def build_cart_badge_text(item_count: int) -> str:
    # str() turns the number into text so + can join it to other text.
    return "cart(" +str(item_count) + ")"
def build_result_label(test_name: str, status: str) -> str:
    # str() turns the number into text so + can join it to other text.
    return test_name + " - " + status
def build_expected_message(status_code: int, reason: str) -> str:
    # str() turns the number into text so + can join it to other text.
    return "HTTP Status"+str(status_code) + " " + reasoSn 

subtotal: float = 59.98
tax: float = 4.80
item_count: int =4
test_name:str="add backpack to cart"
status:str="PASS"
reason:str="Item added successfully"
status_code:int=200

    
print(calculate_cart_total(subtotal, tax))  
print(build_cart_badge_text(item_count))
print(build_result_label(test_name, status))
print(build_expected_message(status_code, reason))
