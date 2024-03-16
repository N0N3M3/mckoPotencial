def main():
    """
    Функция считывает данные из books.csv,записывает необходимые книги в books_rowling.csv и
    выводит книги с рейтингом >8
    """
    with open("files/books.csv", encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    rouling_books = []
    for line in lines[1:]:
        data = line.split(";")
        if "Дж.К. Роулинг" in data[2]:
            rouling_books.append(data)
    with open("books_rowling.csv", "w") as f:
        f.write("book_id;authors;original_title;ratings_1\n")
        for book in rouling_books:
            f.write(f"{book[0]};{book[2]};{book[4]};{book[5]}\n")
            if float(book[-1].replace(',', '.')) > 8:
                print(f"{book[2]} - {book[4]}\t {book[-1]}")


if __name__ == "__main__":
    main()
