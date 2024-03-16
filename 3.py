def search(lines, target_book):
    """
    Функция ищет книгу по заданному названию среди всего списка книг
    используя линейный поиск.
    :param lines: список книг
    :param target_book: нужная книга
    :return: список книг с нужным названием
    """
    results = []
    for line in lines:
        data = line.split(";")
        if data[4] == target_book:
            results.append(data)
    return results


def main():
    """
    Функция спрашивает у пользователя название книги и выдает информацию о ней используя
    информацию из файла book.csv

    Согласно условию нужно было читать данные из books.txt, однако
    эксперты сказали использовать book.csv. Поэтому используется он.
    """
    with open("files/books.csv", encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    a = input()
    while a != "хватит":
        results = search(lines[1:], a)
        if results:
            for res in results[:5]:
                print(f"{res[4]} - {res[1]} - {res[0]} - {res[-1]}")
            if len(results) > 5:
                print("и др.")
        else:
            print("Данной книги в этой библиотеке нет")
        a = input()


if __name__ == "__main__":
    main()
