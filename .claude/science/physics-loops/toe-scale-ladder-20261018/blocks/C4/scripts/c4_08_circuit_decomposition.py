#!/usr/bin/env python3
"""C4 step 8: are the radius-2 soldered (full action) entangling solutions finite-depth circuits?
Input: the signed images printed by c4_07 (parsed from logs/c4_07_radius2_analysis.txt; re-verified
here: symplectic, det 1, and O-covariant with phases under the full action).
Method: greedy/beam reduction by right/left multiplication with elementary symplectic matrices
E_l(g) = [[1,0],[g,1]], E_u(g) = [[1,g],[0,1]], g = 1 or x^n + x^-n (each is a depth-1 layer of
S or CZ gates, translation-invariant) and on-site SL2(F2), until the identity is reached.  A found
word is verified by exact multiplication.  Failure to find a word is NOT evidence of nontriviality."""
import os, sys, re, ast, itertools
os.environ['C4_RADIUS'] = '2'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4lib as L
P = F = 0
def check(n, ok):
    global P, F
    P += ok; F += (not ok); print(('PASS ' if ok else 'FAIL ') + n, flush=True)
here = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(here, '..', 'logs', 'c4_07_radius2_analysis.txt')).read()
block = txt.split('== full')[1].split('== axis')[0] if '== axis' in txt else txt.split('== full')[1]
xs = re.findall(r'alpha\(X_0\) = sign (\d) \* (\[.*\])', block)
zs = re.findall(r'alpha\(Z_0\) = sign (\d) \* (\[.*\])', block)
h = tuple(L.menu_hom('full'))
def poly_parts(lst):
    px, pz = set(), set()
    for s, a in lst:
        bx, bz = L.LABEL_BITS[a]
        if bx: px.add(s)
        if bz: pz.add(s)
    return frozenset(px), frozenset(pz)
I2 = [[L.ONE, L.ZERO], [L.ZERO, L.ONE]]
def key(M): return tuple(tuple(sorted(M[i][j])) for i in range(2) for j in range(2))
def size(M): return sum(len(M[i][j]) for i in range(2) for j in range(2))
gens = [L.ONE] + [frozenset({n, tuple(-v for v in n)}) for n in itertools.product(range(-2, 3), repeat=3) if n > (0, 0, 0)]
ELEM = []
for g in gens:
    ELEM.append(('El', g, [[L.ONE, L.ZERO], [g, L.ONE]]))
    ELEM.append(('Eu', g, [[L.ONE, g], [L.ZERO, L.ONE]]))
SL2 = []
for a, b, c, d in itertools.product((0, 1), repeat=4):
    if (a * d + b * c) % 2:
        f = lambda t: L.ONE if t else L.ZERO
        SL2.append(('C', (a, b, c, d), [[f(a), f(b)], [f(c), f(d)]]))
def reduce(M, beam=30, depth=40):
    frontier = [(size(M), M, [])]
    seen = {key(M)}
    for _ in range(depth):
        cand = []
        for _, A, w in frontier:
            for side in ('L', 'R'):
                for nm, g, E in ELEM + SL2:
                    B = L.mat_mul(E, A) if side == 'L' else L.mat_mul(A, E)
                    k = key(B)
                    if k in seen: continue
                    seen.add(k)
                    w2 = w + [(side, nm, g, E)]
                    if k == key(I2): return w2
                    cand.append((size(B), B, w2))
        cand.sort(key=lambda t: t[0])
        frontier = cand[:beam]
        if not frontier: return None
    return None
for k, ((sx, lx), (sz, lz)) in enumerate(zip(xs, zs)):
    LX, LZ = ast.literal_eval(lx), ast.literal_eval(lz)
    a, c = poly_parts(LX); b, d = poly_parts(LZ)
    M = [[a, b], [c, d]]
    PX = (int(sx), {tuple(s): l for s, l in LX}); PZ = (int(sz), {tuple(s): l for s, l in LZ})
    check(f'solution {k+1}: symplectic, det 1, O-covariant with phases (full)', L.is_symplectic(M) and L.det(M) == L.ONE and L.signed_covariant(PX, PZ, h, h, L.SUBGROUPS['O']))
    w = reduce(M)
    if w is None:
        print(f'  solution {k+1}: no elementary word found within the beam search (inconclusive)')
        continue
    # verify: applying the word reproduces identity; hence M = product of inverses (E^-1 = E for these)
    A = M
    for side, nm, g, E in w:
        A = L.mat_mul(E, A) if side == 'L' else L.mat_mul(A, E)
    ok = key(A) == key(I2)
    check(f'solution {k+1}: explicit word of {len(w)} elementary S/CZ layers and on-site Cliffords reduces M to 1 '
          f'(so alpha is a finite-depth Clifford circuit, up to phases)', ok)
    print('   word:', [(s, n, L.poly_str(g) if n != 'C' else g) for s, n, g, _ in w])
print(f'TOTAL: PASS={P} FAIL={F}')
