#Proyecto de frecuencia cardiaca
#En el código que pongamos vamos hacer que depende de las bpm que tengas diga si es alta, media, baja
bpm = int(input("Introduce el nº de bpm en reposo: "))
m_alto = 180
alto = 110
medio = 85
normal = 60
bajo = 50

if bpm >= m_alto:
    print("Muy alto")
elif bpm >= alto:
    print("Alto")
elif bpm >= medio:
    print("Medianamente alto")
elif bpm >= normal:
    print("Normal")
elif bpm >= bajo:
    print("Bajo")
else:
    print("Muy bajo")
