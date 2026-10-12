
def count_lines(lines):
    return len(lines)

def count_chars(lines):
    count = 0
    for l in lines:
        count += len(l)
    return count

def test(lines):
    c_l = count_lines(lines)
    c_c = count_chars(lines)
    print(f"Lines: {c_l}\nCharacters: {c_c}")


if __name__ == "__main__":
    lines = ["Hello", "World", "Python"]
    test(lines)