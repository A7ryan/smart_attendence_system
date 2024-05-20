from library import *
from dataset import *

video_capture = cv2.VideoCapture(0)

formatted_date = datetime.date.today()
current_time = time.localtime()
formatted_time = time.strftime("%H:%M:%S")


file_csv = open('demo.csv', 'w+', newline= '')
file_writer = csv.writer(file_csv)

while True:
    image, frame = video_capture.read()

    resized_capture = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_converted_capture = cv2.cvtColor(resized_capture, cv2.COLOR_BGR2RGB)

    face_location = face_recognition.face_locations(resized_capture)
    face_endoding = face_recognition.face_encodings(resized_capture, face_location)

    face_name = []

    for face in face_endoding:
        is_face_atch = face_recognition.compare_faces(known_face_encode, face)
        temp_name = "unknown"
        face_distance = face_recognition.face_distance(known_face_encode, face)
        best_image_fit = numpy.argmin(face_distance)

        if is_face_atch[best_image_fit]:
            temp_name = known_face_name[best_image_fit]

        face_name.append(temp_name)
        if temp_name in known_face_name:
            if temp_name in store_names:
                store_names.remove(temp_name)
                print('match found')
                
                # ---------------------- DB Code Begins ---------------------------------------------------
                # db_name = (datetime.datetime.strftime(dt_obj,"%m/%d/%Y"))
                # mycursor.execute(f"CREATE DATABASE charusat_students")
                
            
                # mycursor.execute("CREATE TABLE present_students (name VARCHAR(255)")

                # Insert Data
                # sql = "INSERT INTO present_students (name) VALUES (%s)"
                # val = ({temp_name})
                # mycursor.execute(sql, val)
                # mydb.commit()
                # print(mycursor.rowcount, "record inserted.")
                # ---------------------- DB Code Ends -----------------------------------------------------
                
                print(temp_name)
                file_writer.writerow([temp_name, formatted_date, formatted_time])

        for (top, right, bottom, left), name in zip(face_location, face_name):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)


    cv2.imshow('Live Attendence', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


mydb.close()
video_capture.release()
cv2.destroyAllWindows()
file_csv.close()
