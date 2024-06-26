import emoji

def main():
    text = input("Input: ")
    to_emoji(text)

def to_emoji(t):
    print(emoji.emojize(t,language="alias"))

main()