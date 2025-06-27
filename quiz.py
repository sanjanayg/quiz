print("welcome to the game!!!")
score=0
user=input("print yes if you want to continue else no: ")
if user!='yes':
    print("ouch :(")
    quit()
print("cool!!! Then let's start the game :) ")
print("1. guess the output: print(5 + 3)")
print('''
A. 53
B. 8
C. 5 + 3
D. Error''')
q1=input("enter your option")
if q1=="B" or q1=='b':
    score+=1
print("2. Which symbol is used to start a comment in Python?")
print('''
A. //
B. #
C. <!--
D. --''')
q2=input()
if q2=="B" or q2=='b':
    score+=1

print("3. What is the correct way to create a string in Python?")
print('''A. "Hello"
B. 'Hello'
C. """Hello"""
D. All of the above''')
q3=input("enter the correct option")
if q3=="D" or q3=='d':
    score+=1

print("4. What does the print() function do?")
print('''A. Reads input
B. Prints output
C. Defines a variable
D. Opens a file''')
q3=input("enter the correct option")
if q3=="B" or q3=='b':
    score+=1

print("5. Which one is a Python data type?")
print('''A. number
B. int
C. digit
D. character''')
q3=input("enter the correct option")
if q3=="B" or q3=='b':
    score+=1

print("6. Which of the following is a correct variable name in Python?")
print('''
A. 2name
B. name@
C. name_1
D. name space''')
q3=input("enter the correct option")
if q3=="C" or q3=='c':
    score+=1

print("7. How do you take input from the user in Python?")
print('''A. scan()
B. cin>>
C. input()
D. read()''')
q3=input("enter the correct option")
if q3=="C" or q3=='c':
    score+=1

print('''8. What will be the output of: print("Python" * 2)''')
print('''A. Python2
B. Python Python
C. PythonPython
D. Error''')
q3=input("enter the correct option")
if q3=="C" or q3=='c':
    score+=1

print("9. Which keyword is used to define a function?")
print('''A. function
B. fun
C. define
D. def''')
q3=input("enter the correct option")
if q3=="D" or q3=='d':
    score+=1

print("""10. What is the output of: print(len("hello"))""")
print('''A. 4
B. 5
C. 6
D. Error''')
q3=input("enter the correct option")
if q3=="B" or q3=='b':
    score+=1

print(f'Your score is {score} out of 10')
if score>=8:
    print(f"Hurray!!! {score}")
if score<=5:
    print("Its ok better luck next time")