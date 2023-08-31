def is_pangram(s):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    alfalist = [*alfabet]
    letters = [*s.lower()]
    for letter in letters:
        if letter in alfalist:
            alfalist.remove(letter)
    if alfalist == []:
        return True
    return False




















print(is_pangram("The quick, brown fox jumps over the lazy dog!"))#, True)

print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))#, False)

print(is_pangram("How quickly daft jumping zebras vex."))#, True)