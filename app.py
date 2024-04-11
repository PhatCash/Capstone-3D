from flask import Flask, render_template
import json

app = Flask(__name__)

# Try to render one first - comment out nav bar
#@app.route('/')
@app.route('/printer_status')
def printer_status():
    # with closes the file
    with open('./printer.JSON') as json_file:
        return render_template("printer_status.html", data=json.load(json_file)) # Send JSON data
    
# Implement the other two webpages - need same JSON
@app.route('/printer_page')
def printer_page():
    with open('./printer.JSON') as json_file: 
        return render_template("printer_page.html", data=json.load(json_file))


if __name__ == '__main__':
    app.run()