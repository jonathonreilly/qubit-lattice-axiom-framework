"""Independent referee for do-records-fall-with-a-universal-weight a1.

Own generators for the lone record and the 18-state tether. Does not call the author's script.
"""
import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS = []
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
OMEGA = {"equal": F(3, 2), "opposite": F(1, 2), "orthogonal": F(1)}


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def add(u, v, s=1):
    return tuple(a + s * b for a, b in zip(u, v))


# ---------------------------------------------------------------- local drift of one record
g1, g2, g3, a = sp.symbols("g1 g2 g3 a")
g = (g1, g2, g3)
s = sp.symbols("s")
ok = True
for label, omega in (("isolated", None), ("equal", F(3, 2)), ("opposite", F(1, 2)), ("orthogonal", F(1))):
    h = F(1, 2) if omega is None else 1 / (1 + omega)
    v = [0, 0, 0]
    for e in E6:
        if omega is not None and e == (1, 0, 0):
            continue
        rate = sp.exp((1 - a) * dot(g, e)) * h / 6
        v = [v[k] + e[k] * rate for k in range(3)]
    series = []
    for vk in v:
        scaled = vk.subs({g1: s * g1, g2: s * g2, g3: s * g3})
        series.append(sp.expand(sp.series(scaled, s, 0, 2).removeO().subs(s, 1)))
    M = sp.eye(3) * (2 * h) if omega is None else sp.eye(3) * (2 * h) - sp.diag(h, 0, 0)
    b0 = [0, 0, 0] if omega is None else [-h / 6, 0, 0]
    want_v = [b0[k] + (1 - a) / 6 * sum(M[k, j] * g[j] for j in range(3)) for k in range(3)]
    ok = ok and all(sp.expand(series[k] - want_v[k]) == 0 for k in range(3))
    ok = ok and all(sp.expand(series[k].subs(a, 1) - b0[k]) == 0 for k in range(3))
    if omega is None:
        ok = ok and h == F(1, 2) and M == sp.eye(3)
    if label == "equal":
        ok = ok and h == F(2, 5)
    if label == "opposite":
        ok = ok and h == F(2, 3)
    if label == "orthogonal":
        ok = ok and h == F(1, 2)
want("T1 one record: v = b + ((1-a)/6) M g; isolated M=I; neighbour h = 2/5, 2/3, 1/2 and M = h(2I - ee^T); a=1 kills the gradient", ok)

# equilibrium exponent
n, aa = sp.symbols("n a")
c_expr = (2 * aa - 1) * n - 1
ident = -c_expr / n + (1 - 1 / n) - 2 * (1 - aa)
ok = sp.simplify(ident) == 0
ok = ok and sp.simplify(sp.exp((1 - 2 * aa) * n * dot(g, (sp.symbols("X1"), sp.symbols("X2"), sp.symbols("X3"))))
                         - sp.exp(-(2 * aa - 1) * n * dot(g, (sp.symbols("X1"), sp.symbols("X2"), sp.symbols("X3"))))) == 0
want("T2 the weight is (2a-1) per record, and c = (2a-1)n - 1 is exactly the detailed-balance exponent", ok)

# ---------------------------------------------------------------- tether and lone chain
NN = list(E6)
FD = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v) == 2 and max(abs(x) for x in v) == 1]
FD = sorted(FD)
assert len(NN) == 6 and len(FD) == 12


def moves_of(states, W, n):
    S = set(states)
    mv = {d: [] for d in states}
    if n == 1:
        mv[()] = [((), 0, e, F(1, 12), (0, 0, 0)) for e in E6]
        return mv
    for d in states:
        for i in (0, 1):
            for e in E6:
                d2 = add(d, e, -1 if i == 0 else 1)
                if d2 not in S:
                    continue
                h = W[d2] / (W[d] + W[d2])
                r = tuple(F(-x, 2) for x in d) if i == 0 else tuple(F(x, 2) for x in d)
                mv[d].append((d2, i, e, h / 6, r))
    return mv


