# s2_55_1 -- exact checks of the lattice measure term div Xi_v (ROTDEF 3.2 field) and of the scheme family Xi'_lambda.
# Criteria: checks/s2_55_1_criteria.md (written before this script). sympy exact arithmetic only; no floats in verdicts.
import itertools
import sympy as sp

I = sp.I
results = {}
controls = {}

def H(M):
    return M.conjugate().T

def pi_proj(M):
    N = M.shape[0]
    A = (M - H(M)) / 2
    return A - (A.trace() / N) * sp.eye(N)

def herm_part(M):
    return (M + H(M)) / 2

def inner(X, Y):            # <X,Y> = -2 tr(XY), orthonormal basis below
    return sp.expand(-2 * (X * Y).trace())

def s_of(P):
    N = P.shape[0]
    return sp.nsimplify(1) - sp.re(sp.expand(P.trace())) / N

sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
T2 = [-(I / 2) * s for s in sig]
lam = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]), sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]), sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]), sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]), sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3)]
T3 = [-(I / 2) * l for l in lam]
for T in (T2, T3):         # orthonormality sanity (not a verdict gate)
    for i, A in enumerate(T):
        for j, B in enumerate(T):
            assert sp.simplify(inner(A, B) - (1 if i == j else 0)) == 0

def CF(N):
    return sp.Rational(N * N - 1, 2 * N)

# ---------------- C1 / X1 ----------------
def casimir_diff(N, T, proj):
    xs = sp.symbols('x0:%d' % (N * N), real=True)
    ys = sp.symbols('y0:%d' % (N * N), real=True)
    M = sp.Matrix(N, N, lambda i, j: xs[N * i + j] + I * ys[N * i + j])
    tot = sum((Ta * proj(Ta * M)).trace() for Ta in T)
    return sp.simplify(sp.expand(tot + sp.Rational(1, 2) * (N - sp.Rational(1, N)) * sp.re(M.trace())))

c1 = [casimir_diff(2, T2, pi_proj) == 0, casimir_diff(3, T3, pi_proj) == 0]
results['C1'] = all(c1)
x1 = casimir_diff(2, T2, herm_part)
controls['X1'] = (x1 != 0)

# ---------------- helpers: rational SU(2) ----------------
def su2(q):
    q0, q1, q2, q3 = [sp.Rational(v) for v in q]
    assert q0**2 + q1**2 + q2**2 + q3**2 == 1
    return sp.Matrix([[q0 + I * q3, q2 + I * q1], [-q2 + I * q1, q0 - I * q3]])

quats = [(sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5), sp.Rational(4, 5)),
         (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7), 0),
         (sp.Rational(1, 9), sp.Rational(4, 9), sp.Rational(8, 9), 0),
         (sp.Rational(2, 9), sp.Rational(4, 9), sp.Rational(5, 9), sp.Rational(6, 9)),
         (sp.Rational(1, 11), sp.Rational(2, 11), sp.Rational(4, 11), sp.Rational(10, 11)),
         (sp.Rational(2, 11), sp.Rational(6, 11), sp.Rational(9, 11), 0),
         (sp.Rational(3, 13), sp.Rational(4, 13), sp.Rational(12, 13), 0),
         (sp.Rational(-3, 13), sp.Rational(12, 13), 0, sp.Rational(4, 13))]
G = [su2(q) for q in quats]
for g in G:
    assert sp.simplify(g * H(g) - sp.eye(2)) == sp.zeros(2) and sp.simplify(g.det() - 1) == 0

def inv(U):
    return H(U)

def div_left(U, Wp, Wm, a, v, T):
    # xi(U) = -a v (2a^2)^-1 [pi(U Wp) - pi(U Wm)];  d/dt at U -> e^{tT}U gives pi(T U W)
    tot = 0
    for Ta in T:
        dxi = -a * v / (2 * a**2) * (pi_proj(Ta * U * Wp) - pi_proj(Ta * U * Wm))
        tot += inner(Ta, dxi)
    return sp.simplify(tot)

def div_right(U, Wp, Wm, a, v, T, sign=-1):
    # Q_pm = U^-1 W_pm^-1 (same plaquettes, based at far end, starting with U^-1); U -> U e^{tT}: Q -> e^{-tT} Q
    # xi~ = -a v * (sign (2a^2)^-1)[pi(Q+) - pi(Q-)], sign = -1 is the classically consistent choice
    Qp, Qm = inv(U) * inv(Wp), inv(U) * inv(Wm)
    tot = 0
    for Ta in T:
        dxi = -a * v * sign / (2 * a**2) * (pi_proj(-Ta * Qp) - pi_proj(-Ta * Qm))
        tot += inner(Ta, dxi)
    return sp.simplify(tot), Qp, Qm

# ---------------- C2 / X2 ----------------
N = 2
c2_ok, x2_fired, cls_ok = [], [], []
datasets = [(0, 1, 2, sp.Rational(3, 7), sp.Rational(5, 3)), (3, 4, 5, sp.Rational(1, 2), sp.Rational(-2, 5)),
            (6, 7, 0, sp.Rational(2, 9), sp.Rational(7, 4)), (1, 3, 6, sp.Rational(5, 11), sp.Rational(1, 6))]
