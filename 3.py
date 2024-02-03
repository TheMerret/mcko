import csv


def main():
    """
    выводи игры с участием персонажа
    :return:
    """
    # читаем файл
    with open("game.txt", "r", encoding="utf8") as fd:
        reader = csv.DictReader(fd, delimiter='$')
        next(reader)
        reader = list(reader)
    # сортируем
    reader.sort(key=lambda x: x["characters"])
    while True:
        req = input()
        if req == "game":
            break
        character = req
        # lower bound
        l = 0
        r = len(reader)
        while l < r:
            m = (l + r) // 2
            if reader[m]['characters'] < character:
                l = m + 1
            else:
                r = m
        lower = l
        # upper bound
        l = 0
        r = len(reader)
        while l < r:
            m = (l + r) // 2
            if reader[m]['characters'] > character:
                r = m
            else:
                l = m + 1
        upper = l
        games = reader[lower:upper]
        # обрабатываем найденное
        if games:
            titles = [i["GameName"] for i in games]
            print(f"Персонаж {character} встречается в играх:")
            print(*titles[:5], sep="\n")
            if len(titles) > 5:
                print("и др.")
        else:
            print("Этого персонажа не существует")


if __name__ == '__main__':
    main()
