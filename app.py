from flask import Flask, render_template
import json

app = Flask(__name__)

# Try to render one first - comment out nav bar
@app.route('/')
def printer_page():
    # with closes the file
    with open('./printer.json') as json_file:
        return render_template("test.html", data=json.load(json_file)) # Send JSON data
    
if __name__ == '__main__':
    app.run()