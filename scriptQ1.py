import math
from arredondamentos import round_half_away_from_zero as rhafz

r=float(input('Indique o valor de r: '))
DDPAD_R = float(input('Indique o DPAD de r: '))
p1 = float(input('Indique o valor de p1: '))
p2 = float(input('Indique o valor de p2: '))
p3 = float(input('Indique o valor de p3: '))
LT = 1*p1 + 2*p2 + 3*p3
print(LT)
M_DDLT = r*LT
print(M_DDLT)
C1=0.345
C2=float(input('Indique o valor de C2: '))
C3=1500
DPAD_LT_SQUARE = (1-LT)**2 * p1 + (2-LT)**2 * p2 + (3-LT)**2 * p3
print(DPAD_LT_SQUARE)
DPAD_DDLT = math.sqrt(DDPAD_R**2*LT + r**2*DPAD_LT_SQUARE)
print(DPAD_DDLT)

def q1(r,C1,C3):
    return rhafz(math.sqrt((2*r*C3)/C1))

def q2(r,C1,C2,C3,E):
    return rhafz(math.sqrt((2*r*(C2*E+C3))/C1))

def calculateS(z,M_DDLT,DPAD_DDLT):
    return rhafz(M_DDLT + z*DPAD_DDLT)

def calculateZ2(S,M_DDLT,DPAD_DDLT):
    return (S-M_DDLT)/DPAD_DDLT

def calculateZ(n):
    return (3*n)/100

def calculateE(sndInt,DPAD_DDLT):
    return sndInt * DPAD_DDLT

def calculateP(C1,C2,q,r):
    return (C1*q)/(C2*r)

def custoTotal(q,r,S,E,C1,C2,C3,M_DDLT):
    return ( C1*(q/2+S-M_DDLT) + C2*(r/q)*E + C3*(r/q) )

def calculateN(z):
    return (z*100)/3

sndIntInicial = float(input(f'Introduza o segundo integral para N {rhafz(calculateN(calculateZ2(1200,M_DDLT,DPAD_DDLT)))}: ' ))

inicialN=0

qInicial = q1(r,C1,C3)
P = calculateP(C1,C2,qInicial,r)
sndInt = float(input(f'Indique o valor do 2o integral correspondente ao 1o integral {P}: '))
inicialN = int(input(f'Indique o valor de N para o 1o integral {P}: '))
E = calculateE(sndInt,DPAD_DDLT)
N=0


while True:
    qSeguinte = q2(r,C1,C2,C3,E)
    PSeguinte = calculateP(C1,C2,qSeguinte,r)
    sndInt = float(input(f'Indique o valor do 2o integral correspondente ao 1o integral {PSeguinte}: '))
    inicialN = int(input(f'Indique o valor de N para o 1o integral {PSeguinte}: '))
    E = calculateE(sndInt,DPAD_DDLT)
    if N != inicialN:
        N = inicialN
    else:
        break

S = calculateS(calculateZ(N),M_DDLT,DPAD_DDLT)

print(f'q*: {qSeguinte}')
print(f'S : {S}')
print(f'E : {E}')
ct = custoTotal(qSeguinte,r,S,E,C1,C2,C3,M_DDLT)
print(f'Custo total: {ct}')
ci = custoTotal(1700,r,1200,calculateE(sndIntInicial,DPAD_DDLT),C1,C2,C3,M_DDLT)
print(f'Custo inicial: {ci}')
print(f'Diferença de custos: {ci-ct}')


