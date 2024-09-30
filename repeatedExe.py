with open('Tv_Show1.csv', 'r') as file:
    # Skip the header line
    next(file)
    
    max_seasons = 0
    max_episodes = 0
    show_with_max_seasons = ""
    show_with_max_episodes = ""
    
    # Iterate through each line in the file
    for line in file:
        # Split the line by comma to extract fields
        fields = line.strip().split(',')
        
        # Extract the show name, number of seasons, and number of episodes
        show_name = fields[0]
        num_seasons = int(fields[1])
        num_episodes = int(fields[2])
        
        # Update the maximum seasons and episodes if necessary
        if num_seasons > max_seasons:
            max_seasons = num_seasons
            show_with_max_seasons = show_name
        
        if num_episodes > max_episodes:
            max_episodes = num_episodes
            show_with_max_episodes = show_name

# Print the results
print(f"Show with the most seasons: {show_with_max_seasons} ({max_seasons} seasons)")
print(f"Show with the most episodes: {show_with_max_episodes} ({max_episodes} episodes)")
