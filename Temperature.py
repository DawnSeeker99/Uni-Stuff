def celsiusCon(farenheit):
   return (farenheit - 32)*(5/9)

def farenheitCon(celsius):
   return ((celsius*(9/5)) + 32)

while True:
    try:
        temp = input('Enter your starting temperature.')
        temp_float = float(temp[0:-1])
        temp_type = temp[-1].upper()
        if temp_type == 'C' :
            celsius = temp_float
            print(temp, 'is', farenheitCon(celsius), 'F')
            break
        elif temp_type == 'F':
            farenheit = temp_float
            print(temp, 'is', celsiusCon(farenheit), 'C')
            break
        else:
            print('Please enter a temperature in the format 15C or 15F')
    except ValueError :
            print('Please enter a temperature in the format 15C or 15F')