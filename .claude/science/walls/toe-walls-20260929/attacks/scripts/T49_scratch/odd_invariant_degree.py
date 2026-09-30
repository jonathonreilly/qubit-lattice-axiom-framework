"""Part B: lowest degree of a polynomial in k that is odd (f(-k) = -f(k)) and invariant under the
24 proper cubic rotations.  Such a function is the small-k form of a rotation-covariant scalar
pairing amplitude Delta(k) of a single-component fermion (plain cubic lattice, no KS signs)."""
import itertools, sympy as sp
x, y, z = sp.symbols('x y z')
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = sp.zeros(3, 3)
        for r in range(3): M[r, perm[r]] = signs[r]
        if M.det() == 1: rots.append(M)
assert len(rots) == 24
def reynolds(mon):
    tot = 0
    for M in rots:
        sub = dict(zip((x, y, z), list(M * sp.Matrix([x, y, z]))))
        tot += mon.subs(sub, simultaneous=True)
    return sp.expand(tot / 24)
for deg in range(1, 12, 2):
    found = []
    for a in range(deg + 1):
        for b in range(deg + 1 - a):
            c = deg - a - b
            r = reynolds(x**a * y**b * z**c)
            if r != 0: found.append(sp.factor(r))
    uniq = []
    for f in found:
        if not any(sp.simplify(f - g) == 0 or sp.simplify(f + g) == 0 for g in uniq): uniq.append(f)
    print(f"odd degree {deg}: {len(uniq)} independent-looking invariant(s)", uniq[:1])
    if uniq: break
