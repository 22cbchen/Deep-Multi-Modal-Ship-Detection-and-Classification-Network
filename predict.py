from ultralytics.models import RTDETR


if __name__ == '__main__':
    model=RTDETR("runs\detect/train\weights/best.pt")
    model.predict(source="images",save=True)
