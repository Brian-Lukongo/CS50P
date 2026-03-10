def convert(text):
    #replace the smiley faces with emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text
def main():
    #user input
    text = input("Say something with an emoticon: ")
    #convert the text
    converted= convert(text)
    print(converted)

main()