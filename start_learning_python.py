print("Hello World")

print("Reza")

print(6+5)

calculation = 5+6

print(calculation)

float_number = 5.7

print(type(float_number))

names = "Reza" + " " + "Mollaei"

print(names)

print(names.lower())

# input_name = input("What is your name? ").capitalize()

# print("hello ", input_name)

bool = False

print(type(bool))

def ask_name():
    input_name = input("What is your name? ").capitalize()
    return input_name

# print(ask_name())

def calculate_expenses(expenses):
    sum_total = sum(expenses)
    return sum_total

exp = [52.5 , 29 , 10.25]

# print(calculate_expenses(exp))

command = "expenses"

if command == "expenses":
    print(calculate_expenses(exp))
elif command == "ask_name":
    ask_name()
else:
    print("invalid command")

def calculate_savings(income, expenses):
    savings = income - expenses
    return f"Total saving: ${savings: .2f}"

square =[]
for i in range(10):
    square.append(i**2)

print(square)

coordinate = [(x,y) for x in range(3) for y in range(3)]
print("coordinates: ",coordinate)


Double = lambda x: x*2
print(Double(5))


def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6]
even_numbers = list(filter(is_even,numbers))
print(even_numbers)


sqr = list(map(lambda x:x*x , numbers))
print("squared number: ",sqr)


from functools import reduce

total = reduce(lambda x,y: x + y , numbers)
print("Total sum: ",total)



def log_function_run(func):
    def wrapper(*args , **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@log_function_run
def getFlights():
    print("Fetching flight details...")

@log_function_run
def printPrices():
    print("printing prices...")

getFlights()
printPrices()
