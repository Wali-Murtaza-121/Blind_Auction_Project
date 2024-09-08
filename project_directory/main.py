from art import logo
print(logo)

name = input("What's your name?: ")
bid = int(input("Type your 'bid' in: $"))

dictionary = {}
def bid_calculation(name,bid):
    should_end = False
    while not should_end:
        dictionary[name] = bid
        bidder_choice = input("Type 'yes' to another bid.Otherwise 'no'? ")
        if bidder_choice == "yes":
            name = input("What's your name?: ")
            bid = int(input("Type your 'bid' in: $"))
        else:
            should_end = True
            highest_bid = 0
            for key in dictionary:
                if dictionary[key] > highest_bid:
                    highest_bid = dictionary[key]
                    final_name = key
            
            print(f"The Highest bid of {final_name} is ${highest_bid}")
bid_calculation(name,bid)