from art import logo2, vsvar
import random
from higherlower_data import data

def format_data(account):
    account_name = account["name"]
    account_descrption = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descrption}, from {account_country}"



def compare(user_answer,follower_a,follower_b):
    if follower_a > follower_b:
        return user_answer == 'a'
    else:
        return user_answer =='b'
    
        
 



account_b = random.choice(data)
score = 0
while True:
     
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    
    
    print(logo2)
    print(f"Compare A: {format_data(account_a)}")

    print(vsvar)

    print(f"Compare B: {format_data(account_b)}")


    user_answer = input("Who has more followers? Type 'A' or 'B':").lower()
    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]
    is_check = compare(user_answer,follower_a,follower_b)

    if is_check:
        score +=1
        print(f"You're right. Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break







#obs3: it is a list of dicts (use random to choose one of the dicts inside)
#step -3 ask the players inpput answer for 'A' or 'B'
#step 4 - compare the user_answer with the right answer (value in data)
#obs if the answer is right user_score goes up and the right data goes to A. it substitutes only B.