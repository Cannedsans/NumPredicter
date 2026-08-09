# Previsor de Números Escritos à Mão

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)

</div>

<p align="center">
  <b>Um aplicativo web interativo que reconhece dígitos desenhados na tela usando Deep Learning.</b>
</p>

---

## Sobre o Projeto

Este projeto foi desenvolvido com foco no estudo prático de **Inteligência Artificial** e **Visão Computacional**. A aplicação permite que o usuário desenhe qualquer número de **0 a 9** em um canvas interativo na Web, e um modelo de rede neural treinado com **TensorFlow / Keras** faz a predição em tempo real de qual dígito foi desenhado.

---

## Demonstração

<div align="center">
  <img src="media/print.png" alt="Demonstração do funcionamento do projeto" width="700px">
</div>

---

## Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem principal do projeto.
- **[TensorFlow / Keras](https://www.tensorflow.org/)** - Criação, treinamento e inferência do modelo de rede neural.
- **[Streamlit](https://streamlit.io/)** - Interface web rápida e interativa.
- **[Streamlit Drawable Canvas](https://github.com/andfanilo/streamlit-drawable-canvas)** - Componente para desenho do dígito na tela.
- **[NumPy](https://numpy.org/) & [OpenCV / Pillow](https://pillow.readthedocs.io/)** - Processamento e pré-processamento de imagens.

---

## Como Funciona o Modelo?

1. **Desenho:** O usuário desenha no canvas $280 \times 280$ pixels.
2. **Pré-processamento:** A imagem é convertida para escala de cinza, redimensionada para $28 \times 28$ pixels e normalizada (de forma semelhante ao dataset **MNIST**).
3. **Predição:** A imagem tratada é passada para o modelo treinado em TensorFlow, que retorna as probabilidades para cada dígito ($0$ a $9$).