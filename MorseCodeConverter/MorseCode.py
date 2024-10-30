# Text to Morse Code Converter
# Morse code
morse_code_rules = {
    'a': '·− ',
    'b': '−··· ',
    'c': '−·−· ',
    'd': '−·· ',
    'e': '· ',
    'f': '··−· ',
    'g': '−−· ',
    'h': '···· ',
    'i': '·· ',
    'j': '·−−− ',
    'k': '−·− ',
    'l': '·−·· ',
    'm': '−− ',
    'n': '−· ',
    'o': '−−− ',
    'p': '·−−· ',
    'q': '−−·− ',
    'r': '·−· ',
    's': '··· ',
    't': '− ',
    'u': '··− ',
    'v': '···− ',
    'w': '·−− ',
    'x': '−··− ',
    'y': '−·−− ',
    'z': '−−·· ',
    '0': '−−−−− ',
    '1': '·−−−− ',
    '2': '··−−− ',
    '3': '···−− ',
    '4': '····− ',
    '5': '····· ',
    '6': '−···· ',
    '7': '−−··· ',
    '8': '−−−·· ',
    '9': '−−−−· ',
    ' ': '/ ',
}

user_input = input("Welcome to Text to Morse Code Convertor\n"
                   "Please put your message here: ").lower()


def text_to_morse(text_to_convert):
    message = ""

    for _ in text_to_convert:
        if _ in morse_code_rules:
            message += morse_code_rules[_]

    return message


print(text_to_morse(user_input))
