from flask import Flask, flash, redirect, render_template, request, session, abort
import requests


app = Flask(__name__)



@app.route("/")
def index():
	return render_template('index.html')


@app.route("/currency", methods=["post"])
def currency():
	other = request.form.get("currencyname")
	res = requests.get("http://data.fixer.io/api/latest?access_key=18bfa087d7e77b59f23e3d7a3857d46a")
	data = res.json()
	Base = data["base"]
	rate = data["rates"][other]
	return render_template('currency.html', base = Base, value= rate, name= other)

def main():
	app.run(debug='True')

 

if __name__ == '__main__':
	main()
