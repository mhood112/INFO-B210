def most_common_schedule_time(file_path):
    # Step 1: Open and read the CSV file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Step 2: Parse the CSV data
    headers = lines[0].strip().split(',')
    genre_index = headers.index('Genres')
    schedule_time_index = headers.index('Schedule (time)')

    # Step 3: Create a dictionary to store the count of each Schedule (time) for each genre
    genre_schedule_count = {}

    # Step 4: Iterate through the data and populate the dictionary
    for line in lines[1:]:
        fields = line.strip().split(',')
        genres_str = fields[genre_index].strip()
        # Manually parse the genres from the string representation
        genres = genres_str.strip("[]").replace("'", "").split(", ")
        schedule_time = fields[schedule_time_index]

        for genre in genres:
            genre = genre.strip().lower()  # Ensure genre is treated as a lowercase string
            if genre not in genre_schedule_count:
                genre_schedule_count[genre] = {}
            if schedule_time not in genre_schedule_count[genre]:
                genre_schedule_count[genre][schedule_time] = 0
            genre_schedule_count[genre][schedule_time] += 1

    # Step 5: Prompt the user for a genre
    user_genre = input("Enter a genre: ").strip().lower()

    # Step 6: Determine the most common Schedule (time) for the inputted genre
    if user_genre in genre_schedule_count:
        schedule_times = genre_schedule_count[user_genre]
        most_common_time = max(schedule_times, key=schedule_times.get)
        return most_common_time
    else:
        return "Genre not found."

# Example usage
file_path = 'TV_show_data (2).csv'
print(most_common_schedule_time(file_path))
