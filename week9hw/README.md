# HW 9 Questions

### Annotating the Dataset
![Annoted Image](./image_annotations.jpg)

 - It took me approx. 2.5 hrs to annotate the 384 images in the data set.  
 - Using `grep -i "Tie" * | wc -l` in the annotations folder I count 319 labels for Tie Fighter and 312 for Millennium Falcon.
 - Larger datasets will require several people to annotate, unless there are sophisticated software tools to assist in the task. There are online services like Amazon's Mechanical Turk that can be utilized in contracting out this work to hundreds or thousands of workers.
 - Once images are annotated, that data has to also be transformed by any image augmentations like flip, translate, crop, scale etc.  There are libraries such as https://github.com/albumentations-team/albumentations that also augment the annotation data, but specific augmentation operations may require custom annotation operations as well.


### Image Augmentations

Describe the image augmentation operations of the tool https://github.com/codebox/image_augmentor:
