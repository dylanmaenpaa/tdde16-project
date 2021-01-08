# Tokenizer from the course TDDE16 at Linköping Unversity.
# Used for tokenizing the Swedish Parliament speeches in this project.

def tokenize(text):
    for token in re.findall(r'-?\w+(?:[:-]\w+|-)?', text):
        if token.isalpha():
            yield token.lower()
