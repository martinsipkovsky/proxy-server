from flask import Flask
from config_read import read_db

HOST = "127.0.0.1"
PORT = 5000

app = Flask(__name__, static_url_path="/php")

def open_webfile(filename):
    # This function will return web file from php folder
    with open("./php/" + filename, "r") as filehandle:
        return filehandle.read()

@app.route('/')
def index():
    return open_webfile('index.html')

@app.route('/Chart.min.js')
def chartjs():
    return open_webfile('Chart.min.js')

@app.route('/style.css')
def style():
    return open_webfile('style.css')

@app.route('/sidebar.js')
def sidebarjs():
    return open_webfile('sidebar.js')

@app.route('/jquery-3.6.0.min.js')
def jquery():
    return open_webfile('jquery-3.6.0.min.js')

@app.route('/api_requests')
def api_requests():
    return str(read_db()['counters']['requests'])

@app.route('/api_blocked')
def api_blocked():
    return str(read_db()['counters']['blocked'])

@app.route('/stats.js')
def statsjs():
    return open_webfile('/stats.js')

