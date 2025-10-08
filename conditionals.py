def check_temperature():
    """Simple if/else - good for beginners to read and understand"""
    temp = None
    while True:
        try:
            temp = int(input("Enter temperature: "))
            break
        except ValueError:
            print("Please enter a valid number")

    if temp > 30:
        return "It's very hot today!"
    elif temp > 25:
        return "It's hot today!"
    elif temp > 20:
        return "It's warm today"
    elif temp > 10:
        return "It's cool today!"
    else:
        return "It's freezing today!"

print(check_temperature())

def grade_assignment(score):
    if score >= 97:
        return "Exquisite work! A+"
    if score >= 90:
        return "Excellent work! A"
    elif score >= 70:
        return "Good job! B"
    elif score >= 50:
        return "You passed! C"
    else:
        return "Please try again. F "
    
print(grade_assignment(75))


def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"


# ==============================================================================
# MATCH/CASE EXAMPLE (Python 3.10+)
# ==============================================================================

def handle_http_status(status_code):
    """Basic match/case - compare with if/elif"""
    match status_code:
        case 200:
            return "OK - Request successful"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status code: {status_code}"



# ==============================================================================
# COMPACT ONE-LINE ALTERNATIVES (using ternary operators)
# ==============================================================================


def check_temperature_compact(temp):
    """Ternary operator version - compare with the if/else version above"""
    return "It's warm today!" if temp > 25 else "It's cool today!"


def check_even_odd_compact(number):
    """Ternary with f-strings - very concise"""
    return f"{number} is {'even' if number % 2 == 0 else 'odd'}"


def get_pass_fail(score):
    """Simple ternary for pass/fail"""
    return "Pass" if score >= 50 else "Fail"


def get_discount_rate(is_member, age):
    """Nested ternary - can be harder to read but very compact"""
    return 0.2 if is_member else (0.1 if age >= 65 else 0.0)


def format_price(price, currency="GBP"):
    """Ternary with string formatting"""
    symbol = "£" if currency == "GBP" else ("$" if currency == "USD" else "€")
    return f"{symbol}{price:.2f}"


def validate_input_compact(value):
    """Using 'or' for default values - common Python idiom"""
    return str(value).strip() or "No input provided"


# ==============================================================================
# INTERMEDIATE LEVEL 
# ==============================================================================

def categorise_age(age):
    """Nested conditions and logical operators"""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
    
print(categorise_age(16))


def calculate_shipping(weight, distance, is_express=False):
    """Complex conditions with calculations"""
    if weight <= 0 or distance <= 0:
        return "Invalid input"
    
    base_cost = 5.0
    
    if weight > 10:
        base_cost += (weight - 10) * 1.5
    
    if distance > 100:
        base_cost += (distance - 100) * 0.1
    
    if is_express:
        base_cost *= 2
    
    return round(base_cost, 2)


# ==============================================================================
# MORE COMPACT INTERMEDIATE EXAMPLES
# ==============================================================================

def calculate_tax_compact(income):
    """Multiple ternary operators for tax brackets"""
    return income * (0.4 if income > 50000 else (0.2 if income > 12500 else 0.0))


def get_user_status_compact(login_count, last_active_days):
    """Compact user status with logical operators"""
    return ("New User" if login_count < 5 else 
            "Inactive" if last_active_days > 30 else 
            "Active")


def process_grade_compact(score, extra_credit=0):
    """Compact grade processing with bounds checking"""
    final_score = min(100, score + extra_credit)
    return "A" if final_score >= 90 else ("B" if final_score >= 80 else 
           "C" if final_score >= 70 else ("D" if final_score >= 60 else "F"))




# ==============================================================================
# ADVANCED LEVEL (1-2 years experience)
# ==============================================================================


def validate_password_strength(password):
    """Multiple validation conditions"""
    if len(password) < 8:
        return "Password too short (minimum 8 characters)"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    
    if not has_upper:
        return "Password must contain uppercase letter"
    elif not has_lower:
        return "Password must contain lowercase letter"
    elif not has_digit:
        return "Password must contain a number"
    elif not has_special:
        return "Password must contain special character"
    else:
        return "Strong password!"


# ==============================================================================
# ADVANCED COMPACT EXAMPLES
# ==============================================================================

def validate_email_compact(email):
    """Very compact email validation using all() and any()"""
    return ("Valid email" if "@" in email and "." in email.split("@")[-1] 
            and len(email) > 5 and not email.startswith("@") 
            else "Invalid email")


