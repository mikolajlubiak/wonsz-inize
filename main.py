### ZAMIANA NORMALNEJ
### MOWY NA MOWĘ
### WYZNAWCÓW MEGAWONSZ9

from sys import argv

alfabet: str = {"a": "ą", "A": "Ą", "c": "ć", "C": "Ć", "e": "ę", "E": "Ę", "i": "j", "I": "J", "j": "i", "J": "I", "l": "ł", "L": "Ł", "n": "ń", "N": "Ń", "s": "ś", "S": "Ś", "o": "ó", "w": "f", "W": "F", "f": "w", "F": "W", "z": "ź", "Z": "Ź", "ż": "ź", "Ż": "Ź", "ź": "ż", "Ź": "Ż"}
def wonsz_inize(text: str) -> str:
    return text.translate(text.maketrans(alfabet))

if __name__ == "__main__":
    try:
        text=argv[1]
    except IndexError:
        text=input("Podaj tekst do zwężowania: ")
    print(f"Zwężowany tekst:\n{wonsz_inize(text=text)}")
