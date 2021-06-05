# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

  
@app.route("/")
def home():
    return render_template("name.html")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

sleep(1)

clear()
  
app.run(debug=True, host='0.0.0.0',port=33507)