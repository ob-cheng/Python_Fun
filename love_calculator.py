# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
  
def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    combined_name = name1.upper() + name2.upper()
    for letter in combined_name:
        if letter in ["T", "R", "U", "E"]:
            true_count += 1
        if letter in ["L", "O", "V", "E"]:
            love_count += 1 
    print(str(true_count)+str(love_count))
    
calculate_love_score("Tianen Cheng", "Alla Cheng")
