media = int(input("inserire la media: "))
reddito  = int(input("inserire il reddito: "))

match media:
    case _ if media >= 27:
        match reddito:
            case _ if reddito < 20000:
                print("borsa di studio assegnata")

            case _:
                print("borsa di studio non assegnata, media insufficente e/o reddito elevato")


