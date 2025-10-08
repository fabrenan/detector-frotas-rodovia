import cv2
from ultralytics import YOLO

# caminho para o video a ser analisado
caminho_video = "caminho/para/seu/video.mp4" 

model = YOLO('best.pt')

cap = cv2.VideoCapture(caminho_video)

if not cap.isOpened():
    print(f"Erro ao abrir o vídeo: {caminho_video}")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro na leitura.")
        break

    results = model.track(source=frame, persist=True, conf=0.7)
    
    annotated_frame = results[0].plot()

    cv2.imshow("Detector de Frotas - Pressione 'q' para sair", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()