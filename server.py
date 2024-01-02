from fastapi import FastAPI, File, UploadFile
import uvicorn
import cv2
import face_recognition
import pickle
import numpy as np


 
app = FastAPI()
 
file = open('EncodeFile.pkl', 'rb')
encodeKnown = pickle.load(file)
trained_people, names = encodeKnown


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    img = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    tmp_faces_enc = face_recognition.face_encodings(img)
    
    result = []
    for cur_enc_face in tmp_faces_enc:
        facesDistances = face_recognition.face_distance(trained_people, cur_enc_face)

        best_match = np.argmin(facesDistances)
        if facesDistances[best_match] < 0.4:
            result.append(names[best_match])


    return result




uvicorn.run(app, host="127.0.0.1", port=8000 )
