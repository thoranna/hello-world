enter_int = int(input('Enter an integer: ')) #notandi slær inn tölu 

total_sum = 0 #summan byrjar í núll

counter_even = 0 #teljari fyrir sléttar tölur

counter_odd = 0 #teljari fyrir oddatölur

largest_number = 0 #stærsta talan byrjar í núll

while enter_int > 0: 
    total_sum = enter_int + total_sum
    print('Cumulative total: ',total_sum) #prentar summu
    
    if enter_int>largest_number:
        largest_number=enter_int

    enter_int = int(input('Enter an integer: ')) #notandi slær inn nýja tölu
        
    if enter_int%2 == 0: 
        counter_even += 1  
    
    else:
        counter_odd += 1 
    
    if enter_int <= 0
        print('Largest number: ',largest_number)
        print('Count of even numbers: ',counter_even)
        print('Count of odd numbers: ',counter_odd)






