# Deliver

Docker image: websta8/adl-super-resolution

## Summary of the previous attempts

Could not use GPU for training and therefore stopped early. The intermediate model could not be converted to a JSON representation to reuse it in an Web application.
Another model selected for Super-Resolution could successfully transformed to JSON representation, but I was not able to use it, because I was not aware of the format the model expect as input nor how to create an tensor input from JPG/PNG input (after some research I found [imageToTensor (untested, just for reference)](https://heartbeat.fritz.ai/image-classification-on-react-native-with-tensorflow-js-and-mobilenet-48a39185717c)).

Still have no model in the browser.

## Doing

Some research lead to [Single Image Super-Resolution with EDSR, WDSR and SRGAN](https://github.com/krasserm/super-resolution) which contains a Tensorflow 2.0 implementation of an Super-Resolution Generative Adversarial Network. Training is possible on [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/) dataset, but I simply used the weights of the already trained network.

In the bundled notebooks [exapmle-srgan.ipynb](https://github.com/krasserm/super-resolution/blob/master/example-srgan.ipynb) I could successfully create the super resolution of selected images.

Therefore I extracted the required code into a [Flask](https://github.com/pallets/flask) application which provides two REST endpoints:
- ***/*** to load the initial website
- ***/upscale*** to receive an image and upscale it

The application is wrapped into a docker container which contains everything required to run the example.

Some steps to pack everything in the right folder and test the application:
```
apt update
apt install python3 python3-pip 
pip3 install --upgrade pip3
git clone https://github.com/websta/AppliedDeeplearning
cd AppliedDeeplearning/3_deliver
wget https://github.com/websta/AppliedDeeplearning/releases/download/0.1/weights-srgan.tar.gz weights-srgan.tar.gz
tar -xzf weights-srgan.tar.gz
pip3 install -r requirements.txt
pip3 install --upgrade tensorflow
git clone https://github.com/krasserm/super-resolution super-resolution
cd super-resolution
git checkout 102b1211334d0e786c453744505beb389d2e83b1
cp ../app/app.py .
cp -r ../app/templates .
cp -r ../app/uploads .
cp -r ../weights .
cp ../requirements.txt requirements.txt
flask run --host=0.0.0.0 --port=80
```

Docker commands to create the docker image:
```
docker build -t websta8/adl-super-resolution:latest .
```
Docker command to run it: In background or interactive:
```
docker run -d -p 5000:5000 websta8/adl-super-resolution:latest
docker run -it -p 5000:5000 websta8/adl-super-resolution:latest
```

Docker commands to list images and delete images:
```
docker image ls
docker image rm -f 271095295fbf
```

Docker commands to push image to Dockerhub:
```
docker login
docker tag websta8/adl-super-resolution:latest websta8/adl-super-resolution:1.1
docker push websta8/adl-super-resolution:1.1
```

Docker command to run the final image:
```
docker run -d -p 5000:5000 websta8/adl-super-resolution:1.1
docker run -it -p 5000:5000 websta8/adl-super-resolution:1.1
```

Docker commands to release some space:
```
docker system prune
docker builder prune
```


## Notes

Running the docker image and sending large files (more than 400x400 pixels) to upscale, the memory consumption exceeded 8GB RAM. I could successfully test the docker image on an Azure B2ms (2 vcpu, 8GB memory) with the demo images.