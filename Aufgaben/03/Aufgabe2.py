"""
(a) Warm-up: Schreiben Sie eine Funktion qSumme(<zahl>), die die Quersumme
einer eingegebenen Zahl berechnet (ohne die Zahl in eine Liste oder einen
String zu konvertieren). Nutzen Sie dafür ganzzahlige Teilung und modulo.
"""
def qSumme(zahl:int) -> int:
    summe = 0
    while (zahl / 10 > 0):
        summe += zahl % 10
        zahl //= 10
    return summe
"""
(b) Bei der Caesarverschlüsselung einigen die kommunizierenden Personen sich
auf einen Zahlschlüssel n. Wenn eine der Personen einen Text verschlüsselt,
ersetzt sie jeden Buchstaben ihres Textes mit dem Buchstaben im Alphabet,
der n Positionen nach diesem im Alphabet erscheint. Wenn man während der
Verschiebung bei ’Z’ ankommt, wird an Position ’A’ fortgefahren (Nutzen Sie
modulo und ord.). Beachten Sie auch die Behandlung von Zahlen, Sonderzeichen
und Leerzeichen.
(i) Schreiben Sie eine Funktion encrypt(n,<text>), die einen Text bei Eingabe
des Textes und des Schlüssels verschlüsselt und zurückgibt.
"""
def encrypt(n: int, text: str) -> str:
    encrypted_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            new_ord = (ord(char) - start + n) % 26 + start
            encrypted_text += chr(new_ord)
        elif 'a' <= char <= 'z':
            start = ord('a')
            new_ord = (ord(char) - start + n) % 26 + start
            encrypted_text += chr(new_ord)
        else:
            encrypted_text += char
    return encrypted_text
"""
(ii) Schreiben Sie eine Funktion decrypt(n,<text>), die einen verschlüsselten
Text und den Schlüssel als Eingabe erhält, und den Text entschlüsselt und
zurückgibt.
"""
def decrypt(n:int, text:str) -> str:
    decrypted_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            new_ord = (ord(char) - start - n) % 26 + start
            decrypted_text += chr(new_ord)
        elif 'a' <= char <= 'z':
            start = ord('a')
            new_ord = (ord(char) - start - n) % 26 + start
            decrypted_text += chr(new_ord)
        else:
            decrypted_text += char
    return decrypted_text
"""
(c) Schreiben Sie eine Funktion dictEncrypt(<wörterbuch>,<text>), welche ein
Wörterbuch und einen Text als Eingabe bekommt. Die Ausgabe ist ein Text,
der die Zeichen durch den Wert ersetzt, der dem entsprechenden Schlüssel im
Wörterbuch zugeordnet ist.
"""
def dictEncrypt(dictionary:dict[str,str],text:str) -> str:
    encrypted = ""
    for t in text:
        if t in dictionary:
            encrypted += dictionary[t]
        else:
            encrypted += t
    return encrypted

"""
(d) Schreiben Sie eine Funktion decryptDict(<wörterbuch>), die als Eingabe
ein Wörterbuch bekommt und das zugehörige Wörterbuch zur Entschlüsselung
ausgibt.
"""
def decryptDict(dictionary: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for k, v in dictionary.items():
        inverted[v] = k
    return inverted
"""
(e) Wir gehen davon aus, dass unsere Verschlüsselung eindeutig ist, so dass eine
Entschlüsselung auch möglich ist. Überlegen Sie sich ein Kriterium, das eine
eindeutige Verschlüsselung ermöglicht und beschreiben Sie Ihre Idee in einem
Satz.
"""
# Jedes Zeichen muss eindeutig auf ein anderes Zeichen abgebildet werden, sodass die Zuordnung bijektiv ist.

if __name__ == '__main__':
    print(qSumme(2345))
    print(encrypt(3,"Hello World"))
    print(decrypt(3,"Khoor Zruog"))
    my_dict = {'a': 'x', 'b': 'y'}
    print(dictEncrypt(my_dict, "ab"))
    print(decryptDict(my_dict))