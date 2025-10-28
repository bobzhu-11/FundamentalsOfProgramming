from rezeptListe import rezepte

# Datentyp: [(String,[(Int,String)])]
'''
(a)
 Schreiben Sie ein Programm, das eine Schleife nutzt, um aus der Liste alle
 Rezepte mit dem Rezeptstichwort fingerfood herauszusuchen und diese in
 einer Liste sammelt.
'''
def aufgabe_a(rezep: list[tuple[str, list[tuple[int, str]]]])->list[tuple[str, list[tuple[int, str]]]]:
    result = []
    # for Version
    # for rez in rezep:
    #     if rez[0] == "fingerfood":
    #         result.append(("fingerfood",rez[1]))
    i = 0
    while i < len(rezep):
        if rezep[i][0] == "fingerfood":
            result.append(rezep[i])
        i += 1
    return result

fingerfood = aufgabe_a(rezepte)
'''
(b) 
Schreiben Sie nun unter Nutzung von Schleifen einen Ablauf, der eine Liste
aller benötigten Zutaten erstellt (noch ohne Menge).
'''
def aufgabe_b(rezep: list[tuple[str, list[tuple[int, str]]]]) -> set[str]:
    # Weil Sets Duplikate automatisch entfernen können.
    result: set[str] = set()
    i = 0
    while i < len(rezep):
        zutaten_liste = rezep[i][1]
        j = 0
        while j < len(zutaten_liste):
            menge, zutat = zutaten_liste[j]
            result.add(zutat)
            j += 1
        i += 1
    return result
zutaten = aufgabe_b(fingerfood)
'''
(c) Nutzen Sie die Listen aus (a) und (b) um mit Schleifen, die Einkaufsliste mit
den aufsummierten Mengen zu erstellen (Liste aus Tupeln
(<Menge>,<Zutat>)). Es ist hilfreich, zuerst eine Einkaufsliste mit Menge 0
für jede Zutat zu initialisieren. Beachten Sie beim Aktualisieren der Mengen,
dass Tupel unveränderbar sind
'''
def aufgabe_c(rezep: list[tuple[str, list[tuple[int, str]]]],zutaten:set[str]) -> list[tuple[int,str]]:
    result: list[tuple[int,str]] = []
    for z in zutaten:
        result.append((0, z))

    for rezept in rezep:
        fingerfood_zutaten = rezept[1]
        for menge, zutat in fingerfood_zutaten:
            for i, (m, z) in enumerate(result):
                if z == zutat:
                    result[i] = (m + menge, z)
    return result

einkaufsliste = aufgabe_c(fingerfood,zutaten)
#TEST
def main():
    print(fingerfood)
    print(zutaten)
    print(einkaufsliste)

if __name__ == '__main__':
    main()