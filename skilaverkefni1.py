population_now = 307357870

#60 sek
#60 min
#24 klst
#365 dagar

sec_year = 60*60*24*365  #sek í ári

birth_year = sec_year/7 #fæðingar á ári

death_year = sec_year/13 #dauðsföll á ári

immigrant_year = sec_year/35 #innflytjendur á ári

change_year = (birth_year+immigrant_year-death_year) #breyting á einu ári

year_str = input('Year:')

year_float = float(year_str) #breyti str í int

if year_float<0:
    print('Invalid input')

population_now = float((year_float*change_year)+population_now) #ár*breyting+fjöldi

population_now = int(population_now)

year_float = int(year_float)
    
print('New population after', year_float, 'years is', population_now)



