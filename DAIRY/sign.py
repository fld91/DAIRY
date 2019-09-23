from django.http import HttpResponse
from django.shortcuts import render
@app.route('sign', methods = ['POST'])



def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')