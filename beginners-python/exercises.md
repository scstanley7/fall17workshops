# Exercises

1. Create a list of courses you're taking this semester. Use a for loop to create a series of sentences that say "I'm taking *course* this semester."

2. Turn the above list into a dictionary, where the course name is the key, and the values are the days of the week that it meets. Create a for loop that will create a list of sentences that say "*course name* meets on *day[s] of the week*"

3. You can create a range of numbers in Python:
  `list(range(1,10))`
  
play around with this for a bit. What does `list(range(1,10,2))` do?

4. You can create for loops for loops with ranges. How would you create a for loop that says "I'm at number *n*"? *Hint: You will need to use "str" to return the number in the range as a string rather than an integer*

5. In addition to using "==" for equivalency, you can also use ">", "<", "<=", and ">=". Try to create an if/else statement that lists of whether the numbers in the range 1 through 25 are greater than or equal to 15.

## Answers

1. 
`courses = ["Biology", "Shakespeare", "Symbolic Logic", "Chaucer", "Astronomy"]`

```
for course in courses:
  print("I'm taking " + course + " this semester")
```
  
**Remember: the straight single quote is often used to designate that something is a string. If you are going to use the single quote method, you need to escape the apostrophe in "I'm":**

```
for course in courses:
  print('I\'m taking ' + course + ' this semester')
```
  
2. 
```
courses = {"Biology": "Monday", "Shakespeare": "Tuesday", "Symbolic Logic": "Wednesday", "Chaucer": "Thursday", "Astronomy": "Friday"}
```

```
for course, day in courses.items():
  print(course + " meets on " + day)
```
  
4. 
```
for i in range(1, 11):
  print("I'm at number" + str(i))
```
  
5. 
```
for i in range(1, 26):
  if i < 15:
    print(str(i) + " is less than 15")
  elif i == 15:
    print(str(i) + " is equal to 15")
  else:
    print(str(i) + " is greater than 15")
```
