import sys

def lower(ch, add):
    return chr((ord(ch) - ord('a') + add) % 26 + ord('a'))

def upper(ch, add):
    return chr((ord(ch) - ord('A') + add) % 26 + ord('A'))

def keygen(name):
    key = ""
    for ch in name:
        if ch.islower():
            key += lower(ch, len(name))
        elif ch.isupper():
            key += upper(ch, len(name))
        else:
            print("!!! ONLY LETTERS ALLOWED !!!")
            sys.exit(1)

    return key

def main():
    if len(sys.argv) < 2:
        print("python keygen.py <username>")
        sys.exit(1)

    print(f"KEY : {keygen(sys.argv[1])}")

if __name__ == "__main__":
    main()