# HW 8 Questions

### Annotating the Dataset
![Annoted Image](./image_annotations.jpg)

 - It took me approx. 2.5 hrs to annotate the 384 images in the data set.  
 - Using `grep -i "Tie" * | wc -l` in the annotations folder I count 319 labels for Tie Fighter and 312 for Millennium Falcon.
 - Larger datasets will require several people to annotate, unless there are sophisticated software tools to assist in the task. There are online services like Amazon's Mechanical Turk that can be utilized in contracting out this work to hundreds or thousands of workers.
 - Once images are annotated, that data has to also be transformed by any image augmentations like flip, translate, crop, scale etc.  There are libraries such as https://github.com/albumentations-team/albumentations that also augment the annotation data, but specific augmentation operations may require custom annotation operations as well.


### Image Augmentations

Describe the image augmentation operations of the tool https://github.com/codebox/image_augmentor:

 - Flip: mirrors the image in either vertically or horizontally
 - Rotation: rotates the image to an arbitrary angle
 - Scale: can either increase the size of the image, or zoom in which increases the content of the image without changing it's resolution
 - Crop: cuts and keeps just a particular section of the image 
 - Translation: is usually a 2D movement of the image contents.
 - Noise: adds random values on a per pixel basis
 
### Audio Augmentations

Using the audio annotation tool provided at https://github.com/CrowdCurio/audio-annotator, audio annotations differ from image annotations in that they require just a start and end timestamp, as well as a class label and any other tags we wish to associate with each image (ie in the provided examples we also labelled audio as near, far, etc).
