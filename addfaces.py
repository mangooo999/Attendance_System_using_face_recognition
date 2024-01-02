import face_recognition
import cv2
import pickle
import numpy as np
import os
import random

def read_random_frames(video_path, num_frames_to_read):
    
    output_directory = "images"
  
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Choose random frames
    random_frames = random.sample(range(total_frames), num_frames_to_read)

    # Read and store the selected frames
    for frame_number in random_frames:
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        # Read the frame
        ret, frame = cap.read()

        if ret:
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            output_file_path = os.path.join(output_directory, f"{video_name}.{frame_number}.jpg")
            cv2.imwrite(output_file_path, frame)


    # Release the video capture object
    cap.release()



def create_images_AND_names():
    path = 'images'
    images = []     # LIST CONTAINING ALL THE IMAGES
    names = []    # LIST CONTAINING ALL THE CORRESPONDING CLASS Names
    files = os.listdir(path)
    for im_name in files:
            curImg = cv2.imread(f'{path}/{im_name}')
            images.append(curImg)
            names.append((im_name).split(".")[0])
    return images, names


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        enc = face_recognition.face_encodings(img)[0]
        encodeList.append(enc)
    return encodeList



def creatpik():
    images, names = create_images_AND_names()
    trained_people = findEncodings(images)
    encodeListKnownWithIds = [trained_people, names]
    with open("EncodeFile.pkl", 'wb') as file:
        pickle.dump(encodeListKnownWithIds, file)


def update_pickle():
    with open("EncodeFile.pkl", 'rb') as file:
        existing_data = pickle.load(file)
    trained_people, names = existing_data
    new_images, new_names = create_images_AND_names()
    new_trained_people = findEncodings(new_images)
    trained_people.extend(new_trained_people)
    names.extend(new_names)
    updated_data = [trained_people, names]
    with open("EncodeFile.pkl", 'wb') as file:
        pickle.dump(updated_data, file)


def main():
        files = os.listdir("people")
        for person in files:
             read_random_frames( f"people/{person}", 1)
        

     

if __name__ == "__main__":
     main()