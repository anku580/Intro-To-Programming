print ""
print "welcome to my quiz"  #
#questios
easy_level=['_____ is the pm of india','_____ is the best 2016 bollywood movie','________ is the First indian women who won silver medal at rio Olympics','_______ develop 0 in Mathematics'] #string for easy level quiz
medium_level=['_____ is the best singer worldwide','In _____  first world war was fought','_____ is the best indian youtube comedian','Approximately _____ test matches have been played by india now'] #string for medium level quiz
hard_level=['_____ is the worlds fastest man','Ussain Boult won _____ medals in rio 2016 olympics','_____ is the most powerful country','_____ country is expected more tourits over the year'] #srting for hard level
#answers
easy_ans=['Narender Modi','PK','PV sindhu','Aryabhatt'] #answers for easy level
medium_ans=['Taylor swif','1950','Bhuvam bam','500']#answers for medium level
hard_ans=['Ussain Bolt','3','USA','Paris']#answers for hard level
def sel_level(choice): #this procedure is  made so that whenever user inputs the type of level he wants to play...this procedure comes in action and do further proess as mention inside this procedure.
    if choice == 'easy':
        return game(easy_level,easy_ans)   #returns to the function named as game() for question bank for the level easy game
    elif choice == 'medium':
        return game(medium_level,medium_ans)    #return to function named as game() for the question bank for the level medium game
    elif choice == "hard":
        return game(hard_level,hard_ans)  #return to function named as game() for the question bank for the hard level game
    else:
        return sel_level(raw_input("Enter quiz challenge level: easy, medium, hard: "))


def game(level,answer): # procedure made for the questions of diffrent level
    print "__"*20
    index=0  #used for counting the question
    print "Welcome to your Selected level"
    print "__"*20
    ans = [] #it is used to store the answers input by the user
    limit=4  #maximun no. of questions
    while index<limit:
        print "Here is your question:"
        print level[index]
        check_ans = raw_input("Your Answer:")                           #check-ans stores the answer inputs by the user
        if check_ans == answer[index]:                                #here  comparison of the answer input by the user and the actual answer,if answer evaluates to true then we go inside this loop
            ans.append(check_ans)                                       # its adds a string to the list named as ans
            print "Your answer is correct"
            print level[index].replace("_____",answer[index])           #here replace is used so that que with the blank should be replaced by the blank filled with answer correctly
            index=index+1                                               #increment of the index for the next que to occur
        else:                                                           #if the above condition false then the condition goes here
            print "Oops you Entered wrong Answer please try again"      #question is asked again.
    return "You Answered all questions correctly"                       #return this value if all the questions are correctly answered

print " "*10
choice = raw_input("Enter quiz challenge level: easy, medium, hard: ")   #choice is used to store the value enterd by the user that he/she wants what kind of level to play
print sel_level(choice)                                                  #here calling the function named as sel_level so that it follows instruction as per the user demand
