#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def trackcar(path):
  cap = cv2.VideoCapture(path)
  car_cascade = cv2.CascadeClassifier('/content/cars.xml')
  # loop runs if capturing has been initialized.
  try:
    while True:
        # reads frames from a video
        ret, frames = cap.read()
          
        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
          
      
        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
          
        # To draw a rectangle in each cars
        for (x,y,w,h) in cars:
          if w*h > 3500:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
      
      # Display frames in a window 
        #cv2_imshow(frames)
        frameslist.append(frames)
  except: 
    pass
  video_name = 'video.avi'

  images = frameslist
  frame = images[0]
  height, width, layers = frame.shape
  #fourcc = cv2.VideoWriter_fourcc('H','2','6','4') 
  video = cv2.VideoWriter(video_name, 0, 30, (width,height))

  for i in range(0,len(images)):
      video.write(images[i])
  video.release()

