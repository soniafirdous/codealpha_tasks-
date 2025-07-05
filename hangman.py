
#1- word selection
import random

word_list=["Apple","Mango","Banana","Guvava","Watermelon","Strawberry","Melon","Peach"]
word=random.choice(word_list).lower()


#2- hangman stages

stages=[ "",
        "__________",
        "|    |    ",
        "|    |    ",
        "|    0    ",
        "|   /|\   ",
        "|   / \   "]
# 3-creating variables

wrong=0
max_wrong=len(stages)-1
guessed_letter=set()
display=["_" for _ in word]
win=False

# 4-intro


name=input("enter your name : ")
print(f"Hi {name} ,lets play the Hangman !")


# 5-loop


while wrong< max_wrong and not win:
      letter=input("enter a letter : ").lower()

      if letter in guessed_letter:
        print ("letter  already exists")
        continue
      guessed_letter.add(letter)
    
      if letter in word:
        print("correct guess")

        for i,char in enumerate(word):
          
          if char==letter:
            display[i]=letter

        print("current word :"," ".join(display))

      else:
         wrong+=1
         print("incorrect guess")
         print("\n".join(stages[:wrong+1])) 


      if "_" not in display:
       win=True
     
# 6- result 
if win:
   print(f"you won, you guessed the correct {word}")
else:
     print("you loose")       
           

