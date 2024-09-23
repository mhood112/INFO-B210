#conditionalExcutuion.py
csv_file_path = 'TV_Shows.csv'  # Replace with your actual CSV file path

def find_most_common_day(csv_file_path):
    day_counts = {}
    
    with open(csv_file_path, mode='r') as file:
        # Read the header line to find the index of the 'Schedule (days)' column
        header = file.readline().strip().split(',')
        day_index = header.index('Schedule (days)')
        
        # Read the rest of the lines
        for line in file:
            row = line.strip().split(',')
            days = row[day_index].split(';')  # Assuming multiple days are separated by semicolons
            
            for day in days:
                day = day.strip()
                if day in day_counts:
                    day_counts[day] += 1
                else:
                    day_counts[day] = 1
    
    # Find the most common day
    most_common_day = max(day_counts, key=day_counts.get)
    return most_common_day

most_common_day = find_most_common_day(csv_file_path)
print(f"The most common day for shows to be scheduled is: {most_common_day}")
