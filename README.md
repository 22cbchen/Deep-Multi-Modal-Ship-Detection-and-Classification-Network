# [Deep-Multi-Modal-Ship-Detection-and-Classification-Network](https://ieeexplore.ieee.org/abstract/document/10806870)


[Deep-Multi-Modal-Ship-Detection-and-Classification-Network](https://ieeexplore.ieee.org/abstract/document/10806870).\
Fan Xu, Chuibin Chen, Zhigao Shang, Kai-Kuang Ma, Life Fellow, IEEE, Qihui Wu, Zebin Lin, Jie Zhan, and Yizhou Shi\

<details>
  <summary>
  <font size="+1">Abstract</font>
  </summary>
While a majority of single-modal ship detectors solely rely on RGB images, a novel multi-modal real-time transformer-based ship detection and classification method, called the MM-ShipNet, is proposed in this paper that integrates the data acquired from three modalities—i.e., RGB camera, radar, and automatic identification system (AIS). First, a bounding box is generated based on the position information from radar and ship’s actual size information from AIS. This physical information are fused and projected onto the camera-acquired RGB image frame. Each bounding box is then possibly weighted depending on the ship size presented on the image. The generated weighted ship masks (WSMs) will be exploited for facilitating ship classification task. In the second stage of MM-ShipNet, multi-modal detection transformer (MM-DETR) introduces an multi-modal cross-scale encoder (MCE) for improving ship detection and classification performance. Our MCE exploits a dual-flow structure to fuse the features extracted from the WSMs and the RGB images under different scales. Since our method is the first work entailing three aforementioned modalities, no such dataset with all modalities can be found in the open source. Thus, we construct a multi-modal ship dataset, termed MMShips, as another contribution. Our MMShips dataset comprises 9,513 camera-acquired real-life maritime RGB images and their aligned ship masks generated from radar and AIS. Experimental results clearly demonstrate that our MM-ShipNet significantly outperforms multiple state of-the-art single-modal and multi-modal ship detectors.
</details>

## Notes
- 2024/05/31: Please use the [exported format](https://github.com/THU-MIG/yolov10?tab=readme-ov-file#export) for benchmark. In the non-exported format, e.g., pytorch, the speed of YOLOv10 is biased because the unnecessary `cv2` and `cv3` operations in the `v10Detect` are executed during inference.
- 2024/05/30: We provide [some clarifications and suggestions](https://github.com/THU-MIG/yolov10/issues/136) for detecting smaller objects or objects in the distance with YOLOv10. Thanks to [SkalskiP](https://github.com/SkalskiP)!
- 2024/05/27: We have updated the [checkpoints](https://huggingface.co/collections/jameslahm/yolov10-665b0d90b0b5bb85129460c2) with class names, for ease of use.

## UPDATES 🔥
- 2024/06/01: Thanks to [ErlanggaYudiPradana](https://github.com/rlggyp) for the integration with [C++ | OpenVINO | OpenCV](https://github.com/rlggyp/YOLOv10-OpenVINO-CPP-Inference)
- 2024/06/01: Thanks to [NielsRogge](https://github.com/NielsRogge) and [AK](https://x.com/_akhaliq) for hosting the models on the HuggingFace Hub!
- 2024/05/31: Build [yolov10-jetson](https://github.com/Seeed-Projects/jetson-examples/blob/main/reComputer/scripts/yolov10/README.md) docker image by [youjiang](https://github.com/yuyoujiang)!
- 2024/05/31: Thanks to [mohamedsamirx](https://github.com/mohamedsamirx) for the integration with [BoTSORT, DeepOCSORT, OCSORT, HybridSORT, ByteTrack, StrongSORT using BoxMOT library](https://colab.research.google.com/drive/1-QV2TNfqaMsh14w5VxieEyanugVBG14V?usp=sharing)!
- 2024/05/31: Thanks to [kaylorchen](https://github.com/kaylorchen) for the integration with [rk3588](https://github.com/kaylorchen/rk3588-yolo-demo)!
- 2024/05/30: Thanks to [eaidova](https://github.com/eaidova) for the integration with [OpenVINO™](https://github.com/openvinotoolkit/openvino_notebooks/blob/0ba3c0211bcd49aa860369feddffdf7273a73c64/notebooks/yolov10-optimization/yolov10-optimization.ipynb)!
- 2024/05/29: Add the gradio demo for running the models locally. Thanks to [AK](https://x.com/_akhaliq)!
- 2024/05/27: Thanks to [sujanshresstha](sujanshresstha) for the integration with [DeepSORT](https://github.com/sujanshresstha/YOLOv10_DeepSORT.git)!
- 2024/05/26: Thanks to [CVHub520](https://github.com/CVHub520) for the integration into [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling)!
- 2024/05/26: Thanks to [DanielSarmiento04](https://github.com/DanielSarmiento04) for integrate in [c++ | ONNX | OPENCV](https://github.com/DanielSarmiento04/yolov10cpp)!
- 2024/05/25: Add [Transformers.js demo](https://huggingface.co/spaces/Xenova/yolov10-web) and onnx weights(yolov10[n](https://huggingface.co/onnx-community/yolov10n)/[s](https://huggingface.co/onnx-community/yolov10s)/[m](https://huggingface.co/onnx-community/yolov10m)/[b](https://huggingface.co/onnx-community/yolov10b)/[l](https://huggingface.co/onnx-community/yolov10l)/[x](https://huggingface.co/onnx-community/yolov10x)). Thanks to [xenova](https://github.com/xenova)!
- 2024/05/25: Add [colab demo](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov10-object-detection-on-custom-dataset.ipynb#scrollTo=SaKTSzSWnG7s), [HuggingFace Demo](https://huggingface.co/spaces/kadirnar/Yolov10), and [HuggingFace Model Page](https://huggingface.co/kadirnar/Yolov10). Thanks to [SkalskiP](https://github.com/SkalskiP) and [kadirnar](https://github.com/kadirnar)! 

## Performance
COCO

| Model | Test Size | #Params | FLOPs | AP<sup>val</sup> | Latency |
|:---------------|:----:|:---:|:--:|:--:|:--:|
| [YOLOv10-N](https://huggingface.co/jameslahm/yolov10n) |   640  |     2.3M    |   6.7G   |     38.5%     | 1.84ms |
| [YOLOv10-S](https://huggingface.co/jameslahm/yolov10s) |   640  |     7.2M    |   21.6G  |     46.3%     | 2.49ms |
| [YOLOv10-M](https://huggingface.co/jameslahm/yolov10m) |   640  |     15.4M   |   59.1G  |     51.1%     | 4.74ms |
| [YOLOv10-B](https://huggingface.co/jameslahm/yolov10b) |   640  |     19.1M   |  92.0G |     52.5%     | 5.74ms |
| [YOLOv10-L](https://huggingface.co/jameslahm/yolov10l) |   640  |     24.4M   |  120.3G   |     53.2%     | 7.28ms |
| [YOLOv10-X](https://huggingface.co/jameslahm/yolov10x) |   640  |     29.5M    |   160.4G   |     54.4%     | 10.70ms |

## Installation
`conda` virtual environment is recommended. 
```
conda create -n yolov10 python=3.9
conda activate yolov10
pip install -r requirements.txt
pip install -e .
```
## Demo
```
python app.py
# Please visit http://127.0.0.1:7860
```

## Validation
[`yolov10n`](https://huggingface.co/jameslahm/yolov10n)  [`yolov10s`](https://huggingface.co/jameslahm/yolov10s)  [`yolov10m`](https://huggingface.co/jameslahm/yolov10m)  [`yolov10b`](https://huggingface.co/jameslahm/yolov10b)  [`yolov10l`](https://huggingface.co/jameslahm/yolov10l)  [`yolov10x`](https://huggingface.co/jameslahm/yolov10x)  
```
yolo val model=jameslahm/yolov10{n/s/m/b/l/x} data=coco.yaml batch=256
```

Or
```python
from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/b/l/x}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
model = YOLOv10('yolov10{n/s/m/b/l/x}.pt')

model.val(data='coco.yaml', batch=256)
```


## Training 
```
yolo detect train data=coco.yaml model=yolov10n/s/m/b/l/x.yaml epochs=500 batch=256 imgsz=640 device=0,1,2,3,4,5,6,7
```

Or
```python
from ultralytics import YOLOv10

model = YOLOv10()
# If you want to finetune the model with pretrained weights, you could load the 
# pretrained weights like below
# model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/b/l/x}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
# model = YOLOv10('yolov10{n/s/m/b/l/x}.pt')

model.train(data='coco.yaml', epochs=500, batch=256, imgsz=640)
```

## Push to hub to 🤗

Optionally, you can push your fine-tuned model to the [Hugging Face hub](https://huggingface.co/) as a public or private model:

```python
# let's say you have fine-tuned a model for crop detection
model.push_to_hub("<your-hf-username-or-organization/yolov10-finetuned-crop-detection")

# you can also pass `private=True` if you don't want everyone to see your model
model.push_to_hub("<your-hf-username-or-organization/yolov10-finetuned-crop-detection", private=True)
```

## Prediction
Note that a smaller confidence threshold can be set to detect smaller objects or objects in the distance. Please refer to [here](https://github.com/THU-MIG/yolov10/issues/136) for details.
```
yolo predict model=jameslahm/yolov10{n/s/m/b/l/x}
```

Or
```python
from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/b/l/x}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
model = YOLOv10('yolov10{n/s/m/b/l/x}.pt')

model.predict()
```

## Export
```
# End-to-End ONNX
yolo export model=jameslahm/yolov10{n/s/m/b/l/x} format=onnx opset=13 simplify
# Predict with ONNX
yolo predict model=yolov10n/s/m/b/l/x.onnx

# End-to-End TensorRT
yolo export model=jameslahm/yolov10{n/s/m/b/l/x} format=engine half=True simplify opset=13 workspace=16
# or
trtexec --onnx=yolov10n/s/m/b/l/x.onnx --saveEngine=yolov10n/s/m/b/l/x.engine --fp16
# Predict with TensorRT
yolo predict model=yolov10n/s/m/b/l/x.engine
```

Or
```python
from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/b/l/x}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
model = YOLOv10('yolov10{n/s/m/b/l/x}.pt')

model.export(...)
```

## Acknowledgement

The code base is built with [ultralytics](https://github.com/ultralytics/ultralytics) and [RT-DETR](https://github.com/lyuwenyu/RT-DETR).

Thanks for the great implementations! 

## Citation

If our code or models help your work, please cite our paper:
```BibTeX
@article{wang2024yolov10,
  title={YOLOv10: Real-Time End-to-End Object Detection},
  author={Wang, Ao and Chen, Hui and Liu, Lihao and Chen, Kai and Lin, Zijia and Han, Jungong and Ding, Guiguang},
  journal={arXiv preprint arXiv:2405.14458},
  year={2024}
}
```
