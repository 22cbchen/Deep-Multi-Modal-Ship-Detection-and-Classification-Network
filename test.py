from ultralytics.models import RTDETR
 
 
if __name__ == '__main__':
    model = RTDETR(model='runs/detect/train/weights/best.pt')
    model.val(data='shipdata.yaml',batch=1, device='cpu', imgsz=640, workers=0)

