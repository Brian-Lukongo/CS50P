
def get_words(filename):
    """Read a file and return a list of words"""
    try:
        with open(filename, 'r') as file:
            words = file.read().lower().split()
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []

def save_counts(counts):
    """Save word counts to a file (counts.csv)"""
    with open('counts.csv', 'w') as file:
        for word, count in counts.items():
            file.write(f"{word},{count}\n")

def main():
    counts = {}
    words = get_words("address.txt")
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    save_counts(counts)

main()