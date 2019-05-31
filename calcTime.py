from tempo import *

while True:
    hi = int(input('Hora de inicio: '))
    mi = int(input('Minuto: '))
    hf = int(input('Hora final:'))
    mf = int(input('Minuto: '))

    tmax, tmin = converter_minutos(hi, mi, hf, mf)

    hora, minuto = tempo(tmax, tmin)
    print(hora,":",minuto)

    cont = input('Continuar? (S/N) ').lower()
    if cont == 'n':
        break
