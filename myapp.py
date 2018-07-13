###web server codes
from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
   return("Hello World")
if __name__== '__main__':

   app.run(debug=True, host='0.0.0.0')

### new web server code
from flask import Flask
import myapp.py

if __name__== '__main__':
  app.run

###my web server code
from flask import Flask
app = Flask(__name__)
@app.route('/Jay.com')

def whoami():
    return("Welcome to the Kings' Hub")
if __name__== '__main__':

     app.run(debug=True, host='0.0.0.0')
     
###html code
     
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')
if __name__== '__main__':

    app.run (debug = True, host = '0.0.0.0')


# global_code_files
