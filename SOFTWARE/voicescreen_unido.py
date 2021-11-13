from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import dlib
from math import hypot
import pyglet
import time

cap = cv2.VideoCapture(0)
board = np.zeros((500, 1300), np.uint8)
board[:] = 255

# Sonidos
sound = pyglet.media.load("click.mp3", streaming=False)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

font = cv2.FONT_HERSHEY_SIMPLEX

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

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
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)],
                               np.int32)
    # cv2.polilynes(frame, [left_eye_region], True, (0, 0, 255), 2)

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







class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(1122, 680)
        Inicio.setMaximumSize(QtCore.QSize(1122, 16777215))
        Inicio.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.label = QtWidgets.QLabel(Inicio)
        self.label.setGeometry(QtCore.QRect(690, 120, 275, 206))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Inicio)
        self.label_2.setGeometry(QtCore.QRect(330, 490, 151, 181))
        self.label_2.setStyleSheet("border-image: url(:/cct/human.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Inicio)
        self.line_2.setGeometry(QtCore.QRect(490, 570, 631, 81))
        self.line_2.setMidLineWidth(44)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Inicio)
        self.line_3.setGeometry(QtCore.QRect(0, 570, 331, 81))
        self.line_3.setMidLineWidth(44)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(Inicio)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 481, 421))
        self.label_3.setStyleSheet("border-image: url(:/cct/logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Inicio)
        self.pushButton.setGeometry(QtCore.QRect(670, 430, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 157, 0);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)


        self.pushButton.clicked.connect(self.menu)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Form"))
        self.label.setText(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#e7e7e7;\">Voice</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#e7e7e7;\">Screen</span></p></body></html>"))
        self.pushButton.setText(_translate("Inicio", "Iniciar"))


    def menu(self):
        self.menu = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.menu)
        self.menu.show()
import human_rc

#menu de opciones
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 680)
        MainWindow.setMaximumSize(QtCore.QSize(1122, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.informacion = QtWidgets.QPushButton(self.centralwidget)
        self.informacion.setGeometry(QtCore.QRect(40, 20, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.informacion.setFont(font)
        self.informacion.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.informacion.setStyleSheet("background-color: rgb(234, 201, 158);")
        self.informacion.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/qtdesigner/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.informacion.setIcon(icon)
        self.informacion.setIconSize(QtCore.QSize(167, 172))
        self.informacion.setObjectName("informacion")
        self.Frases = QtWidgets.QPushButton(self.centralwidget)
        self.Frases.setGeometry(QtCore.QRect(400, 20, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Frases.setFont(font)
        self.Frases.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Frases.setStyleSheet("background-color: rgb(234, 201, 158);")
        self.Frases.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("venv/qtdesigner/happy (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Frases.setIcon(icon1)
        self.Frases.setIconSize(QtCore.QSize(167, 172))
        self.Frases.setObjectName("Frases")
        self.Alerta = QtWidgets.QPushButton(self.centralwidget)
        self.Alerta.setGeometry(QtCore.QRect(750, 210, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Alerta.setFont(font)
        self.Alerta.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Alerta.setStyleSheet("background-color: rgb(234, 201, 158);")
        self.Alerta.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("venv/qtdesigner/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alerta.setIcon(icon2)
        self.Alerta.setIconSize(QtCore.QSize(167, 172))
        self.Alerta.setObjectName("Alerta")
        self.Teclado = QtWidgets.QPushButton(self.centralwidget)
        self.Teclado.setGeometry(QtCore.QRect(220, 340, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Teclado.setFont(font)
        self.Teclado.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Teclado.setStyleSheet("background-color: rgb(234, 201, 158);")
        self.Teclado.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("venv/qtdesigner/smart-keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Teclado.setIcon(icon3)
        self.Teclado.setIconSize(QtCore.QSize(167, 172))
        self.Teclado.setObjectName("Teclado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

#Contadores
frames = 0
letter_index = 0
blinking_frames = 0
frames_to_blink = 6
frames_active_letter = 9

text = ""
while True:
    _, frame = cap.read()
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    rows, cols, _ = frame.shape
    frames += 1
    new_frame = np.zeros((500, 500, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame[rows - 50: rows, 0: cols] = (255, 255, 255)


    faces = detector(gray)
    for face in faces:
        # x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        # detectar parpadeo
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        if blinking_ratio > 5.7:
            cv2.putText(frame, "PARPADEO", (50, 150), font, 3, (255, 0, 0), thickness=3)
            blinking_frames += 1
            frames -= 1

            if blinking_frames == 5:
                sound.play()
                time.sleep(1)

        else:
            blinking_frames = 0

        # Deteccion del movimiento de ojo
        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2



    # Blinking loading bar
    percentage_blinking = blinking_frames / frames_to_blink
    loading_x = int(cols * percentage_blinking)
    cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (51, 51, 51), -1)

    cv2.imshow("Frame", frame)
    # cv2.imshow("New frame", new_frame)

    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Inicio()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()






