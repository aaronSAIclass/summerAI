
#part 1
hours = input("Enter a number of hours!")
mins = float(hours)
mins *= 60
print(mins," minutes!")

#part 2
answer = input("Type 1 for hours to minutes and 2 for minutes to hours")
match answer:
    case "1":
        hours = input("Enter a number of hours!")
        mins = float(hours)
        mins *= 60
        print(mins," minutes!")
    case "2":
        hours = input("Enter a number of hours!")
        mins = float(hours)
        mins /= 60
        print(mins," hours!")
    case _:
        print("Thats not an option! Defaulting to hours to minutes.")
        hours = input("Enter a number of hours!")
        mins = float(hours)
        mins *= 60
        print(mins," minutes!")

#part 3

intro = input("Enter a word!")
intro = intro.replace(" ", "")

number = len(intro)
if(intro.isalpha() == True):
    print("Your word has ", number, " letters!")
else:
    print("Your word has ", number, " letters or characters that are not spaces!")

