Simple Python Password Generator
A straightforward command-line utility for generating random passwords based on a user-defined length. 
This project serves as an excellent basic example of utilizing the Python standard library for randomization and character manipulation.

Features
Custom Length: Allows the user to specify the desired length of the generated password.
Broad Character Set: Generates passwords using a wide range of characters, including uppercase letters, lowercase letters, numbers, and common symbols.

How It Works (Code Logic Explained)
The core functionality of this generator relies on two key Python concepts: the random module and ASCII values.

1. The random Module
The script imports the built-in random module. 
The function random.randint(a, b) is used to select a random integer between the lower bound ($a$) and upper bound ($b$), inclusive.

2. Character Generation using ASCII
The generator creates a password character by character in a loop that runs for the specified length. In each iteration:

A random integer is chosen between 33 and 126.
This range, 33-126, corresponds to the printable characters in the standard ASCII table. This covers almost all commonly used symbols, digits (0-9), and all upper- and lowercase English letters.

The built-in Python function chr() is used to convert the randomly selected integer (the ASCII code) back into its corresponding character.
The resulting character is appended to the final password string.

3. Output
Finally, the completed, randomized string is printed to the console as the generated password.
