import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Employee data in JSON format
employee_data = [
    {
        "Name": "John Doe",
        "DOB": "1990-05-15",
        "Height": 175,
        "City": "New York",
        "State": "New York"
    },
    {
        "Name": "Jane Smith",
        "DOB": "1985-08-21",
        "Height": 162,
        "City": "Los Angeles",
        "State": "California"
    },
    {
        "Name": "David Johnson",
        "DOB": "1993-03-10",
        "Height": 180,
        "City": "Chicago",
        "State": "Illinois"
    },
    {
        "Name": "Emily Wilson",
        "DOB": "1988-11-02",
        "Height": 168,
        "City": "Houston",
        "State": "Texas"
    },
    {
        "Name": "Michael Brown",
        "DOB": "1992-07-08",
        "Height": 185,
        "City": "Philadelphia",
        "State": "Pennsylvania"
    }
]

# Save employee data to the JSON file
with open("employee.json", "w") as file:
    json.dump(employee_data, file)

# Read employee data from the JSON file and create a list of Employee objects
employees = []
with open("employee.json", "r") as file:
    employee_data = json.load(file)
    for employee in employee_data:
        employees.append(Employee(employee["Name"], employee["DOB"], employee["Height"], employee["City"], employee["State"]))

# Print the list of Employee objects
for employee in employees:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
