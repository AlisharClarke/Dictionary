import json
# new_dict = {"name" : "alisha", "tiger" : 13, "may" : 5}

# print(new_dict["name"])
# i = 0
# if i in range(100):
#     i += 1
#     answer = input("What is your name?")
#     answer2 = input("What is your favorite color?")
#
# new_dict["person"] = answer
# new_dict["color"] = answer2
#
# for each in new_dict:
#     print(new_dict[each])
#
# surveylist = new_dict["person"], new_dict["color"]
# print(surveylist)

# new_dict = {"name" : "alisha", "tiger" : 13, "may" : 5}
# questions = "What is your name?", "What is your favorite color? Please put it in one sentence."

new_dict = {}
list_key = ["name", "age", " favorite color"]
list_quest = ["your name?", "your age?", "your favorite color?"]
def repeat():
    for i in range(len(list_key)):
        ans = input(list_quest[i])
        new_dict[list_key[i]] = ans
        with open('dictionary.json', 'a+') as outfile:
            json.dump(new_dict, outfile)
        i =+1

for i in range(len(list_key)):
    repeat()
    print(new_dict)
    print("Thank you :D. Your responses have been recorded.")
    # new_dict.append(ans)


# def survey():
#     for i in range(3):
#         # if i in range(3):
#         answer3 = input(questions)
#         new_dict["name, color"] = answer3
#             # print("Your name and favorite color is....:" + new_dict["key"])
#             # print(new_dict["key"])
#             # print("Thanks!!:D")
#             # i += 1
#         # else:
#         # 	break
#
# survey()
# for each in new_dict:
#     print(new_dict[each])
