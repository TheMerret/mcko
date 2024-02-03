import csv


def main():
    """
    делает отчет, помечает обработанные
    :return:
    """
    # читаем файл
    header = "GameName$characters$nameError$date".split('$')
    with open("game.txt", "r", encoding="utf8") as fd:
        r = csv.DictReader(fd, delimiter='$')
        next(r)
        r = list(r)
    # ищем особые баги
    for row in r:
        if "55" in row["nameError"]:
            print(f"У персонажа\t{row['characters']}\tв игре\t{row['GameName']}\tнашлась ошибка с кодом:\t {row['nameError']}.\tДата фиксации:\t {row['date']}")
            row["nameError"] = 'Done'
            row['date'] = '0000-00-00'
    # сохраняем
    with open("game_new.csv", "w", encoding="utf8", newline='') as fd:
        w = csv.DictWriter(fd, fieldnames=header, delimiter='$')
        w.writeheader()
        w.writerows(r)


if __name__ == '__main__':
    main()
