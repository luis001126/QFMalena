print('********************************************************')
print('********************> B E N C E N O <*******************')
print('********************************************************')

#datos fijos
m1 = 1.3467 #g
m2 = 0.6335 #g
I1 = 90*0.04 #A
I2 = 80*0.04 #A
V1 = 15*0.4 #V
V2 = 10*0.4 #V
T = 80.1 + 273.15 #K
R1 = 8.314 #J/molK
R2 = 0.082 #atmL/molK
t = 180 #s
M = 78.11 #g/mol
P = 1 #atm

# ecuaciones de entalpia
delta_H_exp = ((I1 * V1 - I2 * V2) * t) / (m1 - m2)
deta_H = delta_H_exp * M

# determinacon del trabajo
W = R1 * T

# determinacion de la entropia
del_S = deta_H / T

# determinacion de la variacion de la funcion del trabajo
det_A = W * -1

# determinacion de la energia interna
del_Ener = deta_H - W

print(f"La energia interna del tolueno es {del_Ener} J")
print(f'El calor que se le suministra al sistema {deta_H} J')
print(f'La variacion de la funcion de trabajo es de {det_A} J')
print(f'El valor de la entropia es de {del_S} J/K')
print(f'El valor del trabajo es de {W} J')
print(f'El valor de entalpia es de {deta_H} J')
print('La variacion de la energia libre de Gibbs es 0')

