# Calculator
Complex calculator built and developed with python. Supports calculating brackets, powers, multiplication and division, addition and subtraction from equations taken from input and some different methods like simplification (e.g +- to -) and tokenization

# Configuration/Installation
## Platforms
Code should compile with python 3.x on these platforms : 
- Windows
- MacOS
- Linux

## Getting or updating the code
To get the code :
- Clone the repository with `git clone --recursive https://github.com/MaxCieplinski/Calculator.git`
- Download the latest release it with the green button `Download`

In order to update existing code use :
```
cd Calculator
git pull
git submodule update --init --recursive
```

# How to use
Whole projects consist of 2 files [`main.py`, `calculations.py`]. The main logic is in `calculations.py` in `Calculations` class. `main.py` is used for getting input, passing it into the imported class and printing the result. 
--> 
```py
from calculations import Calculations
while True:
    calculation = input("Calculator : ")
    result = Calculations.calculate(calculation)
    print(result)
```

# Issues
If you have found any bug/s make sure to first check if they already hadn't been reported in `issues` and if not, 
fell free to note them down in `issues`

# Contribution
If you have any new ideas for new features or improvements feel free to note them down in pull requests
