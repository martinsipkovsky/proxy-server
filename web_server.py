from flask import Flask, render_template
from config_read import read_db
from random import choice

HOST = "127.0.0.1"
PORT = 5000

app = Flask(__name__, template_folder='/static')

def open_webfile(filename):
    # This function will return web file from php folder
    with open("./static/" + filename, "r") as filehandle:
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

@app.route('/chart.js')
def chart2js():
    return open_webfile('/chart.js')

@app.route('/api_chart_requests')
def api_chart_requests():
    return str(choice(range(0, 500)))

@app.route('/api_chart_blocked')
def api_chart_blocked():
    return str(choice(range(0, 500)))

@app.route('/get_ip')
def get_ip():
    return str(read_db()['network']['ip'])

@app.route('/ip_checker.js')
def ip_checker():
    return open_webfile('ip_checker.js')

@app.route('/proxy_status')
def proxy_status():
    return str(read_db()['status']['proxy'])

@app.route('/ghost_status')
def ghost_status():
    return str(read_db()['status']['ghost'])

@app.route('/vpn_status')
def vpn_status():
    return str(read_db()['status']['vpn'])

@app.route('/tor_status')
def tor_status():
    return str(read_db()['status']['tor'])
