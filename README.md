# Password Checker Web Application

This project is a simple Flask-based web application that checks the strength of a password entered by the user. 
The password is evaluated based on specific criteria to determine whether it is strong or weak.

Features

- **Frontend**: A user-friendly interface where users can enter their password and view the results.
- **Backend**: Flask server to process password validation and respond with results.
- **Password Validation Criteria**:
  - Minimum length of 8 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one digit.
  - At least one special character (@, #, $, %, ^, &, +, =).
- **Visibility Toggle**: Allows users to show or hide the password input.
- **Dynamic Feedback**: Provides feedback on password strength in real-time.

---

Installation

Prerequisites

- Python 3.x
- Flask (install using `pip install flask`)



 Usage

1. Open the application in your web browser.
2. Enter a password in the input field.
3. Click the **Check Password** button.
4. View the feedback on password strength below the input field.

---

## Code Overview

### Backend (Flask)

- `app.py` contains the Flask server logic.
  - `/`: Renders the main HTML interface.
  - `/check-password`: API endpoint to validate the password.

- `is_strong_password(password)`: A function that checks if the password meets the required criteria.

### Frontend

- HTML rendered using Flask's `render_template_string`.
- JavaScript for dynamic interactions:
  - Sends password to the `/check-password` endpoint via a POST request.
  - Updates the UI based on the response.

Customization

1. **Styling**: Modify `file.css` to change the appearance.
2. **Password Validation**: Adjust criteria in the `is_strong_password` function within `app.py`.
3. **Background Image**: Replace the image URL in the CSS `body` style to change the background.

---

## Notes

- Ensure Flask is installed before running the application.
- The application is designed for local use. For production deployment, configure the server and security settings accordingly.

---

## License

This project is licensed under the MIT License. Feel free to modify and distribute it.

---

## Acknowledgments

- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Background image sourced from iStockPhoto.

