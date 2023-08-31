def is_valid_IP(strng):
    for c in strng:
        if c not in '.0123456789':
            return False
    lst = strng.split('.')
    if len(lst) != 4:
        return False
    for i in lst:
        if len(i) > 1 and i[0] == '0':
            return False
        if not i or not 0<=int(i)<=255:
            return False
    return True

# tillåt bara int och .

# nästa blir .split('.')

# kolla att det är 4 element i list

# läs talen som int()

# iterera elementen i listan och kolla 0<=talet<=255

# retunera Ture om True

print(is_valid_IP('123.254.23.12'))
print(is_valid_IP('123.654.2f.12'))
print(is_valid_IP('123.654.2f'))
print(is_valid_IP('123.654.2f.12.oio'))
print(is_valid_IP('...'))
print(is_valid_IP('1..2.3'))
print(is_valid_IP('123.254.023.12'))