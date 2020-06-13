
from flask import Flask
from flask import render_template # This function enables us to send our html file into the web site
from flask import request, redirect
import csv
app = Flask(__name__)

@app.route('/') # this makes that any body demand from our server, print "Hello, World".
#@app.route is a decorator used to match URLs to view functions in Flask apps.
def my_home():
  
    return render_template("index.html") # this function looks for template in our file, if not find it , give an error
# so we have to add a template file into our html file

@app.route('/<string:page_name>') 
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open("database.txt", "a") as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
	with open("database.csv", "a",newline="") as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database2,delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data=request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			return redirect("/thankyou.html") 
		except:
			return "The data is not asevd to the database!"
	else:
		return "Something went wrong"
    


