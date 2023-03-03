from time import localtime
from time import sleep
from pygame import mixer


first_hour = int(input('\nDigite a hora do primeiro alarme: '))
first_min = int(input('\nDigite o minuto do primeiro alarme: '))

primeiro_remedio = str(input('\nDigite remédio que será colocado: '))

hora_despertar = first_hour
minuto_despertar = first_min

remedio_da_vez = primeiro_remedio


def tocar_musica():
    mixer.init()
    mixer.music.load("despertador.mp3")
    mixer.music.play()


def mensagem_remedio_colorida():
    cores = {"Verde": 32, "Amarelo": 33, "Azul": 34}
    codigo_cor = cores[remedio_da_vez]
    print(f'\n \033[{codigo_cor}m -:---:---:---:---:---:---:---{remedio_da_vez}---:---:---:---:---:---:---:-\033[m')


while localtime().tm_hour != 00:
    if localtime().tm_hour == hora_despertar and localtime().tm_min == minuto_despertar:

        mensagem_remedio_colorida()

        remedios = {"Verde": 0, "Amarelo": 1, "Azul": 2}
        nomes_remedio = ["Verde", "Amarelo", "Azul"]

        codigo_do_remedio_da_vez = remedios[remedio_da_vez]

        tocar_musica()

        # considerando que não haverá mudança na ordem do remédio

        if codigo_do_remedio_da_vez < 2:
            sleep(599)
        else:
            sleep(1799)

        hora_despertar = localtime().tm_hour
        minuto_despertar = localtime().tm_min

        if codigo_do_remedio_da_vez < 2:
            codigo_do_remedio_da_vez = codigo_do_remedio_da_vez + 1
        else:
            codigo_do_remedio_da_vez = 0

        remedio_da_vez = nomes_remedio[codigo_do_remedio_da_vez]

    else:
        continue

