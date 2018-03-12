## Option 3: PyBoss HW

"""
Your task is to help bridge the gap by creating a Python script able to 
convert your employee records to the required format. 
#Your script will need to do the following:

1- Import the `employee_data1.csv` and `employee_data2.csv` files, 
which currently holds employee records like the below:
2- Then convert and export the data to use the following format instead:
"""

#import csv and datetime modules
import csv, datetime

# Files to load and output (Remember to change these)
file_to_load = "raw_data/employee_data1.csv"
file_to_output = "analysis/employee_data_reformatted1.csv"


# Dictionary of states with abbreviations
#http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.DictReader(emp_data)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row["Emp ID"]]

        # Grab names, split them, and store them in a temporary variable
        # ** https://docs.python.org/2/library/string.html  String.split(s[, sep[, maxsplit]])
        split_name = row["Name"].split(" ")

        # Then save first and last name in separate lists
        emp_first_names = emp_first_names + [split_name[0]]
        emp_last_names = emp_last_names + [split_name[1]]

        # Grab DOB and reformat it
        # ** http://strftime.org/
        reformatted_dob = datetime.datetime.strptime(row["DOB"], "%m/%d/%Y")
        reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")

        # Then store it into a list
        emp_dobs = emp_dobs + [reformatted_dob]

        # Grab SSN and reformat it
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        # Then store it into a list
        emp_ssns = emp_ssns + [joined_ssn]

        # Grab the states and use the dictionary to find the replacement
        # ** http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
        state_abbrev = us_state_abbrev[row["State"]]

        # Then store the abbreviation into a list
        emp_states = emp_states + [state_abbrev]

# Zip all of the new lists together
# **def zip(*iterables):    # zip('ABCD', 'xy') --> Ax By https://docs.python.org/3/library/functions.html#zip
empdb = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)

# Write all of the election data to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)
