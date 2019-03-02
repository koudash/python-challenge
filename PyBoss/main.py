"""
This is codes for PyBoss
"""
# Modules
import os
import csv
import datetime

# Python Dict to translate US states to two letter codes
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Define "append" funciton
def append(List, element):
    # Function appends an element to a list and returns the new list
    return List.append(element)

# Lists to store "Employ ID", "Name", "DOB", "SSN", and "State"
emp_id = []
name = []
dob = []
ssn = []
state = []

# Lists to store "First Name", "Last Name", adjusted "DOB", last four digits and "SSN", as well as "State" values, respectively
first_name = []
last_name = []
dob_adj = []
last_four_digit = []
ssn_adj = []
state_adj = []

# Set path for the location of original csv file
employee_path = os.path.join("Resources", "employee_data.csv")

# Open the csv file
with open(employee_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    # Loop through csvreader
    for row in csvreader:

        # Append all "Date" values to "date" list
        append(emp_id, row[0])
        append(name, row[1])
        append(dob, row[2])
        append(ssn, row[3])
        append(state, row[4])

    # Loop through list "name"
    # Note that 'first_name = list(i.split(" ")[0] for i in name)' also works
    for i in name:
        # Split each name in list by space, store first name and last name into "first_name" and "last_name" lists
        append(first_name, i.split(" ")[0])
        append(last_name, i.split(" ")[1])
    
    # Loop through list "dob"
    for i in dob:
        # Convert each DOB in list to Python striptime
        datetime_object = datetime.datetime.strptime(i, "%Y-%m-%d")
        # Output the DOB in mm-dd-yyyy format and store in "dob_adj" list
        append(dob_adj, datetime_object.strftime("%m/%d/%Y"))
    
    # Loop through list "ssn"
    for i in ssn:
        # Split each ssn in list by "-", store last four digits into "last_four_digit" list
        append(last_four_digit, i.split("-")[2])
    
    # Loop through "last_four_digit" list
    for i in last_four_digit:
        # Concatenate "***-**-" with last four digit (string) and store in "ssn_adj" list
        append(ssn_adj, "***-**-" + str(i))
    
    # Loop through "state" list
    for i in state:
        # Loop through dictionary "us_state_abbrev" and look for its key that match the element in "state" list 
        for key in us_state_abbrev:
            # Once matched, append the key's corresponding value to "state_adj" list
            if i == key:
                append(state_adj, us_state_abbrev[key])

# Zip lists together
employee_adj = zip(emp_id, first_name, last_name, dob_adj, ssn_adj, state_adj)

# Set path for the location of file to write to
output_path = os.path.join("Resources", "employee_data_adj.csv")

# Open the csv file in "write" mode
with open(output_path, "w", newline="") as newcsvfile:
    
    # Initialize cvs.writer
    writer = csv.writer(newcsvfile)
    
    # Write the first row (header)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write the zipped rows
    writer.writerows(employee_adj)