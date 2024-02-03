import csv
from collections import defaultdict


def main():
    """
    считает баги по играм
    :return:
    """
    with open("game.txt", "r", encoding="utf8") as fd:
        r = csv.DictReader(fd, delimiter='$')
        next(r)
        r = list(r)
    r.sort(key=lambda row: row["GameName"])
    bugs_count = defaultdict(int)
    for row in r:
        bugs_count[row["GameName"]] += 1
    for k, v in bugs_count.items():
        print(k, '-', 'количество багов:', v)


if __name__ == '__main__':
    main()
