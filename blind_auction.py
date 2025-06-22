# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# import art
# print(art.logo)

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bid_record = {}
if_continue = "yes"

while if_continue == "yes":
    key = input("What is your name?\n")
    value = int(input("How much would you like to bid?\n$ "))
    bid_record[key] = value
    print(bid_record)
    user_response = input("Is there new bids need to be added? Type 'yes' or 'no.'\n").lower()
    while user_response not in ["yes", "no"]:
        user_response = input("Unexpected answer. Please clarify: is there new bids need to be added? Type 'yes' or 'no.'\n").lower()
    if_continue = user_response
    print("\n"*100)
    if if_continue == "no":
        # Solution 1
        # max_key = max(bid_record,key=bid_record.get)
        # max_value = bid_record[max_key]

        # Solution 2
        max_key = ""
        max_value = 0
        for keys in bid_record:
            if bid_record[keys] > max_value:
                max_value = bid_record[keys]
                max_key = keys
        print(f"The winner is {max_key} with bidding price of ${max_value}.")
