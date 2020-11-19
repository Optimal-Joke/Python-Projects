number = 0
combo_list = []
for a in range(201):
    for b in range(101):
        for c in range(41):
            for d in range(21):
                for e in range(11):
                    for f in range(5):
                        for g in range(3):
                            for h in range(2):
                                value = (0.01*a)+(0.02*b)+(0.05*c)+(0.1*d)+ \
                                        (0.2*e)+(0.5*f)+(1*g)+(2*h)
                                if value == 2.0:
                                    number +=1
print(number)