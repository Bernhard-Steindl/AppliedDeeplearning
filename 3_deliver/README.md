# Deliver

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


```
git clone https://github.com/websta/AppliedDeeplearning
cd 3_deliver
pip install -r requirements.txt
git clone https://github.com/krasserm/super-resolution super-resolution
cd super-resolution
git checkout 102b1211334d0e786c453744505beb389d2e83b1
cd ..
flask run
```
