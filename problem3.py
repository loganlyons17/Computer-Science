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
                                                            if (a + b) / c == 1 and (d + 5) / e == 1 and (f + g) + h == 15 and (a + d) / f == 2 and (b + 5) * g == 44 and (c + e) * h == 13:
                                                                print(f"{a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}")
print("done")