lst = ['i',
       'have',
       'no',
       'space',
       'test',
       ]

newlst = []
for i in range(len(lst)):
       newlst.append(''.join(lst[0:i+1]))
print(newlst)