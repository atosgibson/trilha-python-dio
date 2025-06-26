# Simulação do comportamento vertical do atum amarelo (Thunnus albacares)
# no Atlântico Tropical ao longo de 24h

print("Simulação diária do comportamento vertical do atum amarelo (Albacora-laje)\n")

# Laço de 0 a 23 horas (um ciclo completo de 24h)
for hora in range(24):
    if 6 <= hora < 18:
        # Durante o dia (06:00 às 17:59), ele está em águas profundas
        profundidade = 60  # metros
        zona = "profunda"
        comportamento = "descanso e termorregulação"
    else:
        # Durante a noite (18:00 às 05:59), ele sobe para superfície
        profundidade = 15  # metros
        zona = "superficial"
        comportamento = "alimentação ativa"

    # Formatação da hora
    hora_formatada = f"{hora:02d}:00"

    print(f"Horário: {hora_formatada} | Profundidade: {profundidade} m | Zona: {zona} | Atividade: {comportamento}")

# Fim da simulação
print("\n* Padrão observado com base em estudos de comportamento diurno-noturno do YFT no Atlântico Tropical.")
