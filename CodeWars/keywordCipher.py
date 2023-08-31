def keyword_cipher(msg, keyword):
    alph = "abcdefghijklmnopqrstuvwxyz "
    oldalph = [*alph]
    newalph = []
    [newalph.append(k) for k in [*keyword] if k not in newalph]
    [newalph.append(l) for l in [*alph] if l not in newalph]
    inp = [*msg.lower()]
    msgindex = []
    for i in inp:
        for l in range(len(oldalph)):
            if oldalph[l] == i:
                msgindex.append(l)
    outp = []
    for i in msgindex:
        for l in range(len(newalph)):
            if i == l:
                outp.append(newalph[l])
    print(''.join(outp))

keyword_cipher("Welcome home","secret")
keyword_cipher("hello","wednesday")
keyword_cipher("HELLO","wednesday")
keyword_cipher("HeLlO","wednesday")
keyword_cipher("WELCOME HOME", "gridlocked")
keyword_cipher("alpha bravo charlie", "delta")
keyword_cipher("Home Base", "seven")
keyword_cipher("basecamp", "covert")
keyword_cipher("one two three", "rails")
keyword_cipher("Test", "unbuntu")