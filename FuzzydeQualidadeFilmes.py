import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada e saída
roteiro = ctrl.Antecedent(np.arange(0, 6, 0.1), 'roteiro')
direcao = ctrl.Antecedent(np.arange(0, 6, 0.1), 'direcao')
producao = ctrl.Antecedent(np.arange(0, 6, 0.1), 'producao')
qualidade = ctrl.Consequent(np.arange(0, 6, 0.1), 'qualidade')

# Definindo os conjuntos fuzzy para cada variável
conjunto_ruim = fuzz.trimf(roteiro.universe, [0, 0, 2])
conjunto_mediano = fuzz.trimf(roteiro.universe, [0, 2, 4])
conjunto_bom = fuzz.trimf(roteiro.universe, [2, 4, 6])
conjunto_otimo = fuzz.trimf(roteiro.universe, [4, 6, 6])

roteiro['ruim'] = conjunto_ruim
roteiro['mediano'] = conjunto_mediano
roteiro['bom'] = conjunto_bom
roteiro['otimo'] = conjunto_otimo

direcao['ruim'] = conjunto_ruim
direcao['mediano'] = conjunto_mediano
direcao['bom'] = conjunto_bom
direcao['otimo'] = conjunto_otimo

producao['ruim'] = conjunto_ruim
producao['mediano'] = conjunto_mediano
producao['bom'] = conjunto_bom
producao['otimo'] = conjunto_otimo

qualidade['ruim'] = conjunto_ruim
qualidade['mediano'] = conjunto_mediano
qualidade['bom'] = conjunto_bom
qualidade['otimo'] = conjunto_otimo

# Definindo as regras fuzzy
rule1 = ctrl.Rule(roteiro['mediano'] & direcao['bom'] & producao['bom'], qualidade['otimo'])
rule2 = ctrl.Rule(roteiro['mediano'] & direcao['bom'] & producao['mediano'], qualidade['bom'])
rule3 = ctrl.Rule(roteiro['ruim'] & direcao['mediano'] & producao['mediano'], qualidade['mediano'])
rule4 = ctrl.Rule(roteiro['ruim'] & direcao['ruim'] & producao['ruim'], qualidade['ruim'])

# Criando o sistema de controle fuzzy
sistema_qualidade = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

# Executando a simulação com valores de entrada
simulador = ctrl.ControlSystemSimulation(sistema_qualidade)

simulador.input['roteiro'] = 2
simulador.input['direcao'] = 4
simulador.input['producao'] = 5

simulador.compute()

print(simulador.output['qualidade'])
qualidade.view(simulador)
plt.show()