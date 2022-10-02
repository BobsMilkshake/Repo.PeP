import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()




cap = cv2.VideoCapture("output.avi") # diretorio e arquivo do video

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # desenho dos landmarks
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 4, (255,0,0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime - pTime)  # ajusta a velocidade dos frames do video
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,60), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 3)

    cv2.imshow("image", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break  



    
