def filter_tv_shows_by_end_date(input_file, output_file, given_date):
    try:
        # Convert the given date to a comparable format
        given_date = given_date.split('-')
        given_date = [int(part) for part in given_date]
    except ValueError:
        print("Error: Given date is not in the correct format (YYYY-MM-DD).")
        return

    def is_date_before(date_str, given_date):
        if not date_str:
            return False
        try:
            date_parts = date_str.split('-')
            date_parts = [int(part) for part in date_parts]
            return date_parts < given_date
        except ValueError:
            return False

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    except IOError:
        print(f"Error: An error occurred while reading the file {input_file}.")
        return

    try:
        header = lines[0].strip().split(',')
        end_date_index = header.index('End Date')
        name_index = header.index('Name')
    except IndexError:
        print("Error: The CSV file does not contain the required columns.")
        return
    except ValueError:
        print("Error: The CSV header is not in the correct format.")
        return

    filtered_shows = []

    for line in lines[1:]:
        columns = []
        current_column = ''
        inside_quotes = False

        for char in line:
            if char == '"' and not inside_quotes:
                inside_quotes = True
            elif char == '"' and inside_quotes:
                inside_quotes = False
            elif char == ',' and not inside_quotes:
                columns.append(current_column.strip())
                current_column = ''
            else:
                current_column += char

        columns.append(current_column.strip())

        if len(columns) > end_date_index and is_date_before(columns[end_date_index], given_date):
            filtered_shows.append(columns[name_index])

    try:
        with open(output_file, 'w') as file:
            file.write('Name\n')
            for show in filtered_shows:
                file.write(f'{show}\n')
    except IOError:
        print(f"Error: An error occurred while writing to the file {output_file}.")
        return

# Example usage
filter_tv_shows_by_end_date('TV_Show.csv', 'Filtered_TV_Shows.csv', '2010-01-01' )

