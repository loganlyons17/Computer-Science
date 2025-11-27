import fractions as fr
for a in range(1, 10):
    for b in range(1, 10):
        if a != b:
            for c in range(1, 10):
                if c != b and c != a:
                    for d in range(1, 10):
                        if d != c and d != b and d != a:
                            for e in range (1, 10):
                                if e != d and e != c and e != b and e != a:
                                    for f in range(1, 10):
                                        if f != e and f != d and f != c and f != b and f != a:
                                            for g in range(1, 10):
                                                if g != f and g != e and g != d and g != c and g != b and g != a:
                                                    for h in range(1, 10):
                                                        if h != g and h != f and h != e and h != d and h != c and h != b and h != a:
                                                            for i in range(1, 10):
                                                                if i != h and i != g and i != f and i != e and i != d and i != c and i != b and i != a:
                                                                    if a + fr.Fraction(f"{b}/{c}") + d + fr.Fraction(f"{e}/{f}") == g + fr.Fraction(f"{h}/{i}"):
                                                                        if b < c and e < f and h < i:
                                                                            print(f"{a}({b}/{c}) + {d}({e}/{f}) = {g}({h}/{i})")