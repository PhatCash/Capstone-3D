from flask import Flask, render_template

app = Flask(__name__)

# Try to render one first - comment out nav bar
@app.route('/')
def printer_page():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()