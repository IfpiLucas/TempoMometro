def converter_minutos(hi, mi, hf, mf):
    if hi > 0 or hf > 0:
        hi *= 60
        hf *= 60

    hi += mi
    hf += mf
    tpma = max(hi, hf)
    tpmi = min(hi, hf)
    print("Valor de hi = {} hf = {} tpmax = {} tpmin = {}".format(hi, hf, tpma, tpmi))
    return(tpma, tpmi)

def tempo(tmax, tmin):
    hora = 0
    minuto = 0
    tmax -= tmin
    if tmax > 59:
        hora = tmax//60
        print("Tempo dividido ", hora)
        if tmax%60 != 0:
            minuto = tmax%60
            print('Resto do tempo', minuto)
    return (hora, minuto)

