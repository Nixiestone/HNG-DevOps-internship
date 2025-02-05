from flask import Flask, request, jsonify
import requests
import math

app = Flask(__name__)

# Function to check if a number is prime
def is_prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

# Function to check if a number is armstrong
def is_armstrong_number(n):
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

# Function to get properties of a number
def get_properties(n):
    properties = []
    if is_armstrong_number(n):
        properties.append('armstrong')
    if n % 2 == 0:
        properties.append('even')
    else:
        properties.append('odd')
    return properties

# API endpoint to classify a number
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = int(request.args.get('number'))
        if number is None:
            return jsonify({'error': 'Number is required'}), 400
        
        # Get fun fact from numbersapi.com
        fun_fact_response = requests.get(f'http://numbersapi.com/{number}')
        fun_fact = fun_fact_response.text
        
        # Calculate properties
        is_prime = is_prime_number(number)
        is_perfect = is_perfect_number(number)
        properties = get_properties(number)
        digit_sum = sum(int(digit) for digit in str(number))
        
        return jsonify({
            'number': number,
            'is_prime': is_prime,
            'is_perfect': is_perfect,
            'properties': properties,
            'digit_sum': digit_sum,
            'fun_fact': fun_fact
        }), 200
    except ValueError:
        return jsonify({'error': 'Invalid number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)