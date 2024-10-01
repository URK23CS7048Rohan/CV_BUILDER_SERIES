from ultralytics import YOLO

model = YOLO("yolov8s.pt")
result = model.predict("1", show=True)
print(result)
