from flask import Flask, render_template

app = Flask(__name__)

@app.route("/XD")
def flask():
	return "Hello Flask!"

@app.route("/")
def test():
	return render_template('bug.html')

@app.route('/chess')
def index():
	return render_template('chess.html')

if __name__ == "__main__":
	app.run(debug=True)