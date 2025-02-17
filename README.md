# [Deep-Multi-Modal-Ship-Detection-and-Classification-Network](https://ieeexplore.ieee.org/abstract/document/10806870)


[Deep-Multi-Modal-Ship-Detection-and-Classification-Network](https://ieeexplore.ieee.org/abstract/document/10806870).\
Fan Xu, Chuibin Chen, Zhigao Shang, Kai-Kuang Ma, Qihui Wu, Zebin Lin, Jie Zhan, and Yizhou Shi\

<details>
  <summary>
  <font size="+1">Abstract</font>
  </summary>
While a majority of single-modal ship detectors solely rely on RGB images, a novel multi-modal real-time transformer-based ship detection and classification method, called the MM-ShipNet, is proposed in this paper that integrates the data acquired from three modalities—i.e., RGB camera, radar, and automatic identification system (AIS). First, a bounding box is generated based on the position information from radar and ship’s actual size information from AIS. This physical information are fused and projected onto the camera-acquired RGB image frame. Each bounding box is then possibly weighted depending on the ship size presented on the image. The generated weighted ship masks (WSMs) will be exploited for facilitating ship classification task. In the second stage of MM-ShipNet, multi-modal detection transformer (MM-DETR) introduces an multi-modal cross-scale encoder (MCE) for improving ship detection and classification performance. Our MCE exploits a dual-flow structure to fuse the features extracted from the WSMs and the RGB images under different scales. Since our method is the first work entailing three aforementioned modalities, no such dataset with all modalities can be found in the open source. Thus, we construct a multi-modal ship dataset, termed MMShips, as another contribution. Our MMShips dataset comprises 9,513 camera-acquired real-life maritime RGB images and their aligned ship masks generated from radar and AIS. Experimental results clearly demonstrate that our MM-ShipNet significantly outperforms multiple state of-the-art single-modal and multi-modal ship detectors.
</details>

## Installation
`conda` virtual environment is recommended. 
```
conda create -n MM-DETR python=3.9
conda activate MM-DETR
pip install -r requirements.txt
pip install -e .
```
## Training
```
python train.py
# You can modify the parameters
```

## Validation
```
python val.py
# You can modify the parameters
```

## Datasets
The datasets of RGB images can be downloaded from the Baidu web disk.
Link:https://pan.baidu.com/s/1N1vlEd425JcrWjwtQGWTsg?pwd=vlvq 
Extract code:vlvq
The dataset of radar-AIS mask images can be downloaded from Baidu Webdisk.
Link:https://pan.baidu.com/s/157xB3zEy8rzX5aBPEvxNmg?pwd=i1s4 
Extract code:i1s4 

## Citation

If our code or models help your work, please cite our paper:
```BibTeX
@article{xu2024deep,
  title={Deep Multi-Modal Ship Detection and Classification Network},
  author={Xu, Fan and Chen, Chuibin and Shang, Zhigao and Ma, Kai-Kuang and Wu, Qihui and Lin, Zebin and Zhan, Jie and Shi, Yizhou},
  journal={IEEE Transactions on Circuits and Systems for Video Technology},
  year={2024},
  publisher={IEEE}
}
```
