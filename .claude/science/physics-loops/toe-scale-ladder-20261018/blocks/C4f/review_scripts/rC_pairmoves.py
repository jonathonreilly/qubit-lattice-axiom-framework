"""Phase C spot-check of C4f Step 2 / C4c Observation M counts, reviewer's own code.
Exception class rho: exists near pair c' (0<|x'-y'|<=r), all four cross distances <= r,
c' fixed (as a set) by Stab(c) in G x| Z^3, COM(c') != COM(c); c = {0, rho}."""
import itertools, numpy as np, sys
sys.path.insert(0, '.')
from rlib import group_O, psign
O = group_O(); T = [M for M in O if psign(M) == 1]
def cheb(a, b): return max(abs(a[i]-b[i]) for i in range(3))
PASS = FAIL = 0
def chk(n, ok):
    global PASS, FAIL; PASS += ok; FAIL += (not ok); print(('PASS ' if ok else 'FAIL ') + n)
res = {}
for r in (1, 2, 3):
    reps = []
    for v in itertools.product(range(-r, r+1), repeat=3):
        if v != (0,0,0) and v > tuple(-x for x in v): reps.append(v)
    win = list(itertools.product(range(-r, 2*r+1), repeat=3))
    for gname, G in (('T', T), ('O', O)):
        exc = 0
        for rho in reps:
            x, y = (0,0,0), rho
            stab = []
            for M in G:
                Mr = tuple(int(a) for a in M @ np.array(rho))
                if Mr == rho: stab.append((M, (0,0,0)))
                if Mr == tuple(-a for a in rho): stab.append((M, rho))
            g = lambda M, t, p: tuple(int(a) + t[i] for i, a in enumerate(M @ np.array(p)))
            pts = [p for p in win if cheb(p, x) <= r and cheb(p, y) <= r]
            found = False
            for a, b in itertools.combinations(pts, 2):
                if not (0 < cheb(a, b) <= r): continue
                if tuple(a[i]+b[i] for i in range(3)) == rho: continue  # same COM (2*COM = rho)
                cp = {a, b}
                if all({g(M, t, a), g(M, t, b)} == cp for M, t in stab): found = True; break
            exc += found
        res[(r, gname)] = (exc, len(reps)); print(f'r={r} {gname}: {exc} of {len(reps)}')
claimed = {(1,'T'): (6,13), (1,'O'): (0,13), (2,'T'): (56,62), (2,'O'): (36,62), (3,'T'): (162,171), (3,'O'): (132,171)}
for k, v in claimed.items(): chk(f'r={k[0]} {k[1]}: reviewer {res[k]} vs claimed {v}', res[k] == v)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
