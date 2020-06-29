

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk.chat.util import Chat, reflections
from tkinter import *
chatbot = ChatBot("My Bot")

conversation = [
    "hi",
    "hello",
    "Weather today",
    "today",
    "wether tomorrow",
    "schedule today"
    "40",
    "30",
    "30",
    "10:00AM"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

#response = chatbot.get_response("what is your name?")
#print(response)
#print ("Talk with bot")
#while True:
#    query=input()
#    if query=='exit':
#        break
#    answer= chatbot.get_response(query)
#    print ("bot : ", answer)

main = Tk()
main.geometry("500x650")
main.title("My chat bot")

img=PhotoImage(file="bot1.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

#function ask for bot

def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)


#create scroll frame
frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
frame.pack()

#create text filed
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

#create button
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


msgs.pack(side=LEFT, fill=BOTH, pady=10)


main.mainloop()