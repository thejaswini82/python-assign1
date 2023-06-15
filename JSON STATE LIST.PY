import json

# Dictionary of Indian states and capitals
state_capitals = {
    "Karnataka":"Banglore",
    "Andhra Pradesh": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow"
}

# Save the dictionary to the JSON file
with open("state_capitals.json", "w") as file:
    json.dump(state_capitals, file)

print("State capitals have been written to state_capitals.json.")
