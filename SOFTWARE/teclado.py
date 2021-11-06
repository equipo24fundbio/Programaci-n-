# -*- coding: utf-8 -*-
import cv2
import numpy as np

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
    cv2.putText(teclado, text, (text_x, text_y), font_letter, font_scale, (1, 31, 93), font_th)


for i in range(20):
    if i == 5:
        light = True
    else:
        light = False    
    letra(i,key_set_1[i], light)

#a = 60
#b = 240
#c = 85
#letra(a,b,"Q")
#letra(a+c,b,"W")
#letra(a+2*c,b,"E")
#letra(a+3*c,b,"R")
#letra(a+4*c,b,"T")
#letra(a+5*c,b,"Y")
#letra(a+6*c,b,"U")
#letra(a+7*c,b,"I")
#letra(a+8*c,b,"O")
#letra(a+9*c,b,"P")








cv2.imshow("teclado", teclado)
cv2.waitKey(0)
cv2.destroyAllWindows()