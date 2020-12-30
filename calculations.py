numbers = '0123456789'
signs = '%^*()/+-='

def _convert_to_int(string):
    try:
        return int(string)
    except Exception:
        return None

class Calculations:
    @staticmethod
    def tokenize(equation : str):
        tokenized_equation = []
        number = ''
        for i in equation:
            if _convert_to_int(i) != None:
                number = number + i
            elif i in signs and number != '':
                tokenized_equation.append(number)
                number = ''
                tokenized_equation.append(i)
            elif i in signs and number == '':
                tokenized_equation.append(i)
        if number != '':
            tokenized_equation.append(number)

        return tokenized_equation

    @staticmethod
    def calculate(equation : str):
        tokenized_equation = Calculations.tokenize(equation)
        simplified_equation = Calculations.simplify(tokenized_equation)
        done_equation = Calculations.__addition_and_subtraction(Calculations.__multiplication_and_division(Calculations.__power(Calculations.__brackets(simplified_equation))))
        return done_equation[0]
        
    @staticmethod
    def simplify(equation : list):
        #Get rid of situations like : ["10", "+", "-", "10"]
        simplified_equation = []
        skip = False
        for idx, i in enumerate(equation):
            if _convert_to_int(i) != None:
                skip = False
                simplified_equation.append(i)
            if i in signs.replace("+-", ''):
                skip = False
                simplified_equation.append(i)
            if i == '+' or i == '-':
                if idx + 1 < len(equation):
                    if equation[idx + 1] == '+' or equation[idx + 1] == '-':
                        skip = True
                        if i == '+' and equation[idx + 1] == '+':
                            simplified_equation.append('+')
                        if i == '+' and equation[idx + 1] == '-':
                            simplified_equation.append('-')
                        if i == '-' and equation[idx + 1] == '+':
                            simplified_equation.append('-')
                        if i == '-' and equation[idx + 1] == '-':
                            simplified_equation.append('+')
                        skip = True
                    elif skip == False:
                        simplified_equation.append(i)
                else:
                    simplified_equation.append(i)

        return simplified_equation

    @staticmethod
    def __addition_and_subtraction(equation : list):
        new_equation = []
        skip = False
        for idx, i in enumerate(equation):
            if skip == False:
                if not i in '+-':
                    new_equation.append(i)
            skip = False
            if i == '+':
                result = int(new_equation.pop()) + int(equation[idx + 1])
                new_equation.append(str(result))
                skip = True
            elif i == '-':
                result = int(new_equation.pop()) - int(equation[idx + 1])
                new_equation.append(str(result))
                skip = True

        return new_equation

    @staticmethod
    def __multiplication_and_division(equation : list):
        new_equation = []
        skip = False
        for idx, i in enumerate(equation):
            if skip == False:
                if i not in '*/':
                    new_equation.append(i)
            skip = False
            if i == '*':
                result = int(new_equation.pop()) * int(equation[idx + 1])
                new_equation.append(str(result))
                skip = True
            elif i == '/':
                result = int(new_equation.pop()) / int(equation[idx + 1])
                new_equation.append(str(result))
                skip = True

        return new_equation

    @staticmethod
    def __brackets(equation : list):
        new_equation = []
        calculation_list = []
        start_idx = None
        counter = 0
        for idx, i in enumerate(equation):
            if i == "(":
                start_idx = idx
            if start_idx == None:
                new_equation.append(i)
            else:
                calculation_list.append(i)
                if i == ")":
                    start_idx = None
                    for idx, i in enumerate(calculation_list):
                        if i == ")" or i == "(":
                            calculation_list.pop(idx)
                    #Calculate the list
                    calculation_list = Calculations.__addition_and_subtraction(Calculations.__multiplication_and_division(Calculations.__power(calculation_list)))
                    new_equation.insert(idx + counter + 1, calculation_list[0])
                    calculation_list.clear()
                    counter += 1

        return new_equation

    @staticmethod
    def __power(equation : list):
        new_equation = []
        skip = False
        for idx, i in enumerate(equation):
            if i == "^" and equation[idx - 2] == '^':
                result = int(new_equation.pop()) ** int(equation[idx - 1])
                new_equation.append(str(result))
            elif i == "^":
                result = int(equation[idx - 1]) ** int(equation[idx + 1])
                new_equation.append(str(result))
                skip = True
            if i in signs.replace('^', ''):
                new_equation.append(i)
                skip = False
            if skip == False:
                if _convert_to_int(i) != None and idx + 1 < len(equation):
                    if equation[idx + 1] != '^':
                        new_equation.append(i) 
                if idx == len(equation) - 1:
                    new_equation.append(i)

        return new_equation 
