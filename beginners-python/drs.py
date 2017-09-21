drs_team = ["Micah", "Devin", "Matt", "Rachel", "Sarah"]

if drs_team[0] == "Micah":
    print(drs_team[0] + " is the director.")
elif drs_team[0] == "Sarah":
    print(drs_team[0] + " is leading this workshop.")
else:
    print(drs_team[0] + " is a really good colleague.")
    
for team_member in drs_team:
    if team_member == "Micah":
        print(team_member + " is the director.")
    elif team_member == "Sarah":
        print(team_member + " is leading this workshop.")
    else:
        print(team_member + " is a really good colleague.")
        
courses = ["Biology", "Shakespeare", "Symbolic Logic", "Chaucer", "Astronomy"]

for course in courses:
  print('I\'m taking ' + course + ' this semester')
  
courses = {"Biology": "Monday", "Shakespeare": "Tuesday", "Symbolic Logic": "Wednesday", "Chaucer": "Thursday", "Astronomy": "Friday"}

for course, day in courses.items():
  print(course + " meets on " + day)
  
for i in range(1, 11):
  print("I'm at number " + str(i))