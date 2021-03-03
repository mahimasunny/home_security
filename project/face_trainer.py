#Copyright Anirban Kar (anirbankar21@gmail.com)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import cv2,os
import numpy as np
from PIL import Image 

path = os.path.dirname(os.path.abspath(__file__))
recognizer = cv2.createLBPHFaceRecognizer()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml'.xml);
dataPath = './dataset'

def get_images_and_labels(datapath):
     image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
     # images will contains face images
     images = []
     # labels will contains the label that is assigned to the image
     labels = []
     for image_path in image_paths:
         # Read the image and convert to grayscale
         image_pil = Image.open(image_path).convert('L')
         # Convert the image format into numpy array
         image = np.array(image_pil, 'uint8')
         # Get the label of the image
         nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
         #nbr=int(''.join(str(ord(c)) for c in nbr))
         print(nbr)
         # Detect the face in the image
         faces = faceCascade.detectMultiScale(image)
         # If face is detected, append the face to images and the label to labels
         for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(nbr)
             cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
             cv2.waitKey(10)
     # return the images list and labels list
     return images, labels


images, labels = get_images_and_labels(dataPath)
cv2.imshow('test',images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.save('.\trainer\trainer.yml')
cv2.destroyAllWindows()