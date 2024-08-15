
name = input("Welcome to GC mini golf! What is your name? ")

option = input(f"Hi, {name}! Would you like to play 3 or 6 holes today? ")
totalPutts = 0

if option == "3":
    for i in range(1, 4):
        totalPutts += int(input(f"How many putts for hole {i}? (par is 3) "))
    totalScore = totalPutts - 9  # Calculate total score after the loop
    if totalScore > 0:
        print(f"Nice try, {name}... Your total score was: +{totalScore}.")
    elif totalScore < 0:
        print(f"Great job, {name}! Your total score was: {totalScore}.")
    else:
        print(f"Good game, {name}. Your total score was: 0.")

elif option == "6":
    for i in range(1, 7):
        totalPutts += int(input(f"How many putts for hole {i}? (par is 3) "))
    totalScore = totalPutts - 18  # Calculate total score after the loop
    if totalScore > 0:
        print(f"Nice try, {name}... Your total score was: +{totalScore}.")
    elif totalScore < 0:
        print(f"Great job, {name}! Your total score was: {totalScore}.")
    else:
        print(f"Good game, {name}. Your total score was: 0.")




