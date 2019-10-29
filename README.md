# AppliedDeeplearning
Repository for lecture Applied Deeplearning, winter term 2019

# Topic

Training a super-resolution network and its application within a web-browser to reduce bandwith consumption.

# Project Type

Kind of: Bring your own method & beat the classics.

# Summary

## Short description

Training a state of the art image super-resolution network. Extract the network for use in a Javascript runtime environment and apply it to low-resolution images loaded from webserver and display the high-resolution images to the user.

## Dataset

I would re-use the dataset from reference 7, ***A Fully Progressive Approach to Single-Image Super-Resolution*** to train the network.

## Work-breakdown

-   recreating the model and training: 30-40h
-   implementing a Javascript part to use the model: 10h week (if possible)
-   setup prototype website with low-resolution images and model 5h
-   try to tune network based on more current research (references from 2019): 15h
-   writing report 5h

# References

1.  Yue, Linwei & Shen, Huanfeng & Li, Jie & Yuan, Qiangqiang & Zhang, Hongyan & Zhang, Liangpei. (2016). Image super-resolution: The techniques, applications, and future. Signal Processing. 128. 10.1016/j.sigpro.2016.05.002. 
[link](https://www.researchgate.net/publication/303182546_Image_super-resolution_The_techniques_applications_and_future)

2.  Khattab, Mahmoud & Zeki, Akram & Alwan, Ali & Badawy, Ahmed & Thota, Lalitha. (2018). Multi-Frame Super-Resolution: A Survey. 1-8. 10.1109/ICCIC.2018.8782382. 
[link](https://www.researchgate.net/publication/334888262_Multi-Frame_Super-Resolution_A_Survey)

3.  Wenming, Yang & Zhang, Xuechen & Tian, Yapeng & Wang, Wei & Xue, Jing-Hao & Liao, Qingmin. (2019). Deep Learning for Single Image Super-Resolution: A Brief Review. IEEE Transactions on Multimedia. PP. 1-1. 10.1109/TMM.2019.2919431. 
[link](https://www.researchgate.net/publication/333440390_Deep_Learning_for_Single_Image_Super-Resolution_A_Brief_Review)

4.  Wang, Zhihao & Chen, Jian & Hoi, Steven. (2019). Deep Learning for Image Super-resolution: A Survey. 
[link](https://arxiv.org/pdf/1902.06068.pdf)

5.  Gao, Shangqi & Zhuang, Xiahai. (2019). Multi-scale deep neural networks for real image super-resolution. 
[link](http://openaccess.thecvf.com/content_CVPRW_2019/papers/NTIRE/Gao_Multi-Scale_Deep_Neural_Networks_for_Real_Image_Super-Resolution_CVPRW_2019_paper.pdf)

6.  Umer, Rao & Foresti, Gian & Micheloni, Christian. (2019). Deep Super-Resolution Network for Single Image Super-Resolution with Realistic Degradations. 
[link](https://www.researchgate.net/publication/335713902_Deep_Super-Resolution_Network_for_Single_Image_Super-Resolution_with_Realistic_Degradations)

7. Wang, Yifan & Perazzi, Federico & Mcwilliams, Brian & Sorkine-Hornung, Alexander & Sorkine-Hornung, Olga & Schroers, Christopher. (2018). A Fully Progressive Approach to Single-Image Super-Resolution.
[link](https://igl.ethz.ch/projects/prosr/)
