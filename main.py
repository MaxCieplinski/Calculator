from calculations import Calculations

while True:
    calculation = input("Calculator : ")
    
    try:
        result = Calculations.calculate(calculation)
        print(result)
    except:
        print('Error')