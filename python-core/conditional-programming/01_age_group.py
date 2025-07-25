#Age Group Categorization
#Classify a person's age gorup: Child(<13), Teenage(13-19), Adult(20-59), Senior(60+)

user_age = 25


age = int(input("Provide me an age: "))

if age < 13:
    print("child")
elif age < 20:
    print("Teenage")
elif age < 60:
    print("Adult")
else:
    print("Senior")


