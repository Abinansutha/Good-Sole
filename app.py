from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
#    return 'Hello World!'

#this will be our login page eventually
    return '<a href="/admin">admin stuff</a> <br> <a href="/employee/">employee stuff</a>'
#

@app.route('/admin')
def admin_home():
    render_template('admin/home.html') #this should work properly??
    #templates/admin/home ?

@app.route('/employee')
def employee_home():
    render_template('employee/home.html')
    #templates/employee/home ?

if __name__ == '__main__':
    app.run()