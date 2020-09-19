def displaywelcome():
    print("This program will convert a range of temperature")
    print("enter (F) to convert  F to  C")
    print("enter (C) to convert  C to  F")
    
def getconvertTo():
    which=input('enter selection')
    while which != 'F' and which != 'C':
        which=input('enter selection:')
        return which
    
def displayFahrentoCelsius(start,end):
    print('Degree','Degree')
    print('Fahrent','Celsius')
    
    for temp in range(start,end+1):
        converted_temp=(temp-32)*5/9
        print(' ',format(temp,'4.1f'),' ',format(converted_temp,'4.1f'))
        
def dispalyCelsiustoFahren(start,end):
     print('Degree','Degree')
     print('Celsius','Fahrent')
    
     for temp in range(start,end+1):
        converted_temp=(9/5*temp)+32
        print(' ',format(temp,'4.1f'),' ',format(converted_temp,'4.1f'))
        
displaywelcome()
which=getconvertTo()
temp_start=int(input("enter starting temperature to convert :"))
temp_end=int(input("enter ending temperature to convert :"))
if which=='F':
    displayFahrentoCelsius(temp_start,temp_end)
else:
   dispalyCelsiustoFahren(temp_start,temp_end)
    
