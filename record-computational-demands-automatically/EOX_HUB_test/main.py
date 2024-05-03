from measurer import Measurer
from types import ModuleType
import time
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np

def main():
    
    # START 
    data_path = '/'
    measurer = Measurer()
    tracker = measurer.start(data_path=data_path)


    # get data
    data = keras.datasets.cifar10
    (train_images, train_labels), (test_images, test_labels) = data.load_data()
    labels = len(np.unique(train_labels))
    print('Train set shape = ', train_images.shape)
    print('Labels = ', labels)
    print('\n')
    

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # CNN
    model = tf.keras.Sequential([
        keras.Input(shape=(train_images.shape[1], train_images.shape[2], train_images.shape[3])),
        
        tf.keras.layers.Conv2D(32, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),
        
        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Conv2D(128, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),
        
        tf.keras.layers.Conv2D(256, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(150, activation="relu"),
        tf.keras.layers.Dense(labels, activation="softmax")
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=20, batch_size=512)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('\n\nTest accuracy:', test_acc)


    # END
    measurer.end(
                tracker=tracker,
                shape=train_images.shape,
                libraries=[v.__name__ for k, v in globals().items() if type(v) is ModuleType and not k.startswith('__')],
                data_path=data_path,
                program_path=__file__,
                variables=locals(),
                csv_file='benchmarks.csv')
    
    
    
if __name__ == "__main__":
    main()