# Python Conditionals - PRIMM Learning Activities

Python code examples and activities for learning conditional statements using the **PRIMM methodology** (Predict, Run, Investigate, Modify, Make).

## What we'll cover

- Basic `if`, `elif`, and `else` statements
- Comparison and logical operators
- Ternary operators for compact conditions
- Modern `match/case` statements (Python 3.10+)
- Complex conditional logic and validation

## Getting Started

1. Clone or download this repository
2. Open `conditionals.py` in your Python environment
3. Follow the PRIMM activities below

---

## 🔮 PREDICT Activities

Before running any code, look at these functions and **predict** what they will output:

### Task P1: Basic Predictions
Look at these function calls and note down what you think they'll return:
```python
check_temperature(30)
check_temperature(15)
grade_assignment(95)
grade_assignment(45)
```

### Task P2: Complex Predictions
Predict the output of these more complex examples:
```python
categorise_age(16)
calculate_shipping(15, 200, True)
get_discount_rate(True, 70)
```

**Note your predictions before moving to the next section!**

---

## 🏃 RUN Activities

Now test your predictions by running the code:

### Task R1: Run Beginner Examples
```bash
python conditionals.py
```

### Task R2: Uncomment and Run Other Examples
In the `if __name__ == "__main__":` section, uncomment these lines one by one:
```python
# run_intermediate_examples()
# run_advanced_examples()
# run_match_examples()
```

### Task R3: Interactive Testing in VS Code
Test functions interactively using VS Code's integrated terminal:

**Method 1: Python REPL**
1. Open VS Code terminal (`Ctrl+`` or `View > Terminal`)
2. Type `python` to start Python REPL
3. Import and test functions:
```python
from conditionals import *
check_even_odd(7)
validate_password_strength("test123")
grade_assignment(85)
```
4. Type `exit()` to leave REPL


---

## 🔍 INVESTIGATE Activities

Examine the code structure and understand how it works:

### Task I1: Trace Through Logic
Pick one function from your difficulty level and the one above and trace through the execution step-by-step:
- **Beginner**: `grade_assignment(75)`
- **Intermediate**: `categorise_age(16)`
- **Advanced**: `validate_password_strength("MyPass123!")`

### Task I2: Compare Approaches
Compare these two functions that do the same thing:
- `check_temperature()` vs `check_temperature_compact()`
- `check_even_odd()` vs `check_even_odd_compact()`

**Questions to investigate:**
- Which approach is more readable?
- Which is more maintainable?
- When might you use each approach?

### Task I3: Understand Match/Case
Study the `handle_http_status()` function:
- How does `match/case` differ from `if/elif`?
- What are the advantages of each approach?

---

## ✏️ MODIFY Activities

Make changes to existing functions to deepen your understanding. You don't have to do them all, just pick and choose. Be prepared to feed back to the group on what you've been working on.

### Task M1: Extend Basic Functions
Modify `grade_assignment()` to include:
- A+ grade for scores ≥ 97
- Different grade boundaries (e.g., 85+ for A, 75+ for B)

### Task M2: Add Validation
Enhance `check_temperature()` to:
- Handle invalid inputs (non-numeric values)
- Add more temperature categories (freezing, hot, very hot)

### Task M3: Improve Complex Functions
Modify `calculate_shipping()` to:
- Add weekend delivery surcharge
- Include different rates for different regions
- Add bulk discount for heavy items

### Task M4: Create Compact Versions
Convert these verbose functions to compact ternary versions:
- `categorise_age()`
- `validate_password_strength()` (simplified version)

---

## 🛠️ MAKE Activities

Create your own functions from scratch:

### Task MA1: Basic Conditionals
Create functions for:
```python
def check_voting_eligibility(age, citizenship):
    """Return if person can vote (18+, citizen)"""
    pass

def calculate_tip(bill_amount, service_quality):
    """Return tip: excellent=20%, good=15%, poor=10%"""
    pass

def determine_season(month):
    """Return season based on month number (1-12)"""
    pass
```

### Task MA2: Intermediate Challenges
```python
def validate_username(username):
    """Check if username is valid (3-20 chars, alphanumeric + underscore)"""
    pass

def calculate_insurance_premium(age, car_value, accidents):
    """Calculate car insurance based on risk factors"""
    pass

def process_exam_results(scores_list):
    """Return statistics and grade distribution"""
    pass
```

### Task MA3: Advanced Projects
```python
def smart_password_validator(password):
    """Advanced password validation with detailed feedback"""
    pass

def loan_approval_system(income, credit_score, debt_ratio, employment_years):
    """Determine loan approval and interest rate"""
    pass

def game_difficulty_selector(player_level, win_rate, preferred_challenge):
    """Select appropriate game difficulty using match/case"""
    pass
```

### Task MA4: Real-World Application
Choose one of these projects:
1. **Grade Calculator**: Complete system for calculating final grades
2. **Weather Advisory**: System that gives clothing/activity recommendations
3. **Shopping Cart**: Discount and tax calculation system
4. **User Access Control**: Role-based permission system

---

## 📚 Learning Progression

### Beginner Level
- Simple `if/else` statements
- Basic comparison operators (`>`, `<`, `==`, `!=`)
- Ternary operators for simple conditions

### Intermediate Level
- `elif` chains for multiple conditions
- Logical operators (`and`, `or`, `not`)
- Nested conditions
- Input validation

### Advanced Level
- Complex boolean logic
- Multiple validation conditions
- `match/case` statements (Python 3.10+)
- Performance considerations

---

## 🎯 Assessment Checklist

After completing the activities, you should be able to:

- [ ] Write basic `if/else` statements
- [ ] Use comparison and logical operators correctly
- [ ] Create `elif` chains for multiple conditions
- [ ] Write compact ternary operators
- [ ] Validate user input effectively
- [ ] Use `match/case` for pattern matching
- [ ] Debug conditional logic errors
- [ ] Choose appropriate conditional structures for different problems

---

## 💡 Tips for Success

1. **Start Simple**: Begin with basic `if/else` before moving to complex logic
2. **Test Edge Cases**: Always test boundary conditions and invalid inputs
3. **Read Aloud**: Verbalise your conditional logic to check it makes sense

---

## 🔗 Additional Resources

- [Python Official Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Python Match/Case Documentation](https://docs.python.org/3/tutorial/controlflow.html#match-statements)

---
