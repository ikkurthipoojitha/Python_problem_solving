mins = 60
hins = 3600
dins = 86400
 
#Read the inputs from user
days    = int(input("Enter number of Days: "))
hours   = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))
 
#Calculate the days, hours, minutes and seconds
total_seconds = days * dins
total_seconds = total_seconds + ( hours * hins)
total_seconds = total_seconds + ( minutes * mins)
total_seconds = total_seconds + seconds
 
#Display the result
print("Total number of seconds: ","%d"%(total_seconds))