for (iu, ip, im, a, v) in datasets:
    U, Wp, Wm = G[iu], G[ip], G[im]
    dl = div_left(U, Wp, Wm, a, v, T2)
    pred_l = sp.simplify(N * CF(N) / a * v * (s_of(U * Wp) - s_of(U * Wm)))
    dr, Qp, Qm = div_right(U, Wp, Wm, a, v, T2, sign=-1)
    pred_r = sp.simplify(N * CF(N) / a * v * (s_of(Qp) - s_of(Qm)))
    c2_ok.append(sp.simplify(dl - pred_l) == 0 and sp.simplify(dr - pred_r) == 0)
    cls_ok.append(sp.simplify(s_of(Qp) - s_of(U * Wp)) == 0 and sp.simplify(s_of(Qm) - s_of(U * Wm)) == 0)
    drbad, _, _ = div_right(U, Wp, Wm, a, v, T2, sign=+1)
    nonvac = sp.simplify(s_of(Qp) - s_of(Qm)) != 0
    x2_fired.append(nonvac and sp.simplify(drbad - pred_r) != 0)
results['C2'] = all(c2_ok) and all(cls_ok)
controls['X2'] = all(x2_fired)

# ---------------- C3 / X3 ----------------
R, aa = sp.symbols('R a', positive=True)
x = sp.Matrix(sp.symbols('x1:5', real=True))
c = sp.Matrix(sp.symbols('c1:5', real=True))
dot = lambda p, q: (p.T * q)[0, 0]
vc = R**2 * c + 2 * dot(c, x) * x - dot(x, x) * c
divv = sum(sp.diff(vc[i], x[i]) for i in range(4))
c3a = []
for nu in range(4):
    h = sp.zeros(4, 1); h[nu] = aa / 2
    vm = vc.subs({x[i]: x[i] - h[i] for i in range(4)}, simultaneous=True)
    vp = vc.subs({x[i]: x[i] + h[i] for i in range(4)}, simultaneous=True)
    c3a.append(sp.expand(vm[nu] - vp[nu] + aa * sp.diff(vc[nu], x[nu])) == 0)
c3b = [sp.expand(sp.diff(vc[mu], x[mu]) - divv / 4) == 0 for mu in range(4)]
results['C3'] = all(c3a) and all(c3b)
vbad = sp.Matrix([x[0]**2, 0, 0, 0])
divbad = sum(sp.diff(vbad[i], x[i]) for i in range(4))
controls['X3'] = any(sp.expand(sp.diff(vbad[mu], x[mu]) - divbad / 4) != 0 for mu in range(4))

# ---------------- C4 / X4: 2D torus 3x3, SU(2) ----------------
Lt = 3
sites = [(i, j) for i in range(Lt) for j in range(Lt)]
e = {1: (1, 0), 2: (0, 1)}
def add(xx, d, s=1):
    return ((xx[0] + s * d[0]) % Lt, (xx[1] + s * d[1]) % Lt)
