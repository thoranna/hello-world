#QUESTION 1

#age_int = int(input('Enter your age: '))

#if age_int>=0 and age_int<=34:
    #print('Young')
#elif age_int>=35 and age_int<=50:
    #print('Mature')
#elif age_int>=51 and age_int<=69:
    #print('Middle-aged')
#else: 
    #print('Old')

#QUESTION 2

#for i in range(100,1000): #i is any integer between 100 and 999
    #if i%17==0: #if i is divisible by 17 it's printed out
        #print(i)

#QUESTION 3

first_int = int(input('First: '))

step_int = int(input('Step: '))

sum_of_series = 0 

#values start at the first integer minus the step
values_in_series = first_int-step_int
    
for i in range(first_int, 100):
    #add the step in the first loop of the for-loop
    values_in_series+=step_int
    print(values_in_series, end=' ')
    sum_of_series += values_in_series
    if sum_of_series>=100:
        break

print(' ')
print('Sum of series: ', sum_of_series)

#ATH PRENTA ÞETTA ÚT ALLT Í RÖÐ HVERNIG

#QUESTION 4

#stars_int = int(input('Number of stars: '))

#for loop ends when i=stars_int
#for i in range(1, stars_int+1):
    #print the star as a str multiplied with i 
    #print('*'*i)

