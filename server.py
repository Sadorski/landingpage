from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def info():
    return render_template('index.html')

@app.route("/ninjas")
def ninja():
    return render_template('ninjas.html')

@app.route("/dojos/new")
def dojo():
    return render_template('dojos.html')
    # name = request.form['name']
    # email = request.form['email']
    # return redirect('/')
  

app.run(debug=True)