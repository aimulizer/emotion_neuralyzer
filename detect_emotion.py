import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D
from tensorflow.keras  import layers
import pickle
import numpy as np


def mood():
    cap = cv2.VideoCapture(0)
    # img = cv2.imread('test1.jpg')
    _,img = cap.read()
    # cap.release()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img_size=48
    faces = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    train_data=[]
    for x,y,w,h in faces:
        new_img=cv2.resize(gray[y:y+h,x:x+w],(img_size,img_size))
        train_data.append(new_img)
    train_data=np.asarray(train_data)
    train_data = train_data.reshape(-1,img_size,img_size,1)
    train_data = train_data/255


    # model
    model = Sequential()
    model.add(Conv2D(64,(3,3),input_shape=(48,48,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(128,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(32,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(32,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    

    model.add(Flatten())


    model.add(Dense(64,activation = 'relu',kernel_regularizer=tf.keras.regularizers.l2(0.02)))
    model.add(Dense(4,activation = 'softmax'))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.load_weights('v3/v3_checkpoints')

    ypred= model.predict(train_data)
    ypred = [np.argmax(x) for x in ypred]
    label = pickle.load(open("labels.pickle","rb"))
    cap.release()
    return label[ypred[0]]