def generator(states, mv, weight):
    ix = {s: i for i, s in enumerate(states)}
    N = len(states)
    L = sp.zeros(N)
    for s in states:
        for t, i, e, q0, r in mv[s]:
            val = q0 * weight(i, e, r)
            L[ix[s], ix[t]] += val
            L[ix[s], ix[s]] -= val
    return L, ix


def stationary(L, rhs=None):
    N = L.shape[0]
    A = L.T.as_mutable()
    A.row_del(N - 1)
    A = A.row_insert(N - 1, sp.Matrix(1, N, lambda i, j: 1))
    b = sp.zeros(N, 1) if rhs is None else sp.Matrix(-rhs)
    if rhs is None:
        b[N - 1] = 1
    else:
        b[N - 1] = 0
    return A.LUsolve(b)


def poisson(L, f, p0):
    N = L.shape[0]
    A = (-L).as_mutable()
    A.row_del(N - 1)
    A = A.row_insert(N - 1, sp.Matrix(1, N, lambda i, j: p0[j]))
    b = f.as_mutable()
    b[N - 1] = 0
    return A.LUsolve(b)


def diffusion(states, mv, n):
    L0, ix = generator(states, mv, lambda i, e, r: 1)
    p0 = stationary(L0)
    D = sp.zeros(3)

    def lam2(k):
        f = sp.zeros(len(states), 1)
        for s in states:
            f[ix[s]] = sum(q0 * F(dot(k, e), n) for t, i, e, q0, r in mv[s])
        psi = poisson(L0, f, p0)
        tot = 0
        for s in states:
            for t, i, e, q0, r in mv[s]:
                ke = F(dot(k, e), n)
                tot += p0[ix[s]] * q0 * (ke ** 2 / 2 + ke * psi[ix[t]])
        return sp.simplify(tot)

    for i in range(3):
        ei = tuple(1 if j == i else 0 for j in range(3))
        D[i, i] = lam2(ei)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        eij = tuple(1 if m in (i, j) else 0 for m in range(3))
        D[i, j] = D[j, i] = sp.simplify((lam2(eij) - D[i, i] - D[j, j]) / 2)
    return L0, p0, sp.simplify(D)


def velocity(states, mv, n, a_val, ghat, p0, L0):
    ix = {s: i for i, s in enumerate(states)}
    L1, _ = generator(states, mv, lambda i, e, r: dot(ghat, r) + (1 - a_val) * dot(ghat, e))
    p1 = stationary(L0, rhs=(p0.T * L1).T)
    V = [0, 0, 0]
    for s in states:
        for t, i, e, q0, r in mv[s]:
            bump = dot(ghat, r) + (1 - a_val) * dot(ghat, e)
            for c in range(3):
                V[c] += (p1[ix[s]] * q0 + p0[ix[s]] * q0 * bump) * F(e[c], n)
    return [sp.simplify(v) for v in V]


# lone
lone_states = [()]
lone_mv = moves_of(lone_states, {(): F(1)}, 1)
L0, p0, D = diffusion(lone_states, lone_mv, 1)
ok = D == sp.Rational(1, 12) * sp.eye(3) and p0[0] == 1
for a_val in (F(1), F(3, 4), F(0)):
    c = (2 * a_val - 1) * 1 - 1
    for ghat in ((1, 0, 0), (1, 2, 3)):
        V = velocity(lone_states, lone_mv, 1, a_val, ghat, p0, L0)
        pred = [-c * sum(D[k, j] * ghat[j] for j in range(3)) for k in range(3)]
        ok = ok and all(sp.simplify(V[k] - pred[k]) == 0 for k in range(3))
want("T3 lone record: D0 = 1/12 and V1 = -c D0 g at a = 1, 3/4, 0 along x and along (1,2,3)", ok)

