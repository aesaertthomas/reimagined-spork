from model.Birthdate import Birthdate


def test_birthdates_basics():
    # controle
    date1 = Birthdate(25, 9, 1977)
    print(date1)
    date1.day = 32  # controle testen
    print(date1)

    date2 = Birthdate(25, 9, 1977)
    if (date1 == date2):
        print("Date1 and date2 are equal!")

    date3 = Birthdate(25, 11, 2023)
    if (date2 != date3):
        print("Date2 and date3 are not equal!")

    date4 = Birthdate(25, 11, 2023)
    if (date3 == date4):
        print("Date3 and date4 are equal!")

    list_dates = [date1, date2, date3]
    print(list_dates)


test_birthdates_basics()

