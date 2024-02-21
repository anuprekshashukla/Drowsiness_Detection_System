from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn

secret_key = str(os.urandom(24))



# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index.html")
    else:
        # pass # unknown
        return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run()
    
