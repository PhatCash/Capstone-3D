from flask import Flask, request, render_template, redirect
import json
from update_funcs.updateJSON import add_printer

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/printer_status')

# Try to render one first - comment out nav bar
@app.route('/printer_status')
def status():
    # with closes the file
    with open('./data/data.json') as json_file, open('./data/printers.json') as printer_file:
        return render_template("printer_status.html", data=json.load(json_file), printers=json.load(printer_file)) # Send json data
    
# Implement the other two webpages - need same json
@app.route('/printer_page', methods=["GET","POST"])
def page():
    if request.method == "POST":
        printerID = request.form.get("printer-id")
        printerPort = request.form.get("printer-port")
        filamentType = request.form.get("filament-type")
        nozzleSize = request.form.get("nozzle-size")
        add_printer(printerID, printerPort, filamentType, nozzleSize)

    with open('./data/printers.json') as json_file: 
        return render_template("printer_page.html", data=json.load(json_file))

@app.route('/configure_printer')
def configure():
    with open('./data/data.json') as json_file:
        return render_template("configure_printer.html", data=json.load(json_file))

@app.route('/job_queue')
def queue():
    with open('./data/data.json') as json_file:
        return render_template("job_queue.html", data=json.load(json_file))

@app.route('/add_printer', methods=["GET","POST"])
def add():
    with open('./data/data.json') as json_file:
        return render_template("add_printer.html", data=json.load(json_file))

if __name__ == '__main__':
    app.run()