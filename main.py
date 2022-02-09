# Free Homework Manager 2022
# CREATED BY: Group S, Ethan Wang JQ, Joshua Lim ZK, Yeo ZW Quentin
# OPEN SOURCED ON GITHUB: https://github.com/JoshuaLimZK/CPCoursework/
# CREATED FOR: 2022 Sec 4 Computing Coursework


from urllib.parse import uses_relative
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import uuid

# Fetch the service account key JSON file contents
cred = credentials.Certificate('fhm2022-90ce4-firebase-adminsdk-ikwgp-ea96c48b2a.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fhm2022-90ce4-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Database reference')
data = ref.get()

import tkinter as tk
from tkcalendar import Calendar as cal
from PIL import ImageTk, Image

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Free Homework Manager 2021")
        
        self.nametxtvar = tk.StringVar()
        self.timeTakenVar = tk.StringVar()

        name = tk.Entry(self, textvariable=self.nametxtvar)
        saveInfoBn = tk.Button(self, text="Save Homework", command= self.saveInfo)
        pullDataBn = tk.Button(self, text="Pull Data", command= self.pullData)
        timeTaken = tk.Entry(self, textvariable=self.timeTakenVar)
        self.dueDataCal = cal(self, selectmode = "day", year = 2022, month = 1, day = 1, date_pattern = "dd-mm-yyyy")
        """
        logo = tk.Label(self, width = 20, height = 20)
        img = Image.open("./logo.png")
        img = img.resize((20, 20), Image.ANTIALIAS)
        logo.image = ImageTk.PhotoImage(img)

        logo.pack()
        """ 

        name.pack()
        timeTaken.pack()
        self.dueDataCal.pack()
        saveInfoBn.pack()
        pullDataBn.pack()

    def saveInfo(self):
        try:
            self.timeTakenVar = int(self.timeTakenVar.get())
        except:
            return

        randomUUID = str(uuid.uuid4())

        print("name is {}".format(self.nametxtvar.get()))
        firebase_admin.db.reference("server/data/homework")

        homeworkRef = ref.child(randomUUID)
        homeworkRef.update({
            "UUID": randomUUID,
            "name": self.nametxtvar.get(),
            "dueDate": self.dueDataCal.get_date(),
            "timeTaken": self.timeTakenVar
        })

        self.nametxtvar.set("")
        self.timeTakenVar = tk.StringVar()

    def pullData(self):
        data = ref.get()
        for key, value in data.items():
            print("{} : {}".format(key, value))


if __name__ == "__main__":
    window = Window()
    window.mainloop()