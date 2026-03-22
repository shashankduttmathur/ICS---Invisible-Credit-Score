
def build_features(data):
    income = data.get("income", 0)
    expenses = data.get("expenses", 0)
    savings = data.get("savings", 0)
    late = data.get("late_payments", 0)
    ratio = expenses / income if income else 1
    return [income, expenses, savings, late, ratio]
