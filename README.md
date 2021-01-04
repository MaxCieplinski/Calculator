# Calculator
Complex calculator built and developed with python. Supports calculating brackets, powers, multiplication and division, addition and subtraction from equations taken from input and some different methods like simplification (e.g +- to -) and tokenization
## Example
Examples of the usage
```
input -> 2+2, output -> 4
input -> 2^2^2, output -> 16
input -> 2*(2+-4)^2, output -> 8
input -> 2*(2^2^2)/16, output -> 2
input -> (2+(2+(2+(2+(2+(2+2)))), output -> 14
input -> 4+-2, output -> 2
input -> 5!, output -> 120
input -> (2+2)!, output -> 24
...
```
# Configuration/Installation
## Platforms
Code should compile with python 3.x on these platforms : 
- Windows
- MacOS
- Linux

## Getting or updating the code
To get the code :
- Clone the repository with `git clone https://github.com/MaxCieplinski/Calculator.git`
- Download the latest release it with the green button `Download`

In order to update existing code open the terminal and write :
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
    try:
        result = Calculations.calculate(calculation)
        print(result)
    except:
        print('Error')
```

# Issues
If you have found any bug/s make sure to first check if they already hadn't been reported in `issues` and if not, 
feel free to note them down in `issues`

# Contribution
If you have any new ideas for new features or improvements feel free to note them down in pull requests 

# Contact
Feel free to contact me via email (`max.cieplinski@gmail.com`) or discord (`Maxi#2392`)
