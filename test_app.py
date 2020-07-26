import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib
import sys

try:
    sys.path.append('/usr/local/lib64/python3.6/site-packages')
    import cv2
except Exception as e:
    print(e)


def main():
    st.header('Test app')


if __name__ == '__main__':
    main()
