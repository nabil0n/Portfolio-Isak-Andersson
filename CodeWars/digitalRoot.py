def digital_root(n):
    digits = [int(x) for x in str(abs(n))]
    answer = 0
    for d in digits:
        if answer < 10:
            answer += d
            if answer >= 10:
                digits = [int(x) for x in str(abs(answer))]
                answer = 0
                for d in digits:
                    answer += d
    print(answer)

digital_root(16)#, 7)
digital_root(942)#, 6)
digital_root(132189)#, 6)
digital_root(493193)#, 2)