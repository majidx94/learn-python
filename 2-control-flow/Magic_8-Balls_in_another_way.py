#Hello Guys,
#I've tried to make it looks better, give it a try ;)

import random

name = input("Enter your Name: ")
question = input("Ask a question: ")
answer = ""
random_number = random.randint(1, 13)

#print(random_number)
if len(question) == 0 and len(name) == 0:
  print("Please Enter at least a question! The Magic 8-ball cannot provide a fortune unles you ask it something")


elif len(question) == 0:
   print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")

elif random_number == 1:
  answer = "Yes - definitely."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 2:
  answer = "It is decidedly so."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 3:
  answer = "Without a doubt."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 4:
  answer = "Reply hazy, try again."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 5:
  answer = "Ask again later."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 6:
  answer = "Better not tell you now."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 7:
  ansawer = "My sources say no."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 8:
  answer = "Outlook not so good."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 9:
  answer = "Very doubtful."
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 10:
  answer = "mmm....I can't tell now"
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 11:
  ansawer = "Wish you the best!"
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 12:
  answer = "Better not to ask now"
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif random_number == 13:
  answer = "Try Something else"
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

elif len(name) == 0:
  print("Question :", question)
  print("Magic 8-Ball's answer: " + answer)
  
else:
  answer = "Error"
