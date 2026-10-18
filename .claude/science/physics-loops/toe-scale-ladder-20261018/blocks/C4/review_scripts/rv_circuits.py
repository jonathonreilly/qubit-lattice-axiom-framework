"""Phase-exact check that alpha_P = prod_r exp(+- i pi/4 P_r) (P a covariant string whose translates
commute) is an O-covariant Clifford QCA with images in the 125-ball, and equals one of the reviewer's
four range-2 solutions *with phases*. Also: tau = tr M for each range-2 solution, M^2 = 1, signed
period, and the composition-range check."""
import itertools, time
from rv_common import O, mul, canon, translate, anticomm
from rv_classify import classify, explicit_symplectic, signed_ok
from rv_linear import decode

PASS = FAIL = 0
def check(name, ok):
    global PASS, FAIL
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    PASS += bool(ok); FAIL += (not ok)

CHAMON = {(1,0,0):'X',(-1,0,0):'X',(0,1,0):'Y',(0,-1,0):'Y',(0,0,1):'Z',(0,0,-1):'Z'}
CUBO = {}
for a, b in itertools.product((1,-1), repeat=2):
    CUBO[(0,a,b)] = 'X'; CUBO[(a,0,b)] = 'Y'; CUBO[(a,b,0)] = 'Z'

def rotate(Pd, eps, Q):
    """conjugate phased string Q by prod_r exp(i eps pi/4 P_r): each anticommuting P_r maps Q -> i eps P_r Q."""
    out = Q
    for t in itertools.product(range(-4, 5), repeat=3):
        Pr = translate((0, Pd), t)
        if anticomm(Pr, out):
            ph = 1 if eps > 0 else 3
            out = mul(mul((ph, {}), Pr), out)
    return out

def mutually_commuting(Pd):
    return all(not anticomm((0, Pd), translate((0, Pd), t)) for t in itertools.product(range(-4,5), repeat=3))

sols = {}
for action in ('axis', 'full'):
    sites, vecs, d = classify(2, action)
    sols[action] = [decode(v, sites) for v in vecs]

for name, Pd in (('Chamon octahedron', CHAMON), ('cuboctahedral 12-site', CUBO)):
    check(f'{name}: translates mutually commute', mutually_commuting(Pd))
    for eps in (1, -1):
        aX = rotate(Pd, eps, (0, {(0,0,0): 'X'}))
        aZ = rotate(Pd, eps, (0, {(0,0,0): 'Z'}))
        inball = all(max(abs(c) for c in r) <= 2 for r in list(aX[1]) + list(aZ[1]))
        real = aX[0] in (0, 2) and aZ[0] in (0, 2)
        sx = 1 if aX[0] == 0 else -1; sz = 1 if aZ[0] == 0 else -1
        for action in ('axis', 'full'):
            match = [k for k, (PX, PZ) in enumerate(sols[action]) if PX == aX[1] and PZ == aZ[1]]
            ok = inball and real and len(match) == 1 and signed_ok(aX[1], aZ[1], sx, sz, action)
            check(f'{name}, exponent sign {eps:+d}, {action}: images in 125-ball, |supp X|={len(aX[1])}, '
                  f'signs ({sx:+d},{sz:+d}), equals reviewer solution #{match} with phases and is signed-covariant', ok)

# polynomial (F2) matrices: trace, M^2, composition ranges
def poly(Pd, want):  # want 'x' or 'z' part
    return frozenset(r for r, a in Pd.items() if (a in 'XY' if want == 'x' else a in 'ZY'))
def pmul(A, B):
    out = set()
    for a in A:
        for b in B:
            s = (a[0]+b[0], a[1]+b[1], a[2]+b[2])
            out ^= {s}
    return frozenset(out)
def padd(A, B): return frozenset(set(A) ^ set(B))
def mat(PX, PZ):
    return [[poly(PX,'x'), poly(PZ,'x')], [poly(PX,'z'), poly(PZ,'z')]]
def mmul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]
ONE = frozenset({(0,0,0)}); I2 = [[ONE, frozenset()], [frozenset(), ONE]]
Ms = [mat(PX, PZ) for PX, PZ in sols['full']]
for k, M in enumerate(Ms):
    tau = padd(M[0][0], M[1][1])
    print(f'  solution {k}: |supp X-image|={len(sols["full"][k][0])}, tau={sorted(tau)}', flush=True)
    check(f'solution {k}: tau = 0 and M^2 = 1', len(tau) == 0 and mmul(M, M) == I2)
rng = lambda M: max((max(abs(c) for c in e) for row in M for p in row for e in p), default=0)
for i, j in itertools.combinations(range(1, 4), 2):
    print(f'  range of M{i} M{j} = {rng(mmul(Ms[i], Ms[j]))}; M{i}M{j} == M{j}M{i}: {mmul(Ms[i],Ms[j]) == mmul(Ms[j],Ms[i])}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
