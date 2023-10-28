from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_password():
    if request.method == "POST":
        password_length = int(request.form.get("password_length", 12))
        use_digits = "use_digits" in request.form
        use_letters = "use_letters" in request.form
        use_symbols = "use_symbols" in request.form

        if not use_digits and not use_letters and not use_symbols:
            return "Error: At least one option must be selected."

        characters = ""
        if use_digits:
            characters += string.digits
        if use_letters:
            characters += string.ascii_letters
        if use_symbols:
            characters += string.punctuation
        
        password = generate_random_password(characters, password_length)
        #password = ensure_first_and_last_letters(password, use_letters)
        return render_template("index.html", password=password)

    return render_template("index.html")

def generate_random_password(characters, length):
    return "".join(random.choice(characters) for _ in range(length))

"""
def ensure_first_and_last_letters(password, use_letters):
    if use_letters and password and not password[0].isalpha():
        # Ensure first character is a letter
        password = random.choice(string.ascii_letters) + password[1:]

    if use_letters and password and not password[-1].isalpha():
        # Ensure last character is a letter
        password = password[:-1] + random.choice(string.ascii_letters)

    return password
"""
if __name__ == "__main__":
    app.run(debug=True)
