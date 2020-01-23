# Hacking

Selected Tensorflow implementation of ***Super-Resolution_CNN***[1]. This is a reference of ***A Fully Progressive Approach to Single-Image Super-Resolution***[2]. The switch happened because the very dense networks in this implementation has a similar PSNR (peek signal-to-noise ratio) for 2x upsampling.

# Implementation

1. Checkout Tensorflow repository and implemenation in [Colab](https://colab.research.google.com/drive/1oPgjW7k23esFMHMgTT_eK5b4xy129AR9)
2. Copied repository to Google Drive to access training data
3. Established connection to Google Drive and started training
4. Finally got colab running ('''reset and run all''' for the rescue), but received an '''Out of memory''' error after ~200 epochs and tried to enable GPU to improve training performance
5. Could not convince implementation to use GPU
6. Tried to use on local machine (laptop w/o GPU), fixed problems with Qt dependency which is required for matplotlib, created requirements.txt for python dependencies:
```
tensorflow==1.14.0
tensorflow-gpu==1.14.0
tensorboard
numpy==1.14.0
matplotlib==3.1.1
sklearn
```
Created conda environment:
```
conda create -n srnn1 python=3.6.8
conda env list
conda activate srnn1

pip3 install -r requirements.txt
```

7. Tried to setup Azure virtual machine (Standard NC6_Promo (6 vcpus, 56 GiB memory) + Nvidia K80; cheapest GPU model) with different tutorials (how hard can it be):

Check installed Nvidia card: 
```
lspci | grep -i nvidia
update-pciids
```

***Tutorial 1***:
```
gcc --version
sudo apt install gcc-6 g++-6
sudo apt-get install linux-headers-$(uname -r)
sudo apt install nvidia-384
sudo apt install ubuntu-drivers-common
ubuntu-drivers devices
```

***Tutorial 2***:
```
wget -c https://developer.nvidia.com/compute/cuda/9.2/Prod/local_installers/cuda_9.2.88_396.26_linux
chmod +x cuda_9.2.88_396.26_linux
sudo ./cuda_9.2.88_396.26_linux --verbose --silent --toolkit --override
export PATH="$PATH:/usr/local/cuda-9.2/bin"
sudo ./cuda_9.2.88_396.26_linux --verbose --silent --driver --override
echo "/usr/local/cuda-9.2/lib64" >> /etc/ld.so.conf
ldconfig
wget https://developer.nvidia.com/compute/cuda/9.2/Prod/patches/1/cuda_9.2.88.1_linux
chmod +x cuda_9.2.88.1_linux
./cuda_9.2.88.1_linux --silent --accept-eula
ln -s /usr/bin/gcc-6 /usr/local/cuda-9.2/bin/gcc
ln -s /usr/bin/g++-6 /usr/local/cuda-9.2/bin/g++
```

***Tutorial 3***: [https://docs.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup
)
```
CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
wget -O ${CUDA_REPO_PKG} http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/${CUDA_REPO_PKG} 
sudo dpkg -i ${CUDA_REPO_PKG}
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub 
rm -f ${CUDA_REPO_PKG}
sudo apt-get update
sudo apt-get install cuda-drivers
reboot
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-440_440.33.01-0ubuntu1_amd64.deb
```

***Tutorial 4***: [https://www.tensorflow.org/install/gpu](https://www.tensorflow.org/install/gpu)
```
# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt-get update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt-get update

# Install NVIDIA driver
sudo apt-get install --no-install-recommends nvidia-driver-418
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install development and runtime libraries (~4GB)
sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0
```


***Tutorial 5***: Ubuntu 18.04 + NVIDIA
```
sudo apt install nvidia-390 nvidia-cuda-toolkit libcupti-dev gcc-6 python3-numpy python3-dev python3-pip python3-wheel
sudo mkdir -p /usr/local/cuda /usr/local/cuda/extras/CUPTI /usr/local/cuda/nvvm
sudo ln -s /usr/bin /usr/local/cuda/bin
sudo ln -s /usr/include /usr/local/cuda/include
sudo ln -s /usr/lib/x86_64-linux-gnu /usr/local/cuda/lib64
sudo ln -s /usr/local/cuda/lib64 /usr/local/cuda/lib
sudo ln -s /usr/include /usr/local/cuda/extras/CUPTI/include
sudo ln -s /usr/lib/x86_64-linux-gnu /usr/local/cuda/extras/CUPTI/lib64
sudo ln -s /usr/lib/nvidia-cuda-toolkit/libdevice /usr/local/cuda/nvvm/libdevice

```

***Finally tried official tensorflow docker image***:
```
# install docker on ubuntu
sudo apt-get remove docker docker-engine docker.io containerd runc;\
sudo apt-get update;\
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common;\
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -;\
sudo apt-key fingerprint 0EBFCD88;\
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable";\
sudo apt-get update;\
sudo apt-get install docker-ce docker-ce-cli containerd.io;\
sudo docker run hello-world;

# check gpu via docker image
https://www.tensorflow.org/install/docker

sudo docker run --gpus all --rm nvidia/cuda nvidia-smi
```


***All of the setup's resulted into positive results***
```
nvidia-smi
Wed Dec 18 22:43:57 2019
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla K80           Off  | 00000D3E:00:00.0 Off |                    0 |
| N/A   34C    P0    71W / 149W |      0MiB / 11441MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

***But Tensorflow did not recognize GPU***:
```
Python

import tensorflow as tf; print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')));
```


8. Dismissed GPU, started training based on CPU (Azure compute optimized Standard F8s_v2 (8 vcpus, 16 GiB memory). ~5h for 1000 epochs.
Extracted checkpoint model for javascript application.

9. Translate model to Tensorflow JS
```
pip3 install tensorflowjs

tensorflowjs_converter model .

   237  checkpoint
80,396  model_checker.data-00000-of-00001
   287  model_checker.index
39,548  model_checker.meta

but got error:
SavedModel file does not exist at: ./{saved_model.pbtxt|saved_model.pb}

```

10. Downloaded existing model from [SRzoo](https://github.com/idearibosome/srzoo) and translated it to a JSON representation:
```
4,194,304   group1-shard1of2.bin
  555,604   group1-shard2of2.bin  
   41,560   model.json
```

11. In Progress: Problem implementing HTML/JS application, do not know in which format the image is required to be upscaled by the model. Searching for a solution.


Colleague recommended at the presentation, but have not tried yet (from Tensorflow [Install GPU](https://www.tensorflow.org/install/gpu)):
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
```


# References

1. C. Dong, C. C. Loy, K. He and X. Tang, "Image Super-Resolution Using Deep Convolutional Networks," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 38, no. 2, pp. 295-307, 1 Feb. 2016.
doi: 10.1109/TPAMI.2015.2439281,
[Github link](https://github.com/YeongHyeon/Super-Resolution_CNN), 
[PDF](8_Image_Super-Resolution_using+deep_convolutional_networks.pdf)


2. Wang, Yifan & Perazzi, Federico & Mcwilliams, Brian & Sorkine-Hornung, Alexander & Sorkine-Hornung, Olga & Schroers, Christopher. (2018). A Fully Progressive Approach to Single-Image Super-Resolution,
[Homepage link](https://igl.ethz.ch/projects/prosr/),
[PDF](7_prosr-cvprw-2018-wang-et-al.pdf)