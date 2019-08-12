import sys

mystring = list(input("enter a sentence: "))

while(True):
    print("Your sentence is: "+ str(mystring))
    inp = input("Do you want to change your sentence? Answer Y/N: ")
    
    if inp=="Y":
        print("Please use 'continue' to continue \n 'change' to change \n 'add to add \n 'exit' to exit\n 'print' to print \n 'swap' to swap \n 'delete' to delete")
        while(True):
            key = input("\n: ")
            if key == "exit":
                print(mystring)
                sys.exit(1)
            elif key == "change":
                ch = ""
                i = int(input("What is the posision of the word you want to change(count from 0): "))
                ch = input("what is the charecter you want to change with "+mystring[i]+": ")
                mystring[i] = ch
            elif key == "print":
                print("Your sentence is "+''.join(mystring))
            elif key == "add":
                i = int(input("What is the posision of the word you want to add(count from 0): "))
                ch = input("what is the character you want to add: ")
                mystring.insert(i,ch)
            elif key  == "swap":
                s1=int(input("What is the posision of words you want to swap?(count from 0): "))
                s2=int(input("What is the posision of words you want to swap?(count from 0): "))
                x=mystring.pop(s1)
                y=mystring.pop(s2-1)
                mystring.insert(s1,y)
                mystring.insert(s2,x)
            elif key == "delete":
                delKey=int(input("What is the posision of word you want to delete?(count from 0): "))
                mystring.pop(delKey) 
            else:
                print("please try again...")
    elif inp=="N":
        str(mystring)
        sys.exit(1)   
    else:
        print("please answer with Y for 'yes' or N for 'no'")
