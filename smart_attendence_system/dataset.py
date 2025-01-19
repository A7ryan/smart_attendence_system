from library import face_recognition, os
from images import *

known_face_encode = []
known_face_name = []

image_path = "./images/"
images_file = os.listdir(image_path)

for images in images_file:
    if images.endswith((".jpg", ".png", ".jpeg")):
        face_pic = face_recognition.load_image_file(os.path.join(image_path, images))
        face_encoded = face_recognition.face_encodings(face_pic)[0]

        known_face_encode.append(face_encoded)
        known_face_name.append(images) # add the name of picture ie. (already contain name and id)

# print(known_face_encode)
# print(known_face_name)
        
store_names = known_face_name.copy()

face_location = []
face_endoding = []
face_names = []
