from ultralytics.models import RTDETR
 
if __name__ == '__main__':
    # 加载模型
    model = RTDETR(model='runs/detect/train3-30/weights/best.pt') 
    metrics = model.val(batch = 1)  # no arguments needed, dataset and settings remembered
    print(f"mAP50-95: {metrics.box.map}") # map50-95
    print(f"mAP50: {metrics.box.map50}")  # map50
    print(f"mAP75: {metrics.box.map75}")  # map75
    speed_metrics = metrics.speed
    total_time = sum(speed_metrics.values())
    fps = 1000 / total_time
    print(f"FPS: {fps}") # FPS