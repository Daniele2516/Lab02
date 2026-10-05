def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    album = {}
    try:
        with open(file_path, "r") as file_album:
            linee = file_album.readlines()
            for line in linee[1:]:
                line = line.strip()
                if not line:
                    continue
                parti = line.split(",")
                if len(parti) == 5:
                    codice = parti[0]
                    titolo = parti[1]
                    autore = parti[2]
                    mese = int(parti[3])
                    anno = int(parti[4])
                # aggiunge l'anno se non esiste
                    if anno not in album:
                        album[anno] = []
                    album[anno].append([codice, titolo, autore, mese, anno])
        return album
    except FileNotFoundError:
        print("None")


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    if not (1 <= mese <= 12):
        return None

    for y in album:
        for foto in album[y]:
            if foto[0] == codice:
                return None
    # devo aprire il file in modo che prima lo leggo e leggo tutte le righe, poi lo apro in modo che posso scriverci e modificarlo.
    try:
        with open(file_path, "r") as f:
            righe = f.readlines()

        with open(file_path, "w") as f:
            for riga in righe: #scrive un file nuovo, e ci riscrive tutte le righe del file che abbiamo"
                f.write(riga)                                       #--> print(riga, end="", file=f)
            f.write(f"{codice},{titolo},{autore},{mese},{anno}\n") # si poteva scrivere tutto in modo diverso --> print (f"{codice},{titolo},{autore},{mese},{anno}", file=f)
    except FileNotFoundError:
        return None


def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    for anno in album:
        for foto in album[anno]:
            if foto[0] == codice:
                return f"{foto[0]},{foto[1]},{foto[2]},{foto[3]},{foto[4]}"
    return None


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    if anno not in album:
        return None
    titoli = []
    for foto in album[anno]:
        titoli.append(foto[1])
    titoli.sort()
    return titoli



def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
