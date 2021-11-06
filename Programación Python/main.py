import cv2
import numpy as np
import dlib
from math import hypot
import pyglet
import time
#Sonidos

sound = pyglet.media.load("click.mp3", streaming =False)
espacio = pyglet.media.load("espacio.mp3",streaming =False )
borrar = pyglet.media.load("borrar.mp3", streaming =False)


cap = cv2.VideoCapture(0)
board = np.zeros((500,1300), np.uint8)
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#teclado
teclado = np.zeros((750, 1200, 3), np.uint8)
key_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
              5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
              10: "A", 11: "S", 12: "D", 13: "F", 14: "G",
              15: "H", 16: "J", 17: "K", 18: "L", 19: "Ñ"}
          

def letra (letter_index, text, letter_light):
    

    # Keys
    if letter_index == 0:
        x = 60
        y = 240
    elif letter_index == 1:
        x = 145
        y = 240
    elif letter_index == 2:
        x = 230
        y = 240
    elif letter_index == 3:
        x = 315
        y = 240
    elif letter_index == 4:
        x = 400
        y = 240
    elif letter_index == 5:
        x = 485
        y = 240
    elif letter_index == 6:
        x = 570
        y = 240    
    elif letter_index == 7:
        x = 655
        y = 240
    elif letter_index == 8:
        x = 740
        y = 240
    elif letter_index == 9:
        x = 825
        y = 240
    elif letter_index == 10:
        x = 60
        y = 325
    elif letter_index == 11:
        x = 145
        y = 325
    elif letter_index == 12:
        x = 230
        y = 325
    elif letter_index == 13:
        x = 315
        y = 325
    elif letter_index == 14:
        x = 400
        y = 325
    elif letter_index == 15:
        x = 485
        y = 325
    elif letter_index == 16:
        x = 570
        y = 325
    elif letter_index == 17:
        x = 655
        y = 325
    elif letter_index == 18:
        x = 740
        y = 325
    elif letter_index == 19:
        x = 825
        y = 325


    width = 85
    height = 85
    th = 3

    if letter_light is True:
        cv2.rectangle(teclado, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
    else:
        cv2.rectangle(teclado, (x + th, y + th), (x + width - th, y + height - th), (153, 204, 255), -1)
        
    # Text settings
    font_letter = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1.5
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(teclado, text, (text_x, text_y), font_letter, font_scale, (5, 37, 101), font_th)


def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_SIMPLEX


def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    #hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    #ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio


def get_gaze_ratio(eye_points, facial_landmarks):

    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)

    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)

    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white == 0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white

    return gaze_ratio

#Contadores
frames = 0
letter_index = 0
blinking_frames = 0
frames_to_blink = 6
frames_active_letter = 9

text = ""

while True:
    _, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    rows, cols, _ = frame.shape
    teclado [:] = (0,0,0)
    frames += 1
    new_frame = np.zeros((500, 500, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame[rows - 50: rows, 0: cols] = (255, 255, 255)

    active_letter = key_set_1[letter_index]


    faces = detector(gray)
    for face in faces:
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        #detectar parpadeo
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        if blinking_ratio > 5.7:
            cv2.putText(frame, "PARPADEO", (50, 150), font, 3, (255, 0, 0), thickness = 3)
            blinking_frames += 1
            frames -= 1

            if blinking_frames == 5:
                text += active_letter
                sound.play()
                time.sleep(1)
                
        else:
            blinking_frames=0

        #Deteccion del movimiento de ojo
        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2

        """
        if gaze_ratio <= 1:
            cv2.putText(frame, "DERECHA", (50, 100), font, 2, (0, 0, 255), 3)
            new_frame[:] = (0, 0, 255)
        elif 1 < gaze_ratio < 1.7:
            cv2.putText(frame, "CENTRO", (50, 100), font, 2, (0, 0, 255), 3)
        else:
            new_frame[:] = (255, 0, 0)
            cv2.putText(frame, "IZQUIERDA", (50, 100), font, 2, (0, 0, 255), 3)

            #threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
            #eye = cv2.resize(gray_eye, None, fx=5, fy=5)
            #cv2.imshow("Eye", eye)
            #cv2.imshow("Threshold", threshold_eye)
            #cv2.imshow("Left eye", left_eye)

        """        

    #Letras
    if frames == 11:
        letter_index  += 1
        frames = 0
    if letter_index == 20:
        letter_index = 0


    for i in range(20):
        if i == letter_index:
            light = True
        else:
            light = False    
        letra(i,key_set_1[i], light)

    
    # Show the text we're writing on the board
    cv2.putText(board, text, (10, 100), font, 2, 0, 3)

    # Blinking loading bar
    percentage_blinking = blinking_frames / frames_to_blink
    loading_x = int(cols * percentage_blinking)
    cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (51, 51, 51), -1)

    cv2.imshow("Frame", frame)
    #cv2.imshow("New frame", new_frame)
    cv2.imshow("Teclado", teclado)
    cv2.imshow("Cuadro de texto", board)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
