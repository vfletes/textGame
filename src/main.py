#user inputs here
#https://stackoverflow.com/questions/21136241/what-is-the-right-way-to-create-project-structure-in-pycharm
#import package src.main
# code of interest
location = 2.0 
name = input("What is your name knight?")
#print name
intro = input('Hello ' + name + ' I have been told you are the best in the land. My jewels from my crown have been stolen. We caught the thief but he hid the jewels throughout the country, will you retrieve them for me?')
#print intro
if intro.lower() in ['y', 'yes']:
    answer = input("Great")
else:
    print("Well then you are no use to me. Good Bye")
# straight, back, left, right, s, b, l, r