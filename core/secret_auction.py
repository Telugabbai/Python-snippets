import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def auction():

    auction_done = False
    bid_auctioned = {}

    def highest_bid(bidding):
        highest_bid_amount = 0
        winner = ''
        for bidder in bidding:
            bid_amount = bidding[bidder]
            if bid_amount > highest_bid_amount:
                highest_bid_amount = bid_amount
                winner = bidder
        print(f"The winner is {winner} with bid of {highest_bid_amount} ")

    while not auction_done:
        name = input("Enter your name: ")
        bid = int(input("Enter bid price: "))
        bid_auctioned[name] = bid

        result = input("Are there any other bidders ?. Type 'Yes' or 'No' ").lower()
        if result == 'no':
            auction_done = True
            highest_bid(bid_auctioned)
        elif result == 'yes':
            clear_screen()


auction()
