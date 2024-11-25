def sort_tv_shows_and_write_to_csv(input_csv, output_csv):
    """ Sorts the TV shows alphabetically by their names and writes the sorted data to a new CSV file."""
    def parse_csv_line(line):
        """ Parses a line of CSV data and returns the fields as a list."""
        fields = []
        field = ''
        in_quotes = False
        """ check if the character is a quote and if it is not in quotes, then set in_quotes to True."""
        for char in line:
            if char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == ',' and not in_quotes:
                fields.append(field)
                field = ''
            else:
                field += char
        fields.append(field)
        return fields

    try:
        # Read the CSV data
        with open(input_csv, 'r') as file:
            lines = file.readlines()

        # Extract the header and data rows
        header = lines[0].strip().split(',')
        data = lines[1:]

        # Parse the data to extract the required fields
        tv_shows = []
        for line in data:
            fields = parse_csv_line(line.strip())
            name = fields[0]
            genres = fields[5]
            language = fields[7]
            rating = fields[9]
            tv_shows.append((name, genres, language, rating))

        # Sort the TV shows alphabetically by their names
        tv_shows.sort(key=lambda x: x[0])

        # Write the ordered sets to a new CSV file
        with open(output_csv, 'w') as file:
            file.write('Name,Genres,Language,Rating\n')
            for show in tv_shows:
                file.write(f'"{show[0]}","{show[1]}","{show[2]}","{show[3]}"\n')

        print(f"CSV file '{output_csv}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
sort_tv_shows_and_write_to_csv('TV_Show.csv', 'sorted_tv_shows.csv')
