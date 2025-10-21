def emoji_converter(note):
    emoji_mapping = {
        ':)': '🙂',
        ':(': '🙁',
        ';)': '😉'
    }
    words = note.split(' ')
    output = ''
    for word in words:
        output += emoji_mapping.get(word, word) + ' '
    return output


message = input(">")
print(emoji_converter(message))