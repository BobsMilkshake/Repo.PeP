import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()



cap = cv2.VideoCapture("test1.mp4")

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # desenho dos landmarks
        

    cTime = time.time()
    fps = 1/(cTime - pTime)  # ajusta a velocidade dos frames do video
    pTime = cTime


    cv2.imshow("image", img)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break  

    

    """""
while True:
    success, img = cap.read()
    cv2.imshow("image", img)
    cv2.waitKey(10)

    """