def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text
def main():
    text = input("Say something with an emoticon: ")
    converted= convert(text)
    print("Converted text:", converted)

main()