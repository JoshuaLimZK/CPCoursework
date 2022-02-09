from tkinter import *

root = Tk()

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)

        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        frame = Login(container, self)
        frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.showFrame(frame)

class Login(Frame):
    def __init__(self, master):
        self.master = master
        emailLabel = Label(root, text="Email:")
        passwordLabel = Label(root, text="Password:")
        emailEn = Entry(root)
        passwordEn = Entry(root)

        loginBn = Button(root, text="Login")
        signupBn = Button(root.master, text="Sign Up for new account", command=lambda : root.showFrame(Signup(container, self)))

        emailLabel.grid(row=0, column=0, sticky=E)
        passwordLabel.grid(row=1, column=0, sticky=E)
        emailEn.grid(row=0, column=1, columnspan=2, sticky=N+E+S+W)
        passwordEn.grid(row=1, column=1, columnspan=2, sticky=N+E+S+W)
        loginBn.grid(row=2, column=0, sticky=E)
        signupBn.grid(row=2, column=2, sticky=W, columnspan=1)

class SignUp(Frame):
    def __init__(self, master):
        emailLabel = Label(root, text="Email:")
        passwordLabel = Label(root, text="Password:")
        emailEn = Entry(root)
        passwordEn = Entry(root)

        signupBn = Button(root, text="Sign Up")
        resetPwBn = Button(root, text="Reset Password")

        emailLabel.grid(row=0, column=0, sticky=E)
        passwordLabel.grid(row=1, column=0, sticky=E)
        emailEn.grid(row=0, column=1, columnspan=2, sticky=N+E+S+W)
        passwordEn.grid(row=1, column=1, columnspan=2, sticky=N+E+S+W)
        signupBn.grid(row=2, column=0, sticky=E)
        resetPwBn.grid(row=2, column=2, sticky=W, columnspan=1)    

def main():
    app = Main()
    root.mainloop()

if __name__ == "__main__":
    main()