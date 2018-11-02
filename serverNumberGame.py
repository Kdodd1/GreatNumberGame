from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)
app.secret_key = "secrect"
@app.route('/')
def index():
	if 'randNum' not in session:
		session['randNum'] = random.randrange(0, 101)
	if "guess" not in session:
		session["guess"] = 0
	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] = int(request.form['guess'])

	return redirect("/")
@app.route('/reset')
def reset():
	session.clear()

	return redirect("/")

if __name__=='__main__':
	app.run(debug=True)