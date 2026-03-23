from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Only allow Afira Azeiz
ALLOWED_NAME = "Afira Aziez"
ALLOWED_DOB = "2008-05-09"  # YYYY-MM-DD

# ---------------------------
# Login page
# ---------------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        dob = request.form.get('dob', '')
        if name.lower() == ALLOWED_NAME.lower() and dob == ALLOWED_DOB:
            # Redirect to birthday message page first
            return redirect(url_for('birthday_msg', user_name=name))
        else:
            error = "Access Denied! ❌"
    return render_template('login.html', error=error)

# ---------------------------
# Birthday message page
# ---------------------------
@app.route('/birthday')
def birthday_msg():
    user_name = request.args.get('user_name', 'Friend')
    return render_template('birthday_msg.html', user_name=user_name)

# ---------------------------
# About pages
# ---------------------------
@app.route('/about1')
def about1():
    user_name = request.args.get('user_name', 'Friend')
    return render_template('about1.html', user_name=user_name)

@app.route('/about2')
def about2():
    return render_template('about2.html')

@app.route('/about3')
def about3():
    return render_template('about3.html')

# ---------------------------
# Photo pages with music
# ---------------------------
@app.route('/photo1')
def photo1():
    return render_template('photo1.html')

@app.route('/photo2')
def photo2():
    return render_template('photo2.html')

@app.route('/photo3')
def photo3():
    return render_template('photo3.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        feedback_text = request.form.get('feedback')
        # For now, we just print to console. Later you can save to a file.
        print(f"Feedback from {name}: {feedback_text}")
        message = "Thank you for your feedback! 💖"
    return render_template('feedback.html', message=message)
# ---------------------------
# Run the app
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)