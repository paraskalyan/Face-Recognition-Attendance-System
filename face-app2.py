import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from datetime import datetime, date
from tkinter import ttk
import connect_mongo as db
import pyttsx3
from keras.models import load_model
import notifications as notify

def capture():
    def take_attendance(pred):
        print(pred)
        current_time = datetime.now().time().strftime('%H:%M:%S')
        current_date = date.today().strftime('%d-%m-%Y')
        db.insert_data(emp_dict[pred],pred, current_date, current_time)
        speak(f"Hi {pred} your attendace is saved")
        contact =db.get_phone(2310)  
        message = f"Hello {pred}, Your Attendance is saved at {current_time} on {current_date}"
        notify.send_text_message(contact, message)

    def check_key(event):
        if event.keysym == 's': 
            take_attendance(labels[predicted_class])
            
    root.bind('<Key>', check_key)
    while True:
        ret, frame = cap.read()
        # imgOutput = img.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

         # Process the detected faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_region = gray[y:y+h, x:x+w]
            # Resize the face region to the desired input size of the model
            resized_face = cv2.resize(face_region, (64, 64))
            resized_face = np.expand_dims(resized_face, axis=0)
            resized_face = resized_face / 255.0
            # Perform face recognition using the loaded model
            predictions = model.predict(resized_face)
            predicted_class = np.argmax(predictions)
            confidence = predictions[0][predicted_class] * 100
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if confidence > 70:
                cv2.putText(frame, labels[predicted_class], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.putText(frame, 'Confidence: {:.2f}%'.format(confidence), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        img2 = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image = img2)
        L1['image'] = imgtk
        root.update()



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Load the haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the saved model
model = load_model('unk_vgg_model.h5')
# Access the webcam
cap = cv2.VideoCapture(0)
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
labels = ['Kirpal', 'Krishna', 'Paras','Satwik','Unknown']
emp_dict = {'Kirpal': 2321, 'Krishna':2343, 'Paras':2345, 'Satwik':2346}
con_label = np.array(labels)
root = tk.Tk()
root.resizable(False, False)
big_font = ('Verdana', 20, 'bold')
title_label = tk.Label(root, text="Face based Attendance System", font=big_font, bg='black', fg='white')
title_label.pack(pady=15)
style = ttk.Style(root)
style.theme_use('alt')

f1 = tk.LabelFrame(root)
f1.pack()
L1 = tk.Label(f1)
L1.pack()

label1 = tk.Label(root, text="Press 's' to save attendance", font=('Verdana', 13, 'bold'))
label1.pack(pady=15)
image = Image.open("C:/Users/Admin/Desktop/Detection-systems/face-logo.jpg")  
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)
photo_label = tk.Label(root, image=photo)
photo_label.place(x = 10, y = 10)

capture()

root.mainloop()
