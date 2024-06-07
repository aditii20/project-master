





import random
var_1 = ["hi","hello"]
var_2 = ["how are you", "how are you doing", "how is your health"]
var_3 = ["What is your name", "how should i call you", "Your name is "]
var_4 = ["How are you feeling today","So what is going on in your life" ]
var_5 = ["So what would you like to do today  listen to some songs or watch a movie"]

y = True
while (y == True):
    user_input = input ("YOU: ")
    
    if user_input.lower() in var_1:
        stella_1 = ["hello", "hi"]
        print("STELLA: " + random.choice(stella_1) + "\n")
    
    if user_input.lower in var_2:
        stella_2 = ["I am good", "I am doing good", " i am fine"]
        print("STELLA: " + random.choice(stella_2) + "\n")
    
    if user_input.lower in var_3:
        stella_3 = ["I am Stella", "Call me Stella", " Stella"]
        print("STELLA: " + random.choice(stella_3) + "\n")
    
    if user_input.lower in var_4:
        stella_4 = ["I am feeling good today. Thanks for asking. What about you?"]
        print("STELLA: " + (stella_4) + "\n")
    
    if user_input.lower in var_5:
        stella_5 = ["I would like to listen to music today!"]
        print("STELLA: " + (stella_5) + "\n")
    
    if user_input.lower not in var_1 or var_2 or var_3 or var_4 or var_5:
        print("STELLA: " + "I am not able to get your question" + "\n")
    
# import random
# var_1 = ["hi","hello"]
# var_2 = ["how are you", "how are you doing", "how is your health"]
# var_3 = ["What is your name", "how should i call you", "Your name is "]
# var_4 = ["How are you feeling today","So what is going on in your life" ]
# var_5 = ["So what would you like to do today  listen to some songs or watch a movie"]

# y = True
# while (y == True):
#     user_input = input ("YOU: ")
    
#     if user_input.lower() in var_1:
#         stella_1 = ["hello", "hi"]
#         print("STELLA: " + random.choice(stella_1) + "\n")
    
#     if user_input.lower in var_2:
#         stella_2 = ["I am good", "I am doing good", " i am fine"]
#         print("STELLA: " + random.choice(stella_2) + "\n")
    
#     if user_input.lower in var_3:
#         stella_3 = ["I am Stella", "Call me Stella", " Stella"]
#         print("STELLA: " + random.choice(stella_3) + "\n")
    
#     if user_input.lower in var_4:
#         stella_4 = ["I am feeling good today. Thanks for asking. What about you?"]
#         print("STELLA: " + (stella_4) + "\n")
    
#     if user_input.lower in var_5:
#         stella_5 = ["I would like to listen to music today!"]
#         print("STELLA: " + (stella_5) + "\n")
    
#     if user_input.lower not in var_1 or var_2 or var_3 or var_4 or var_5:
#         print("STELLA: " + "I am not able to get your question" + "\n")
    



    


    