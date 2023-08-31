import re

def to_camel_case(text):
    t = re.split(r'-|_', text)
    x = t[:1]
    s = [i.title() for i in t[1:]]
    cam = ''.join(x+s)
    print(cam)





to_camel_case("")
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")