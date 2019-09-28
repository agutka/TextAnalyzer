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

while True:
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

    try:
        option = int(input())
    except:
        print('Musisz podać liczbę!')

    if option == 1:
        print('Download file')
        download_file()

    elif option == 2:
        print('Count letters')
        count_letter()

    elif option == 3:
        print('Count words')
        count_words()

    elif option == 4:
        print('Count punctuation marks')
        count_punctuation_marks()

    elif option == 5:
        print('Count sentences')
        count_sentences()

    elif option == 6:
        print('Generate report of letters usage')
        generate_report_of_letters_usage()

    elif option == 7:
        print('Save statistics to file')
        save_statistics_to_file()

    elif option == 8:
        print('Koniec programu')
        break

    else:
        print('Nie ma takiej opcji!')
