#Rule based AI Python ChatBot
import datetime
import time
name=input("Enter Your name:")
presenthour=datetime.datetime.now().hour
if 1<=presenthour<=12:
    print("Good Morning",name)
elif  12<presenthour<16:
    print("Good Afternoon",name)   
elif  16<=presenthour<=19:
    print("Good Evening",name)       
else:
    print("Good Night",name)
print("Welcome to your ChatBot")
print("You can ask your basic question,Type Bye to exit!")
responses={
    "hello":"hii, welcome.How can I help you?",
    "how are you":"I am fine,Thank you!",
    "who are you?":"I am Smart AI Chatbot!",
    "motivate me":"Keep Going,DREAM big and work for it.",
    "reminder":"you are extraordinary keep doing!",
    "happy":"Good to hear this.","sad":"how can I help ,You can share your problems."

}
def getresponseofchatbot(userquestion):
    userquestion=userquestion.lower()
    for eachKey in responses:
        if eachKey in userquestion:
            return responses[eachKey]
    return "I am not able to tell this yet,I am trying best next time!"
while True:
    userinput=input("Please ask your question:")
    reply=getresponseofchatbot(userinput)
    print("ChatBot response:",reply)
    if "bye" in userinput.lower():
        break    