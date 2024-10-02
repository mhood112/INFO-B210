#conditionalExecution.py
import csv

# Dictionary to count the frequency of each day
day_count = {}

# Read the CSV file
with open('TV_show_data (2).csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Extract the schedule days and clean the string
        schedule_days = row['Schedule (days)'].strip("[]").replace("'", "").split(", ")
        
        # Count the frequency of each day
        for day in schedule_days:
            if day in day_count:
                day_count[day] += 1
            else:
                day_count[day] = 1

# Find the most common day
most_common_day = max(day_count, key=day_count.get)

# Print the result
print(f"The most common day for a show to be scheduled is '{most_common_day}' with {day_count[most_common_day]} occurrences.")
