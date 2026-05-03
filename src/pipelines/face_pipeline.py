
import dlib
import numpy as np
import streamlit as st
from sklearn.svm import SVC
import face_recognition_models

from src.Database.db import get_all_students


@st.cache_resource                           # use to load only 1 time
def load_dlib_models():                      # for face detection
    detector = dlib.get_frontal_face_detector()                   # make bounding boxes

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )                                                              # shape predictor => face landmarks

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )                                                              # convert into 128 dim vector
    return detector, sp, facerec


def get_face_embeddings(image_np):
    dectector, sp, facerec = load_dlib_models()
    faces = dectector(image_np, 1)

    encodings = []
    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embeddings

        encodings.append(np.array(face_descriptor))
    
    return encodings


@st.cache_resource
def get_trained_model():                    # train model on student data!
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get("face_embedding")
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))
    
    if len(X)==0:
        return None
    

    clf = SVC(kernel="Linear", probability=True, class_weight="balanced")
    try:
        clf.fit(X,y)
    except ValueError:
        pass
    return {'clf':clf, 'X':X, 'y':y}

  
def train_model():                       # train model again when new student added!
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool[model_data]


def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_students, [], len(encodings)      # => return student_embed.. (0), student list (0), no of stu (0)
    
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))              # set => unique

    for encoding in encodings:
        if len(all_students)>=2:
            predicted_id = int(clf.predict(encoding)[0])
        else:
            predicted_id =  int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]        # checking prediction

        best_match_score = np.linalg.norm(student_embedding - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_students[predicted_id] =  True
        
    return detected_students, all_students, len(encoding)