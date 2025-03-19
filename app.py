from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()


print("EMAIL_USER:", os.getenv("EMAIL_USER"))
print("EMAIL_PASS:", os.getenv("EMAIL_PASS"))

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  
app.config['MAIL_DEFAULT_SENDER'] = 'buzontrisha@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        strand = request.form['strand']

        msg = Message("New Enrollment Request",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=['delossantostrisha6@gmail.com'])

        msg.body = f"Name: {name}\nEmail: {email}\nStrand: {strand}"
        
        try:
            print("Attempting to send email...")
            print(f"Sender: {app.config['MAIL_DEFAULT_SENDER']}")
            print(f"Recipient: {msg.recipients}")
            print(f"Email Body:\n{msg.body}")
          
            mail.send(msg) 

            print("Email sent successfully!")
            flash('Enrollment submitted successfully! You will receive an email confirmation.', 'success')
        except Exception as e: 
            print(f"Error sending email: {e}")
            flash('An error occurred while submitting your enrollment. Please try again.', 'error')

        return redirect(url_for('enrollment'))

    return render_template('enrollment.html')

@app.route('/records')
def records():
    return render_template('records.html')

if __name__ == '__main__':  
    app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')  
    app.run(debug=True)
