import os
import platform
from dataclasses import dataclass, field

class ConsoleRenderer:
    GALLOWS = [
        """




        =========
        """,
        """

          |
          |
          |
          |
        =========
        """,
        """
         +---.
          |
          |
          |
          |
        =========
        """,
        """
         +---.
         |   |
          |
          |
          |
        =========
        """,
        """
         +---.
         |   |
         O   |
          |
          |
        =========
        """,
        """
         +---.
         |   |
         O   |
         |   |
          |
        =========
        """,
        """
         +---.
         |   |
         O   |
        /|   |
          |
        =========
        """,
        """
         +---.
         |   |
         O   |
        /|\\  |
          |
        =========
        """,
        """
         +---.
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
         +---.
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """,
        """
         +---.
         |   |
        [O]  |
        /|\\  |
        / \\  |
        =========
        """,
    ]

    def masked_word(self, secret: str, discovered: set[str]) -> str:
        output_word = []
        for ch in secret:
            if ch in discovered:
                output_word.append(ch)
            else:
                output_word.append("_")
        return " ".join(output_word)

    def render(self, game: "HangmanGame"):
        print("=== Galgenmännchen ===\n")
        print(f"Spieler: {game.p1.name} vs. {game.p2.name}")
        print(f"Fehlversuche: {game.wrong_count}/{game.max_wrong}\n")
        print(self.GALLOWS[min(game.wrong_count, game.max_wrong)])
        print("Aktueller Stand:", self.masked_word(game.secret, game.discovered))
        if game.guessed:
            print("Bereits geraten:", ", ".join(sorted(game.guessed)))
        print()

    def show_hit(self, letter: str, positions: list[int]):
        print(f"Treffer: '{letter}' an Position(en) {positions}.\n")

    def show_miss(self, letter: str, wrong_count: int, max_wrong: int):
        print(f"Falsch: '{letter}'. Fehlversuche {wrong_count}/{max_wrong}.\n")

    def show_repeat(self, letter: str):
        print(f"Bereits geraten: '{letter}'. Kein Abzug.\n")

    def show_invalid(self):
        print("Bitte genau EINEN Buchstaben (A–Z) eingeben.\n")

    def show_win(self, winner: str, secret: str):
        print(f"Glückwunsch, {winner}! Gelöst: {secret.upper()}")

    def show_lose(self, secret: str):
        print(f"Verloren! Das Wort war: {secret.upper()}")


@dataclass
class Player:
    name: str

@dataclass
class HangmanGame:
    p1: Player
    p2: Player
    secret: str
    max_wrong: int = 10
    discovered: set = field(default_factory=set)
    guessed: set = field(default_factory=set)
    wrong_count: int = 0

    @staticmethod
    def normalize_word(word: str) -> str:
        return word.strip().lower()

    @classmethod
    def from_inputs(cls):
        p1 = Player(input("Name Spieler1: ").strip() or "Spieler1")
        p2 = Player(input("Name Spieler2: ").strip() or "Spieler2")

        while True:
            raw = input(f"{p1.name},geheimes Wort (nur Buchstaben): ").strip()
            if raw.isalpha():
                secret = cls.normalize_word(raw)
                break
            print("Ungültig: Nur Buchstaben (A–Z).")
        return cls(p1=p1, p2=p2, secret=secret)

    def positions_of(self, ch: str) -> list[int]:
        result = []
        for i, c in enumerate(self.guessed):
            if c == ch:
                result.append(i + 1)
        return result

    def is_won(self) -> bool:
        for ch in self.secret:
            if ch not in self.discovered:
                return False
        else:
            return True


    def is_lost(self) -> bool:
        return self.wrong_count >= self.max_wrong

    def guess(self, raw_input: str):
        s = raw_input.strip().lower()
        if len(s) != 1 or not s.isalpha():
            return "invalid", None
        if s in self.guessed:
            return "repeat", s

        self.guessed.add(s)
        if s in self.secret:
            self.discovered.add(s)
            return "hit", self.positions_of(s)
        else:
            self.wrong_count += 1
            return "miss", s


class HangmanController:
    def __init__(self, game: HangmanGame, renderer: ConsoleRenderer):
        self.game = game
        self.view = renderer

    def run(self):
        print(f"{self.game.p2.name}, das geheime Wort hat {len(self.game.secret)} Buchstaben.\n")
        input("Drücke Enter, um zu starten …")

        while True:
            self.view.render(self.game)

            if self.game.is_won():
                self.view.show_win(self.game.p2.name, self.game.secret)
                break
            if self.game.is_lost():
                self.view.show_lose(self.game.secret)
                break

            guess = input(f"{self.game.p2.name}, gib einen Buchstaben ein: ")
            status, info = self.game.guess(guess)

            if status == "invalid":
                self.view.show_invalid()
                continue
            if status == "repeat":
                self.view.show_repeat(info)
                continue
            if status == "hit":
                self.view.show_hit(guess.strip().lower(), info)
            elif status == "miss":
                self.view.show_miss(info, self.game.wrong_count, self.game.max_wrong)


def main():
    game = HangmanGame.from_inputs()
    renderer = ConsoleRenderer()
    HangmanController(game, renderer).run()


if __name__ == "__main__":
    main()
