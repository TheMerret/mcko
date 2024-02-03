import csv
from collections import defaultdict


def main():
    """
    добавляет счетчик багов в отчет
    :return:
    """
    header = "GameName$characters$nameError$date".split('$')
    with open("game.txt", "r", encoding="utf8") as fd:
        r = csv.DictReader(fd, delimiter='$')
        next(r)
        r = list(r)
    bugs_count = defaultdict(int)
    for row in r:
        bugs_count[row["GameName"]] += 1
    for row in r:
        row["counter"] = bugs_count[row["GameName"]]
    new_header = header + ["counter", ]
    with open("game_counter.csv", "w", encoding="utf8", newline='') as fd:
        w = csv.DictWriter(fd, fieldnames=new_header, delimiter='$')
        w.writeheader()
        w.writerows(r)


if __name__ == '__main__':
    main()
