from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
print(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route('/<username>')
def always_send_back(username=None):
    # show the user profile for that user
    return render_template("index.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect("./success.html")
    else:
        return redirect('./error.html')
