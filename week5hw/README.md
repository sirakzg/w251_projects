# HW 5 Questions

For questions refer to HW repo: https://github.com/MIDS-scaling-up/v2/tree/master/week05/hw

#### 1) 
Tensorflow is a deep learning framework opensourced and maintained by Google.

#### 2) 
TensorRT is an optimization framework for deep learning models to run more efficiently on Nvidia GPUs. It is not a complete development framework for deep learning as models must be trained beforehand and translated into a compatable format.

#### 3) 
ImageNet is an dataset collection of currently 14,197,122 images indexed into 21841 synsets.  The ImageNet challenges of 2010-2017 focused on training sets of 1.2 million images consisting of 1000 classifications.  

#### 4) 
GoogleNet or Inception uses a series of inception modules containing convolution layers with several different filter sizes that allows the model to capture both local and global features in the image, and then gets passed thru a concat/filter stage before proceeding further down the network. MobileNet is a much smaller, mobile optimized network that uses depth-wise separable convolutions to determine both the desired size and speed of the model and its expected accuracy.

#### 5) 
A bottleneck in neural networks is were a layer in the model has fewer neurons than the layers before and after it. Bottlenecks force the model to create a reduced dimensionality of the data passing thru it.  These reduced representations can often be used to represent the original data in a more compressed manner, like we do in this model by saving them to file for later use.

#### 6) 
Layer freezing is where you take a previously trained neural network and prevent certain layers from updating their weights.  This can be useful in scenarious where transfer learning is required while minimizing additional calculations.

#### 7) 
In our TF1 lab we utilized the MobileNet v1.0 pretrained model, provided by Google, which is downloaded from their site and saved in the tf_files/models folder.  Using the frozen layers we then create a bottleneck file for each image and save those to disk, so that during the re-training phase we can avoid multiple passes and calculations over the layers of the model that won't change.

#### 8) 
When reducing the learning rate from the default `0.01` to `0.005` I did indeed see it take longer to reach 80% accuracy on Tensorboard, bt it also achieve a couple more percentage from ~82% to 85%.

#### 9) 
When using a learning rate of `1.0` the accuracy of the validation set dips below 80% but still managed to train a useful graph in this instance. Note for certain training runs I was only able to do  100 iterations to avoid Tensorboard from crashing and core dumping.  Longer runs with this learning rate and no decay could potentially produce unusable models

#### 10) 
For a different set of images to train on I used the Beans dataset also provided by Goole here:  https://www.tensorflow.org/datasets/catalog/beans.  I trained on 400 iterations (again Tensorboard tended to core dump after too many iterations) and achieved a train accuracy of 92%, and validation accuracy 86%.

#### 11) 
Using 400 training iterations I observed running time for MobileNet on the GPU (including bottleneck run as I found this step was GPU heavy) came to 4 minutes and 10 seconds.  Compare this to the CPU run of 7 minutes and 7 seconds.

#### 12) 


#### 13) 
The following values should be passed to the retrain script to run the Inception model:

> --input_layer=Mul:0

> --input_height=299

> --input_width=299

Using Tensorboard you can double click the input node to see more attributes, dimension size, etc. 
