
file_handle = open('PARA.txt', 'r')

total_word_count = 0

for line_text in file_handle:
    word_list = line_text.split()
    total_word_count += len(word_list)
    formatted_line = '#'.join(word_list)
    print(formatted_line)

file_handle.close()

print(f"\nTotal number of words: {total_word_count}")
