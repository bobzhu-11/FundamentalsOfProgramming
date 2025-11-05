"""
Beim Spiel Tic Tac Toe spielen zwei Spieler:innen abwechselnd auf einem 3x3 Feld
gegeneinander. Wir legen fest, dass Spieler:in 1 das Zeichen x setzt und Spieler:in 2
das Zeichen o. In der Aufgabe wollen wir uns darauf fokussieren, falsche Eingaben zu
behandeln und das Programm auf einzelne Funktionen zu reduzieren. Wir wollen
das Spielfeld als eine Liste von 3 Listen der Länge 3 angeben. Wir können das
Spielfeld mit spielfeld = [3*[None] for i in range(3)] initialisieren. (Wer
möchte kann auch Namen einlesen, aber das muss nicht sein.)
"""
Board = list[list[str]]


def q_none_to_str(x: str) -> str:
    return " " if x is None else x
"""
(a) Schreiben Sie eine Funktion placeSign(<spieler>,<spielfeld>). Diese
bekommt das aktuelle Spielfeld übergeben und die Information, welche:r Spieler:in
an der Reihe ist. Die Rückgabe ist das aktualisierte Spielfeld. Dabei soll die
Position mit input eingelesen werden. Die Position ist ein Tupel mit einer
Koordinate im Spielfeld zwischen (0,0) und (2,2). Behandeln Sie dabei die
möglichen Fehler (Position außerhalb des Spielfelds, Position bereits besetzt)
sinnvoll mittels try-except und if-else.
"""
def placeSign(spieler: str, spielfeld: Board) -> Board:

    while True:
        try:
            inp = input(f"Spieler {spieler}, Position eingeben (z.B. 0 2 oder (0,2)): ")
            r, c = parse_position(inp)
            if not in_bounds(r, c):
                print("Position außerhalb des Spielfelds! Erlaubt: (0..2, 0..2).")
                continue
            if spielfeld[r][c] is not None:
                print("Diese Position ist bereits besetzt.")
                continue
            # 放置
            spielfeld[r][c] = spieler
            return spielfeld
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}")
        except Exception:
            print("Eingabe konnte nicht verarbeitet werden. Bitte erneut versuchen.")


"""
(b) Schreiben Sie eine Funktion buildLine(<reihe>), die einen String zurückgibt.
Dieser soll die Zeichen der Reihe (Liste in der Liste) durch | getrennt hintereinander
setzen. Bedenken Sie, dass Sie None behandeln müssen.
"""

def buildLine(reihe: list[str]) -> str:
    return "|".join(q_none_to_str(ch) for ch in reihe)
"""
(c) Schreiben Sie eine Methode printBoard(<spielfeld>), die das Spielfeld ausgibt.
Diese soll das gesamte Spielfeld darstellen. Nutzen Sie dafür auch Ihre
buildLine Funktion.
Beispiel:
printBoard([['o','x',None][None,'o',None][None,None,'x']]) ⇒
o|x|
|o|
| |x
"""

def printBoard(spielfeld: Board) -> None:

    for r in range(3):
        print(buildLine(spielfeld[r]))
def parse_position(inp: str) -> tuple[int, int]:

    s = inp.strip()
    s = s.replace("(", "").replace(")", "")
    s = s.replace(",", " ")
    parts = [p for p in s.split() if p]
    if len(parts) != 2:
        raise ValueError("Bitte genau zwei Zahlen angeben.")
    r, c = int(parts[0]), int(parts[1])
    return r, c


def in_bounds(r: int, c: int) -> bool:
    return 0 <= r <= 2 and 0 <= c <= 2


def board_full(spielfeld: Board) -> bool:
    return all(cell is not None for row in spielfeld for cell in row)

"""
(d) Schreiben Sie eine Funktion checkWin(<spielfeld>). Diese bekommt das
Spielfeld übergeben und soll ein Tupel (True,<spieler>) oder (False,None)
zurückgeben. Das Tupel gibt True und den/die gewinnende:n Spieler:in zurück,
wenn eine Person eine Reihe/Spalte/Diagonale vervollständigt hat. Sie können
hier auch weitere Hilfsfunktionen für Reihen/Spalten/Diagonalen schreiben,
wenn Sie möchten.
"""

def checkWin(spielfeld: Board) -> tuple[bool, [str]]:

    lines = []

    lines.extend(spielfeld)

    cols = [[spielfeld[r][c] for r in range(3)] for c in range(3)]
    lines.extend(cols)

    diag1 = [spielfeld[i][i] for i in range(3)]
    diag2 = [spielfeld[i][2 - i] for i in range(3)]
    lines.extend([diag1, diag2])

    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return True, line[0]

    return False, None

"""
(e) Schreiben Sie eine Methode ticTacToe(), die unter Verwendung der Subroutinen
aus (a)-(d), zwei Spieler:innen ein Tic Tac Toe Spiel spielen lässt.
"""
def ticTacToe() -> None:

    spielfeld: Board = [[None for _ in range(3)] for _ in range(3)]
    aktueller_spieler = "x"  # Spieler:in 1

    while True:
        print("\nAktuelles Spielfeld:")
        printBoard(spielfeld)

        placeSign(aktueller_spieler, spielfeld)

        gewonnen, sieger = checkWin(spielfeld)
        if gewonnen:
            print("\nEndstand:")
            printBoard(spielfeld)
            print(f"\nSpielende! Gewinner: {sieger}")
            break

        if board_full(spielfeld):
            print("\nEndstand:")
            printBoard(spielfeld)
            print("\nUnentschieden!")
            break

        aktueller_spieler = "o" if aktueller_spieler == "x" else "x"


if __name__ == "__main__":
    ticTacToe()