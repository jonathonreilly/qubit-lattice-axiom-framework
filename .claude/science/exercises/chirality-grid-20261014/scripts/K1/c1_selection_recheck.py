import itertools
C = list(itertools.product((0, 1), repeat=3)); add = lambda *v: tuple(sum(x) % 2 for x in zip(*v))
Lt = [c for c in C if sum(c) == 1]; M = [c for c in C if sum(c) != 1]; z = (0, 0, 0)
lm3 = [(l, a, b, c) for l in Lt for a, b, c in itertools.combinations_with_replacement(M, 3) if add(l, a, b, c) == z]
l3m = [(a, b, c, m) for a, b, c in itertools.combinations_with_replacement(Lt, 3) for m in M if add(a, b, c, m) == z]
s = [f"light*mirror^3 allowed label sets: {len(lm3)} e.g. {lm3[:2]}",
     f"light^3*mirror allowed label sets: {len(l3m)} e.g. {l3m[:2]}",
     f"C1 verdict: X2-L3 {'PASS (F1:108 rule false for the walker 3-light split)' if lm3 and l3m else 'FAIL'}"]
print("\n".join(s)); open(__file__.replace('.py', '.out'), 'w').write("\n".join(s) + "\n")
