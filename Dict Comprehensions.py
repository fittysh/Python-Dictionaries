# Dict Comprehensions - allows you to combine two list in 1 dictionary

# Create a student list by name and height
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students)

# Create a employee list by name and employee numbers
employee_names = ["Fitri", "Khairul", "Yati", "Nik", "Fazrin", "Ananda"]
employee_numbers = [1404388, 1404289, 1404371, 1404677, 1404133, 1401288]
process_team = {key:value for key, value in zip(employee_names, employee_numbers)}
print(process_team)