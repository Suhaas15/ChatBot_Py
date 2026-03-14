from functions import *
import time

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
# write your code here
if identity == "Mark":
    print("Welcome, Mark. Happy to have you at home.")
    time.sleep(3)
elif identity == "Jane":
    print("Mark is out right now, but you are welcome to the house.")
    time.sleep(3)
else:
    print("Your access is denied here.")
    exit()

# custom data
house_owner = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
# write your code here
if identity=="Mark":
    city_born = [
        "Where was I born?",
        "Mark you were born in Hyderabad."
    ]
    fav_book = [
        "What is my favorite book?",
        "That is easy. You're favorite book is Percy Jackson."
    ]
    fav_movie = [
        "What is my favorite movie?",
        "You have watched Interstellar more times than I can count."
    ]
    fav_sport = [
        "What is my favorite sport?",
        "You have always loved Badminton."
    ]
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sport)

# start chatbot
start_chatbot(home_bot)