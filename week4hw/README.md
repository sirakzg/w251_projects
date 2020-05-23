#Question 2

## a) 
The ConvnetJS MNIST demo has 9 layers in its network:

- input: this layer defines the starting dimensions of the network and accepts the images in 24x24 resolution  
- relu: runs non-linear activations on each value of the preceding layer
- pool: Pooling reduces the dimesions of the preceding layer by taking the max value of a 2x2 grid per filter. resulting output resoluion is now 12x12x8
- conv: Our second convolution operation with 16 filters of filter size 5x5, stride 1, padding of 2
- relu: another non-linear activation on all values passed down from previous convolution
- pool: another dimension reduction, this time over 3x3 grids across the 16 filters, resulting in an output resolution of 4x4x16
- fully connected: this layer 'flattens' the network into a 1-D array of length 10, and each of these 10 neurons is connected to every neuron of the preceding layer
- softmax: a non-linear activation that outputs the predicted digit probabilities, with sum across its 10 actications summing to 1.

## b)
I doubled the number of filters in the conv layers and noticed training and validation accuracy went down, possibly requiring more training iterations.  I reverted teh first conv to 8 filters and then cut the second conv to 8 filters as well and noticed slightly better performance but a greater difference between training and validation accuracies.

## c)
By removing the pooling layers I noticed similar performance in the training accuracy as before, ie 90-95% at 4k iterations, but the validation accuracy was much lower at around 80-83%.

## d)
Adding an additional conv layer (with 16 filters) improved training accuracy slightly to 96% but I did not see an increase in validation accuracy, which remained at 82%.

## e)
Increasing the batch size to 50 made a significant improvement on the default model, with training accuracy reaching 98% and validation at 90%.

## f)
With the original model I lowered the learning rate to 0.001, reduced momentum to 0.8 and increased batch size to 40.  It took several more iterations but at 12k steps I'm getting training accuracy of 98%, validation of 96%.
