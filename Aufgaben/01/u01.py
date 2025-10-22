#region Aufgabe1
# a）
#     i,ii)
#         a = 8 + 10 (18)
#         3 + 5 * 7 == a - 2 -> 38==16(False)
#         Ausgabetyp:<bool>False
#
#     iii）
#         a = 40
#         3 + 5 * 7 == a - 2 -> 38==38(True)
#         Ausgabetyp:<bool>True
#
#     iv)
#     print("KDP", str(a * 50 + 2*10 + 4 - 1) + ".\n")
#         -> a=40, Ergebnis：2023
#         Ausgabetyp:<string>"KDP,2023
#         "
#
#     v）if a - 4 <= 5: ->36<=5(false)
#         print("Ja")
#         else:
#         print("Nein") -> output
#         Ausgabetyp:<string>"Nein"
# b)
# def mystery(s):
#     """A mysterious Python function."""
#     return s[::-1] == s
#
# print(mystery("anna")) #return "anna"=="anna" ->true
# print(mystery("banana"))#return "ananab"=="banana" ->false
# print(mystery("ananas"))#return "sanana"=="ananas" ->false
# print(mystery("kajak"))#return "kajak"=="kajak" ->true
# print(mystery("reittier"))#return "reittier"=="reittier" ->true
# print(mystery("ritter"))#return "rettir"=="ritter" ->false
#
# c)
# #Diese Funktion vergleicht, ob das Ergebnis der Umkehrung einer Zeichenfolge mit dem ursprünglichen Ergebnis identisch ist.

#endregion

#region Aufgabe2
# a)
# int ist eine ganze Zahl (z. B. 3, −5).
# float ist eine Kommazahl (z. B. 3.5, −2.1)
# b)
# Die Funktion int() schneidet die Nachkommastellen ab.
# Beispiel: int(3.9) → 3
# c)
# In Python haben int-Zahlen keine feste Größe.
# Sie können beliebig groß werden.
# In vielen anderen Sprachen (z. B. C, Java) haben int-Zahlen feste Bit-Größen (z. B. 32 Bit).
# d)
#bin(8) → '0b1000' (Binärdarstellung von 8).
#bin(8.1) gibt einen Fehler, weil bin() nur mit ganzen Zahlen funktioniert.
# e)
# ord('A') → 65, ord('a') → 97.
# ord() gibt den ASCII- oder Unicode-Wert eines Zeichens zurück.
# Beispiel-Anwendung: Buchstaben in Zahlen umwandeln (z. B. für Sortierung oder Kryptografie).
#endregion