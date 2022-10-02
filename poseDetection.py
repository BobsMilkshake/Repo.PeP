import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# VIDEO FEED -- captura de video normal, sem nenhum track
"""
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Testando a camera', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

"""

"""""
cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), # muda a cor, grossura e raio dos track
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               

                #^^^^^^^ Vai desenhar os tracos no track e pegar os eixos x, y, z
                # e possivel customizar quais partes o track pegara
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

"""""

cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        """""
        try:
            landmarks = results.pose_landmarks.landmark # captura os eixos tridimensionais
            print(landmarks)                            # neste caso ele printa todos os landmarks
        except:
            pass
        """
    
        try:
            landmarksLeft = [mp_pose.PoseLandmark.LEFT_SHOULDER.value] # ombro esquerdo
            landmarksRight = [mp_pose.PoseLandmark.RIGHT_SHOULDER.value] # ombro direito
            landmarks = results.pose_landmarks.landmark
            print(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

        except:
            pass

            # [mp_pose.PoseLandmark.LEFT_SHOULDER.value].x == plano x
            # [mp_pose.PoseLandmark.LEFT_SHOULDER.value].y == plano y
            # [mp_pose.PoseLandmark.LEFT_SHOULDER.value].z == plano z
            # landmarks[3] == visibility(???) 

            # shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]  -- array com os valores x[0] e y[1]


        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               


                                 # texto na gravacao

        image = cv2.putText(image, "Texto de teste", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('Teste', image)


        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



# criar uma funcao que calcula o angulo do ombro esquerdo e direito
# quais outras partes podem ser uteis para o trabslho