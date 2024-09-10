from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a', encoding='utf-8') as database:
        name = data['nev']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {name}, {email}, {subject}, {message}')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong! Try again!'
    
def write_to_csv(data):
    with open('database.csv', mode='a', newline='', encoding='utf-8') as database2:
        name = data['nev']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])