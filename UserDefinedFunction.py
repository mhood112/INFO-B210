def most_common_schedule_time(file_path):
    """Find the most common schedule time for each genre."""
    genre_schedule = {}

    # Open the file and read the lines
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            
            # Identify the index of the genres and schedule time in the headers
            genre_index = 5  # Column 5 for genres
            schedule_time_index = 11  # Column 11 for schedule times

            for line in lines[1:]:
                # Split the lines into fields by the delimiter ,
                fields = line.strip().split(',')
                
                #checks for empty fields
                if len(fields) <= max(genre_index, schedule_time_index):
                    print(f"Skipping line due to insufficient fields: {line}")
                    continue

                genres_str = fields[genre_index].strip("[]").replace("'", "").replace('"', '')
                genres = [genre.strip() for genre in genres_str.split(',')]
                schedule_time = fields[schedule_time_index]

                # Debug prints to verify correct parsing
                #print(f"Parsed genres: {genres}")
                #print(f"Parsed schedule time: {schedule_time}")

                if not schedule_time:
                    print(f"Skipping line due to missing schedule time: {line}")
                    continue

                for genre in genres:
                    if genre not in genre_schedule: #checks if the genre is in the dictionary
                        genre_schedule[genre] = [] #if not, adds the genre to the dictionary
                    genre_schedule[genre].append(schedule_time) #appends the schedule time to the genre

        # Calculate the most common schedule time for each genre
        most_common_times = {}
        for genre, times in genre_schedule.items():
            if not times:
                continue  # Skip genres with no schedule times
            time_count = {}
            for time in times: #iterates through the schedule times
                if time not in time_count:
                    time_count[time] = 0
                time_count[time] += 1
                #initializes a dictionary to count the number of times a schedule time appears          
            most_common_time = max(time_count, key=time_count.get) # finds the most common schedule time
            most_common_times[genre] = most_common_time

        print("Most Common Times:")
        for genre, time in most_common_times.items(): 
            print(f"\t{genre}: {time}")  # Print each result with a tab
        return most_common_times

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example call to the function
most_common_schedule_time('TV_show_data.csv')
