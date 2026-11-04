import sys

def char_sum(name):
    return sum(ord(ch) for ch in name)

SHIFT = len("./keygenme") & 0x1f

def main():
    if len(sys.argv) < 2:
        print("python keygen.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    ans = ((char_sum(name) ^ ord(name[0]) * 3) << SHIFT) & 0xFFFFFFFF
    if ans >= 0x80000000:   # atoi returns signed int
        ans -= 0x100000000

    print(f"KEY : {ans}")

if __name__ == "__main__":
    main()