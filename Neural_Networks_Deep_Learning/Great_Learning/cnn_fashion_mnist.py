# -*- coding: utf-8 -*-
"""CNN Fashion MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCH5J6_P6rr8Dgwev5jgC5M_dWmLq0qi
"""

import tensorflow as tf
import keras

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input , Conv2D,Dense , Flatten , Dropout
from tensorflow.keras.models import Model # Model why?

# Classification
fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train , y_train) , (x_test , y_test) = fashion_mnist.load_data()

x_train.shape

x_train[0]
# gray scale values between the 0 to 255

# Standardization using scaling

x_train , x_test = x_train/255.0 , x_test/255.0

x_train.shape

x_train[0]
# scaled

x_test.shape

x_test[0]

x_train = np.expand_dims(x_train , -1)
x_test = np.expand_dims(x_test , -1)

x_train.shape

x_test.shape

# Number of classes
K = len(set(y_train))
print(' the number of classes :' , K)

# Functional API? Search

x_train[0].shape

# Building the model using the Funcional API

i = Input(shape = x_train[0].shape)
x = Conv2D(32 , (3,3) , strides=2 , activation='relu')(i)
x = Conv2D(64 , (3,3) , strides=2 , activation='relu')(x)
x = Conv2D(128 , (3,3) , strides=2 , activation='relu')(x)
x = Flatten()(x)
x = Dropout(0.2)(x)
# Dense layer NN 
x = Dense(512 , activation='relu')(x)
x = Dropout(0.2)(x)
x = Dense(K , activation='softmax')(x)

model = Model(i , x)

# compile nad fit the model

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'],
              )
r = model.fit(x_train , y_train , validation_data=(x_test , y_test),
              epochs = 15)



# plot the loss per iteration
plt.plot(r.history['loss'] , label = 'loss')
plt.plot(r.history['val_loss'] , label = 'val_loss')
plt.legend()

# plot the accuracy per iteration

plt.plot(r.history['accuracy'] , label = 'accuracy')
plt.plot(r.history['val_accuracy'] , label = 'val_accuracy')
plt.legend()

# confusion Matrix
from sklearn.metrics import confusion_matrix
import itertools

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
  """
  This function prints and plots the confusion matrix.
  Normalization can be applied by setting `normalize=True`.
  """
  if normalize:
      cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
      print("Normalized confusion matrix")
  else:
      print('Confusion matrix, without normalization')

  print(cm)

  plt.imshow(cm, interpolation='nearest', cmap=cmap)
  plt.title(title)
  plt.colorbar()
  tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks, classes, rotation=45)
  plt.yticks(tick_marks, classes)

  fmt = '.2f' if normalize else 'd'
  thresh = cm.max() / 2.
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
      plt.text(j, i, format(cm[i, j], fmt),
               horizontalalignment="center",
               color="white" if cm[i, j] > thresh else "black")

  plt.tight_layout()
  plt.ylabel('True label')
  plt.xlabel('Predicted label')
  plt.show()


p_test = model.predict(x_test).argmax(axis=1)
cm = confusion_matrix(y_test, p_test)
plot_confusion_matrix(cm, list(range(10)))

# label mapping ?
labels = ''' T-shirt
Trouser 
Pullover
Dress
Coat
Sandal
Shirt
Sneaker
Bag
Ankle Boot''' .split('\n')

labels

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));

# Let us show the misclassified 

misclassified_img = np.where(p_test != y_test)[0]
i = np.random.choice(misclassified_img)
plt.imshow(x_test[i].reshape(28, 28) , cmap = 'gray')
plt.title('True label: %s Predicted : %s' %(labels[y_test[i]] , labels[p_test[i]]));







