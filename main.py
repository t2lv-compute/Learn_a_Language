import random

selected_language = ""
lessons = {"Chinese":{0:["Greetings!",
                    ["你好","再见","早上好","晚上好","下午好"], 
                    ["ni hao","zai jian","zao shang hao",
                     "wan shang hao","xia wu hao"]]}}
all_languages = ["Chinese"]
#print(list(range(1,len(all_languages)+1)))
print("Welcome to Language Learner.\nSelect a language:")
for language in all_languages:
    print(f"-> {language}. Type the key {str(all_languages.index(language)+1)} to select.")
while selected_language == "":  
    selected_language = input("Enter your choice here: ")
    if int(selected_language) not in list(range(1,len(all_languages)+1)):
        print("Sorry, Try Again.")
        selected_language = ""
selected_language = all_languages[int(selected_language)-1]
#print(selected_language)
print(f"Let's start learning {selected_language}!")
for i in range(0,len(lessons[selected_language])):
    print(f"Lesson {i+1}: {lessons[selected_language][i][0]}")
