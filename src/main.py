from flask import Flask 
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import os

class app:
	def __init__(self):
		self = Flask(__name__)
		_dir = os.path.dirname(os.path.abspath(__file__))
		self.template_folder = os.path.join(_dir, "templates")
		self.static_folder = os.path.join(_dir, "static")
		self.debug = True

		@self.errorhandler(404)
		async def page_not_found(e):
			return redirect(url_for("index"))

		@self.before_request
		async def before_request():
			pass

		@self.after_request
		async def after_request(response):
			response.headers.add("Access-Control-Allow-Origin", "*")
			response.headers.add("Cache-control", "no-cache, no-store, must-revalidate")
			return response

		@self.route("/", methods = ["GET"])
		async def slash():
			return redirect(url_for("index"))

		@self.route("/index.html", methods = ["GET"])
		async def index():
			return render_template("index.html")

		@self.route("/login", methods = ["POST"])
		async def login():

			data = [
				request.form["name"],
				request.form["pwd"],
			]
			print(data)
			return render_template("data.html",data=data)

		self.run(threaded=True)

if __name__ == "__main__":
	app()
