# Object Detection Image Browser:
## **Personal Protective Equipment**

## Background

This project demonstrates the [YOLOv3 object detection](https://pjreddie.com/publications/) technology using a custom dataset of images containing safety vests and hard hats, packaged into an interactive [Streamlit](https://streamlit.io) app. This project was created using the [Streamlit demo-self-driving](https://github.com/streamlit/demo-self-driving) app as a template.
The neural network was trained using transfer learning by using pre-trained weights from [Darknet YOLOv3](https://pjreddie.com/darknet/yolo/). Model training was performed using [Google Colab](https://colab.research.google.com/) to take advantage of the free GPU acceleration.

The dataset used for training is relatively small, and therefore leaves lots of room for improvement. Limited availability of labeled images with bounding box coordinates means the current model does not yet generalize to broad types of images. Try uploading your own images to see how the model performs on new data.

👈 **Please select _Run the App_ in the sidebar to start.**

## Example
![](https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/results/example-results.gif)

This example was created using Google Colab to run YOLO on each frame individually. Post-processing software was used to stitch the frames back into a video format.

The images generated in this Streamlit application use a different method to draw the object bounding boxes but the same neural network is used to make the predictions as the example video.

## Applications

Reduce workplace injuries in construction and manufacturing environments by determining if employees are wearing the appropriate safety equipment to perform their jobs.

The model can be configured to detecting [foreign object debris (FOD)](https://en.wikipedia.org/wiki/Foreign_object_damage) to maintain a flightline or factory environment.

## Future Work

Increase the size of the training dataset. The current model cannot generalize to any image containing PPE equipment and therefore is inaccurate when faced with never before seen imagery. By gathering more labeled data, the model will improve performance by learning a better representation of what safety vests and hard hats look like in different scenarios.

Implement an object tracking algorithm to lock on to specific objects and determine if the object is the same as the one present in the previous frame. This could be done by using the previous frame's data, computing the IOU (intersection over union) of object in the two frames, and make use of the linear sum assignment to assign a unique ID based on the least IOU.

## Contact Me

**Eric Nunn**

[Email](mailto:ejnunn1@msn.com) | [GitHub](https://github.com/ejnunn/) | [LinkedIn](https://linkedin.com/in/eric-j-nunn/)

![](https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/images/profile-thumbnail.jpg)
