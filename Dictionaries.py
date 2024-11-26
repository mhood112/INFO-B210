def sort_tv_shows_and_write_to_csv(input_csv, output_csv):
    """ this is a function that reads a CSV file containing TV show data and writes a new CSV file with the TV shows sorted alphabetically by their names."""
    def parse_csv_line(line):
        """Parse a line of CSV data and return a list of fields."""
        fields = []
        field = ''
        in_quotes = False
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

        if not lines:
            raise ValueError("The input CSV file is empty.")

        # Extract the header and data rows
        header = parse_csv_line(lines[0].strip())
        data = lines[1:]

        # Parse the data to extract the required fields
        tv_shows = []
        for line in data:
            fields = parse_csv_line(line.strip())
            if len(fields) < 10:
                raise ValueError("The input CSV file has an incorrect format.")
            tv_show = {
                'Name': fields[0],
                'Genres': fields[5],
                'Language': fields[7],
                'Rating': fields[9]
            }
            tv_shows.append(tv_show)

        # Sort the TV shows alphabetically by their names
        tv_shows.sort(key=lambda x: x['Name'])

        # Write the ordered sets to a new CSV file
        with open(output_csv, 'w') as file:
            file.write('Name,Genres,Language,Rating\n')
            for show in tv_shows:
                file.write(f'"{show["Name"]}","{show["Genres"]}","{show["Language"]}","{show["Rating"]}"\n')

        print(f"CSV file '{output_csv}' created successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{input_csv}' or '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
sort_tv_shows_and_write_to_csv('TV_Show.csv', 'sorted_tv_shows.csv')
