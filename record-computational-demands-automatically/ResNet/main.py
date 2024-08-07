from measurer import Measurer
from types import ModuleType
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras
import numpy as np

def main():
    
    # START 
    data_path = '/'
    measurer = Measurer()
    tracker = measurer.start(data_path=data_path)


    data = keras.datasets.cifar10
    (train_images, train_labels), (test_images, test_labels) = data.load_data()
    labels = len(np.unique(train_labels))
    print('Train set shape = ', train_images.shape)
    print('Labels = ', labels)
    print('\n')
    

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # ResNet
    resnet = keras.applications.ResNet152V2(
        include_top=False,
        weights=None,
        input_shape=(train_images.shape[1], train_images.shape[2], train_images.shape[3]),
        pooling='max'
    )

    model = keras.models.Sequential()
    model.add(resnet)
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(labels, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=20, batch_size=256, validation_split=0.3)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('\n\nTest accuracy:', test_acc)

    model_path = "./resnet.keras"
    model.save(model_path)

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
