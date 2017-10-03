"""
Queenie Xiang
SoftDev1 pd7
HW6 -- Echo Echo Echo
2017-10-02
"""

#import all the libraries and functinos needed 
from flask import Flask, render_template, request

#create a new app 
app = Flask(__name__)


#Returns and displays the home page
@app.route("/") 
def hello_world():
    return render_template('submit_form.html');


#After user fills out the necessary information and click submit, they are directed to this page
@app.route("/information")
def return_user_info():
    #Grabs all of the information needed
    firstname = request.args['firstname']

    lastname = request.args['lastname']
    
    username = request.args['username'] 

    adjective = request.args['adj']

    method = request.method
    
    #Returns the information to the template
    return render_template('userinfo.html', username = username, firstname = firstname, lastname = lastname, adjective = adjective, method = method)



if __name__ == "__main__":
    app.debug = True
    app.run()


    
