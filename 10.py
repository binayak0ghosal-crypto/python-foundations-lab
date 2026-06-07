
with open('PARA.txt', 'r') as source_file:

    with open('Destination.txt', 'w') as dest_file:
        for line in source_file:

            if 'a' not in line:
                dest_file.write(line)

print("Lines without 'a' have been written to Destination.txt.")
