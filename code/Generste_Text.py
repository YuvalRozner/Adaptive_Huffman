import random
import string

def generate_random_word(length): # randomize a word
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_text(blocks, block_size, total_length): # create the text
    text = []
    for _ in range(blocks+1):
        word = generate_random_word(8)
        repeat_count = block_size // len(word)
        text.append(word * repeat_count)
    return ''.join(text)[:total_length]

blocks = 552 #last 3 digit of my ID number
total_length = 10000000 # 10Mega
block_size = total_length // blocks

text = create_text(blocks, block_size, total_length)

# Save the text to a txt file
with open("text.txt", "w") as file:
    file.write(text)

print(f"Generated text length: {len(text)}")
print(f"Blocks: {blocks}")
print(f"Block size: {block_size}")