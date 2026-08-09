import numpy as np
import tensorflow as tf
from PIL import Image

MODELO = tf.keras.models.load_model("model/modelo_mnist.keras")


def preverImagem(imagem):
    # Converter para escala de cinza e redimensionar para 28x28
    img = Image.fromarray(imagem.astype(np.uint8)).convert("L").resize((28, 28))

    #  Normalizar entre 0.0 e 1.0
    img_array = np.array(img, dtype=np.float32) / 255.0

  # Adicionar dimensões de batch e canal: (1, 28, 28, 1)
    img_array = img_array.reshape(1, 28, 28, 1)

    # Predição
    raw_data = MODELO.predict(img_array)

    probs = raw_data[0]
    num_previsto = np.argmax(probs)
    certeza = float(probs[num_previsto]) * 100

    return int(num_previsto), round(certeza, 2)