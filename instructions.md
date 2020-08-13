# Object Detection Image Browser:
## **Personal Protective Equipment**

## Background

This project demonstrates the [YOLOv3 object detection](https://pjreddie.com/publications/) technology using a custom dataset of images containing safety vests and hard hats, packaged into an interactive [Streamlit](https://streamlit.io) app. This project was created using the [Streamlit demo-self-driving](https://github.com/streamlit/demo-self-driving) app as a template.
The neural network was trained using transfer learning by using pre-trained weights from [Darknet YOLOv3](https://pjreddie.com/darknet/yolo/). Model training was performed using [Google Colab](https://colab.research.google.com/) to take advantage of the free GPU acceleration.

Streamlit allows this data science applicaton to be easily viewed by multiple stakeholders to visualize their model's performance without knowing how to code.

👈 **Please select _Run the App_ in the sidebar to start.**

## Example
![](https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/results/example-results.gif)

This example was created using Google Colab to run YOLO on each frame individually. Post-processing software was used to stitch the frames back into a video format.

The images generated in this Streamlit application use a different method to draw the object bounding boxes but the same neural network is used to make the predictions as the example video.

## Applications

Reduce workplace injuries in construction and manufacturing environments by determining if employees are wearing the appropriate safety equipment to perform their jobs.

The model can be configured to detecting [foreign object debris (FOD)](https://en.wikipedia.org/wiki/Foreign_object_damage) to maintain a flightline or factory environment.

## Future Work

Implement an object tracking algorithm to lock on to specific objects and determine if the object is the same as the one present in the previous frame. This could be done by using the previous frame's data, computing the IOU (intersection over union) of object in the two frames, and make use of the linear sum assignment to assign a unique ID based on the least IOU.

## Contact Me

**Eric Nunn**

[Email](mailto:ejnunn1@msn.com) | [GitHub](https://github.com/ejnunn/) | [LinkedIn](https://linkedin.com/eric-j-nunn/)

![](https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/images/profile-thumbnail.jpg)
