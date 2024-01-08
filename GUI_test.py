import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import pyrebase
import firebase_admin
import customtkinter as ctk 
from CTkMessagebox import CTkMessagebox
from firebase_admin import db, credentials
import cv2
import pickle
import face_recognition




class FirebaseAuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")
        self.root.title("Login Page")

        # Firebase Configuration
        self.firebase_config = {
            'apiKey': "AIzaSyBbJQSqlpv_xh9M2EePWjYVDgmqa7QNSuE",
            'authDomain': "atendance-app-2ead8.firebaseapp.com",
            'databaseURL': "https://atendance-app-2ead8-default-rtdb.firebaseio.com",
            'projectId': "atendance-app-2ead8",
            'storageBucket': "atendance-app-2ead8.appspot.com",
            'messagingSenderId': "260193144573",
            'appId': "1:260193144573:web:42b93da0dd8e2f9406b894",
        }

        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()

        self.course = tk.StringVar()
        self.week = tk.StringVar()
        self.user_id = tk.StringVar()
        self.logincreate_widgets()

    def logincreate_widgets(self):
        #greyframe
        self.loginframe = ctk.CTkFrame(self.root)
        self.loginframe.pack(pady=100,padx=40, fill='both',expand=True) 
        #main label
        self.main_page = ctk.CTkLabel(self.root, text="Log In Page", font=('Arial', 22),  width=12, height=2)
        self.main_page.pack(pady=12,padx=10)
        self.main_page.place(x = 320, y = 60)
        # Welcome label
        self.welcom = ctk.CTkLabel(self.loginframe, text="Welcome :) ", font=('Arial', 16),  width=12, height=2)
        self.welcom.pack(pady=12,padx=10)
        self.welcom.place(x = 300, y = 40)

        self.mail_entry= ctk.CTkEntry(self.loginframe,placeholder_text="EX:McGonagall@hogwarts.edu.uk", width= 300) 
        self.mail_entry.pack(pady=12,padx=10) 
        self.mail_entry.place(x = 200, y = 90)

        self.password_entry= ctk.CTkEntry(self.loginframe, placeholder_text="Password", show="*",width= 300) 
        self.password_entry.pack(pady=12,padx=10) 
        self.password_entry.place(x = 200, y = 150)

        self.login_button = ctk.CTkButton(self.loginframe, text="Login", command=self.login)
        self.login_button.pack()
        self.login_button.place(x = 270, y = 220)

        self.signup_button = ctk.CTkButton(self.loginframe, text="Signup", command=self.signup)
        self.signup_button.pack()
        self.signup_button.place(x = 270, y = 260)

    def pathcreate_widgets(self):
            self.root.title("Select Course And Week")
            #greyframe
            self.pathframe = ctk.CTkFrame(self.root)
            self.pathframe.pack(pady=150,padx=190, fill='both',expand=True) 

            self.course_label = ctk.CTkLabel(self.pathframe, text="Course Name :", font=('Arial', 18))
            self.course_label.pack()
            self.course_label.place(x = 70, y = 90)

            self.course_entry = ctk.CTkEntry(self.pathframe, placeholder_text="CSE123")
            self.course_entry.pack()
            self.course_entry.place(x = 200, y = 90)

            self.week_label = ctk.CTkLabel(self.pathframe, text="Week Number :", font=('Arial', 18))
            self.week_label.pack()
            self.week_label.place(x = 70, y = 150)

            self.week_entry = ctk.CTkEntry(self.pathframe, placeholder_text= "5")
            self.week_entry.pack()
            self.week_entry.place(x = 200, y = 150)


            # Buttons to take input and print values
            self.button_path = ctk.CTkButton(self.pathframe, text="Save", command=self.save_input, height= 40, width= 100)
            self.button_path.pack()
            self.button_path.place(x = 165, y = 220)

    def FRcreate_widgets(self):
        self.root.title("Face Recognition App")
        self.fr = ctk.CTkFrame(self.root)
        self.fr.pack(pady=40,padx=40, fill='both',expand=True) 


        # Create a frame to display the image
        self.image_frame = ctk.CTkFrame(self.fr)
        self.image_frame.pack()
        self.image_frame.place(x = 10, y = 10)

        self.upload_button = ctk.CTkButton(self.fr, width=15, height=2, text="Upload Image", command=self.upload_image,font=('Arial', 12))
        self.upload_button.pack()
        self.upload_button.place(x = 10, y = 330)

        # Display an initial frame before the image is chosen
        initial_image = Image.new("RGB", (300, 300), "white")
        initial_photo = ctk.CTkImage(initial_image)

        self.img_label = ctk.CTkLabel(self.image_frame,text="",width= 250, height=250)
        self.img_label.pack()

        # # Create and set up the recognition result label
        self.result_label = ctk.CTkLabel(self.fr, text="Recognized People", font=('Arial', 16), width=16, height=3)
        self.result_label.pack()
        self.result_label.place(x = 500, y = 20)

        # # Create a text widget to display the result
        self.result_text = tk.Text(self.fr, height=5, width=40)
        self.result_text.pack()
        self.result_text.place(x = 530, y = 60)


        # Create and set up the recognize button
        self.recognize_button = ctk.CTkButton(self.fr, text="Recognize", font=('Arial', 12), width=15, height=2,command=self.recognize)
        self.recognize_button.pack(pady=10)
        self.recognize_button.place(x = 168,y = 330 )

        #delte button 
        self.delete_button = ctk.CTkButton(self.fr, width=15, height=2, text="Delete", command=self.delete_image,
                                       font=('Arial', 12)) 
        self.delete_button.pack()
        self.delete_button.place(x=10, y=390)

        #QUIT
        self.quit_button = ctk.CTkButton(self.root, text = 'Quit', command = root.destroy, font = ('calibri', 16, 'bold', 'underline'), width=10, height=2)
        self.quit_button.pack()
        self.quit_button.place(x = 660, y = 510)

        # self.personid= ctk.CTkEntry(self.fr,placeholder_text="120200028", width= 150) 
        # self.personid.pack(pady=12,padx=10) 
        # self.personid.place(x = 200, y = 90)

        #    # Create and set up the recognize button
        # self.addp = ctk.CTkButton(self.fr, text="Add Person", font=('Arial', 19),command=self.update_pickle, width= 20, height= 10)
        # self.addp.pack(pady=10)
        # self.addp.place(x = 168,y = 530 )

        
    def delete_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        email = self.mail_entry.get()
        password = self.password_entry.get()
        try:
            login = self.auth.sign_in_with_email_and_password(email, password)
            print(self.auth.get_account_info(login['idToken']))
            email = self.auth.get_account_info(login['idToken'])['users'][0]['email']
            print(email)
            self.user_id =  login['localId']
            self.delete_widgets()
            self.pathcreate_widgets()
            CTkMessagebox(title = "log In",message=  "Loged In successfully!", icon= "check")
        except:
            CTkMessagebox(title = "Error",message=  "An Unexpected Error happened :(", icon= "cancel")

    def signup(self):
        email = self.mail_entry.get()
        password = self.password_entry.get()
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            CTkMessagebox(title = "Signup",message=  "Account created successfully!", icon= "check")
            msg = CTkMessagebox(title="login", message="Do you want to login?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            response = msg.get()
            if response=="Yes":
                self.login()      
        except:
            CTkMessagebox(title = "Signup",message=  "Signup Error ;( ,Check your e-mail format!", icon= "cancel")

    def upload_image(self):
        self.result_text.delete(1.0, tk.END)
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Display the selected image in the frame
            image = Image.open(file_path)
            image = image.resize((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.img_label.configure(image=photo)
            self.img_label.image = photo
            # Save the file path for later use
            self.file_path = file_path

    def recognize(self):
        if hasattr(self, 'file_path'):
            files = {'file': open(self.file_path, 'rb')}
            response = requests.post('http://127.0.0.1:8000/upload/', files=files)
            # Update the result text widget
            result = response.json()
            self.result_text.delete(1.0, tk.END)
            for person in result:
                self.result_text.insert(tk.END, f"{person}\n")
            db.reference(f"/{self.user_id}/{self.course}").update({ self.week : result})
        else:
            # If no file is selected, show an error message
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please upload an image first.")

    def delete_image(self):
        # Delete the uploaded image and reset the image frame to white
        if hasattr(self, 'file_path'):
                initial_image = Image.new("RGB", (300, 300), "white")
                initial_photo = ImageTk.PhotoImage(initial_image)
                self.img_label.configure(image=initial_photo)
                self.img_label.image = initial_photo
                self.result_text.delete(1.0, tk.END)
                del self.file_path
        else:
            # If no file is selected, show an error message
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "No image to delete.")

    def save_input(self):
        self.course = self.course_entry.get()
        self.week = self.week_entry.get()
        if(self.week != "" and self.course != ""):
            self.delete_widgets()
            self.FRcreate_widgets()
        else:
            CTkMessagebox(title="Error", message="Cells cannot be empty", icon="warning")

    def update_pickle(self):
        with open("EncodeFile.pkl", 'rb') as file:
            existing_data = pickle.load(file)
        trained_people, names = existing_data
        new_image = cv2.imread(self.file_path)
        new_name = self.personid.get()
        new_trained_people = findEncodings(new_image)
        trained_people.extend(new_trained_people)
        names.extend(new_name)
        updated_data = [trained_people, names]
        with open("EncodeFile.pkl", 'wb') as file:
            pickle.dump(updated_data, file)



    
if __name__ == "__main__":

    cred = credentials.Certificate(creds)
    firebase_admin.initialize_app(cred, {"databaseURL" : "https://atendance-app-2ead8-default-rtdb.firebaseio.com"})


    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("blue") 
    root = ctk.CTk() 
    app = FirebaseAuthenticationApp(root)
    root.mainloop()
