

def guess_words_from_french(list_of_french_words, list_of_correct_english_translations):

    # for i in range(0, len(list_of_french_words)):
    #     print("What is the English word for "+ list_of_french_words[i] + "?")
    #     eng = input("Input: ")
    #     if eng == list_of_correct_english_translations[i]:
    #         print("Correct")
    #         list_of_french_words.pop(i)
    #         list_of_correct_english_translations.pop(i)
    #         i -= 1
    #     else:
    #         print("Incorrect")
    #         temp_e = list_of_correct_english_translations.pop(i)
    #         temp_f = list_of_french_words.pop(i)
    #         list_of_correct_english_translations.insert(len(list_of_correct_english_translations) - 1, temp_e)
    #         list_of_french_words.insert(len(list_of_french_words) - 1, temp_f)
    #         i -= 1

    index = 0
    while len(list_of_french_words) > 0:
        print("What is the English word for " + list_of_french_words[index] + "?")
        user_input = input("Input: ")
        if user_input == list_of_correct_english_translations[index]:
            print("Correct")
            list_of_french_words.pop(index)
            list_of_correct_english_translations.pop(index)
        else:
            print("Incorrect")
            index += 1
        # If index is greater than the length of the list, its resetted to access the next set of variables
        if index >= len(list_of_french_words):
            index = 0



guess_words_from_french(["Chat", "Chien", "Poisson"], ["Cat", "Dog", "Fish"])


# Console Output:
# What is the English word for Chat? Input: ‘Cat’
# ‘Correct’
# What is the English word for Chien? Input: ‘Rabbit’
# ‘Incorrect’
# What Is the English word for Poisson? Input: ‘Fish’
# ‘Correct’
# What is the English word for Chien? Input: ‘Dog’
# ‘Correct’
# All words are translated correctly!

#
# french  english
# 1       -> a
# 3       -> c
# 4       -> d  <-  I
# 5       -> e
# 6       -> f

# i = ++i % count()