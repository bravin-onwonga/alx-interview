# 0x0A. Prime Game

This project covers these concepts:

## Prime Numbers
This are numbers only divisible by one and the number itself.
While there are a number of methods to optimally find prime numbers in this project the method used will be  [Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/).

### Sieve of Eratosthenes
This method is the most effecient for finding prime numbers when ```n``` is less that 10 million. 
- First, we begin by listing all numbers between **2** and **n**.
- With all numbers being unmarked the first number is 2. We proceed by marking all numbers greater and divisible by 2
- This is repeated for all unmarked numbers until we are left only with prime numbers

**Time complexity**: ```O(N*log(log(N)))```
**Auxilliary Space**: ```O(N)```

## Dynamic Programming (Memoization)

Dynamic Programming tackles efficiency by preventing repetition. Take for example the ```Factorization Problem```. We can prevent repetition by storing the factors of n in a list so that if we get the same number it's complexity is ```O(N)```. Similarly, if the number is large than ***n*** we can break the recursive loop once we reach ***n***.

The con of it is that we need more space to store our list but this increase in space complexity is offset by the improved efficiency of the time complexity.

## Game Theory

Game Theory is the study of how and why individuals and entities make decisions about their situations.
The intention of game theory is to produce optimal decision-making of independent and competing actors in a strategic setting. 
Using game theory, real-world scenarios for such situations as pricing competition and product releases (and many more) can be laid out and their outcomes predicted.

## Python Lists

A python list is an array containing values that can be of one data-type or different data types. Lists values can be accessed through index beginning from ***0*** to the total number of the index (excluded).

If our list is [0, 1, 2, 3] then to access the last element we will use ***list[3]*** and to access the first element we will us ***list[0]*** .

Lists can also be accessed through loops i.e. ```for``` and ```while``` loops.


## File in this project

File | Description
---- | ------------
[0-prime_game.py](https://github.com/bravin-onwonga/alx-interview/blob/main/0x0A-primegame/0-prime_game.py) | Determines a winner between two contesants who pick out prime numbers lesser or equal to a number

## Requirements:
- Allowed editors:  ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- You cannot import any packages in this task
