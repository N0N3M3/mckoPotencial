def get_rating(book_rating):
    """
    Функция для определения ярлыка для системы рекомендаций
    :param book_rating: рейтинг книги
    :return: ярлык для системы рекомендаций
    """
    if book_rating < 5:
        return "не рекомендовать"
    elif 5 <= book_rating < 8:
        return "рекомендовать после"
    elif book_rating >= 8:
        return "рекомендовать в первую очередь"


def main():
    """
    Фукция считывает со стандартного ввода название csv файла и записывает данные с ярлыком рекомендаций
    в файл books_grade.csv
    """
    csv_file = input("Введите название csv файла: ")
    with open(csv_file, encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    with open("books_grade.csv", "w", encoding='utf-8') as f:
        f.write(lines[0] + "\n")
        for line in lines[1:]:
            data = line.split(";")
            rating = get_rating(float(data[5].replace(',', '.')))
            f.write(f"{line};{rating}\n")


if __name__ == "__main__":
    main()
