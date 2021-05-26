#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install ffmpeg')
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow
from IPython.display import HTML
from base64 import b64encode
import tempfile
import ffmpeg
from moviepy.editor import *

