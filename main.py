import requests
from collections import Counter


class TextAnalyzer:

    text_to_analyze = ''

    def download_file(self):

        url = 'https://s3.zylowski.net/public/input/1.txt'
        response = requests.get(url)

        with open('./file.txt', 'wb') as file:
            file.write(response.content)

        return response.content

    def count_letter(self):
        pass

    def count_words(self):
        pass

    def count_punctuation_marks(self):
        pass

    def count_sentences(self):
        pass

    def generate_report_of_letters_usage(self):
        pass

    def save_statistics_to_file(self):
        pass


def main_loop():
    ta = TextAnalyzer()

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

        option = input()

        if option == '1':
            print('Download file')
            ta.text_to_analyze = ta.download_file()

        elif option == '2':
            print('Count letters')
            ta.count_letter()

        elif option == '3':
            print('Count words')
            ta.count_words()

        elif option == '4':
            print('Count punctuation marks')
            ta.count_punctuation_marks()

        elif option == '5':
            print('Count sentences')
            ta.count_sentences()

        elif option == '6':
            print('Generate report of letters usage')
            ta.generate_report_of_letters_usage()

        elif option == '7':
            print('Save statistics to file')
            ta.save_statistics_to_file()

        elif option == '8':
            print('Koniec programu')
            break

        else:
            print('Nie ma takiej opcji!')


if __name__ == '__main__':
    main_loop()
