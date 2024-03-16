def main():
    """
    Функция считывает данные из books_rowling.csv и выводит
    ответ в соответвии с условием
    """
    with open("files/books_rowling.csv", encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    for line in lines[1:]:
        data = line.split(";")
        if float(data[-1].replace(',', '.')) > 8:
            print(f"{data[1]} - {data[2]}\t {data[-1]}")


if __name__ == "__main__":
    main()
