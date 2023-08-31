# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be 
# rearranged to match str2, otherwise returns false.

# Notes:

#     Only lower case letters will be used (a-z). No punctuation or digits will be included.
#     Performance needs to be considered.


def scramble(s1, s2):
    st1 = [*s1]
    st2a = [*s2]
    st2b = [*s2]
    st3 = []
    for letter in st1:
        if letter in st2a:
            st3.append(letter)
            st2a.remove(letter)
    if len(st2b) == len(st3):
        return True
    return False

# FÖR LÅNGSAM LÖSNING. Måste klara en timer på 12000ms för ett visst antal (dolt antal) lösningar.
# Nedan är en chatGPT lösning som klarade jobbet på 53ms
# Och CodeWars vinnaren är under den.

def scramble(s1, s2):
    st1_counts = [0] * 26  # Count occurrences of each letter in s1
    
    for letter in s1:
        st1_counts[ord(letter) - ord('a')] += 1
    
    for letter in s2:
        index = ord(letter) - ord('a')
        if st1_counts[index] <= 0:
            return False
        st1_counts[index] -= 1
    
    return True

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


# Examples

print(scramble('rkqodlw', 'world'))# ==> True
print(scramble('cedewaraaossoqqyt', 'codewars'))# ==> True
print(scramble('katas', 'steak'))# ==> False