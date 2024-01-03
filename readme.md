<img src="media/image1.jpg" style="width:6.26806in;height:1.82917in" />

**CSE429**

**Computer vision and pattern recognition**

**Final Project Documentation**

**Group Members:  
**Ahmed Abdelkader Ahmed – 120200028

Ahmad Mongy Saad – 120200033

Mahmoud Akrm Mohamed – 120200045

Mohamed Ayman Mohamed – 120200081

Peter Fayez Shafiq – 120200073

Ziad Hesham Al-Safy – 120200078

**To:**

DR. Ahmed Saleh

Eng. Mahmoud Sharshira

# Table of Contents

[• Overview: [3](#overview)](#overview)

[• Key Features: [3](#key-features)](#key-features)

[1. Login and Signup: [3](#login-and-signup)](#login-and-signup)

[2. Course and Week Selection:
[3](#course-and-week-selection)](#course-and-week-selection)

[3. Face Recognition: [4](#face-recognition)](#face-recognition)

[4. Attendance Recording:
[4](#attendance-recording)](#attendance-recording)

[5. Dynamic GUI: [5](#dynamic-gui)](#dynamic-gui)

[6. Firebase Integration:
[5](#firebase-integration)](#firebase-integration)

[7. WEB Deploying using NGrok:
[5](#web-deploying-using-ngrok)](#web-deploying-using-ngrok)

[[6](#section)](#section)

[• Technologies Used: [6](#technologies-used)](#technologies-used)

[1. Programming Language:
[6](#programming-language)](#programming-language)

[2. Libraries and Frameworks:
[6](#libraries-and-frameworks)](#libraries-and-frameworks)

[3. Database: [6](#database)](#database)

[4. Web Framework: [6](#web-framework)](#web-framework)

[5. Image Processing: [7](#image-processing)](#image-processing)

[6. Android Development Dependencies:
[7](#android-development-dependencies)](#android-development-dependencies)

[• How to Use: [7](#how-to-use)](#how-to-use)

[1. Login or Signup: [7](#login-or-signup)](#login-or-signup)

[2. Course and Week Selection:
[7](#course-and-week-selection-1)](#course-and-week-selection-1)

[3. Face Recognition: [7](#face-recognition-1)](#face-recognition-1)

[4. Attendance Recording:
[7](#attendance-recording-1)](#attendance-recording-1)

[• Benefits: [8](#benefits)](#benefits)

[1. Efficiency: [8](#efficiency)](#efficiency)

[2. Accuracy: [8](#accuracy)](#accuracy)

[3. Accessibility: [8](#accessibility)](#accessibility)

[• Project structure [8](#project-structure)](#project-structure)

[1. ADD_Faces.py [8](#add_faces.py)](#add_faces.py)

[1. read_random_frames function:
[8](#read_random_frames-function)](#read_random_frames-function)

[2. create_images_AND_names function:
[8](#create_images_and_names-function)](#create_images_and_names-function)

[3. findEncodings function:
[9](#findencodings-function)](#findencodings-function)

[4. creatpik function: [9](#creatpik-function)](#creatpik-function)

[5. update_pickle function:
[9](#update_pickle-function)](#update_pickle-function)

[6. main function: [9](#main-function)](#main-function)

[2. FastAPI Server Code [9](#fastapi-server-code)](#fastapi-server-code)

[1. Importing Libraries and Modules
[9](#importing-libraries-and-modules)](#importing-libraries-and-modules)

[2. FastAPI App Setup: [9](#fastapi-app-setup)](#fastapi-app-setup)

[3. Loading Encoded Data:
[9](#loading-encoded-data)](#loading-encoded-data)

[4. Endpoint for Image Upload:
[9](#endpoint-for-image-upload)](#endpoint-for-image-upload)

[5. Image Processing and Face Recognition:
[10](#image-processing-and-face-recognition)](#image-processing-and-face-recognition)

[6. Face Matching and Result Compilation:
[10](#face-matching-and-result-compilation)](#face-matching-and-result-compilation)

[7. Returning Result: [10](#returning-result)](#returning-result)

[8. Running the FastAPI Server:
[10](#running-the-fastapi-server)](#running-the-fastapi-server)

[9. Additional Notes [10](#additional-notes)](#additional-notes)

[3. Firebase Authentication and Face Recognition GUI
[10](#firebase-authentication-and-face-recognition-gui)](#firebase-authentication-and-face-recognition-gui)

[1. Importing Libraries and Modules
[10](#importing-libraries-and-modules-1)](#importing-libraries-and-modules-1)

[2. Class: FirebaseAuthenticationApp
[10](#class-firebaseauthenticationapp)](#class-firebaseauthenticationapp)

[3. Additional Notes: [11](#additional-notes-1)](#additional-notes-1)

[4. Mobile APP [11](#mobile-app)](#mobile-app)

[1. Introduction [11](#introduction)](#introduction)

[2. Dependencies [11](#dependencies)](#dependencies)

[3. Firebase Integration
[11](#firebase-integration-1)](#firebase-integration-1)

[4. UI Components [11](#ui-components)](#ui-components)

[5. Camera Integration [12](#camera-integration)](#camera-integration)

[6. HTTP POST Request [12](#http-post-request)](#http-post-request)

[7. Image Handling [12](#image-handling)](#image-handling)

-   # Overview:

Welcome to the documentation for the Face Recognition and Attendance
System project. This application is a mobile-based Application developed
using face_recognition (Python), and Kotlin .The Face Recognition and
Attendance System is an innovative application that combines the power
of face recognition technology, Firebase authentication, and a
user-friendly graphical interface. This project is designed to
streamline the process of taking attendance by utilizing facial features
for recognition.

-   # Key Features:

1.  ### **Login and Signup:**

    -   Users can securely log in or sign up using their email and
        password through Firebase authentication.

<img src="media/image2.png" style="width:2.43333in;height:1.89653in" /><img src="media/image3.png" style="width:1.33333in;height:1.96736in" /><img src="media/image4.png" style="width:1.41667in;height:2.09028in" />

2.  ### **Course and Week Selection:**

    -   After authentication, users can select the course and week for
        which they want to mark attendance.

<img src="media/image5.png" style="width:1.65in;height:2.43472in" />

<img src="media/image6.png" style="width:1.48333in;height:2.18889in" /><img src="media/image7.png" style="width:2.78333in;height:2.19167in" />

3.  ### **Face Recognition:**

    -   The heart of the system lies in its face recognition
        capabilities. Users can upload an image, and the system will
        recognize faces, linking them to registered individuals.

<img src="media/image8.png" style="width:3.33333in;height:2.60764in" />

<img src="media/image9.png" style="width:1.66597in;height:2.45903in" />

4.  ### **Attendance Recording:**

    -   The recognized faces are then used to mark attendance for the
        selected course and week. The attendance data is stored securely
        on Firebase Realtime Database.

<img src="media/image10.png" style="width:6.26806in;height:2.90347in" />

5.  ### **Dynamic GUI:**

    -   The Graphical User Interface (GUI) is dynamic, adapting to
        different stages of the attendance process. It provides a smooth
        and intuitive user experience.

6.  ### **Firebase Integration:**

    -   Firebase is utilized for user authentication and as a backend
        for storing attendance data. This ensures data security and
        accessibility from anywhere.

7.  ### **WEB Deploying using NGrok:**

### <img src="media/image11.png" style="width:2.53333in;height:1.49373in" /><img src="media/image12.png" style="width:4.84741in;height:2.46667in" />

-   # Technologies Used:

1.  ### **Programming Language**: 

    -   Python, Kotlin

2.  ### **Libraries and Frameworks:**

    -   Tkinter

    -   Pyrebase

    -   Firebase Admin SDK

    -   FastAPI

    -   AndroidX Navigation (2.7.5)

    -   Kotlin Coroutines (1.3.9)

    -   Firebase BOM (32.7.0)

    -   OkHttp (4.9.1)

    -   AndroidX Core (1.12.0)

    -   AndroidX AppCompat (1.6.1)

    -   Material Design Library (1.11.0)

    -   ConstraintLayout (2.1.4)

    -   Firebase Authentication

    -   Google Play Services Authentication (20.7.0)

    -   Firebase Realtime Database

    -   Firebase Realtime Database (KTX, 20.3.0)

3.  ### **Database:**

    -   Firebase Realtime Database

4.  ### **Web Framework:** 

    -   FastAPI

5.  ### **Image Processing:** 

    -   OpenCV, Pillow, face_recognition

6.  ### **Android Development Dependencies:**

> implementation "androidx.navigation:navigation-fragment-ktx:2.7.5"
>
> implementation "androidx.navigation:navigation-ui-ktx:2.7.5"
>
> implementation
> "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.9"
>
> implementation platform("com.google.firebase:firebase-bom:32.7.0")
>
> implementation "com.squareup.okhttp3:okhttp:4.9.1"
>
> implementation "androidx.core:core-ktx:1.12.0"
>
> implementation "androidx.appcompat:appcompat:1.6.1"
>
> implementation "com.google.android.material:material:1.11.0"
>
> implementation "androidx.constraintlayout:constraintlayout:2.1.4"
>
> implementation "com.google.firebase:firebase-auth"
>
> implementation "com.google.android.gms:play-services-auth:20.7.0"
>
> implementation "com.google.firebase:firebase-database"
>
> implementation"com.google.firebase:firebase-database**-ktx:20.3.0"  
> **

-   # How to Use:

1.  ### **Login or Signup:**

    -   Users start by logging in or creating an account through the
        secure Firebase authentication system.

2.  ### **Course and Week Selection:**

    -   After authentication, users choose the course and week for which
        they want to mark attendance.

3.  ### **Face Recognition:**

    -   Users upload an image containing faces. The system recognizes
        faces and displays the recognized names.

4.  ### **Attendance Recording:**

    -   Recognized names are used to mark attendance for the selected
        course and week, and the data is stored in Firebase.

-   # Benefits:

1.  ### **Efficiency:**

    -   Streamlines attendance marking, reducing the time and effort
        required in traditional methods.

2.  ### **Accuracy:**

    -   Face recognition **ensures accurate and reliable attendance
        recording.**

3.  ### **Accessibility:**

    -   Firebase integration allows access to attendance data from
        anywhere, promoting remote management.

    -   **User-Friendly:**

    -   The intuitive GUI makes the system user-friendly, catering to
        users with varying technical expertise.

-   # Project structure 

## ADD_Faces.py

1.  ### **read_random_frames function:**

    -   Purpose:

> Reads a specified number of random frames from a video file.

-   Parameters:

> video_path: Path to the input video file.
>
> num_frames_to_read: Number of frames to read from the video.

-   Output:

> Saves the randomly selected frames as individual image files in the
> "images" directory.

2.  ### **create_images_AND_names function:**

    -   Purpose:

> Reads images from the "images" directory and extracts names from file
> names.

-   Output:

> Two lists: images (containing images) and names (containing
> corresponding names).

3.  ### **findEncodings function:**

    -   Purpose:

> Converts images to RGB format and finds face encodings using the
> face_recognition library.

-   Parameters:

> images: List of images.

-   Output:

> List of face encodings.

4.  ### **creatpik function:**

    -   Purpose:

> Creates and saves a Pickle file containing face encodings and
> corresponding names.

-   Output:

> Saves the Pickle file named "EncodeFile.pkl".

5.  ### **update_pickle function:**

    -   Purpose:

> Updates an existing Pickle file with new face encodings and names.

-   Output:

> Saves the updated Pickle file.

6.  ### **main function:**

    -   Purpose:

> The heart of the file as it , iterates through a directory of videos,
> reads random frames, and updates the Pickle file.

## FastAPI Server Code

1.  ### **Importing Libraries and Modules**

2.  ### **FastAPI App Setup:**

3.  ### **Loading Encoded Data:**

    -   Reads the face encodings and corresponding names from the Pickle
        file.

4.  ### **Endpoint for Image Upload:**

    -   Defines a FastAPI endpoint for uploading images.

5.  ### **Image Processing and Face Recognition:**

    -   Reads the uploaded image, processes it for face recognition.

6.  ### **Face Matching and Result Compilation:**

    -   Compares the face encodings with the known encodings and appends
        the corresponding names to the result if a match is found.

7.  ### **Returning Result:**

    -   Returns the result (list of recognized names) as the response.

8.  ### **Running the FastAPI Server:**

    -   Runs the FastAPI server on http://127.0.0.1:8000/.

9.  ### **Additional Notes**

    -   Ensure the necessary libraries (fastapi, uvicorn,
        face_recognition, cv2, numpy) are installed before running the
        script.

    -   Add more comments if needed, especially for complex logic or
        important parts of the code.

    -   Consider adding exception handling to deal with potential errors
        during image processing or file reading.

## Firebase Authentication and Face Recognition GUI

1.  ### **Importing Libraries and Modules**

2.  ###  **Class: FirebaseAuthenticationApp**

-   Initialization**:**

    -   Initializes the GUI and sets up the initial configuration.

    -   Sets up the Firebase configuration using the provided
        > credentials.

    -   Initializes Firebase authentication and required variables.

-   logincreate_widgets Method:

    -   Creates and displays login widgets.

    -   Entry fields for email and password, login and signup buttons.

-   pathcreate_widgets Method:

    -   Creates and displays widgets for selecting the course and week.

    -   Entry fields for course name and week number, save button.

-   FRcreate_widgets Method**:**

    -   Creates and displays widgets for face recognition.

    -   Image upload button, image display frame, recognition result
        > display.

-   delete_widgets Method**:**

    -   Deletes all widgets in the GUI.

-   login Method**:**

    -   Attempts to log in the user with provided email and password.

    -   Handles successful login and errors.

-   signup Method**:**

    -   Attempts to sign up a new user with provided email and password.

    -   Prompts the user to log in after successful signup.

-   upload**\_**image Method**:**

    -   Allows the user to upload an image for recognition.

    -   Displays the selected image in the GUI.

-   recognize Method**:**

    -   Sends the uploaded image to the FastAPI server for recognition.

    -   Displays recognized people in the result text widget.

-   delete_image Method**:**

    -   Deletes the uploaded image and resets the image frame.

-   save_input Method:

    -   Saves the course name and week number from input fields.

    -   Resets the GUI for face recognition.

-   update_pickle Method:

    -   Updates the face recognition pickle file with a new person's
        face.

-   findEncodings Method:

    -   Finds face encodings for a given set of images.

### **Additional Notes:**

-   The code seems to use a custom Tkinter library (**customtkinter**)
    and **CTkMessagebox**. Ensure they are available or replace them
    with standard Tkinter elements if necessary.

-   Confirm that the Firebase configuration is accurate and secure.

-   Consider adding more detailed comments for complex or crucial parts
    of the code.

## Mobile APP 

### **Introduction**

> This document provides an overview of the Kotlin code implementation
> for the Attendance App developed in Android Studio. The app
> facilitates tracking attendance for classes and weeks, utilizing
> Firebase for data storage and retrieval.

### **Dependencies**

> The app relies on the following dependencies:

-   Kotlin

-   AndroidX

-   Firebase SDK

-   OkHttp

-   Data Binding

### **Firebase Integration**

> Firebase is used for real-time data storage and retrieval. Key
> references include:

-   database.reference: Reference to the root of the Firebase database.

-   auth: Firebase Authentication instance.

-   userRef, classRef, weekRef: References to specific locations in the
    > database based on user and class information.

### **UI Components**

-   FragmentAtendanceBinding: Data Binding object for the attendance
    > fragment.

-   FAB (Floating Action Button): Toggles camera and person icons for
    > user interaction.

-   RecyclerView: Displays a list of students using SectionsAdapter.

-   ProgressBar and TextView: Indicate loading state and provide user
    > feedback.

### **Camera Integration**

-   startActivityForResult: Launches the camera intent to capture
    > images.

-   onActivityResult: Handles the result of the camera activity and
    > processes the captured image.

### **HTTP POST Request**

-   postBitmapWithHeaderAsync: Sends a POST request with a Bitmap image
    > to a specified API endpoint.

-   Utilizes OkHttp for networking.

-   Custom header ("ngrok-skip-browser-warning") added for skipping
    > ngrok warning.

### **Image Handling**

-   saveImage: Saves a Bitmap image to the device's external storage.

-   Uses Environment.getExternalStoragePublicDirectory for storing
    > images.
