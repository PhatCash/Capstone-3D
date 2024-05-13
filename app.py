from flask import Flask, request, render_template, redirect, flash
import json
from update_funcs.updateJSON import add_printer

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return redirect('/printer_status')

# Try to render one first - comment out nav bar
@app.route('/printer_status')
def status():
    # with closes the file
    with open('./Web_UI/data/data.json') as json_file, open('./Web_UI/data/printers.json') as printer_file:
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
        flash("Printer {printerID} Added", printerID)

    # Distinguish between the printers.JSON and filaments.JSON
    with open('./Web_UI/data/printers.json') as printer_file, open('./Web_UI/data/filaments.json') as filament_file:
        printers = json.load(printer_file)
        filaments = json.load(filament_file)
        return render_template("printer_page.html", data_printers=printers, data_filaments=filaments)

@app.route('/configure_printer')
def configure():
    with open('./Web_UI/data/data.json') as json_file:
        return render_template("configure_printer.html", data=json.load(json_file))

@app.route('/job_queue')
def queue():
    with open('./Web_UI/data/data.json') as json_file:
        return render_template("job_queue.html", data=json.load(json_file))

@app.route('/add_printer', methods=["GET","POST"])
def add():
    with open('./Web_UI/data/data.json') as json_file:
        return render_template("add_printer.html", data=json.load(json_file))

if __name__ == '__main__':
    app.run(port=5100)