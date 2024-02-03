import csv

p = 341
m = int(1e9) + 7


def get_hash(s: str) -> int:
    """
    получить хэш
    :param s: строка
    :return: хэш
    """
    n = len(s)
    h = [0] * n
    h[0] = ord(s[0])
    power = 1
    for i in range(1, n):
        power *= p
        h[i] = (ord(s[i]) * power) % m
    return sum(h)


def main():
    """
    добавляет хеш по названию игры + персонаж
    :return:
    """
    header = "GameName$characters$nameError$date".split('$')
    # читаем файл
    with open("game.txt", "r", encoding="utf8") as fd:
        r = csv.DictReader(fd, delimiter='$')
        next(r)
        r = list(r)
    # хешируем
    for row in r:
        string = row["GameName"].replace(" ", '') + row["characters"]
        row[""] = get_hash(string)
    # сохраняем
    with open("game_with_hash.csv", "w", encoding="utf8", newline='') as fd:
        w = csv.DictWriter(fd, fieldnames=[""] + header, delimiter='$')
        w.writeheader()
        w.writerows(r)


if __name__ == '__main__':
    main()
