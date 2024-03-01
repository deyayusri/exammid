

#q2
print(2+3*6/2)

#q3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#q4
# D  because this number is not a palindrome because it is different when read backward.

#q5
def find_pattern_occurrences(text):
    pattern = "C"
    match_count = 0

    # Iterate through the text
    for i in range(len(text)):
        # Check if the current character matches the start of the pattern
        if text[i] == pattern[0]:
            # Check if the subsequent characters form the rest of the pattern
            if text[i:].startswith(pattern) and text[i:].endswith("jeb"):
                match_count += 1

    return match_count

#q6
# Mutable list
mutable_list = [1, 2, 3, 4]

# Modifying the list
mutable_list[0] = 5
print("Mutable list after modification:", mutable_list)

# Immutable string
immutable_string = "programinglord"

# Trying to modify the string (will result in an error)
# immutable_string[0] = 'H'  # This line will cause an error

# Concatenating strings instead of modifying
new_string = 'THEPRO' + immutable_string[3:]
print("New string after concatenation:", new_string)

#q7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)

# Removing odd numbers and doubling even numbers
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 != 0:
        random_numbers[i] = None  # Mark odd numbers for removal
    else:
        random_numbers[i] *= 2

# Remove None values (odd numbers) from the list
random_numbers = [num for num in random_numbers if num is not None]

print("Modified list:", random_numbers)

#q8
def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://' and has at least one '.' after that
    if url.startswith("http://") or url.startswith("https://"):
        if '.' in url[url.index("//")+2:]:
            return True
    return False

# Example usage:
url = "https://www.example.com"
print(is_valid_url(url))  # Output: True

url = "not_a_url"
print(is_valid_url(url))  # Output: False

#q9
from datetime import datetime


def days_passed_since_birthday(your_birthday):
    # Ask the user for their birthday
    user_birthday_str = input("Please enter your birthday (DD-MM-YYYY): ")
    user_birthday_date = datetime.strptime(user_birthday_str, "%d-%m-%Y")
    current_date = datetime.now()
    age = current_date.year - user_birthday_date.year
    total_days_passed = (current_date - user_birthday_date.replace(year=current_date.year)).days
    total_days_passed -= age * 365
    return total_days_passed

#example
user_birthday_date = "01-01-2000"  # Your birthday in "DD-MM-YYYY" format
print("Days passed since your birthday:", days_passed_since_birthday(user_birthday_date))

