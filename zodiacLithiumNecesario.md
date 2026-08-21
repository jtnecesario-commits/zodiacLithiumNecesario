# Requirments :

Instructions:
1. Create a zodiacSectionLN.py file. This file will contain your solutions to the requirements below.
a. Ask the user to enter a year of birth. The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.
Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1980
d. Otherwise determine the chinese zodiac sign based on the following starting from 1900. Note: A zodiac sign will recur after each 12 years. i. Rat (i/Shú)
Ox (+/Nu)
Tiger (/HO)
iv.
Rabbit (/T)
v
Dragon (Long)
vi.
Snake (/She)
vii.
Horse (/Ma)
vii.
ix
Monkey (/Hou)
x
xi.
Goat (/Yang)
Rooster (J)
Dog (/Gou)
xi. Pig (/Zh0)
e. CONSIDER only the year of birth.
Example input and output:
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (# / Long)
2. Test and Run your code before submitting.
3. Document this graded exercise in your Github portfolio and save it in
zodiac SectionLN.md. This md will include the requirements for this coding exercise, your actual code and a screenshot of your output. Update also your README.md file to have the link to your files.
4. Commit your changes in your github account and submit the live code link to your teacher and also your git repository link.
5. Refer to Annex D for Code Exercise Rubrics for Grading.

# Code :
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

# Output :
<img width="1919" height="1079" alt="Screenshot 2026-08-21 182019" src="https://github.com/user-attachments/assets/f41bc1db-0485-49e8-9709-64c9dfc1b8f8" />