link = {}
k = 0
for xx in sites:
    for mu in (1, 2):
        link[(xx, mu)] = G[k % len(G)] if (k // len(G)) % 2 == 0 else inv(G[(3 * k + 1) % len(G)])
        k += 1
vals = {}
rat = [sp.Rational(p, q) for p, q in [(3, 7), (-2, 5), (5, 3), (1, 4), (-7, 6), (2, 9), (4, 11), (-1, 3), (6, 5)]]
k = 0
for xx in sites:
    for mu in (1, 2):
        vals[(xx, mu)] = rat[k % len(rat)] * (1 + sp.Rational(k, 17)); k += 1
a4 = sp.Rational(2, 3)
def Pplus(xx, mu):
    nu = 3 - mu
    return link[(xx, mu)] * link[(add(xx, e[mu]), nu)] * inv(link[(add(xx, e[nu]), mu)]) * inv(link[(xx, nu)])
def Pminus(xx, mu):
    nu = 3 - mu
    return link[(xx, mu)] * inv(link[(add(add(xx, e[mu]), e[nu], -1), nu)]) * inv(link[(add(xx, e[nu], -1), mu)]) * link[(add(xx, e[nu], -1), nu)]
LHS = 0
for xx in sites:
    for mu in (1, 2):
        U = link[(xx, mu)]
        Pp, Pm = Pplus(xx, mu), Pminus(xx, mu)
        Wp, Wm = inv(U) * Pp, inv(U) * Pm
        dl = div_left(U, Wp, Wm, a4, vals[(xx, mu)], T2)
        dr, _, _ = div_right(U, Wp, Wm, a4, vals[(xx, mu)], T2, sign=-1)
        LHS += (dl + dr) / 2
LHS = sp.simplify(LHS)
RHS = 0
RHSbad = 0
for xx in sites:
    Pp = Pplus(xx, 1)                     # plaquette at xx, plane (1,2)
    sp_ = s_of(Pp)
    br = vals[(xx, 1)] - vals[(add(xx, e[2]), 1)] + vals[(xx, 2)] - vals[(add(xx, e[1]), 2)]
    brb = vals[(add(xx, e[2]), 1)] - vals[(xx, 1)] + vals[(xx, 2)] - vals[(add(xx, e[1]), 2)]
    RHS += N * CF(N) / a4 * sp_ * br
    RHSbad += N * CF(N) / a4 * sp_ * brb
RHS = sp.simplify(RHS); RHSbad = sp.simplify(RHSbad)
results['C4'] = sp.simplify(LHS - RHS) == 0
controls['X4'] = sp.simplify(LHS - RHSbad) != 0

# ---------------- C5 / X5: scheme family at leading order ----------------
# run-2 fix (2026-10-29, after run 1): t and lambda must be REAL symbols; run 1 declared them complex, so sp.re(.)
# split t into re(t), im(t) and the t-coefficient comparison of C5/X5 was meaningless (see s2_55_1_out_run1.txt).
t = sp.symbols('t', real=True)
lmb = sp.Symbol('lambda', real=True)
def ah(a1, a2, a3):
    return I * (sp.Rational(a1) * sig[0] + sp.Rational(a2) * sig[1] + sp.Rational(a3) * sig[2])
def expser(A, order=7):
    Mt = sp.eye(2); term = sp.eye(2)
    for n in range(1, order + 1):
        term = term * (t * A) / n
        Mt = Mt + term
    return Mt.applyfunc(sp.expand)
c5_ok, x5_fired, nonvac5 = [], [], []
for (Ap, Am) in [(ah(1, 2, -1), ah(sp.Rational(1, 2), -3, 2)), (ah(3, 0, 1), ah(-1, 1, 1)), (ah(sp.Rational(2, 3), 1, 0), ah(0, -2, sp.Rational(5, 4)))]:
    Pp, Pm = expser(Ap), expser(Am)
    ff = (pi_proj(Pp) - pi_proj(Pm)) / 2                      # a = 1
    E = -lmb / N * sp.re(sp.expand((ff * (Pp + Pm)).trace()))
    target = lmb * (s_of(Pp) - s_of(Pm))
    diff = sp.expand(E - target)
    coeffs = [sp.simplify(diff.coeff(t, kk)) for kk in (0, 1, 2, 3)]
    c5_ok.append(all(cc == 0 for cc in coeffs))
    s2coef = sp.simplify(sp.expand(s_of(Pp) - s_of(Pm)).coeff(t, 2))
    nonvac5.append(s2coef != 0)
    Ebad = -lmb * sp.re(sp.expand((ff * (Pp + Pm)).trace()))   # 1/N dropped
    x5_fired.append(sp.simplify(sp.expand(Ebad - target).coeff(t, 2)) != 0)
results['C5'] = all(c5_ok) and all(nonvac5)
controls['X5'] = all(x5_fired)
mt = {NN: CF(NN) - CF(NN) * NN / NN for NN in (2, 3)}   # m~ at lambda = N C_F: C_F - lambda/N
assert all(v == 0 for v in mt.values())

# ---------------- C6 / X6: numbers with rational pi enclosure ----------------
pl, pu = sp.Rational(333, 106), sp.Rational(355, 113)
c6 = []
info = []
for NN in range(2, 7):
    lo = 12 * pl**2 * (NN**2 - 1) / (11 * NN**2)
    hi = 12 * pu**2 * (NN**2 - 1) / (11 * NN**2)
    cap = 12 * pu**2 / 11
    two_b0_hi = sp.Rational(11 * NN, 24) / pl**2
    c6.append((hi < cap) and (cap < sp.Rational(1077, 100)) and (CF(NN) > two_b0_hi))
    if NN == 2:
        c6.append(lo > 8)
    l2lo, l2hi = sp.Rational(6931, 10000), sp.Rational(6932, 10000)
    span_pert = (2 * NN * sp.Rational(11 * NN, 24) / pu**2 * l2lo, 2 * NN * sp.Rational(11 * NN, 24) / pl**2 * l2hi)
    span_tree = ((NN**2 - 1) * l2lo, (NN**2 - 1) * l2hi)
    info.append((NN, float(lo), float(hi), [float(z) for z in span_pert], [float(z) for z in span_tree]))
results['C6'] = all(c6)
lo2 = 12 * pl**2 * 3 / 44
controls['X6'] = not (lo2 < 8)          # "ratio_2 < 8" must be False under the enclosure

for kk in sorted(results):
    print(kk, 'PASS' if results[kk] else 'FAIL')
for kk in sorted(controls):
    print(kk, 'FIRED' if controls[kk] else 'DID-NOT-FIRE')
print('X1 residual (Hermitian part, N=2):', x1)
print('C4 LHS =', LHS)
print('C4 RHS =', RHS)
print('informational (float display only): N, ratio C_F/(2beta_0) enclosure, octave span in beta-units [perturbative 2N*2beta_0*log2], [tree (N^2-1)log2]:')
for row in info:
    print('  ', row)
ok = all(results.values()) and all(controls.values())
print('VERDICT:', 'PASS' if ok else 'FAIL')
