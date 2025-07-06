#1.
s = "Programming"
# Extract the substring "gram" using slicing
substring = s[3:7]
print("Slicing from 3 to 7:", substring)
# Extract the last character using a negative index
last_char = s[-1]
print("Last character:", last_char)
# Print the characters from position 3 to 7 (inclusive)
print("Characters from position 3 to 7:", s[3:8])

#2.
text = " Hello, World! "
# 1. Remove spaces from the beginning and end (trim spaces)
trimmed_text =text.strip()
print("After trimming spaces:", '"' + trimmed_text + '"')
# 2. Convert the entire text to lowercase
lower_text = trimmed_text.lower()
print("Lowercase text:", lower_text)
# 3. Replace the word "World" with "Python"
replaced_text = trimmed_text.replace("World", "Python")
print("After replacing 'World' with 'Python':", replaced_text)

#3. 
txt = "Python is fun"
# Check if "fun" is in the string
contains_fun = "fun" in txt
print("Contains 'fun':", contains_fun)
# Check if the string starts with "Py"
starts_with_py = txt.startswith("Py")
print("Starts with 'Py':", starts_with_py)

#4.
fruits = "apple-banana-cherry"
# Split the string into a list using the '-' delimiter
fruits_list = fruits.split("-")
print("List of fruits:", fruits_list)  # Output: ['apple', 'banana', 'cherry']
# Join the list elements into a string using the '-' delimiter
fruits_str = "-".join(fruits_list)
print(fruits_str)  # Output: apple-banana-cherry


#5
name = "Ahmed"
age = 25
score = 95.5
sentence = "{} is {} years old and scored {}".format(name, age, score)
print(sentence)

#6 
num = 1234567.89
# Currency format with commas and dollar sign at the end
formatted_currency = f"{num:,.2f}$"
print(formatted_currency)
# Number with 4 decimal places
formatted_decimal = f"{num:.4f}"
print(formatted_decimal)


#7 
s = "Hello, Python!"
# 2. Count the occurrences of the letter "o"
count_o = s.count("o")
print("Number of 'o':", count_o)
# 3. Length of the string
length_s = len(s)
print("Length of the string:", length_s)
# 4. Count the number of spaces
count_spaces = s.count(" ")
print("Number of spaces:", count_spaces)


#8 
def clean_text(txt):
    # List of punctuation marks we want to remove
    punctuation = [',', '.', '?', '!', ':'] 
    # Remove all digits from the text
    no_digits = ''.join(char for char in txt if not char.isdigit())  
    # Remove all punctuation marks
    cleaned = ''.join(char for char in no_digits if char not in punctuation)   
    # Remove leading and trailing spaces
    return cleaned.strip()
text = ":Hello! 123 World."
result = clean_text(text)
print(result)


#9 
# 1. Using triple quotes
text1 = """Name: Ahmed
Age: 25
Country: Egypt"""

# 2. Using escape characters (\n)
text2 = "Name: Ahmed\nAge: 25\nCountry: Egypt"

# 3. Using format method to generate the string
text3 = "Name: {}\nAge: {}\nCountry: {}".format("Ahmed", 25, "Egypt")

# Print the results
print("Using triple quotes:")
print(text1)
print("\nUsing escape characters:")
print(text2)
print("\nUsing format method:")
print(text3)


