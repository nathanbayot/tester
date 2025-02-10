print("whats up")
print("im nathan")
nathan = input("whats your name")
if nathan == "cool":
    print("nice")
print("")
print("I want to play football")
print("do you want to play")
try:
    play_football = int(input("1 for yes and 0 for no"))
except ValueError:
    print("only numbers")
    play_football = int(input("1 for yes and 0 for no"))

if play_football > 1:
    print("try again")
    play_football = int(input("1 for yes and 0 for no"))
if play_football == 1:
    print("lets play")
elif play_football == 0:
    print("sad for you")
