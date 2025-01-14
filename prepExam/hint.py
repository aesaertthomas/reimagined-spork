from datetime import datetime

#Hint: str ---> datetime
test = "2015-01-31"
my_date = datetime.strptime(test, '%Y-%m-%d')
print(my_date)
