from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page is working!"

@app.route('/htop')
def htop():
    print("htop endpoint is accessed")  # Add this log
    name = "Tashu Garg"
    username = os.getenv('USER') or os.getenv('USERNAME')
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top command output
    top_output = subprocess.getoutput('top -n 1 -b')

    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    print("Flask is starting...")
    app.run(host='0.0.0.0', port=5000)
