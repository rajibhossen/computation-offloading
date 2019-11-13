import face_recognition


def recognize_func():
    image = face_recognition.load_image_file("images/me.jpg")
    face_encoding = face_recognition.face_encodings(image)[0]

    unknown_picture = face_recognition.load_image_file("images/unknown.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_picture)[0]

    results = face_recognition.compare_faces([face_encoding], unknown_encoding)

    return results[0]
