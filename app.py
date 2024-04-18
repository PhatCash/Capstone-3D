from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

@app.route("/")
def home():
    #return "hell no, flask!"
    return redirect('/printer_status')

# Try to render one first - comment out nav bar
#@app.route('/')
@app.route('/printer_status')
def status():
    # with closes the file
    with open('./printer.JSON') as json_file:
        return render_template("printer_status.html", data=json.load(json_file)) # Send JSON data
    
# Implement the other two webpages - need same JSON
# Will change soon
@app.route('/printer_page')
def page():
    with open('./printer.JSON') as json_file: 
        return render_template("printer_page.html", data=json.load(json_file))

@app.route('/configure_printer')
def configure():
    with open('./printer.JSON') as json_file:
        return render_template("configure_printer.html", data=json.load(json_file))

if __name__ == '__main__':
    app.run()