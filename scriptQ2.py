import math
from arredondamentos import round_half_away_from_zero as rhafz

N=58
t=4
r=float(input('Indique o valor de r: '))
DDPAD_R = float(input('Indique o DPAD de r: '))
p1 = float(input('Indique o valor de p1: '))
p2 = float(input('Indique o valor de p2: '))
p3 = float(input('Indique o valor de p3: '))
LT = 1*p1 + 2*p2 + 3*p3
C1=0.345
C3=1500
DPAD_LT_SQUARE = (1-LT)**2 * p1 + (2-LT)**2 * p2 + (3-LT)**2 * p3
M_DDPP = r*(t+LT)
DPAD_DDPP = math.sqrt((t+LT)*DDPAD_R**2 + r**2*DPAD_LT_SQUARE)

def calculateZ(n):
    return (3*n)/100

Z = calculateZ(58)

def calculateS(z,M_DDPP,DPAD_DDPP):
    return rhafz(M_DDPP + z*DPAD_DDPP)

S = calculateS(Z,M_DDPP,DPAD_DDPP)

sndInt = float(input(f'Indique o valor do 2o integral correspondente ao N {N}: '))

def calculateE(sndInt,DPAD_DDPP):
    return sndInt * DPAD_DDPP

E = calculateE(sndInt,DPAD_DDPP)

def calculates(S,r,C1,C3,t):
    return S - math.sqrt((2*r*C3)/C1) + (r*t)/2

s = calculates(S,r,C1,C3,t)

print(f's: {s}')
print(f'S: {S}')
print(f'E: {E}')