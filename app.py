#Name: Ransford Addai
#Training ID: 32524
#Week Three(3) Python Programming Project



# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store operation functions
def safe_divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"

operations = {
    'add': lambda num1, num2: num1 + num2,       # Addition operation
    'subtract': lambda num1, num2: num1 - num2,  # Subtraction operation
    'multiply': lambda num1, num2: num1 * num2,  # Multiplication operation
    'divide': safe_divide,                      # Division operation with error handling
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    operation = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])  # Get the first number from the form
        num2 = float(request.form['num2'])  # Get the second number from the form
        operation_type = request.form['operation_type']  # Get the selected operation
        operation = operation_type.capitalize()  # Capitalize the operation name for display
        result = operations[operation_type](num1, num2)  # Perform the selected operation
    return render_template('index.html', result=result, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
