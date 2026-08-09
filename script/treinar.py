import os
import tensorflow as tf
from tensorflow.keras import Sequential, layers

print("Baixando MNIST e criando o seu modelo...")
mnist = tf.keras.datasets.mnist

(train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()

train_imgs = train_imgs / 255.0

test_imgs = test_imgs / 255.0

model = Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_imgs, train_labels, epochs=10)


test_loss, test_acc = model.evaluate(test_imgs,  test_labels, verbose=2)

print('\nPrecisão do modelo: ', test_acc)

model.save('./model/modelo_mnist.keras')
print("Modelo salvo com sucesso!")