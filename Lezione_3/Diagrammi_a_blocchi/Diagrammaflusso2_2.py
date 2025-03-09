soglia = 70
nord_sud = int(input("Inserire numero macchine direzione NS: "))
est_ovest = int(input("Inserire numero macchine direzione EO: "))

# Logica di controllo
if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    totale = nord_sud + est_ovest
    if totale == 0:  # Evita la divisione per zero
        time_ns = 50
        time_eo = 50
    else:
        time_ns = (nord_sud / totale) * 100
        time_eo = (est_ovest / totale) * 100

# Stampa dei risultati
print(f"Il tempo per il semaforo nord_sud è: {time_ns}")
print(f"Il tempo per il semaforo est_ovest è: {time_eo}")