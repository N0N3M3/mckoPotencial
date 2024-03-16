def main():
    """
    Функция считывает данные из files/books.csv и выводит
    10 авторов с самым большим средним рейтингом
    """
    with open("files/books.csv", encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    authors_raw = {}
    for line in lines[1:]:
        data = line.split(";")
        el = authors_raw.get(data[2], [])
        el.append(float(data[-1].replace(',', '.')))
        authors_raw[data[2]] = el
    authors = {}  # хэш-таблица
    for author, val in authors_raw.items():
        authors[author] = sum(val) / len(val)
    authors_tuples = [(a, v) for a, v in authors.items()]
    authors_tuples.sort(key=lambda el: el[1], reverse=True)
    for a, _ in authors_tuples[:10]:
        print(f"Автор: {a}, Средний рейтинг: {authors[a]}")


if __name__ == "__main__":
    main()
