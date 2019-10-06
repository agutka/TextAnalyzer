import requests
import os

class TextAnalyzer:
    text_to_analyze = None
    pathToFile = './file.txt'

    def download_file(self):
        url = 'https://s3.zylowski.net/public/input/1.txt'
        response = requests.get(url)

        with open('./file.txt', 'wb') as file:
            file.write(response.content)

        file.close()

        with open('file.txt', 'r') as file:
            file_string = file.read()

        return file_string

    def count_letter(self):
        return len(self.text_to_analyze)

    def count_words(self):
        return len(self.text_to_analyze.split())

    def count_punctuation_marks(self):
        if self.text_to_analyze is None:
            return None

        punctuation_marks = [",", ".", "!", ":", ";", "?", "-"]

        number_of_punctuation_marks = 0

        for punctuation_mark in punctuation_marks:
            number_of_punctuation_marks += self.text_to_analyze.count(punctuation_mark)

        return number_of_punctuation_marks

    def count_sentences(self):
        if self.text_to_analyze is None:
            return None
        else:

            number_of_sentences = 0

            for i in range(0, len(self.text_to_analyze)):

                if self.text_to_analyze[i] == '.' or self.text_to_analyze[i] == '!' or self.text_to_analyze[i] == '?':

                    if self.text_to_analyze[i + 1] != '.' and self.text_to_analyze[i + 1] != '!' and self.text_to_analyze[i + 1] != '?':
                        number_of_sentences += 1

            return number_of_sentences

    def generate_report_of_letters_usage(self):
        if self.text_to_analyze is None:
            return None

        else:
            number_of_every_letters = {}

            # great letters A-Z -> dec 65-90
            for ascii_code in range(65, 91):
                number_of_every_letters[chr(ascii_code)] = self.text_to_analyze.count(chr(ascii_code))

            # little letters a-z -> dec 97-122
            for ascii_code in range(97, 123):
                number_of_every_letters[chr(ascii_code)] = self.text_to_analyze.count(chr(ascii_code))

            return number_of_every_letters

    def save_statistics_to_file(self):
        pass

    def exiting_program(self):
        if os.path.isfile('statistics.txt'):
            os.unlink('statistics.txt')

        if os.path.isfile(self.pathToFile):
            os.unlink(self.pathToFile)
        else:
            print("Wybacz, plik nie istnieje.")


def main_loop():
    ta = TextAnalyzer()
    ta.text_to_analyze = ta.download_file()

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
            print(ta.count_letter())

        elif option == '3':
            print('Count words')

            if os.path.isfile(TextAnalyzer.pathToFile):
                print(ta.count_words())
            else:
                print("Błąd! Brak pobranego pliku!")

        elif option == '4':
            print('Count punctuation marks')
            counted_punctuations = ta.count_punctuation_marks()
            if counted_punctuations is None:
                print("Błąd! Brak pobranego pliku")
            else:
                print (counted_punctuations)

        elif option == '5':
            print('Count sentences')
            counted_sentences = ta.count_sentences()
            if counted_sentences is None:
                print("Błąd! Brak pobranego pliku")
            else:
                print(counted_sentences)

        elif option == '6':
            print('Generate report of letters usage')
            counted_letters = ta.generate_report_of_letters_usage()
            if counted_letters is None:
                print("Błąd! Brak pobranego pliku!")
            else:
                for letter in counted_letters:
                    print(letter + ': ' + str(counted_letters[letter]))

        elif option == '7':
            print('Save statistics to file')
            ta.save_statistics_to_file()

        elif option == '8':
            ta.exiting_program()
            print('Koniec programu')
            break

        else:
            print('Nie ma takiej opcji!')


if __name__ == '__main__':
    main_loop()