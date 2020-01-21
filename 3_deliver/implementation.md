Tried on localmachine, no GPU, only i7-7500u cpu/16GB RAM
Could not train out of the box, got QT error, so update source not to do matplotlib stuff
Ran training for some epochs, skipped then and transfered code to colab.

After some updates, got code on codelab to run ("Reset and run all" is your friend) but it terminated after ~200 epochs on an out of memory error.
Changed to more RAM environment (as colab suggested) and enabled GPU, but got the same speed and error again and again.

Activated an Azure VM, cloned the repo there and created a specific conda environment for that task:
git clone git@github.com:YeongHyeon/Super-Resolution_CNN.git

conda create --name srnn1
conda env remove --name srnn1
conda create -n srnn1 python=3.6.8
conda env list
conda activate srnn1

some problems with tensorflow-tensorboard which is no longer required
https://github.com/tensorflow/tensorboard/issues/1862

requirements.txt
tensorflow==1.14.0
tensorflow-gpu==1.14.0
tensorboard
numpy==1.14.0
matplotlib==3.1.1
sklearn

pip3 install -r requirements.txt


CUDA
lspci | grep -i nvidia
update-pciids
gcc --version
sudo apt install gcc-6 g++-6
sudo apt-get install linux-headers-$(uname -r)
sudo apt install nvidia-384
sudo apt install ubuntu-drivers-common
ubuntu-drivers devices

hwinfo --gfxcard --short
sudo lshw -C display

Dowloads
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

nvidia-smi



# Azure installation
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup
CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
wget -O ${CUDA_REPO_PKG} http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/${CUDA_REPO_PKG} 
sudo dpkg -i ${CUDA_REPO_PKG}
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub 
rm -f ${CUDA_REPO_PKG}
sudo apt-get update
sudo apt-get install cuda-drivers
reboot
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-440_440.33.01-0ubuntu1_amd64.deb

python
import tensorflow as tf; print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')));


sudo apt-get remove --purge '^nvidia-.*'
sudo apt autoremove


https://www.tensorflow.org/install/gpu
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


# Install TensorRT. Requires that libcudnn7 is installed above.
sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0 \
    libnvinfer-dev=5.1.5-1+cuda10.0







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




conda update conda -n root
conda deactivate
conda install anaconda=2019.10



ubuntu 18.04 + NVIDIA
sudo apt install nvidia-390 nvidia-cuda-toolkit libcupti-dev gcc-6 python3-numpy python3-dev python3-pip python3-wheel
sudo mkdir -p /usr/local/cuda /usr/local/cuda/extras/CUPTI /usr/local/cuda/nvvm
sudo ln -s /usr/bin /usr/local/cuda/bin
sudo ln -s /usr/include /usr/local/cuda/include
sudo ln -s /usr/lib/x86_64-linux-gnu /usr/local/cuda/lib64
sudo ln -s /usr/local/cuda/lib64 /usr/local/cuda/lib
sudo ln -s /usr/include /usr/local/cuda/extras/CUPTI/include
sudo ln -s /usr/lib/x86_64-linux-gnu /usr/local/cuda/extras/CUPTI/lib64
sudo ln -s /usr/lib/nvidia-cuda-toolkit/libdevice /usr/local/cuda/nvvm/libdevice




Train on CPU


Download model from
https://github.com/ychfan/tf_estimator_barebone/blob/master/docs/super_resolution.md


Convert model for Tensorflow.js
https://www.tensorflow.org/js/tutorials/conversion/import_saved_model
example:
tensorflowjs_converter \
    --input_format=tf_frozen_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    /mobilenet/frozen_model.pb \
    /mobilenet/web_model

on localhost:
tensorflowjs_converter model .

Web APP
https://github.com/dida-do/public/tree/master/handwriting_app/web
https://github.com/idearibosome/srzoo/tree/master/demo/tfjs

load model into browser

do prediction






tensorflow plt imgshow TypeError: Image data of dtype object cannot be converted to float
import tensorflow as tf
tf.enable_eager_execution()

https://krasserm.github.io/2019/09/04/super-resolution/
https://github.com/krasserm/super-resolution/tree/master/demo


serve.py
pip install flask flask-jsonpify 


prepare some small pics, allow upload too
show loader



