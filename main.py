def download_file():
    pass


def count_letter():
    pass


def count_words():
    pass


def count_punctuation_marks():
    pass


def count_sentences():
    pass


def generate_report_of_letters_usage():
    pass


def save_statistics_to_file():
    pass


option = ''

while option != 8:
    print("""
Analizator tekstu
    
Menu:
    1. Pobierz plik z internetu
    2. Zlicz liczbę liter w pobranym pliku
    3. Zlicz liczbę wyrazów w pliku
    4. Zlicz liczbę znaków interpunkcyjnych w pliku.
    5. Zlicz liczbę zdań w pliku
    6. Wygeneruj raport o użyciu liter (A-Z)
    7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt
    8. Wyjście z programu
    
Podaj numer opcji: """)

    option = input()
