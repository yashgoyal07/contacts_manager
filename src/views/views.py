from flask import request, redirect, url_for, session
from controllers.contacts_controller import ContactsController
from controllers.customers_controller import CustomersController
from helpers.utils import is_login
from my_service import app
import jinja2
import os

# this is very important because this will tell where our template folder is placed.
# without this we cannot render our templates or cannot attach external css/js.
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../', 'templates', )))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = ################   # your secret key (see readme to make a new one)


# views home page with main navbar if not logged in
# otherwise redirects to diary_home page with diary_navbar
@app.route('/')
def home():
    if is_login():
        return redirect(url_for('diary_home'))
    else:
        template = template_env.get_template("home.html")
        return template.render()


# render diary_home page with diary_navbar with logged customer(user) name
@app.route('/home')
def diary_home():
    template = template_env.get_template("diary_home.html")
    name = CustomersController().find_customer_name(session['email'], session['password'])
    return template.render(name=name)


# redirects to diary page if customer or user logged in
# otherwise redirects to login page
@app.route('/phone_diary')
def phone_diary():
    if is_login():
        return redirect(url_for('diary'))
    else:
        return redirect(url_for('login'))


# render phone_diary html file with particular content of logged  person
# which is checked using session cookies otherwise redirects to login page
@app.route('/diary')
def diary():
    try:
        if is_login():
            result = ContactsController().show_contact(session['email'], session['password'])
            if result == "something went wrong":
                return "please try again"
            else:
                template = template_env.get_template("phone_diary.html")
                name = CustomersController().find_customer_name(session['email'], session['password'])
                return template.render(list=result, name=name)
        else:
            return redirect(url_for('login'))
    except:
        return "Page Not Loaded Properly"


# perform action for new user or customer registration if request coming form post method
# otherwise renders signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            customer = request.form
            name = customer['name']
            email = customer['email']
            mobile = customer['mobile']
            password = customer['pass']
            error = CustomersController().create_customer(name, email, mobile, password)
            if error:
                return "Please Try Again"
            else:
                return "Registration Successful"
        except:
            return "Something Went Wrong"

    template = template_env.get_template("signup.html")
    return template.render()


# check credentials for user or customer who wants to login
# and setup cookies for future login if request coming form post method
# otherwise renders login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            customer = request.form
            email = customer['email']
            password = customer['pass']
            error = CustomersController().check_cred(email, password)
            if error:
                return "Please Try Again"
            else:
                session['email'] = customer['email']
                session['password'] = customer['pass']
                return redirect(url_for('diary'))
        except:
            return "Something Went Wrong"

    template = template_env.get_template("login.html")
    return template.render()


# simply remove cookies and renders login page
@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('login'))


# checked customer or user logged in or not
# if logged in, take data from form and customer id from
# customer's cookies and create new contact and redirect again on diary
# for updated values
# otherwise redirects to login page or showing error
@app.route('/cr_con', methods=['POST'])
def cr_con():
    try:
        if is_login():
            result = CustomersController().find_customer(session['email'], session['password'])
            if result == "something went wrong":
                return "please try again"
            else:
                contact = request.form
                contactname = contact['name']
                contactnumber = contact['mobile']
                contactdescription = contact['description']
                customerid = result
                error = ContactsController().create_contact(contactname, contactnumber, contactdescription, customerid)
                if error:
                    return "Please Try Again"
                else:
                    return redirect(url_for('diary'))
        else:
            return redirect(url_for('login'))

    except:
        return "Something Went Wrong"


# delete contact using customer's id from cookies and contact id send through url
# if delete function performed successfully, redirects again phone_diary page for
# updated values, otherwise render login page or showing error
@app.route('/del_con/<int:contactid>')
def del_con(contactid):
    try:
        if is_login():
            result = CustomersController().find_customer(session['email'], session['password'])
            if result == "something went wrong":
                return "please try again"
            else:
                customerid = result
                error = ContactsController().delete_contact(contactid, customerid)
                if error:
                    return "Please Try Again"
                else:
                    return redirect(url_for('diary'))
        else:
            return redirect(url_for('login'))

    except:
        return "Something Went Wrong"


# update contact using customer's id from cookies and contact id send through url
# and data send by user with post method. if delete function
# performed successfully, redirects again phone_diary page for
# updated values, otherwise render login page or showing error
@app.route('/upd_con/<int:contactid>', methods=['POST'])
def upd_con(contactid):
    try:
        if is_login():
            result = CustomersController().find_customer(session['email'], session['password'])
            if result == "something went wrong":
                return "please try again"
            else:
                contact = request.form
                contactname = contact['name']
                contactnumber = contact['mobile']
                contactdescription = contact['description']
                customerid = result
                error = ContactsController().update_contact(contactname, contactnumber, contactdescription, contactid, customerid)
                if error:
                    return "Please Try Again"
                else:
                    return redirect(url_for('diary'))
        else:
            return redirect(url_for('login'))

    except:
        return "Something Went Wrong"


if __name__ == '__main__':
    app.run(debug=True)
