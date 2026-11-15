# a2_55_nc.py -- exact checks for ALIGN2_55 section 3.1 (N1 path-product derivative; N2 first contour moment of S4').
# Criteria: a2_55_nc_criteria.md (written first). Fractions/ints only; stdout only.
from fractions import Fraction as F
import random, itertools
from collections import Counter
NM = 6
def zero(): return [[F(0)]*NM for _ in range(NM)]
def eye():
    M = zero()
    for i in range(NM): M[i][i] = F(1)
    return M
def add(A, B): return [[A[i][j]+B[i][j] for j in range(NM)] for i in range(NM)]
def scal(s, A): return [[s*A[i][j] for j in range(NM)] for i in range(NM)]
def mul(A, B):
    C = zero()
    for i in range(NM):
        for k in range(NM):
            if A[i][k] != 0:
                for j in range(NM):
                    if B[k][j] != 0: C[i][j] += A[i][k]*B[k][j]
    return C
def rand_n(rng):
    M = zero()
    for i in range(NM):
        for j in range(i+1, NM): M[i][j] = F(rng.randint(-6, 6), rng.randint(1, 5))
    return M
def expm(X):
    R, P = eye(), eye()
    for n in range(1, 2*NM):
        P = scal(F(1, n), mul(P, X)); R = add(R, P)
    return R
def inv_unip(A):  # A = I + N, N nilpotent
    N = add(A, scal(F(-1), eye())); R, P = eye(), eye()
    for j in range(1, 2*NM):
        P = scal(F(-1), mul(P, N)); R = add(R, P)
    return R
def tmul(A, B): return (mul(A[0], B[0]), add(mul(A[0], B[1]), mul(A[1], B[0])))
okN1, fireCN1 = True, False
for seed in (7, 8, 9, 10):
    rng = random.Random(seed); m = 7
    ys = [rand_n(rng) for _ in range(m)]; vs = [rand_n(rng) for _ in range(m)]
    ss = [rng.choice((1, -1)) for _ in range(m)]
    P = (eye(), zero()); prefix = eye(); rhs = zero(); rhs_bad = zero()
    for y, v, s in zip(ys, vs, ss):
        Ey = expm(y); Eyi = expm(scal(F(-1), y))
        if s == 1:
            Ft = tmul((eye(), v), (Ey, zero()))
            A = prefix; Ab = prefix
            rhs = add(rhs, mul(mul(A, v), inv_unip(A)))
            rhs_bad = add(rhs_bad, mul(mul(Ab, v), inv_unip(Ab)))
            prefix = mul(prefix, Ey)
        else:
            Ft = tmul((Eyi, zero()), (eye(), scal(F(-1), v)))
            A = mul(prefix, Eyi); Ab = prefix
            rhs = add(rhs, scal(F(-1), mul(mul(A, v), inv_unip(A))))
            rhs_bad = add(rhs_bad, scal(F(-1), mul(mul(Ab, v), inv_unip(Ab))))
            prefix = mul(prefix, Eyi)
        P = tmul(P, Ft)
    lhs = mul(P[1], inv_unip(P[0]))
    okN1 &= (lhs == rhs)
    if lhs != rhs_bad: fireCN1 = True
print("N1 (left-trivialised derivative of a path product):", "PASS" if okN1 else "FAIL")
print("N1 control CN1 (wrong prefix for reversed links):", "FIRES" if fireCN1 else "does NOT fire")

def axial_path(start, end, order):
    pos = list(start); steps = []
    for a in order:
        while pos[a] != end[a]:
            sgn = 1 if end[a] > pos[a] else -1
            steps.append((a, sgn, tuple(pos))); pos[a] += sgn
    return steps, tuple(pos)
def contour_steps(d, L, mu, sigma, y):
    o = (L - 1)//2; cX = tuple([0]*d)
    leg1, p1 = axial_path(cX, y, sigma)
    assert p1 == y
    straight = []; pos = list(y)
    for _ in range(L): straight.append((mu, 1, tuple(pos))); pos[mu] += 1
    cY = tuple(L if a == mu else 0 for a in range(d)); yL = tuple(y[a] + (L if a == mu else 0) for a in range(d))
    leg3f, _ = axial_path(cY, yL, sigma)
    leg3 = [(a, -sgn, tuple(p[i] + (sgn if i == a else 0) for i in range(d))) for (a, sgn, p) in reversed(leg3f)]
    return leg1 + straight + leg3
def nu_record(steps, nu):
    rec = []
    for (a, sgn, p) in steps:
        if a != nu: continue
        h = p[nu] if sgn == 1 else p[nu] - 1     # lower height of the traversed link
        rec.append((sgn, h))
    return rec
okN2, fireCN2 = True, False
for (d, L) in ((2, 3), (2, 5), (4, 3)):
    o = (L - 1)//2
    for mu in range(d):
        for sigma in itertools.permutations(range(d)):
            for y in itertools.product(range(-o, o+1), repeat=d):
                st = contour_steps(d, L, mu, sigma, y)
                for nu in range(d):
                    rec = nu_record(st, nu)
                    if nu == mu:
                        s1 = sum(sg*h for sg, h in rec); s0 = sum(sg for sg, _ in rec)
                        okN2 &= (s1 == L*(L-1)//2 and s0 == L)
                        if sum(sg*(h+1) for sg, h in rec) != L*(L-1)//2: fireCN2 = True
                    else:
                        plus = Counter(h for sg, h in rec if sg == 1); minus = Counter(h for sg, h in rec if sg == -1)
                        okN2 &= (plus == minus)
    print("N2 checked (d, L) =", (d, L))
print("N2 (first moment L(L-1)/2 along mu; exact cancellation across):", "PASS" if okN2 else "FAIL")
print("N2 control CN2 (upper-height convention):", "FIRES" if fireCN2 else "does NOT fire")
print("OVERALL:", "PASS" if (okN1 and okN2 and fireCN1 and fireCN2) else "FAIL")
