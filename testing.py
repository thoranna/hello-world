#ASSIGNMENT 1

#QUESTION1

#speed_of_light = 300000000 #m/s

#mass_object_str = input('Mass of object: ')
#mass_object_float = float(mass_object_str)

#e = mass_object_float*(speed_of_light**2)#e=mc^2

#print('e=',e)

#QUESTION2

#digits_str = input('Input a string of digits: ')

#digits_int = int(digits_str)

#print(digits_int)

#digits_float = float(digits_str)

#print(digits_float)

#QUESTION3

#QUESTION 4

#weight_kg = int(input('Weight in kg: '))
#height_cm = int(input('Height in cm: ' ))

#height_m = height_cm*0.01

#bmi = weight_kg/(height_m**2)

#print(bmi)

#QUESTION 5

#input_int=int(input('Input a six-digit integer: '))

#QUESTION 6

#int_sec = int(input('Seconds: '))

#hours = int_sec//60*60

#minutes = (int_sec%60*60)//60

#sec = int_sec%60

#PROJECT 2

#input_int = int(input('Input an integer: '))

#if input_int>0 or input_int<0:
    #print('True')
#else:
    #print('False')

#number_int = int(input('Input a number: '))

#if number_int<0:
    #print('Negative')
#elif number_int>0:
    #print('Positive')
#else:
    #print('Zero')

#QUESTION 3

#number1_int = int(input('Input the first number: '))

#number2_int = int(input('Input the second number: '))

#number3_int = int(input('Input the third number: '))

#if number1_int>number2_int and number1_int>number3_int:
    #print(number1_int)
#elif number2_int>number1_int and number2_int>number3_int:
    #print(number2_int)
#else:
    #print('Largest number is: ', number3_int)

#QUESTION 4

#grade_float = float(input('Input grade: '))

#if grade_float>10.0 or grade_float<0.0:
    #print('Invalid grade!')
#elif grade_float<5.0:
    #print('Failing grade')
#else:
    #print('Passing grade')

#QUESTION 5

#year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
#if year%4!=0:
    #print('False')
#elif year%4==0 and year%100!=0:
    #print('True')
#elif year%4==0 and year%100==0 and year%400!=0:
    #print('False')
#elif year%4==0 and year%100==0 and year%400==0:
    #print('True')

#QUESTION 6

#d1_int = int(input('Input d1: '))
#d2_int = int(input('Input d2: '))

#if d1_int>6 or d1_int<1:
    #print('Invalid input')
#elif d2_int>6 or d2_int<1:
    #print('Invalid input')

#if d1_int+d2_int==7 or d1_int+d2_int==11: 
    #print('Winner')
#elif d1_int+d2_int==2 or d1_int+d2_int==3 or d1_int+d2_int==12:
    #print('Loser')
#else:
    #print('The sum: ', d1_int+d2_int)

#age_int = int(input('Age: '))

#ticket_price = 30

#if age_int>=65 or age_int<=5:
    #ticket_price = ticket_price*0.5
    #print(ticket_price)
#else:
    #print(ticket_price)

#ASSIGNMENT 3

#QUESTION 1

#num = int(input('Input a number: '))

#n = 0

#while num-1!=n: 
    #n+=1
    #print(n)

#QUESTION 2

#num = int(input('Input a number: '))

#n = 1

#while num!=n:
    #n+=1
    #if n%2!=0:
        #print(n)

#QUESTION 3

#num = int(input('Input a number: '))
#summa = 0

#while num!=10:
    #summa+=num
    #num = int(input('Input a number: '))
#print(summa)

#QUESTION 4

#num = int(input('Input a number: '))

#n = 0

#while n<=num: 
    #n+=1
    #if num%n==0:
        #print(n)

#QUESTION 5

#num = int(input('Input a number: '))

#n = 0

#prime = 0

#while n<num:
    #n+=1
    #if num%2==0 and num%3!=0:
        #prime = 0
    #else:
        #prime = 1

#if prime:
    #print('Prime')
#else: 
    #print('Not prime')

#QUESTION 6

#ASSIGNMENT 4

#num = int(input('Input a number: '))

#for i in range(1,num):
    #print(i)

#QUESTION 2

num = int(input('Input a number: '))

for i in range(1,num+1,2):
    print(i)

#QUESTION 3

#64 kassar í chessboard

#squares = 64

#grains = 1

#sum_of_grains = 0

#for i in range (1,squares+1):
    #sum_of_grains +=grains
    #grains = grains*2

#print(sum_of_grains)

#QUESTION 4

#num_1 = int(input('Input first number: '))

#num_2 = int(input('Input second number: '))

#GCD = 0

#for i in range(1,num_1+1):
    #if num_1%i==0 and num_2%i==0: 
        #GCD = i

#print(GCD)

#QUESTION 5

#num = int(input('Input a number: '))

#counter = 0

#for i in range(1, num+1):
    #counter+=i
    #print(counter)

#QUESTION 6

#n = int(input('Input a number: '))

#perf_num = 0 

#for i in range(1,n+1)
    #perf_num = 0

    #for j in range(1,i) 
        #if i%j==0:
            #perf_num = perf_num+j
    #if perf_num = i:
        #print(i)

