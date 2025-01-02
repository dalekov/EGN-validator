def validate_egn(egn):
    if len(egn) != 10 or not egn.isdigit():
        return False

    year = int(egn[:2])
    month = int(egn[2:4])
    day = int(egn[4:6])

    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 1800
        month -= 20
    elif 41 <= month <= 52:
        month -= 40
        year += 2000
    else:
        return False

    try:
        from datetime import date
        dob = date(year, month, day)
        regions = {"Благоевград": [i for i in range(0, 44)],
                   "Бургас": [i for i in range(44, 94)],
                   "Варна": [i for i in range(94, 140)],
                   "Велико Търново": [i for i in range(140, 170)],
                   "Видин": [i for i in range(170, 184)],
                   "Враца": [i for i in range(184, 218)],
                   "Габрово": [i for i in range(218, 234)],
                   "Кърджали": [i for i in range(234, 282)],
                   "Кюстендил": [i for i in range(282, 302)],
                   "Ловеч": [i for i in range(302, 320)],
                   "Монтана": [i for i in range(320, 342)],
                   "Пазарджик": [i for i in range(342, 378)],
                   "Перник": [i for i in range(378, 396)],
                   "Плевен": [i for i in range(396, 435)],
                   "Пловдив": [i for i in range(436, 502)],
                   "Разград": [i for i in range(502, 528)],
                   "Русе": [i for i in range(528, 555)],
                   "Силистра": [i for i in range(556, 576)],
                   "Сливен": [i for i in range(576, 602)],
                   "Смолян": [i for i in range(602, 624)],
                   "София - град": [i for i in range(624, 722)],
                   "София - окръг": [i for i in range(722, 751)],
                   "Стара Загора": [i for i in range(752, 790)],
                   "Добрич": [i for i in range(790, 822)],
                   "Търговище": [i for i in range(822, 844)],
                   "Хасково": [i for i in range(844, 872)],
                   "Шумен": [i for i in range(872, 904)],
                   "Ямбол": [i for i in range(904, 926)],
                   "Друг/Неизвестен": [i for i in range(926, 1000)]
        }

        region_code = int(egn[6:9])

        for region_name, codes in regions.items():
            if region_code in codes:
                region = region_name
                break

        print(f"Дата на раждане: {dob.strftime("%d/%m/%Y")}. Пол: {"Мъж" if int(egn[-2]) % 2 == 0 else "Жена"}. Регион: {region}. ")


    except ValueError:
        return False

    weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
    check_sum = sum(int(egn[i]) * weights[i] for i in range(9)) % 11
    check_sum = 0 if check_sum == 10 else check_sum

    return check_sum == int(egn[-1])



print("Проверка за валидност на ЕГН")
egn = input("Моля въведете вашето ЕГН тук: ")
if validate_egn(egn):
    print("ЕГН номер е валиден.")
else:
    print("ЕГН номер е невалиден.")

