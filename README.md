![](RackMultipart20240103-1-dfdzyl_html_a4a6072c68dd1cd9.jpg)

**CSE429**

**Computer vision and pattern recognition**

**Final Project Documentation**

**Group Members:**
Ahmed Abdelkader Ahmed – 120200028

Ahmad Mongy Saad – 120200033

Mahmoud Akrm Mohamed – 120200045

Mohamed Ayman Mohamed – 120200081

Peter Fayez Shafiq – 120200073

Ziad Hesham Al-Safy – 120200078

**To:**

DR. Ahmed Saleh

Eng. Mahmoud Sharshira

# Table of Contents

[ Overview: 3](#_Toc155205017)

[ Key Features: 3](#_Toc155205018)

[1.Login and Signup: 3](#_Toc155205019)

[2.Course and Week Selection: 3](#_Toc155205020)

[3.Face Recognition: 4](#_Toc155205021)

[4.Attendance Recording: 4](#_Toc155205022)

[5.Dynamic GUI: 5](#_Toc155205023)

[6. Firebase Integration: 5](#_Toc155205024)

[7.WEB Deploying using NGrok: 5](#_Toc155205025)

[6](#_Toc155205026)

[ Technologies Used: 6](#_Toc155205027)

[1.Programming Language: 6](#_Toc155205028)

[2.Libraries and Frameworks: 6](#_Toc155205029)

[3.Database: 6](#_Toc155205030)

[4. Web Framework: 6](#_Toc155205031)

[5. Image Processing: 7](#_Toc155205032)

[6. Android Development Dependencies: 7](#_Toc155205033)

[ How to Use: 7](#_Toc155205034)

[1.Login or Signup: 7](#_Toc155205035)

[2.Course and Week Selection: 7](#_Toc155205036)

[3.Face Recognition: 7](#_Toc155205037)

[4.Attendance Recording: 7](#_Toc155205038)

[ Benefits: 8](#_Toc155205039)

[1.Efficiency: 8](#_Toc155205040)

[2.Accuracy: 8](#_Toc155205041)

[3.Accessibility: 8](#_Toc155205042)

[ Project structure 8](#_Toc155205043)

[1. ADD\_Faces.py 8](#_Toc155205044)

[1. read\_random\_frames function: 8](#_Toc155205045)

[2. create\_images\_AND\_names function: 8](#_Toc155205046)

[3. findEncodings function: 9](#_Toc155205047)

[4. creatpik function: 9](#_Toc155205048)

[5. update\_pickle function: 9](#_Toc155205049)

[6. main function: 9](#_Toc155205050)

[2. FastAPI Server Code 9](#_Toc155205051)

[1. Importing Libraries and Modules 9](#_Toc155205052)

[2. FastAPI App Setup: 9](#_Toc155205053)

[3. Loading Encoded Data: 9](#_Toc155205054)

[4. Endpoint for Image Upload: 9](#_Toc155205055)

[5. Image Processing and Face Recognition: 10](#_Toc155205056)

[6. Face Matching and Result Compilation: 10](#_Toc155205057)

[7. Returning Result: 10](#_Toc155205058)

[8. Running the FastAPI Server: 10](#_Toc155205059)

[9. Additional Notes 10](#_Toc155205060)

[3. Firebase Authentication and Face Recognition GUI 10](#_Toc155205061)

[1. Importing Libraries and Modules 10](#_Toc155205062)

[2. Class: FirebaseAuthenticationApp 10](#_Toc155205063)

[3. Additional Notes: 11](#_Toc155205064)

[4. Mobile APP 11](#_Toc155205065)

[1. Introduction 11](#_Toc155205066)

[2. Dependencies 11](#_Toc155205067)

[3. Firebase Integration 11](#_Toc155205068)

[4. UI Components 11](#_Toc155205069)

[5. Camera Integration 12](#_Toc155205070)

[6. HTTP POST Request 12](#_Toc155205071)

[7. Image Handling 12](#_Toc155205072)

-
# Overview:

Welcome to the documentation for the Face Recognition and Attendance System project. This application is a mobile-based Application developed using face\_recognition (Python), and Kotlin .The Face Recognition and Attendance System is an innovative application that combines the power of face recognition technology, Firebase authentication, and a user-friendly graphical interface. This project is designed to streamline the process of taking attendance by utilizing facial features for recognition.

-
# Key Features:

1.
### **Login and Signup:**

- Users can securely log in or sign up using their email and password through Firebase authentication.

![](RackMultipart20240103-1-dfdzyl_html_e0f69855b390397c.png) ![](RackMultipart20240103-1-dfdzyl_html_da88ac8311904134.png) ![](RackMultipart20240103-1-dfdzyl_html_2c268dec5390ce14.png)

1.
### **Course and Week Selection:**

- After authentication, users can select the course and week for which they want to mark attendance.

![](RackMultipart20240103-1-dfdzyl_html_443c20d192b02b8.png)

![](RackMultipart20240103-1-dfdzyl_html_aa350567d2c6b6b0.png) ![](RackMultipart20240103-1-dfdzyl_html_1e03992fd799f896.png)

1.
### **Face Recognition:**

- The heart of the system lies in its face recognition capabilities. Users can upload an image, and the system will recognize faces, linking them to registered individuals.

![](RackMultipart20240103-1-dfdzyl_html_811dddbce2ff1077.png)

![](RackMultipart20240103-1-dfdzyl_html_6992c2e32dc4e3a0.png)

1.
### **Attendance Recording:**

- The recognized faces are then used to mark attendance for the selected course and week. The attendance data is stored securely on Firebase Realtime Database.

![](RackMultipart20240103-1-dfdzyl_html_e26010d543b312d5.png)

1.
### **Dynamic GUI:**

- The Graphical User Interface (GUI) is dynamic, adapting to different stages of the attendance process. It provides a smooth and intuitive user experience.

1.
### **Firebase Integration:**

- Firebase is utilized for user authentication and as a backend for storing attendance data. This ensures data security and accessibility from anywhere.

1.
### **WEB Deploying using NGrok:**

### ![](RackMultipart20240103-1-dfdzyl_html_6058b86d540aee39.png) ![](RackMultipart20240103-1-dfdzyl_html_909978a4c965fbb9.png)


-
# Technologies Used:

1.
### **Programming Language** :

- Python, Kotlin

1.
### **Libraries and Frameworks:**

- Tkinter
- Pyrebase
- Firebase Admin SDK
- FastAPI
- AndroidX Navigation (2.7.5)
- Kotlin Coroutines (1.3.9)
- Firebase BOM (32.7.0)
- OkHttp (4.9.1)
- AndroidX Core (1.12.0)
- AndroidX AppCompat (1.6.1)
- Material Design Library (1.11.0)
- ConstraintLayout (2.1.4)
- Firebase Authentication
- Google Play Services Authentication (20.7.0)
- Firebase Realtime Database
- Firebase Realtime Database (KTX, 20.3.0)

1.
### **Database:**

- Firebase Realtime Database

1.
### **Web Framework:**

- FastAPI

1.
### **Image Processing:**

- OpenCV, Pillow, face\_recognition

1.
### **Android Development Dependencies:**

implementation "androidx.navigation:navigation-fragment-ktx:2.7.5"

implementation "androidx.navigation:navigation-ui-ktx:2.7.5"

implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.9"

implementation platform("com.google.firebase:firebase-bom:32.7.0")

implementation "com.squareup.okhttp3:okhttp:4.9.1"

implementation "androidx.core:core-ktx:1.12.0"

implementation "androidx.appcompat:appcompat:1.6.1"

implementation "com.google.android.material:material:1.11.0"

implementation "androidx.constraintlayout:constraintlayout:2.1.4"

implementation "com.google.firebase:firebase-auth"

implementation "com.google.android.gms:play-services-auth:20.7.0"

implementation "com.google.firebase:firebase-database"

implementation"com.google.firebase:firebase-database **-ktx:20.3.0"**

-
# How to Use:

1.
### **Login or Signup:**

- Users start by logging in or creating an account through the secure Firebase authentication system.

1.
### **Course and Week Selection:**

- After authentication, users choose the course and week for which they want to mark attendance.

1.
### **Face Recognition:**

- Users upload an image containing faces. The system recognizes faces and displays the recognized names.

1.
### **Attendance Recording:**

- Recognized names are used to mark attendance for the selected course and week, and the data is stored in Firebase.

-
# Benefits:

1.
### **Efficiency:**

- Streamlines attendance marking, reducing the time and effort required in traditional methods.

1.
### **Accuracy:**

- Face recognition **ensures accurate and reliable attendance recording.**

1.
### **Accessibility:**

- Firebase integration allows access to attendance data from anywhere, promoting remote management.
- **User-Friendly:**
- The intuitive GUI makes the system user-friendly, catering to users with varying technical expertise.

-
# Project structure

1.
## ADD\_Faces.py

1.
### **read\_random\_frames function:**

- Purpose:

Reads a specified number of random frames from a video file.

- Parameters:

video\_path: Path to the input video file.

num\_frames\_to\_read: Number of frames to read from the video.

- Output:

Saves the randomly selected frames as individual image files in the "images" directory.

1.
### **create\_images\_AND\_names function:**

- Purpose:

Reads images from the "images" directory and extracts names from file names.

- Output:

Two lists: images (containing images) and names (containing corresponding names).

1.
### **findEncodings function:**

- Purpose:

Converts images to RGB format and finds face encodings using the face\_recognition library.

- Parameters:

images: List of images.

- Output:

List of face encodings.

1.
### **creatpik function:**

- Purpose:

Creates and saves a Pickle file containing face encodings and corresponding names.

- Output:

Saves the Pickle file named "EncodeFile.pkl".

1.
### **update\_pickle function:**

- Purpose:

Updates an existing Pickle file with new face encodings and names.

- Output:

Saves the updated Pickle file.

1.
### **main function:**

- Purpose:

The heart of the file as it , iterates through a directory of videos, reads random frames, and updates the Pickle file.

1.
## FastAPI Server Code

1.
### **Importing Libraries and Modules**
2.
### **FastAPI App Setup:**
3.
### **Loading Encoded Data:**

- Reads the face encodings and corresponding names from the Pickle file.

1.
### **Endpoint for Image Upload:**

- Defines a FastAPI endpoint for uploading images.

1.
### **Image Processing and Face Recognition:**

- Reads the uploaded image, processes it for face recognition.

1.
### **Face Matching and Result Compilation:**

- Compares the face encodings with the known encodings and appends the corresponding names to the result if a match is found.

1.
### **Returning Result:**

- Returns the result (list of recognized names) as the response.

1.
### **Running the FastAPI Server:**

- Runs the FastAPI server on http://127.0.0.1:8000/.

1.
### **Additional Notes**

- Ensure the necessary libraries (fastapi, uvicorn, face\_recognition, cv2, numpy) are installed before running the script.
- Add more comments if needed, especially for complex logic or important parts of the code.
- Consider adding exception handling to deal with potential errors during image processing or file reading.

1.
## Firebase Authentication and Face Recognition GUI

1.
### **Importing Libraries and Modules**
2.
### **Class: FirebaseAuthenticationApp**

- Initialization **:**
  - Initializes the GUI and sets up the initial configuration.
  - Sets up the Firebase configuration using the provided credentials.
  - Initializes Firebase authentication and required variables.
- logincreate\_widgets Method:
  - Creates and displays login widgets.
  - Entry fields for email and password, login and signup buttons.
- pathcreate\_widgets Method:
  - Creates and displays widgets for selecting the course and week.
  - Entry fields for course name and week number, save button.
- FRcreate\_widgetsMethod **:**
  - Creates and displays widgets for face recognition.
  - Image upload button, image display frame, recognition result display.
- delete\_widgetsMethod **:**
  - Deletes all widgets in the GUI.
- loginMethod **:**
  - Attempts to log in the user with provided email and password.
  - Handles successful login and errors.
- signupMethod **:**
  - Attempts to sign up a new user with provided email and password.
  - Prompts the user to log in after successful signup.
- upload **\_** image Method **:**
  - Allows the user to upload an image for recognition.
  - Displays the selected image in the GUI.
- recognizeMethod **:**
  - Sends the uploaded image to the FastAPI server for recognition.
  - Displays recognized people in the result text widget.
- delete\_imageMethod **:**
  - Deletes the uploaded image and resets the image frame.
- save\_input Method:
  - Saves the course name and week number from input fields.
  - Resets the GUI for face recognition.
- update\_pickle Method:
  - Updates the face recognition pickle file with a new person's face.
- findEncodingsMethod:
  - Finds face encodings for a given set of images.

1.
### **Additional Notes:**

- The code seems to use a custom Tkinter library ( **customtkinter** ) and **CTkMessagebox**. Ensure they are available or replace them with standard Tkinter elements if necessary.
- Confirm that the Firebase configuration is accurate and secure.
- Consider adding more detailed comments for complex or crucial parts of the code.

1.
## Mobile APP

1.
### **Introduction**

This document provides an overview of the Kotlin code implementation for the Attendance App developed in Android Studio. The app facilitates tracking attendance for classes and weeks, utilizing Firebase for data storage and retrieval.

1.
### **Dependencies**

The app relies on the following dependencies:

- Kotlin
- AndroidX
- Firebase SDK
- OkHttp
- Data Binding

1.
### **Firebase Integration**

Firebase is used for real-time data storage and retrieval. Key references include:

- reference: Reference to the root of the Firebase database.
- auth: Firebase Authentication instance.
- userRef, classRef, weekRef: References to specific locations in the database based on user and class information.

1.
### **UI Components**

- FragmentAtendanceBinding: Data Binding object for the attendance fragment.
- FAB (Floating Action Button): Toggles camera and person icons for user interaction.
- RecyclerView: Displays a list of students using SectionsAdapter.
- ProgressBar and TextView: Indicate loading state and provide user feedback.

1.
### **Camera Integration**

- startActivityForResult: Launches the camera intent to capture images.
- nActivityResult: Handles the result of the camera activity and processes the captured image.

1.
### **HTTP POST Request**

- postBitmapWithHeaderAsync: Sends a POST request with a Bitmap image to a specified API endpoint.
- Utilizes OkHttp for networking.
- Custom header ("ngrok-skip-browser-warning") added for skipping ngrok warning.

1.
### **Image Handling**

- saveImage: Saves a Bitmap image to the device's external storage.
- Uses Environment.getExternalStoragePublicDirectory for storing images.

16 **|** Page
