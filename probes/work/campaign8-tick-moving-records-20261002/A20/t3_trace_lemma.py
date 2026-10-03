"""Trace lemma, exact over F2 in w-coordinates.
phi = f_x in F2[w1,w2,w3] (w_i = z_i + 1/z_i). With A..F = phi o (id, cyc, cyc^2, (23), (12), (13)):
   linearity (alpha(Y)=alpha(X)+alpha(Z))  <=>  A+F = B+D = C+E ;   tr M = A+F.
Brute force: for an S3-orbit of exponents with distinct entries, enumerate all 2^6 phi on the orbit,
keep those obeying linearity, report possible traces. Also re-derive the relations symbolically with sympy."""
import itertools
import sympy as sp
w1, w2, w3 = sp.symbols("w1 w2 w3")
W = (w1, w2, w3)
perms = {"A": (0, 1, 2), "B": (1, 2, 0), "C": (2, 0, 1), "D": (0, 2, 1), "E": (1, 0, 2), "F": (2, 1, 0)}
def sub(phi, p):
    return phi.subs({W[0]: W[p[0]], W[1]: W[p[1]], W[2]: W[p[2]]}, simultaneous=True)
def red2(e):
    P = sp.Poly(sp.expand(e), *W, modulus=2)
    return P
for m in [(0, 1, 2), (0, 1, 3), (1, 2, 3), (0, 2, 5)]:
    orbit = sorted({tuple(m[i] for i in p) for p in itertools.permutations(range(3))})
    mons = [w1**e[0] * w2**e[1] * w3**e[2] for e in orbit]
    ok, traces = 0, set()
    for bits in itertools.product([0, 1], repeat=6):
        phi = sum(b * mo for b, mo in zip(bits, mons))
        if phi == 0:
            continue
        v = {k: sub(phi, p) for k, p in perms.items()}
        t1, t2, t3 = red2(v["A"] + v["F"]), red2(v["B"] + v["D"]), red2(v["C"] + v["E"])
        if t1 == t2 == t3:
            ok += 1
            traces.add(str(t1.as_expr()))
    print(f"orbit of {m}: {ok} nonzero phi obey linearity; traces seen: {traces}")
