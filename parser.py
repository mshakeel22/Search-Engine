from tokenizer import Tokenizer
from word_dictionary import WordDictionary
from file_dictionary import FileDictionary

# Initialize the tokenizer, word dictionary, and file dictionary
tokenizer = Tokenizer()
word_dict = WordDictionary()
file_dict = FileDictionary()

# Read and parse the TREC data
with open("data/trec_data.txt", "r") as trec_file:
    for line in trec_file:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            filename, text = parts
            # Add the file to the file dictionary
            file_dict.add_file(filename)
            # Tokenize the text and add tokens to the word dictionary
            token_stream = tokenizer.tokenize(text)
            for token in token_stream:
                word_dict.add_token(token)

# Print the mappings
for token, token_id in word_dict.token_to_id.items():
    print(f"{token}: {token_id}")

for filename, file_id in file_dict.file_to_id.items():
    print(f"{filename}: {file_id}")