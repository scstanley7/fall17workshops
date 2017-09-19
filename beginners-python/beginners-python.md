# Python for Beginners
## September 19th, 2017
## Led by Sarah Stanley

Today we will learn:

* Basic Python vocabulary
* Creating Variables
* Datatypes
* Intro to for loops
* If, else statements
* Basic troubleshooting

What we *wont* learn today:

* Advanced Python
* The different modules and libraries

**SET UP AN ACCOUNT WITH DHBOX**

Go to http://dhbox.org and set up an account for the amount of time you think you would like to use it (definitely get a month-long account if you plan on attending future workshops in this series)

### Creating Variables

`my_variable = “test”`

`my-variable = “Another test”`

`variable1 = 17`

`1stvariable = “Hello World!”`

`variable2 = hello world`

### Lists and Dictionaries

#### Lists:

`["every", "object", "is", "separated", "by”, "a", "comma"]`

`lost = [4, 8, 15, 16, 23, 42]`

`hitchhiker = ["the", "answer", "to", "life", "the", "universe", "and", "everything", "is", 42]`

Appending to lists:

`list_variable.append("new list item")`

Getting information about list items:

`list_variable[1]`

`type(list_variable[1])`

#### Dictionaries:

```
wizard_info = {"name": "Harry Potter", "education": "Hogwarts", "address": "Cupboard Under the Stairs, 4 Privet Drive, Little Whinging, Surrey"}
```

What happens if we try to get the third key:value pair from the dictionary?

`wizard_info[2]`

Try displaying the whole dictionary again. Why do you think the above code didn't work?

Appending to dictionaries:

`wizard_info['age'] = 37`

### for loops

```
drs_team = ["Micah", "Devin", "Matt", "Rachel", "Sarah"]
for team_member in drs_team:
	print(team_member)
```

```
for team_member in drs_team:
  print(team_member + " is a pretty cool person.")
```

```
hurricanes = {"Arlene": "Tropical Storm", "Bret": "Tropical Storm", "Cindy": "Tropical Storm", "Don": "Tropical Storm", "Emily": "Tropical Storm", "Franklin": "Category 1", "Gert": "Category 2", "Harvey": "Category 4", "Irma": "Category 5", "Jose": "Category 1", "Katia": "Category 2", "Lee": "Tropical Storm", "Maria": "Category 5"}
```

```
for name, strength in hurricanes.items():
  print(name + " is a " + strength)
```
  
### if, elif

`drs_team = ["Micah", "Devin", "Matt", "Rachel", "Sarah"]`

```
if drs_team[0] == "Micah":
    print(drs_team[0] + " is the director.")
elif drs_team[0] == "Sarah":
    print(drs_team[0] + " is leading this workshop.")
else:
    print(drs_team[0] + " is a really good colleague.")
```

Combining for loops with if/else statements:    

```
for team_member in drs_team:
    if team_member == "Micah":
        print(team_member + " is the director.")
    elif team_member == "Sarah":
        print(team_member + " is leading this workshop.")
    else:
        print(team_member + " is a really good colleague.")
```