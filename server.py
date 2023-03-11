from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

#
# with open('database.csv', 'a') as database2:
#     fieldnames = ['Email', 'Subject', 'Message']
#     csv_writer = csv.DictWriter(database2, delimiter=',', fieldnames=fieldnames, quotechar='"',
#                                 quoting=csv.QUOTE_MINIMAL)
#     csv_writer.writeheader()


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        fieldnames = ['Email', 'Subject', 'Message']
        csv_writer = csv.DictWriter(database2, delimiter=',', fieldnames=fieldnames, quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow({'Email': email, 'Subject': subject, 'Message': message})


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. try again'




# @app.route('/index.html')
# def index_page():
#     return render_template('index.html')


# @app.route('/about.html')
# def about_me_page():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works_page():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')

