from ultralytics.models import RTDETR


if __name__ == '__main__':

    model = RTDETR(model='RGBandNIR.yaml')
    model.train(pretrained=False, data='shipdata.yaml', epochs=1, batch=1, device='cpu', imgsz=640, workers=0)