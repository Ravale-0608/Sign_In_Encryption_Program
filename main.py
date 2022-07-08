import sqlite3
import tkinter
import tkinter.messagebox
import tkinter.font as tkFont


conn = sqlite3.connect('mydb.db')

cursor = conn.cursor()

encrypted_language = {"A": "3",
                      "B": "23",
                      "C": "Ae",
                      "D": "!A",
                      "E": "SA",
                      "F": "cvG",
                      "G": "gfh",
                      "H": "6",
                      "i": "^%$",
                      "J": "9O",
                      "K": "3#",
                      "l": ")(",
                      "M": "JGC",
                      "N": "45ZDFG",
                      "O": "POKM",
                      "P": "5YTGV",
                      "Q": "087",
                      "R": "546FTVG",
                      "S": "656YGV",
                      "T": "TGV7",
                      "U": "123X",
                      "V": "23N865",
                      "W": "1234)(",
                      "X": "@!#$5",
                      "Y": "{678}",
                      "Z": "zAWDFC"}

class Sign_In:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.font_size = tkFont.Font(family='Lucida Grande', size=50)
        self.sign_in_heading = tkinter.Label(self.main_window, text='Sign In', font=self.font_size)

        self.ask_name = tkinter.Label(self.main_window, text='Enter your name:')
        self.ask_name_entry = tkinter.Entry(self.main_window, width=30)

        self.ask_password = tkinter.Label(self.main_window, text='Enter your password:')
        self.ask_password_entry = tkinter.Entry(self.main_window, width=30)

        self.enter_2 = tkinter.Button(self.main_window, text='ENTER', command=self.checking_password)

        self.sign_in_heading.pack()
        self.ask_name.pack()
        self.ask_name_entry.pack()
        self.ask_password.pack()
        self.ask_password_entry.pack()
        self.enter_2.pack()

        tkinter.mainloop()

    def checking_password(self):
        if (self.ask_name_entry.get() == "" or self.ask_password_entry.get() == ""):
            tkinter.messagebox.showwarning('Error', 'You have entered an empty field')
        else:
            encrypted_password_2 = ""
            password_2 = self.ask_password_entry.get()

            for i in range(len(password_2)):
                for key in encrypted_language:
                    if password_2[i] == key:
                        encrypted_password_2 += encrypted_language[key]


            query_3 = "SELECT [NAME] AS 'name', [PASSWORD] AS 'password' FROM [User] WHERE [NAME] = '" + self.ask_name_entry.get() + "'"
            print(encrypted_password_2)
            cursor.execute(query_3)

            hold = cursor.fetchone()
            print(hold[1])
            if hold is None:
                tkinter.messagebox.showerror('Error', 'Name does not exist')

            if hold[1] == encrypted_password_2:
                tkinter.messagebox.showinfo('Success', "Sign In successful")
            else:
                tkinter.messagebox.showerror('Error', 'You entered the wrong password')

Sign_In()