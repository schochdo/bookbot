def get_book_text(path):
	with open(path) as f:
		return f.read()

def word_count(text):
	words = text.split()
	return(len(words))

def char_count(text):
	lowered_text = text.lower()
	char_counts = {}
	for c in lowered_text:
		if c in char_counts:
			char_counts[c] += 1
		else:
			char_counts[c] = 1
	return char_counts

def char_counts_to_list(char_counts):
	char_list = []
	for char in char_counts:
		if char.isalpha():
			char_count = char_counts[char]
			char_list.append({"char": char, "num": char_count})
	return char_list 

def sort_on(char_dict):
    return char_dict["num"]
	
def main():
	
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = word_count(text)
	#print(f"{num_words} words")
	char_counts = char_count(text)
	char_list = char_counts_to_list(char_counts)
	char_list.sort(reverse=True, key=sort_on)

	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document")

	for item in char_list:
		print(f"The '{item["char"]}' character was found {item["num"]} times")
	print("--- End report ---")

main()