def get_priority_level_compact(user_type, is_premium, days_until_deadline):
    """Complex ternary with multiple conditions"""
    return ("Critical" if days_until_deadline <= 1 else
            "High" if (user_type == "admin" or is_premium) and days_until_deadline <= 3 else
            "Medium" if days_until_deadline <= 7 else
            "Low")


def calculate_final_price_compact(base_price, discount_pct=0, tax_rate=0.2, is_member=False):
    """One-liner with multiple calculations"""
    return round(base_price * (1 - discount_pct - (0.05 if is_member else 0)) * (1 + tax_rate), 2)


def classify_text_length_compact(text):
    """Using walrus operator (Python 3.8+) for compact conditions"""
    return ("Empty" if not text else
            "Short" if (length := len(text)) <= 10 else
            "Medium" if length <= 50 else
            "Long")


# ==============================================================================
# MORE MATCH/CASE EXAMPLES (Python 3.10+)
# ==============================================================================

def process_command(command, *args):
    """Intermediate match/case with guards and multiple patterns"""
    match command.lower():
        case "help" | "h":
            return "Available commands: help, quit, save, load"
        case "quit" | "exit" | "q":
            return "Goodbye!"
        case "save" if len(args) >= 1:
            return f"Saving to {args[0]}"
        case "save":
            return "Please specify filename"
        case "load" if len(args) >= 1:
            return f"Loading from {args[0]}"
        case _:
            return f"Unknown command: {command}"


def analyse_data_structure(data):
    """Advanced match/case with type patterns and destructuring"""
    match data:
        case int() if data > 0:
            return f"Positive integer: {data}"
        case int() if data < 0:
            return f"Negative integer: {data}"
        case 0:
            return "Zero"
        case str() if len(data) == 0:
            return "Empty string"
        case str():
            return f"String with {len(data)} characters"
        case []:
            return "Empty list"
        case [single_item]:
            return f"List with one item: {single_item}"
        case [first, *rest] if len(rest) > 5:
            return f"Long list starting with {first}"
        case [first, second]:
            return f"Two-item list: {first}, {second}"
        case dict() if not data:
            return "Empty dictionary"
        case {"name": name, "age": age}:
            return f"Person: {name}, age {age}"
        case _:
            return f"Unknown data type: {type(data)}"


# ==============================================================================
# TEST FUNCTIONS 
# ==============================================================================

def run_beginner_examples():
    print("=== BEGINNER EXAMPLES ===")
    print(check_temperature(30))
    print(check_temperature(15))
    print(grade_assignment(95))
    print(grade_assignment(75))
    print(grade_assignment(45))
    print(check_even_odd(7))
    print(check_even_odd(12))
    print("\n=== MATCH/CASE EXAMPLE ===")
    print(handle_http_status(200))
    print(handle_http_status(418))
    
    print("\n=== COMPACT VERSIONS ===")
    print(check_temperature_compact(30))
    print(check_even_odd_compact(7))
    print(get_pass_fail(75))
    print(get_discount_rate(True, 70))
    print(format_price(29.99, "GBP"))
    print(validate_input_compact("  "))


def run_intermediate_examples():
    print("\n=== INTERMEDIATE EXAMPLES ===")
    print(categorise_age(10))
    print(categorise_age(16))
    print(categorise_age(30))
    print(calculate_shipping(5, 50))
    print(calculate_shipping(15, 200, True))
    
    print("\n=== COMPACT INTERMEDIATE ===")
    print(calculate_tax_compact(25000))
    print(get_user_status_compact(3, 45))
    print(process_grade_compact(85, 7))


def run_advanced_examples():
    print("\n=== ADVANCED EXAMPLES ===")
    print(validate_password_strength("password"))
    print(validate_password_strength("MyStr0ng!Pass"))
    
    print("\n=== ADVANCED COMPACT ===")
    print(validate_email_compact("user@domain.com"))
    print(get_priority_level_compact("admin", False, 2))
    print(calculate_final_price_compact(100, 0.1, 0.2, True))
    print(classify_text_length_compact("This is a medium length sentence."))


def run_match_examples():
    print("\n=== MATCH/CASE EXAMPLES ===")
    print(process_command("help"))
    print(process_command("save", "myfile.txt"))
    print(analyse_data_structure(42))
    print(analyse_data_structure([1, 2, 3, 4, 5, 6, 7]))
    print(analyse_data_structure({"name": "Alice", "age": 25}))


if __name__ == "__main__":
    pass
    # Comment back in the later examples to run 
    # run_beginner_examples()
    # run_intermediate_examples()
    # run_advanced_examples()
    # run_match_examples()