from SentenceReadingAgent import SentenceReadingAgent
import time


if __name__ == "__main__":

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."

    question_1a = "Who brought the note?"
    result_1a = test_agent.solve(sentence_1, question_1a)
    print("Passed" if result_1a == "Ada" else "question_1a Failed - " + str(result_1a))

    question_1b = "Who did Ada bring the note to?"
    result_1b = test_agent.solve(sentence_1, question_1b)
    print("Passed" if result_1b == "Irene" else "question_1b Failed - " + str(result_1b))

    question_1c = "What did Ada bring?"
    result_1c = test_agent.solve(sentence_1, question_1c)
    print("Passed" if result_1c == "note" else "question_1b Failed - " + str(result_1c))

    question_1d = "How long was the note?"
    result_1d = test_agent.solve(sentence_1, question_1d)
    print("Passed" if result_1d == "short" else "question_1d Failed - " + str(result_1d))


    # ==================================================================================

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."

    question_2a = "Who does Lucy go to school with?"
    result_2a = test_agent.solve(sentence_2, question_2a)
    print("Passed" if result_2a == "David" else "question_2a Failed - " + str(result_2a))

    question_2b = "Where do David and Lucy go?"
    result_2b = test_agent.solve(sentence_2, question_2b)
    print("Passed" if result_2b == "school" else "question_2b Failed - " + str(result_2b))

    question_2c = "How far do David and Lucy walk?"
    result_2c = test_agent.solve(sentence_2, question_2c)
    print("Passed" if result_2c == "mile" else "question_2c Failed - " + str(result_2c))

    question_2d = "How do David and Lucy get to school?"
    result_2d = test_agent.solve(sentence_2, question_2d)
    print("Passed" if result_2d == "walk" else "question_2d Failed - " + str(result_2d))

    question_2e = "At what time do David and Lucy walk to school?"
    result_2e = test_agent.solve(sentence_2, question_2e)
    print("Passed" if result_2e == "8:00AM" else "question_2e Failed - " + str(result_2e))

    # ==================================================================================

    sentence_3 = 'This year David will watch a play.'
    question_3a = 'Who will watch a play?'
    result_3a = test_agent.solve(sentence_3, question_3a)
    print("Passed" if result_3a == "David" else "question_3a Failed - " + str(result_3a))

    # ==================================================================================

    sentence_4 = 'Lucy will write a book.'
    question_4a = 'Who will write a book?'
    result_4a = test_agent.solve(sentence_4, question_4a)
    print("Passed" if result_4a == "Lucy" else "question_4a Failed - " + str(result_4a))

    # ==================================================================================

    sentence_5 = "Bring the box to the other room."
    question_5a = "Where should the box go?"
    result_5a = test_agent.solve(sentence_5, question_5a)
    print("Passed" if result_5a == "room" else "question_5a Failed - " + str(result_5a))

    # ==================================================================================

    sentence_6 = "There are a thousand children in this town."
    question_6a = "How many children are in this town?"
    result_6a = test_agent.solve(sentence_6, question_6a)
    print("Passed" if result_6a == "thousand" else "question_6a Failed - " + str(result_6a))

    # ==================================================================================

    sentence_7 = "Give us all your money."
    question_7a = "Who should you give your money to?"
    result_7a = test_agent.solve(sentence_7, question_7a)
    print("Passed" if result_7a == "us" else "question_7a Failed - " + str(result_7a))
    question_7b = "How much of your money should you give us?"
    result_7b = test_agent.solve(sentence_7, question_7b)
    print("Passed" if result_7b == "all" else "question_7a Failed - " + str(result_7b))

    # ==================================================================================

    sentence_8 = "The water is blue."
    question_8a = "What is blue?"
    result_8a = test_agent.solve(sentence_8, question_8a)
    print("Passed" if result_8a == "water" else "question_8a Failed - " + str(result_8a))

    # ==================================================================================

    sentence_9 = "She told her friend a story."
    question_9a = "What did she tell?"
    result_9a = test_agent.solve(sentence_9, question_9a)
    print("Passed" if result_9a == "story" else "question_9a Failed - " + str(result_9a))

    # ==================================================================================

    sentence_10 = "There is snow at the top of the mountain."
    question_10a = "What is on top of the mountain?"
    result_10a = test_agent.solve(sentence_10, question_10a)
    print("Passed" if result_10a == "snow" else "question_10a Failed - " + str(result_10a))
    question_10b = "Where is the snow?"
    result_10b = test_agent.solve(sentence_10, question_10b)
    print("Passed" if result_10b == "mountain" else "question_10b Failed - " + str(result_10b))

    # ==================================================================================

    sentence_11 = "Frank was busy last night."
    question_11a = "When was Frank busy?"
    result_11a = test_agent.solve(sentence_11, question_11a)
    print("Passed" if result_11a == "night" else "question_11a Failed - " + str(result_11a))
    question_11b = "Who was busy last night?"
    result_11b = test_agent.solve(sentence_11, question_11b)
    print("Passed" if result_11b == "Frank" else "question_11a Failed - " + str(result_11b))

    # ==================================================================================

    sentence_12 = "The sound of rain is cool."
    
    question_12a = "What has a cool sound?"
    result_12a = test_agent.solve(sentence_12, question_12a)
    print("Passed" if result_12a == "rain" else "question_12a Failed - " + str(result_12a))

    question_12b = "What is cool?"
    result_12b = test_agent.solve(sentence_12, question_12b)
    print("Passed" if result_12b == "sound" else "question_12b Failed - " + str(result_12b))

    # ==================================================================================

    sentence_13 = 'A tree is made of wood.'
    question_13a = 'What is made of wood?'
    result_13a = test_agent.solve(sentence_13, question_13a)
    print("Passed" if result_13a == "tree" else "question_13a Failed - " + str(result_13a))

    question_13b = 'What is tree made of?'
    result_13b = test_agent.solve(sentence_13, question_13b)
    print("Passed" if result_13b == "wood" else "question_13b Failed - " + str(result_13b))

    # ==================================================================================

    sentence_14 = 'Frank took the horse to the farm.'
    question_14a = 'Where did Frank take the horse?'
    result_14a = test_agent.solve(sentence_14, question_14a)
    print("Passed" if result_14a == "farm" else "question_14b Failed - " + str(result_14a))

    question_14b = 'Who took the horse to the farm?'
    result_14b = test_agent.solve(sentence_14, question_14b)
    print("Passed" if result_14b == "Frank" else "question_14b Failed - " + str(result_14b))

    # ==================================================================================

    sentence_15 = 'Serena ran a mile this morning.'
    question_15a =  'When did Serena run?'
    result_15a = test_agent.solve(sentence_15, question_15a)
    print("Passed" if result_15a == "morning" else "question_15a Failed - " + str(result_15a))

    # ==================================================================================

    sentence_16 = 'Watch your step.'
    question_16a = 'What should you watch?'
    result_16a = test_agent.solve(sentence_16, question_16a)
    print("Passed" if result_16a == "step" else "question_16a Failed - " + str(result_16a))  
    # ==================================================================================

    sentence_17 = 'There are three men in the car.'
    question_17a = 'How many men are in the car?'
    result_17a = test_agent.solve(sentence_17, question_17a)
    print("Passed" if result_17a == "three" else "question_17a Failed - " + str(result_17a))  
    question_17b = 'Who is in the car?'
    result_17b = test_agent.solve(sentence_17, question_17b)
    print("Passed" if result_17b == "men" else "question_17b Failed - " + str(result_17b))  

    # ==================================================================================

    sentence_18 = 'Lucy will write a book at night.'
    question_18a = 'Who will write a book?'
    result_18a = test_agent.solve(sentence_18, question_18a)
    print("Passed" if result_18a == "Lucy" else "question_18a Failed - " + str(result_18a))  
    question_18b = 'When will Lucy write a book?'
    result_18b = test_agent.solve(sentence_18, question_18b)
    print("Passed" if result_18b == "night" else "question_18b Failed - " + str(result_18b))  

    # ==================================================================================

    sentence_19 = 'The blue bird will sing in the morning.'
    question_19 = 'What color is the bird who sings?'
    result_19 = test_agent.solve(sentence_19, question_19)
    print("Passed" if result_19 == "blue" else "question_19 Failed - " + str(result_19))  
    
    # ==================================================================================

    sentence_20 = 'Their children are in school.'
    question_20 = 'Where are their children?'
    result_20 = test_agent.solve(sentence_20, question_20)
    print("Passed" if result_20 == "school" else "question_20 Failed - " + str(question_20))  
    
    # ==================================================================================

    sentence_21 = 'The white dog and the blue horse play together.'
    question_21 = 'What animal is blue?'
    result_21 = test_agent.solve(sentence_21, question_21)
    print("Passed" if result_21 == "horse" else "question_21 Failed - " + str(question_21))  
    
    # ==================================================================================

    sentence_21 = 'Serena and Ada took the blue rock to the street.'
    question_21 = 'What was blue?'
    result_21 = test_agent.solve(sentence_21, question_21)
    print("Passed" if result_21 == "rock" else "question_21 Failed - " + str(question_21))  
    
    # ==================================================================================

    sentence_22 = 'The white dog and the blue horse play together.'
    question_22 = 'What color is the dog?'
    result_22 = test_agent.solve(sentence_22, question_22)
    print("Passed" if result_22 == "white" else "question_22 Failed - " + str(result_22))  
    
    # ==================================================================================

    sentence_23 = 'Serena saw a home last night with her friend.'
    question_23 = 'What did they see?'
    result_23 = test_agent.solve(sentence_23, question_23)
    print("Passed" if result_23 == "home" else "question_23 Failed - " + str(result_23))  
    
    # ==================================================================================


    print('stop')