# pairs
quoted = {"equal": sp.Rational(2, 105), "opposite": sp.Rational(2, 135), "orthogonal": sp.Rational(1, 54)}
ok = True
for name, omega in OMEGA.items():
    states = NN + FD
    W = {d: (omega if d in NN else F(1)) for d in states}
    mv = moves_of(states, W, 2)
    L0, p0, D = diffusion(states, mv, 2)
    Z = sum(W.values())
    ix = {s: i for i, s in enumerate(states)}
    ok = ok and D == quoted[name] * sp.eye(3)
    ok = ok and all(sp.simplify(p0[ix[s]] - W[s] / Z) == 0 for s in states)
    for a_val in (F(1), F(3, 4), F(0)):
        c = (2 * a_val - 1) * 2 - 1
        for ghat in ((1, 0, 0), (1, 2, 3)):
            V = velocity(states, mv, 2, a_val, ghat, p0, L0)
            pred = [-c * sum(D[k, j] * ghat[j] for j in range(3)) for k in range(3)]
            ok = ok and all(sp.simplify(V[k] - pred[k]) == 0 for k in range(3))
    # one symbolic detailed-balance sweep at this weight
    gg = (g1, g2, g3)
    csym = (2 * a - 1) * 2 - 1
    for s in states:
        for t, i, e, q0, r in mv[s]:
            back = [m for m in mv[t] if m[0] == s and m[1] == i and m[2] == tuple(-x for x in e)]
            if len(back) != 1:
                ok = False
                continue
            _, _, eb, qb, rb = back[0]
            lhs = sp.log(W[s] * q0) + dot(gg, r) + (1 - a) * dot(gg, e)
            rhs = sp.log(W[t] * qb) - csym * dot(gg, tuple(F(x, 2) for x in e)) + dot(gg, rb) + (1 - a) * dot(gg, eb)
            if sp.simplify(sp.expand_log(lhs - rhs, force=True)) != 0:
                ok = False
want("T3 tethered pair: D0 = 2/105, 2/135, 1/54; V1 = -c D0 g; every move balances W exp(-c g.X)", ok)

# instantaneous push, a = 1, exclusion, contact along +x
gs = sp.symbols("g")
Vinst = (F(-1, 12) + F(1, 12) * sp.exp(gs)) / 2
ok = sp.expand(sp.series(Vinst, gs, 0, 2).removeO() - gs / 24) == 0
ok = ok and sp.simplify(Vinst - (sp.exp(gs) - 1) / 24) == 0
want("S9 two records in contact at a=1 have instantaneous centre velocity (e^g - 1)/24, up the gradient", ok)

# the printed special values
ok = True
# a=1 pair: c=1, V = -D
# a=3/4 pair: c = (3/2 - 1)*2 - 1 = 0
# a=0 pair: c = -2 - 1 = -3, V = 3 D
# a=3/4 lone: c = (3/2 - 1) - 1 = -1/2, V = (1/2)/12 = 1/24
# a=0 lone: c = -2, V = 2/12 = 1/6
checks = {
    "pair a=3/4 c": (F(3, 2) - 1) * 2 - 1,
    "pair a=0 c": (0 - 1) * 2 - 1,
    "lone a=3/4": -((F(3, 2) - 1) - 1) * F(1, 12),
    "lone a=0": -((0 - 1) - 1) * F(1, 12),
}
ok = checks["pair a=3/4 c"] == 0 and checks["pair a=0 c"] == -3
ok = ok and checks["lone a=3/4"] == F(1, 24) and checks["lone a=0"] == F(1, 6)
ok = ok and F(3) * F(2, 105) == F(2, 35) and F(3) * F(2, 135) == F(2, 45) and F(3) * F(1, 54) == F(1, 18)
want("T4 the printed drifts follow from V = -c D0: lone 0, 1/24, 1/6 and pairs 3 D0 at a=0", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - at first order in a uniform gradient, one record moves as b + ((1-a)/6) M g, "
    "the equilibrium weight is (2a-1) per record, and a tethered cluster drifts at -((2a-1)n-1) D0 g per centre-clock tick. "
    "D0 is 1/12 for a lone record and 2/105, 2/135, 1/54 for tethered pairs of equal, opposite and orthogonal content. "
    "At a=1 a lone record does not fall and a bound pair falls at D_pair g."
)
print(
    "SUMMARY: confirmed the partial result. The drift is not universal across a lone record and a bound pair, "
    "while the equilibrium weight is one factor (2a-1) per record. "
    "Block 95's free pairs on Z^3 were not shown to be bound; the tether is a finite witness. "
    "The physical-time sketch and the Green-function decay stay as stated, not rebuilt."
)
