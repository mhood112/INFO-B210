
class Show:
    def __init__(self, name, summary, average_runtime, end_date, premiere_date, genres, show_type, language, network, rating, schedule_days, schedule_time, total_seasons, total_episodes, character_names, person_names, official_site):
        self.name = name
        self.summary = summary
        self.average_runtime = average_runtime
        self.end_date = end_date
        self.premiere_date = premiere_date
        self.genres = genres
        self.show_type = show_type
        self.language = language
        self.network = network
        self.rating = rating
        self.schedule_days = schedule_days
        self.schedule_time = schedule_time
        self.total_seasons = total_seasons
        self.total_episodes = total_episodes
        self.character_names = character_names
        self.person_names = person_names
        self.official_site = official_site

filename = 'TV_show_data copy.csv'

with open(filename, 'r') as file:
    lines = file.readlines()

shows = []

# Extract the header
header = lines[0].strip().split(',')

# Process each line in the CSV
for line in lines[1:]:
    try:
        # Initialize variables
        data = []
        current = ''
        in_quotes = False

        # Processes each character in the line for special cases where commas are inside quotes
        for char in line:
            if char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == ',' and not in_quotes:
                data.append(current)
                current = ''
            else:
                current += char

        # Append the last part
        data.append(current)


        def to_int(value, default=0):
            """ Convert a string to an integer. If the conversion fails, return the default value. """
            try:
                return int(value)
            except ValueError:
                return default

        
        def to_float(value, default=0.0):
            """ Convert a string to a float. If the conversion fails, return the default value. """
            try:
                return float(value)
            except ValueError:
                return default

        # Create a Show object
        show = Show(
            name=data[0],
            summary=data[1],
            average_runtime=to_int(data[2]),
            end_date=data[3],
            premiere_date=data[4],
            genres=data[5],
            show_type=data[6],
            language=data[7],
            network=data[8],
            rating=to_float(data[9]),
            schedule_days=data[10],
            schedule_time=data[11],
            total_seasons=to_int(data[12]),
            total_episodes=to_int(data[13]),
            character_names=data[14],
            person_names=data[15],
            official_site=data[16] if len(data) > 16 else None
        )

        shows.append(show)
    except Exception as e:
        print(f"Error processing line: {line.strip()}")
        print(f"Exception: {e}")

for show in shows:
    print(f"Show: {show.name}, Rating: {show.rating}, Genres: {show.genres}, Schedule Time: {show.schedule_time}")
