# Streamlit Web App: Personal Protective Equipment, Object Detection Image Browser

This project implements the [YOLO object detection CNN](https://pjreddie.com/darknet/yolo) using a custom dataset of images containing different types of personal protective equipment into an interactive [Streamlit](https://streamlit.io) app.

The complete demo is [implemented in less than 300 lines of Python](https://github.com/ejnunn/PPE-Object-Detection/blob/master/app.py) and illustrates all the major building blocks of Streamlit.

This project was created using the [Streamlit demo-self-driving](https://github.com/streamlit/demo-self-driving) as a template. The image dataset and neural network have been modified for the specific application of detecting PPE. One potential application of this model would be to detect if construction workers or manufacturing employees are wearing the appropriate safety equipment to perform their jobs while in a dangerous work environment.

![](https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/results/example-results.gif)

## How to run this demo
```
pip install --upgrade streamlit opencv-python
streamlit run https://raw.githubusercontent.com/ejnunn/PPE-Object-Detection/master/app.py
```

### Questions? Comments?

Please ask in the [Streamlit community](https://discuss.streamlit.io).


