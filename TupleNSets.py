def calculate_runtime(premiere_date, end_date):
    """Calculate the runtime of a TV show in days given its premiere and end dates."""
    try:
        if not end_date:
            return 0
        premiere_month, premiere_day, premiere_year = map(int, premiere_date.split('/'))
        end_month, end_day, end_year = map(int, end_date.split('/'))
        premiere_days = premiere_year * 365 + premiere_month * 30 + premiere_day
        end_days = end_year * 365 + end_month * 30 + end_day
        return end_days - premiere_days
    except ValueError:
        return 0

def parse_csv_line(line):
    """Parse a CSV line and return a list of fields."""
    in_quotes = False
    field = ''
    fields = []
    for char in line: #handle the case where there is a comma in the field
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

def order_tv_shows_by_runtime(input_file, output_file):
    """Read TV shows from a CSV file, calculate their runtime, and write them to a new CSV file sorted by runtime."""
    tv_shows = []

    try:
        # Read TV shows from the input CSV file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            headers = parse_csv_line(lines[0].strip())
            name_index = headers.index('Name')
            premiere_index = headers.index('End Date')
            end_index = headers.index('Premiere Date')
            
            for line in lines[1:]:  
                columns = parse_csv_line(line.strip())
                try: 
                    name = columns[name_index].strip('"')
                    premiere_date = columns[premiere_index].strip('"')
                    end_date = columns[end_index].strip('"')
                    runtime = calculate_runtime(premiere_date, end_date)
                    tv_shows.append((name, runtime))
                except IndexError:
                    print(f"Skipping malformed line: {line.strip()}")

        # Sort TV shows by runtime
        tv_shows.sort(key=lambda x: x[1], reverse=True)

        # Write sorted TV show names to a new CSV file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('Name\n')
            for show in tv_shows:
                file.write(f'{show[0]}\n')

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while processing the file {input_file}.")

# Example usage
order_tv_shows_by_runtime('TV_Show.csv', 'Sorted_TV_Shows.csv')
