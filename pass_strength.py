from flask import Flask, request, jsonify
from flask import render_template_string
import re

app = Flask(__name__)
def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[@#$%^&+=]', password):
        return False
    
    return True

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Password Checker</title>
        </head>
        <body>
            <div>
                <label for="passwordInput">Enter Password:</label>
                <input type="password" id="passwordInput" placeholder="Type your password">
                <span id="visibilityToggle" onclick="toggleVisibility()">👁️</span>
                <button id="checkButton" onclick="checkPassword()">Check Password</button>
                <p id="result"></p>
            </div>

            <script>
                function checkPassword() {
                    const passwordInput = document.getElementById('passwordInput');
                    const password = passwordInput.value;

                    fetch('/check-password', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                    .then(response => response.json())
                    .then(data => {
                        const resultElement = document.getElementById('result');
                        resultElement.innerHTML = data.is_strong
                            ? '<span style="color: green;">Password is strong!</span>'
                            : '<span style="color: red;">Password is weak. Please use a strong password and its length msut be > 8.</span>';
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }

                function toggleVisibility() {
                    const passwordInput = document.getElementById('passwordInput');
                    passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password';
                }
            </script>
        </body>
        </html>
    ''')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password is required'}), 400

    is_strong = is_strong_password(password)

    return jsonify({'is_strong': is_strong})

if __name__ == '__main__':
    app.run(debug=True)