# def test():
#     #This will test your SentenceReadingAgent
# 	#with nine initial test cases.

#     test_agent = SentenceReadingAgent()

#     sentence_1 = "Ada brought a short note to Irene."
#     question_1 = "Who brought the note?"
#     question_2 = "What did Ada bring?"
#     question_3 = "Who did Ada bring the note to?"
#     question_4 = "How long was the note?"

#     sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
#     question_5 = "Who does Lucy go to school with?"
#     question_6 = "Where do David and Lucy go?"
#     question_7 = "How far do David and Lucy walk?"
#     question_8 = "How do David and Lucy get to school?"
#     question_9 = "At what time do David and Lucy walk to school?"

#     print(test_agent.solve(sentence_1, question_1))  # "Ada"
#     print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
#     print(test_agent.solve(sentence_1, question_3))  # "Irene"
#     print(test_agent.solve(sentence_1, question_4))  # "short"

#     print(test_agent.solve(sentence_2, question_5))  # "David"
#     print(test_agent.solve(sentence_2, question_6))  # "school"
#     print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
#     print(test_agent.solve(sentence_2, question_8))  # "walk"
#     print(test_agent.solve(sentence_2, question_9))  # "8:00AM"

#     sentence_3 = 'Bring the dog to the other room.'
#     q_3a = 'What should be brought to the other room?'
#     a_3a = 'dog'

#     sentence_4 = 'A tree is made of wood.'
#     q_4a = 'What is made of wood?'
#     a_4a = 'wood'

#     sentence_5 = 'Frank took the horse to the farm.'
#     q_5a = 'Where did Frank take the horse?'
#     a_5a = 'farm'

#     sentence_6 = 'Serena ran a mile this morning.'
#     q_6a =  'When did Serena run?'
#     a_6a = 'morning'

#     sentence_7 = 'Watch your step.'
#     q_7a = 'What should you watch?'
#     a_7a = 'step'

#     sentence_8 = 'This year David will watch a play.'
#     q_8a = 'Who will watch a play?'
#     a_8a = 'David'

#     sentence_9 = 'There are three men in the car.'
#     q_9a = 'How many men are in the car?'
#     a_9a = 'three'
#     q_9b = 'Who is in the car?'
#     a_9b = 'men'

#     sentence_10 = 'Lucy will write a book.'
#     q_10a = 'Who will write a book?'
#     a_10a = 'Lucy'

#     sentence_11 = 'Bring the box to the other room.'
#     q_11a = 'Where should the box go?'
#     a_10a = 'room'


# if __name__ == "__main__":
#     test()