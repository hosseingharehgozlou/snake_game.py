age =39
name ='john' 
print('my name is ' , name , 'and my age is ' ,age)
from datetime import date
current_year = date.today().year
birth_year = current_year - age
print('I was born in', birth_year)