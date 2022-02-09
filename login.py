# Pyrebase Setup
from numpy import column_stack, logical_not
import pyrebase

fbconfig = {
  "apiKey": "AIzaSyAq2OeJ1K1u2rPZG7UBw691gYlpWF-DSKo",
  "authDomain": "fhm2022-90ce4.firebaseapp.com",
  "databaseURL": "https://fhm2022-90ce4-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "fhm2022-90ce4.appspot.com"
}

firebase = pyrebase.initialize_app(fbconfig)

auth = firebase.auth()

# Tkinter + TK Component Imports
from tkinter import *

root = Tk()

root.title("Free Homework Manager 2021")
root.geometry()

emailLabel = Label(root, text="Email:")
passwordLabel = Label(root, text="Password:")
emailEn = Entry(root)
passwordEn = Entry(root)

loginBn = Button(root, text="Login")
signupBn = Button(root, text="Sign Up for new account")

emailLabel.grid(row=0, column=0, sticky=E)
passwordLabel.grid(row=1, column=0, sticky=E)
emailEn.grid(row=0, column=1, columnspan=2, sticky=N+E+S+W)
passwordEn.grid(row=1, column=1, columnspan=2, sticky=N+E+S+W)
loginBn.grid(row=2, column=0, sticky=E)
signupBn.grid(row=2, column=2, sticky=W, columnspan=1)

root.mainloop()