import csv
from collections import defaultdict


def main():
    """
    считает баги по играм
    :return:
    """
    # читаем файл
    with open("game.txt", "r", encoding="utf8") as fd:
        r = csv.DictReader(fd, delimiter='$')
        next(r)
        r = list(r)
    # сортируем
    r.sort(key=lambda x: x["GameName"])
    bugs_count = defaultdict(int)
    # считаем баги
    for row in r:
        bugs_count[row["GameName"]] += 1
    # выводим отчет
    for k, v in bugs_count.items():
        print(k, '-', 'количество багов:', v)


if __name__ == '__main__':
    main()
