birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac_number = (birth_year - 1900) % 12

    if zodiac_number == 0:
        print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
    elif zodiac_number == 1:
        print("Your Chinese Zodiac Sign is : Ox (牛 / Nǐu)")
    elif zodiac_number == 2:
        print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
    elif zodiac_number == 3:
        print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
    elif zodiac_number == 4:
        print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
    elif zodiac_number == 5:
        print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")
    elif zodiac_number == 6:
        print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")
    elif zodiac_number == 7:
        print("Your Chinese Zodiac Sign is : Goat (羊 / Yáng)")
    elif zodiac_number == 8:
        print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
    elif zodiac_number == 9:
        print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
    elif zodiac_number == 10:
        print("Your Chinese Zodiac Sign is : Dog (狗 / Gǒu)")
    elif zodiac_number == 11:
        print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")