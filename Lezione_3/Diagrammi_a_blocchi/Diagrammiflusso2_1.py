max_posti = ()
liberi = 0
while True:
    opzione = input("digitare l'opzione: ")
    match opzione:
        case "ingresso":
           if liberi > 0:
                liberi -= 1
                print("Posto prenotato. Posti liberi rimanenti:", liberi) 
            else:
            print("non ci sono posti liberi")
        case "uscita":
          if liberi < 0:
             liberi += 1
             print("posto liberato")
          else:
             print("nessun posto occupato")
        case "stato":
          print

