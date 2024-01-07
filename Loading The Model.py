from flask import Flask
from flask_ngrok import run_with_ngrok
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = '/content/drive/MyDrive/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (128, 128)) # load image
  print("@@ Got Image for prediction")

  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D

  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)

  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==1:
      return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'

  elif pred==2:
      return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'

  elif pred==3:
      return "Tomato - Late Blight Disease", 'Tomato-Late_blight.html'

  elif pred==4:
      return "Tomato - Leaf Mold Disease", 'Tomato-Leaf_Mold.html'

  elif pred==5:
      return "Tomato - Septoria Leaf Spot Disease", 'Tomato-Septoria_leaf_spot.html'

  elif pred==6:
      return "Tomato - Target Spot Disease", 'Tomato-Target_Spot.html'

  elif pred==7:
      return "Tomato - Tomoato Yellow Leaf Curl Virus Disease", 'Tomato-Tomato_Yellow_Leaf_Curl_Virus.html'
  elif pred==8:
      return "Tomato - Tomato Mosaic Virus Disease", 'Tomato-Tomato_mosaic_virus.html'

  elif pred==9:
      return "Tomato - Two Spotted Spider Mite Disease", 'Tomato-Two-spotted_spider_mite.html'
