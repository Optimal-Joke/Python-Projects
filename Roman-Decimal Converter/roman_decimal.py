# %%
from time import time_ns as time

symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


# %%
def roman_to_decimal(roman_numeral: str):
    total = 0
    for idx in range(len(roman_numeral)):
        symbol_value = symbol_values[roman_numeral[idx]]
        try:
            next_value = symbol_values[roman_numeral[idx+1]]
        except IndexError:
            next_value = 0
        
        if symbol_value >= next_value:
            total += symbol_value
        elif symbol_value <= next_value:
            total -= symbol_value
    
    return total

def decimal_to_roman(decimal_number: int):
    num_digits = len(str(decimal_number))

    dictionary = {}
    for exponent in range(0, num_digits):
        quotient = decimal_number % (10**(exponent+1))

        dictionary[10**exponent] = quotient
        decimal_number -= quotient

    return dictionary


# %%
t0 = time()

result = decimal_to_roman(9999)

t1 = time()

print(result, "\n")
print((t1-t0)/1e9, "seconds")
# %%
t0 = time()

result = roman_to_decimal("MMMMMMM")

t1 = time()

print(result, "\n")
print((t1-t0)/1e9, "seconds")
# %%
