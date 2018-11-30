from keras.models import load_model
import glob
import numpy as np
# from matplotlib import pyplot as plt
import tensorflow as tf
from keras import backend as K
import cv2
# get_ipython().run_line_magic('matplotlib', 'inline')

# class Model:
#     _img_width, _img_height = 150, 150
#     def __init__(self):
#         self._model=load_model('./xray/softmodel.h5')
        
#     def _load_image(self,ImageAddr):
#         self.origin_img=cv2.imread(ImageAddr)
#         print('ImageAddr ===>', self.origin_img.shape)
#         self.temp_img=cv2.resize(self.origin_img,(self._img_width,self._img_height))
        
#     def _img_preprocessing(self):
#         resize_img=self.temp_img
#         scale_img=resize_img/255.
#         self.temp_img=np.expand_dims(scale_img,axis=0)
        
#     def _img_prediction(self):
#         test_img=self.temp_img
#         Normal,Pneumonia=self._model.predict(test_img)[0]
#         label = "NORMAL" if Normal > Pneumonia else "PNEUMONIA"
#         proba = Normal if Normal > Pneumonia else Pneumonia
#         label = "{}: {:.2f}%".format(label, proba * 100)
#         self.proba=round(proba*100,2)
#         #result=self._model.predict_classes(test_img)[0][0]
#         #label='PNEUMONIA' if result else 'NORMAL'
#         self.origin_img=cv2.resize(self.origin_img,(300,300))
#         self.origin_img=cv2.putText(self.origin_img, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
#         #(NORMAL, PNEUMONIA) = model.predict(test_img)[0]
#         #self.proba = santa if santa > notSanta else notSanta
#     def prediction(self,ImageAddr):
#         self._load_image(ImageAddr)
#         self._img_preprocessing()
#         self._img_prediction()
#         return self.origin_img,self.proba
def Model(path):

    _img_width, _img_height = 150, 150
    model = load_model('./xray/model.h5') #sigmoid 모델 넣어야함
    origin_img=cv2.imread(path)
    temp_img=cv2.resize(origin_img,(_img_width, _img_height))
        
    resize_img= temp_img
    scale_img=resize_img/255.
    temp_img=np.expand_dims(scale_img,axis=0)
    #sigmoid 값을 z_value에 저장 만약 z_value<0.5
    #일 경우 z_value=1-z_value
    z_value=model.predict(temp_img)[0][0]
    if z_value<0.5:
        z_value=1-z_value
    #label_ = "NORMAL" if Normal > Pneumonia else "PNEUMONIA"
    #proba = Normal if Normal > Pneumonia else Pneumonia
    #label = "{}: {:.2f}%".format(label_, proba * 100)
    z_value=round(z_value*100,2)
    result=model.predict_classes(temp_img)[0][0]
    label='PNEUMONIA' if result else 'NORMAL'
    origin_img=cv2.resize(origin_img,(300,300))
    origin_img=cv2.putText(origin_img, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (181, 173, 0), 2)
    #(NORMAL, PNEUMONIA) = model.predict(test_img)[0]
    #self.proba = santa if santa > notSanta else notSanta
    
    K.clear_session()

    return origin_img,z_value, label
    
    
