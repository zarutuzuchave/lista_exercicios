def converter_tempo(segundos):

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    print(f"horas:{horas}")
    print(f"minutos:{minutos}")
    print(f"segundos:{segundos_restantes}")

tempo = int(input("Digite o tempo em segundos: "))
converter_tempo(tempo)
