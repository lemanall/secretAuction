import art
print(art.logo)

bid_people = []
end_of_game = False

def getInfo(name, bid):
    bid_person = {}
    bid_person['name'] = name
    bid_person['bid'] = bid
    bid_people.append(bid_person)

def findBigBid():
    bigBid = 0
    winner = ''
    for person in bid_people:
        if person['bid'] > bigBid:
            bigBid = person['bid']
            winner = person['name']
    print(f"Thanks for playing. The big bid is: {bigBid} and the winner is: {winner}")


while not end_of_game:
    name = input("What is your name? ").lower()
    bid = int(input("What is your bid? "))
    getInfo(name, bid)
    again = input("Would you like to play again? (y/n) ").lower()

    if again != "y":
        end_of_game = True
        findBigBid()
        print("Thanks for playing!")
