import re

# Sample list of CVs with qualifications
cvs = [
    "I have a Bachelor's degree in Computer Science.",
    "Master's in Business Administration from XYZ University.",
    "Completed a diploma in Marketing.",
    "I hold a PhD in Economics.",
]

# Predetermined qualification to compare against
predetermined_qualification = "Bachelor's degree in Computer Science"

# Function to check if a CV meets the predetermined qualification
def meets_qualification(cv, predetermined_qualification):
    return re.search(predetermined_qualification, cv, re.IGNORECASE) is not None

# List to store CVs that meet the predetermined qualification
matching_cvs = []

# Check each CV
for cv in cvs:
    if meets_qualification(cv, predetermined_qualification):
        matching_cvs.append(cv)

# Print the CVs that meet the predetermined qualification
print("CVs that meet the predetermined qualification:")
for cv in matching_cvs:
    print("- " + cv)
