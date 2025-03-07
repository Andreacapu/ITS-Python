liberi = 20  #inizializzazionecon numeri posti disponibili

while True:
    opzione = input("Inserisci opzione: ")  #inizializzazione match statement
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
                print("Posto prenotato. Posti liberi rimanenti:", liberi)
            else:
                print("Non ci sono posti disponibili")
        case "libera":
            if liberi < 20:
                liberi += 1
                print("Posto liberato. Posti liberi disponibili:", liberi)
            else:
                print("Tutti i posti sono già liberi")
        case "visualizza":
            print("Posti liberi:", liberi)
            occupati = 20 - liberi
            print("Posti occupati:", occupati)
        case "esci":
            print("Uscita dal programma.")
            break
        case _:
            print("Opzione non valida. Riprova.")