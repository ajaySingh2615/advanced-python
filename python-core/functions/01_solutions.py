# write a function that squares a number

def square_of_num(number):
    return number * number


# print(square_of_num(4))

sum_of_two_numbers = lambda x, y: x+y

# print(sum_of_two_numbers(2, 2))

# write a function that takes varible number of arguments and returns their sum
def summ_all(*args):
    return sum(args)

# print(summ_all(1, 2))
# print(summ_all(1, 2, 3, 4, 5))
# print(summ_all(1, 2, 3, 4, 5, 6, 7, 8))

# create a functions that accepts any number of keywords arguments and prints them in the format key: value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_kwargs(name="mike", power="love")
# print_kwargs(power="love")
# print_kwargs(power="love", name="eleven")
# print_kwargs(power="love", name="eleven", emeny="mindflayer")

# yield
