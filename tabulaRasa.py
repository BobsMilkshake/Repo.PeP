import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


# não faz tracking 

cap = cv2.VideoCapture('output.avi') # diretorio e arquivo do video

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    


    cTime = time.time()
    fps = 1/(cTime - pTime)  # ajusta a velocidade dos frames do video
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,60), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 3)

    cv2.imshow("image", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break  

    

    
