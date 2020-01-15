# io_pyFER
## Goal
The goal of this project is to write a program able to recognize emotions given facial expressions images and also allowing to predict/recognize new emotions based in a combination of <b>Basic Emotions</b>.

<p align="center"> 
    <img src="/md_images/basic_emotions.jpg" alt="Basic Emotions"><br>
    <i>Basic Emotions</i>
</p>

## Theroy-ish 
"<i>FER is more difficult than most other Image Classification tasks. However, well-designed systems can achieve accurate results when constraints are taken into account during development.

For example, higher accuracy can be achieved when classifying a smaller subset of highly distinguishable expressions, such as anger, happiness, and fear. Lower accuracy is achieved when classifying larger subsets, or small subsets with less distinguishable expressions, such as anger and disgust.</i>" (https://www.thoughtworks.com/insights/articles/recognizing-human-facial-expressions-machine-learning)

### Commonly used FER system architectures 
#### Recognizing human facial expressions with machine learning 
<p align="center"> 
    <img src="/md_images/fer_sys_arch.jpeg" alt="Basic Emotions"><br>
</p>

<b>Image Preprocess:</b> Can include image transformations such as scaling, cropping, or filtering images. It is often used to accentuate relevant image information, like cropping an image to remove a background. It can also be used to augment a dataset.

<b>Feature Extraction:</b> This stage goes further in finding the more descriptive parts of an image. Often this means finding information which can be most indicative of a particular class, such as the edges, textures, or colors.

### Commonly used FER system algorithms
#### Support Vector Machines (SVM) 
SVM's are supervised learning algorithms that analyze and classify data, and they perform well when classifying human facial expressions. However, they only do so when the images are created in a controlled lab setting with consistent head poses and illumination.

SVM's perform less well when classifying images captured “in the wild,” or in spontaneous, uncontrolled settings.

#### Convolutional Neural Networks (CNN)
CNN's are currently considered the go-to neural networks for image classification, because they pick up on patterns in small parts of an image, such as the curve of an eyebrow.

CNN's apply kernels, which are matrices smaller than the image, to chunks of the input image. By applying kernels to inputs, new activation matrices, are generated and passed as inputs to the next layer of the network. In this way, CNNs process more granular elements within an image, making them better at distinguishing between two similar emotion classifications.

#### Recurrent Neural Networks (RNN)
RNN's use dynamic temporal behavior when classifying an image. This means that when an RNN processes an input example, it doesn’t just look at the data from that example — it also looks at the data from previous inputs, which are used to provide further context. In FER, the context could be previous image frames of a video clip.



