import csv

# Initialize variables to store the TV show with the most seasons and episodes
most_seasons_show = None
most_seasons_count = 0
most_episodes_show = None
most_episodes_count = 0

# Read the CSV file
with open('TV_show_data (2).csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Convert the Total Seasons and Total Episodes to integers
        total_seasons = int(row['Total Seasons'])
        total_episodes = int(row['Total Episodes'])
        
        # Check for the most number of seasons
        if total_seasons > most_seasons_count:
            most_seasons_count = total_seasons
            most_seasons_show = row['Name']
        
        # Check for the most number of episodes
        if total_episodes > most_episodes_count:
            most_episodes_count = total_episodes
            most_episodes_show = row['Name']

# Print the results
print(f"The TV show with the most number of seasons is '{most_seasons_show}' with {most_seasons_count} seasons.")
print(f"The TV show with the most number of episodes is '{most_episodes_show}' with {most_episodes_count} episodes.")
