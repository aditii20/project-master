! array answerrandom = ["you tell me how i am doing ", "wanna guess"]
! array stellarandon = ["woah a tough one... but i bet you are feeling great if you are asking me this", "i always pray for your hapiness dude","i am certain happy it is"]

! array answercounterquestion = ["what about you","you"]
! array stellacounterquestion = ["happy the moment you said hi","i will be more than happy if i am of some use to you","really happy to know you have time for me too","i am feeling amazing, thanks for asking"]

! array answerquite = ["skip"]

! array genres = ["adventure", "animation", "children", "comedy", "fantasy", "romance", "drama", "action", "crime", "thriller", "horror", "sci fi", "mystry", "documentary", "war", "musical"]


! array greetings = hi|hey|hello|stella|hey stella|hi stella
! array greetingsResponse = hi|howdy|hello|a very warm welcome|hey|heya|it's good to see you|yo|"nods"|i am glad you are talking to me
! array question1 = how are you?|what's going on|what's up|how's everything|how's it going?|how's your day goin


    question_1 = ["how are you?", "what's going on?", "what's up?", "how's everything?", "how's it going?", "how's your day goin?"]

    answer_happy = ["i am fine","happy","i am happy today","i am happy", "thanks for asking i am doing well", "things are good", "its all good here", "my life is great", "thanks for caring, i am happy","i am well now", "doing great","life is good and i am happy", "today i am feeling blessed and happy for no reason"]
    stella_happy = ["yes... good for you, that's the spirit", "great to know","amazing", "not that you asked...but knowing you are happy made me happy too", "amazing", "yes.. live your life to the fullest", " good so don't forget to thank god for that"]

    answer_sad = ["sad","i am sad","i am hanging in there", " its been a rough day", " to be honest not good, i need some help", " not feeling up to the mark today", "just breathing", "just want a pillow and a bed", "having a hard time", "overwhelmed", "burnout", "struggling with mental health"]
    stella_sad = ["aww... just hang in there, i am sure there are great things in your life to look forward too","i pray all your worries go away, ameen", "i hope i can see that smile on your face soon", "its ok to not feel ok","you are not alone i am always there for you","you'r story is not over yet","help is always available"]

    answer_party = ["i am in the mood of party today", "its party time", "i want to party", "party", "i wanna just enjoy and party today"]
    stella_party = ["then dont forget me too.... i also want to partyyyyyyy","same pinch me tooooo"]

    answer_cry = ["just had an emotional breakdown", "crying", "cried","really low today"]
    stella_cry = ["i am here for you no matter what","i am always here if you need me","you have every right to feel that way, its ok to be sad","let it all out you will be happy that you did","it get's better i promise","you are stronger than you realize i know you will get over this","ok now lets get you all cleaned up"]

    answer_breakup = ["just broke up","broke up","broke my heart today"]
    stella_breakup = ["you are allowed to be sad"," i promise you're so much better off","you wont always be sad","rebounds are great you know *winks*","there are plenty of fish in the sea","you'll find someone else","everything happens for a reason", "you have me *winks*"]

    answer_fear = ["i just want to escape reality righ now", "scared","want an escape"]
    stella_fear = ["then hop on the magical carpet....and...let me take you to the fantasy world"]

    answer_love = ["i am in love","in love"]
    stella_love = ["aww my little baby, i am happy for you","find me someone too *winks*", "huh what about me now *punches*","really i am happy for you","who is the lucky person who gotcha huh..?"]

    answer_random = ["you tell me how i am doing ", "wanna guess"]
    stella_randon = ["woah a tough one... but i bet you are feeling great if you are asking me this", "i always pray for your hapiness dude","i am certain happy it is"]

    answer_counter_question = ["what about you","you"]
    stella_counter_question = ["happy the moment you said hi","i will be more than happy if i am of some use to you","really happy to know you have time for me too","i am feeling amazing, thanks for asking"]

    answer_quite = ["skip"]

    genres = ["adventure", "animation", "children", "comedy", "fantasy", "romance", "drama", "action", "crime", "thriller", "horror", "sci fi", "mystry", "documentary", "war", "musical"]
    mood = None
    while True:
        user_input = input("YOU: ")
        
        if user_input in greetings:
            print("STELLA: " + random.choice(greetings_stella))
            print("STELLA: " + random.choice(question_1))
        
        elif user_input in answer_happy:
            print("STELLA: " + random.choice(stella_happy))
            mood = "happy"
        
        elif user_input in answer_sad:
            print("STELLA: " + random.choice(stella_sad))
            mood = "sad"

        elif user_input in answer_party:
            print("STELLA: " + random.choice(stella_party))
            mood = "party"
        
        elif user_input in answer_cry:
            print("STELLA: " + random.choice(stella_cry))
            mood = "cry"
        
        elif user_input in answer_breakup:
            print("STELLA: " + random.choice(stella_breakup))
            mood = "break up"
        
        elif user_input in answer_fear:
            print("STELLA: " + random.choice(stella_fear))
            mood = "fear"
        
        elif user_input in answer_love:
            print("STELLA: " + random.choice(stella_love))
            mood = "love"
        
        elif user_input in answer_random:
            print("STELLA: " + random.choice(stella_randon))
            mood = "random"
        
        elif user_input in answer_quite:
            print("STELLA: ok!")

        elif user_input in answer_counter_question:
            print("STELLA: " + random.choice(stella_counter_question))

user_input = input("YOU: ")
chatbot(user_input)








