import numpy as np
from keras.models import model_from_json

#carregando rede neural treinada
arquivo = open('rede_neural_treinada', 'r')
estrutura_rede = arquivo.read()
arquivo.close()

classificador = model_from_json(estrutura_rede)
classificador.load_weights('pesosTreinados.h5')

#passando valores para previsao já usando a rede neural treinada
novo = np.array([[15.80, 8.34, 118, 900, 0.10, 0.26, 0.08, 0.134, 0.178, 0.20, 0.05, 
                  1098, 0.97, 4500, 145.2, 0.005, 0.04, 0.05, 0.015, 0.03, 0.007, 23.15,
                  16.64, 178.5, 2018, 0.14, 0.185, 0.84, 158, 0.363]]) #valores inseridos pelo usuário 

previsao = classificador.predict(novo) #previsao final para o usuário