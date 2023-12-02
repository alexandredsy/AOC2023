def read_file(dayNo):
    with open(f'Day{dayNo}.txt') as file:
        lines = [line for line in file]
    return lines
