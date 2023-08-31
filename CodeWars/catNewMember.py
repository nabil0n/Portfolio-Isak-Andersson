def open_or_senior(data):
    output = []
    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    print(output)

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])#,['Open', 'Senior', 'Open', 'Senior'])
open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])#,['Open', 'Open', 'Senior', 'Open'])