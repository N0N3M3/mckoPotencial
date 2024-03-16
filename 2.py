import dataclasses
import random
from dataclasses import dataclass


@dataclasses.dataclass
class Data:
    all_data: list[str]
    rating: float


def quick_sort(a):
    """
    Данная функция сортирует массив используя алгоритм quick sort
    со средней сложностью O(n logn)
    :param a: массив с элементами класса Data
    :return:
    """
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)]
        low = [u for u in a if u.rating < x.rating]
        eq = [u for u in a if u.rating == x.rating]
        hi = [u for u in a if u.rating > x.rating]
        a = quick_sort(low) + eq + quick_sort(hi)

    return a


def main():
    """
    Функция считывает данные из books.csv и выводит
    3 худшие книги
    """
    with open("files/books.csv", encoding="utf-8") as f:
        lines = list(map(str.strip, f.readlines()))
    datas = []
    for line in lines[1:]:
        data = line.split(";")
        datas.append(Data(
            all_data=data,
            rating=float(data[-1].replace(',', '.'))
        ))
    sorted_data = quick_sort(datas)
    for i in sorted_data[:3]:
        print(f"{i.all_data[-2]} - {i.all_data[2]} - {i.all_data[-1]}")


if __name__ == "__main__":
    main()
