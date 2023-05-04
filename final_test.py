# installing important libraries
import cv2
from cvzone.HandTrackingModule import HandDetector
from numpy import *
import math
import PIL.Image
import numpy as np


def app():

    # Setting frame dimension for webcam
    w_cam, h_cam = 640, 480

    #White Image dimensions and creation
    ImgSize = 500
    ImgWhite = np.ones((ImgSize,ImgSize,3),uint8)*255

    # storing the image
    im = PIL.Image.open(r"res\\Alphabets.jpeg")

    letter = ""
    word = ""

    ##############################


    #capturing video
    cap = cv2.VideoCapture(0)
    cap.set(3, w_cam)
    cap.set(4, h_cam)
    handt = HandDetector(detectionCon=0.7, minTrackCon=0.6)
    flag_img = 0

    while True:
        success, img = cap.read()
        
        hand, img = handt.findHands(img)

        cv2.line(img, (0,480), (640, 480), (256, 256, 256), 75)

        if len(hand) == 1:
            hand1 = hand[0]
            lmList = hand1['lmList']
            f_up_or_down = handt.fingersUp(hand1)

            # co-ordinates of the points
            x0, y0 = lmList[0][0], lmList[0][1]
            x1, y1 = lmList[1][0], lmList[1][1]
            x2, y2 = lmList[2][0], lmList[2][1]
            x3, y3 = lmList[3][0], lmList[3][1]
            x4, y4 = lmList[4][0], lmList[4][1]
            x5, y5 = lmList[5][0], lmList[5][1]
            x6, y6 = lmList[6][0], lmList[6][1]
            x7, y7 = lmList[7][0], lmList[7][1]
            x8, y8 = lmList[8][0], lmList[8][1]
            x9, y9 = lmList[9][0], lmList[9][1]
            x10, y10 = lmList[10][0], lmList[10][1]
            x11, y11 = lmList[11][0], lmList[11][1]
            x12, y12 = lmList[12][0], lmList[12][1]
            x13, y13 = lmList[13][0], lmList[13][1]
            x14, y14 = lmList[14][0], lmList[14][1]
            x15, y15 = lmList[15][0], lmList[15][1]
            x16, y16 = lmList[16][0], lmList[16][1]
            x17, y17 = lmList[17][0], lmList[17][1]
            x18, y18 = lmList[18][0], lmList[18][1]
            x19, y19 = lmList[19][0], lmList[19][1]
            x20, y20 = lmList[20][0], lmList[20][1]

            


    # ********************************* UNIQUE STARTS HERE ***********************************



            # *********************** Thumb Down and Others Up (FOR B)******************************
            if (f_up_or_down[0] == 0 and f_up_or_down[1:] == [1, 1, 1, 1]):
                cv2.putText(img, f'B', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                letter = "B"

            # *********************** Thumb & Index Down and Others Up (FOR F)******************************
            elif (f_up_or_down[0] == 0 and f_up_or_down[1] == 0 and f_up_or_down[2:] == [1, 1, 1]):
                cv2.putText(img, f'F', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                letter = "F"

            # *********************** Little Up and Others Down (FOR I)******************************
            elif (f_up_or_down[4] == 1 and f_up_or_down[:4] == [0, 0, 0, 0]):
                
                base = math.hypot((x5-x8), (y5-y5))
                perpendicular = math.hypot((x8-x8), (y5-y8))
                hypotenuse = math.hypot((x5-x8), (y5-y8))

                if(hypotenuse!=0):
                    p_ratio_h=perpendicular/hypotenuse
                    theta=(math.asin(p_ratio_h))*(180/math.pi)

                if(theta<15):
                    cv2.putText(img, f'G', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "G"

                else: 
                    cv2.putText(img, f'I', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "I"

            # *********************** Thumb and Index Up and Others Down (FOR L)******************************
            elif (f_up_or_down[0] == 1 and f_up_or_down[1] == 1 and f_up_or_down[2:] == [0, 0, 0]):
                cv2.putText(img, f'L', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                letter = "L"

            # *********************** Thumb & Little Down and Others Up (FOR W)******************************
            elif (f_up_or_down[0] == 0 and f_up_or_down[4] == 0 and f_up_or_down[1:4] == [1, 1, 1]):
                cv2.putText(img, f'W', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                letter = "W"


    # *************************************** UNIQUE ENDS HERE ****************************************

                 

            # *********************************** MAYBE THUMB AND INDEX UP ****************************************
            elif (f_up_or_down[0]==1 or f_up_or_down[0]==0) and f_up_or_down[1]==1 and f_up_or_down[2:] == [0, 0, 0]:

                # ********** For P ************
                if y10>y4 and y4>y6 and x4<x5 and x4<x9:
                    cv2.putText(img, f'P', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "P"
                
                # ********** For X ***********
                elif x8<x7 and x7<x6:
                    cv2.putText(img, f'X', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "X"
                            
                # ********** For D ***********
                elif f_up_or_down[0]==0:
                    cv2.putText(img, f'D', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "D"

                
                            

            # *********************** Thumb Up and Others Down ******************************
            elif (f_up_or_down[0] == 1 and f_up_or_down[1:] == [0, 0, 0, 0]):

                #********FOR C************
                if y4>y8 and y4>y12 and y4>y16 and y4>y20:
                    cv2.putText(img, f'C', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "C"

                #********FOR T************
                elif(x10<x4<x6 and y4<y10 and y4<y14 and y4<y18):
                    cv2.putText(img, f'T', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "T"

                #********FOR A************
                elif(x4>x10 and y4<y6):            
                    cv2.putText(img, f'A', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "A"

            #************************* THUMB AND LIITLE UP STARTS ************************
                                    
            elif (f_up_or_down[0] == 1 and f_up_or_down[4] == 1 and f_up_or_down[1:4] == [0,0,0]):

                #********FOR C************
                if y4>y8 and y4>y12 and y4>y16 and y4>y20:
                    cv2.putText(img, f'C', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "C"

                #********FOR Y ***********
                else:            
                    cv2.putText(img, f'Y', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "Y"

            #************************* THUMB AND LIITLE UP ENDS ***********************




            #********************THUMB MAYBE UP, INDEX AND MIDDLE UP STARTS *********************

            #********************************FOR K, H, U, V, R ***********************************

            elif((f_up_or_down[0]==0 or f_up_or_down[0]==1) and f_up_or_down[1:3]==[1,1] and f_up_or_down[3:]==[0,0]):
                base = math.hypot((x9-x12), (y9-y9))
                perpendicular = math.hypot((x12-x12), (y9-y12))
                hypotenuse = math.hypot((x9-x12), (y9-y12))

                if(hypotenuse!=0):
                    p_ratio_h=perpendicular/hypotenuse
                    theta=(math.asin(p_ratio_h))*(180/math.pi)
                d_8and12=math.hypot((x8-x12), (y8-y12))
                x_8and12_mid=(x8+x12)/2

                if(x12<x_8and12_mid and x_8and12_mid<x8):
                    if(d_8and12<45):
                        if(theta>75):
                            cv2.putText(img, f'U', ((320), (470)),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                            letter = "U"
                        elif(theta<55):
                            cv2.putText(img, f'H', ((320), (470)),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                            letter = "H"

                    else:
                        if(y4<y5 and y4<y9):
                            cv2.putText(img, f'K', ((320), (470)),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                            letter = "K"
                        else:
                            if(d_8and12>60):
                                cv2.putText(img, f'V', ((320), (470)),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                                letter = "V"

                elif(x12>x_8and12_mid and x_8and12_mid>x8):
                    cv2.putText(img, f'R', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "R"


                #**********************THUMB MAYBE UP, INDEX AND MIDDLE UP ENDS *********************




                #***********************ALL DOWN STARTS ******************************

            elif(f_up_or_down[0:]==[0,0,0,0,0]):

                base = math.hypot((x5-x8), (y5-y5))
                perpendicular = math.hypot((x8-x8), (y5-y8))
                hypotenuse = math.hypot((x5-x8), (y5-y8))

                if(hypotenuse!=0):
                    p_ratio_h=perpendicular/hypotenuse
                    theta=(math.asin(p_ratio_h))*(180/math.pi)

                if(y4>y6 and y4>y10 and y4>y14 and y4>y18 and y4<y7 and y4<y11 and y4<y15 and y4<y19):
                    cv2.putText(img, f'S', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "S"

                elif((y4>y8 and y4>y12 and y4>y16 and y4>y20) and (x8-20<x4<x8+20 and x12-20<x4<x12+20 and x16-20<x4<x16+20 and x20-20<x4<x20+20) and math.hypot((x4-x8), (y4-y8))<20):
                    cv2.putText(img, f'O', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "O"

                elif(y14<y4<y18 and x18<x4<x14):
                    cv2.putText(img, f'M', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "M"
                
                elif(y6<y14 and y6<y18 and y10<y14 and y10<y18 and x14<x4<x10 and y4<y14 and y4<y18):
                    cv2.putText(img, f'N', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "N"

                elif(y6<y10 and y6<y14 and y6<y18 and x10<x4<x6 and y4<y10 and y4<y14 and y4<y18):
                    cv2.putText(img, f'T', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "T"

                elif(y3>y7 and x3>x19 and y3>y15 and y3>y19 and math.hypot((x4-x8), (y4-y8))>44):
                    cv2.putText(img,f'Q',((320),(470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0), 3)
                    letter = "Q"

                elif(y4>y8 and y4>12 and y4>y16 and y4>y20 and x4<x8 and x4<x12):
                    cv2.putText(img, f'E', ((320), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "E"

                elif(theta<15):
                    cv2.putText(img, f'G', ((320), (470)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                    letter = "G"

            elif(f_up_or_down[0] == 1 and f_up_or_down[1] == 1 and f_up_or_down[4] == 1 and f_up_or_down[2:4] == [0,0]):
                ImgWhite = np.ones((ImgSize,ImgSize,3),uint8)*255 
                l = len(word)
                x = math.ceil((500 - (22*l))/2)
                cv2.putText(ImgWhite, str(word), ((x), (230)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                
            
        else:
            cv2.putText(img, f'SHOW ANY VALID GESTURE', ((130), (470)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                

        cv2.imshow("PROJECT GD - Week3", img)
        cv2.imshow("ImgWhite", ImgWhite)
        key = cv2.waitKey(1)

        # Press f to form word
        if key == ord('f') or key == ord('F'):  
            key = cv2.waitKey(1000)
            word+= letter
            print(word)

        # Press q to end the code
        if key == ord('q') or key == ord('Q'):  
            print('exit')
            cv2.destroyAllWindows()
            return

        elif(len(hand) == 2):
            hand1 = hand[0]
            lmList1 = hand1['lmList']
            f_up_or_down1 = handt.fingersUp(hand1)


            hand2 = hand[1]
            lmList2 = hand2['lmList']
            f_up_or_down2 = handt.fingersUp(hand2)


            if (f_up_or_down1[0] == 1 and f_up_or_down1[1] == 1 and f_up_or_down1[4] == 1 and f_up_or_down1[2:4] == [0,0] and 
                    f_up_or_down2[0] == 1 and f_up_or_down2[1] == 1 and f_up_or_down2[4] == 1 and f_up_or_down2[2:4] == [0,0]):
                ImgWhite = np.ones((ImgSize,ImgSize,3),uint8)*255  
                word = ""
              

            if f_up_or_down1[0:] == [1, 1, 1, 1, 1] and f_up_or_down2[0:] == [1, 1, 1, 1, 1] and flag_img == 0:
                im.show()
                flag_img = 1

            if f_up_or_down1[0:] == [0, 0, 0, 0, 0] and f_up_or_down2[0:] == [0, 0, 0, 0, 0] and flag_img == 1:
                flag_img = 0




# """[{'lmList': [[163, 381], [210, 364], [246, 330], [264, 295], [274, 266], [219, 272], [237, 230],
# [248, 204], [257, 181], [194, 264], [205, 215], [213, 182], [220, 155], [170, 266], [175, 218],
# [183, 187], [192, 161], [144, 274], [138, 236], [138, 209], [141, 183]],
# 'bbox': (138, 155, 136, 226), 'center': (206, 268), 'type': 'Right'}]
# This was the single hand lmList"""

# """[{'lmList': [[487, 294], [444, 284], [413, 255], [393, 225], [371, 205], [426, 201], [407, 167], [398, 144], [394, 124], [453, 190], [440, 150], 
# [434, 124], [429, 104], [480, 190], [474, 151], [469, 126], [464, 105], [507, 198], [514, 167], [517, 146], [518, 125]], 
# 'bbox': (371, 104, 147, 190), 'center': (444, 199), 'type': 'Left'}, {'lmList': [[117, 324], [164, 311], [199, 283], [225, 255], 
# [249, 239], [186, 225], [204, 188], [212, 164], [216, 142], [160, 215], [174, 173], [180, 145], [184, 122], [132, 214], [140, 174], 
# [146, 148], [152, 127], [101, 220], [95, 189], [92, 166], [92, 145]], 'bbox': (92, 122, 157, 202), 'center': (170, 223), 'type': 'Right'}]
#This was the double hand lmList"""
