#!/usr/bin/env python3
"""Independent referee of deferred-20260924-ledger attempt a1.

Author w-macbookpro9927a-j2f0e (claude-opus-5-5). Referee w-macbookpro90c72-j17e8 (grok-4.6).
Own Gaussian arithmetic and own sympy. The author's check.py is not imported.
"""
from fractions import Fraction as F

import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAILS.append(msg)


class G:
    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, F) else F(r)
        self.i = i if isinstance(i, F) else F(i)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.r + o.r, self.i + o.i)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.r - o.r, self.i - o.i)

    def __neg__(self):
        return G(-self.r, -self.i)

    def __mul__(self, o):
        if not isinstance(o, G):
            o = G(o)
        return G(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)

    def __rmul__(self, o):
        return self * o

    def conj(self):
        return G(self.r, -self.i)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.r == o.r and self.i == o.i

    def __truediv__(self, o):
        if isinstance(o, G):
            n = o.r * o.r + o.i * o.i
            return G((self.r * o.r + self.i * o.i) / n, (self.i * o.r - self.r * o.i) / n)
        return G(self.r / o, self.i / o)


def gpown(z, n):
    if n < 0:
        return gpown(z.conj(), -n)  # |z| = 1
    out = G(1)
    for _ in range(n):
        out = out * z
    return out


I = G(0, 1)
INV2I = G(0, F(-1, 2))  # 1/(2i)


def dot(u, v):
    return u[0].conj() * v[0] + u[1].conj() * v[1]


def sig(a, v):
    x, y = v
    if a == 0:
        return (y, x)
    if a == 1:
        return (-I * y, I * x)
    return (x, -y)


def add2(u, v):
    return (u[0] + v[0], u[1] + v[1])


def scale2(c, v):
    return (c * v[0], c * v[1])


class State:
    def __init__(self, waves):
        # waves: (z1, z2, z3, chi)
        self.waves = waves

    def psi(self, x):
        acc = (G(0), G(0))
        for z, chi in self.waves:
            amp = gpown(z[0], x[0]) * gpown(z[1], x[1]) * gpown(z[2], x[2])
            acc = add2(acc, scale2(amp, chi))
        return acc


def shift(x, a, m=1):
    y = list(x)
    y[a] += m
    return tuple(y)


def apply_S(st, j, x):
    return scale2(INV2I, add2(st.psi(shift(x, j, 1)), scale2(-1, st.psi(shift(x, j, -1)))))


def apply_C(st, j, x):
    return scale2(F(1, 2), add2(st.psi(shift(x, j, 1)), st.psi(shift(x, j, -1))))


def apply_P(st, j, x):
    # P = S C; C first, then S, on the two-component field. Both are scalar shifts.
    # Implement P on psi by applying C's weights inside S.
    # (C psi)(y) = (psi(y+e)+psi(y-e))/2, then S of that.
    def cpsi(y):
        return apply_C(st, j, y)
    return scale2(INV2I, add2(cpsi(shift(x, j, 1)), scale2(-1, cpsi(shift(x, j, -1)))))


def theta(st, a, j, x):
    return dot(st.psi(x), sig(a, apply_S(st, j, x))).r


def current(st, a, j, x, mom):
    y = shift(x, a, 1)
    return (dot(st.psi(y), sig(a, mom(st, j, x))) + dot(mom(st, j, y), sig(a, st.psi(x)))).r / 2


def rho(st, x):
    return dot(st.psi(x), st.psi(x)).r


def eig(s, E):
    return (G(E + s[2]), G(s[0], s[1]))


def reflection(z2, z3, s, E):
    # e^{i(pi/2+th)} = i e^{i th}, e^{i th} = 4/5 + i 3/5
    eth = G(F(4, 5), F(3, 5))
    z1 = I * eth
    z1p = I * eth.conj()
    chi = eig(s, E)
    return State([((z1, z2, z3), chi), ((z1p, z2, z3), chi)])


def box(r):
    return [(a, b, c) for a in range(-r, r + 1) for b in range(-r, r + 1) for c in range(-r, r + 1)]


# ---------------------------------------------------------------- reflection states
z45 = G(F(4, 5), F(3, 5))
one = G(1)
cases = [
    (z45, one, (F(4, 5), F(3, 5), F(0)), F(1), (F(4, 5), F(1))),
    (one, z45, (F(4, 5), F(0), F(3, 5)), F(1), (F(1), F(4, 5))),
    (one, one, (F(4, 5), F(0), F(0)), F(4, 5), (F(1), F(1))),
]
spatial_bad = []
sym_nonzero = 0
states = []
for z2, z3, s, E, cosk in cases:
    st = reflection(z2, z3, s, E)
    states.append(st)
    for x in box(1):
        hp = (G(0), G(0))
        for a in range(3):
            hp = add2(hp, sig(a, apply_S(st, a, x)))
        p = st.psi(x)
        if not (hp[0] == E * p[0] and hp[1] == E * p[1]):
            spatial_bad.append(("H", x))
        r = rho(st, x)
        for a in range(3):
            for j in range(3):
                if theta(st, a, j, x) != s[a] * s[j] * r / E:
                    spatial_bad.append(("Th", a, j))
                want = F(0) if a == 0 else s[a] * s[j] * cosk[a - 1] * r / E
                if current(st, a, j, x, apply_S) != want:
                    spatial_bad.append(("J", a, j, x))
        for j in range(3):
            dv = sum((current(st, a, j, x, apply_S) - current(st, a, j, shift(x, a, -1), apply_S)) for a in range(3))
            if dv != 0:
                spatial_bad.append(("div", x, j))
st0 = states[0]
for x in box(1):
    for j in range(3):
        acc = F(0)
        for a in range(3):
            here = (current(st0, a, j, x, apply_S) + current(st0, j, a, x, apply_S)) / 2
            back = shift(x, a, -1)
            there = (current(st0, a, j, back, apply_S) + current(st0, j, a, back, apply_S)) / 2
            acc += here - there
        if acc != 0:
            sym_nonzero += 1
require(not spatial_bad and sym_nonzero > 0,
        f"A1 reflection states on [-1,1]^3: H psi=E psi, Theta and J match, div J=0, sym-div nonzero at {sym_nonzero} sites")

# ---------------------------------------------------------------- spanning determinants, own matrix from v⊗s and s⊗s
c = sp.symbols("c")
pts = [(sp.Rational(4, 5), sp.Rational(3, 5)), (sp.Rational(3, 5), sp.Rational(4, 5)), (1, 0), (0, 1),
       (sp.Rational(-4, 5), sp.Rational(3, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)),
       (sp.Rational(12, 13), sp.Rational(-5, 13))]
samples = [(pts[0], pts[1]), (pts[1], pts[4]), (pts[5], pts[2]), (pts[2], pts[6]), (pts[0], pts[3]), (pts[6], pts[5])]
rows_j, rows_t = [], []
for (c2, s2), (c3, s3) in samples:
    v = (c2 * s2, c3 * s3)
    u = (c, s2, s3)
    rows_j.append([v[a] * u[j] for a in range(2) for j in range(3)])
    rows_t.append([u[a] * u[b] for a in range(3) for b in range(a, 3)])
det_j = sp.factor(sp.Matrix(rows_j).det())
det_t = sp.factor(sp.Matrix(rows_t).det())
pj, pt = sp.Poly(sp.expand(det_j), c), sp.Poly(sp.expand(det_t), c)
require(pj.degree() == 2 and pt.degree() == 4 and pj.LC() != 0 and pt.LC() != 0
        and sp.expand(det_j - pj.LC() * c**2) == 0 and sp.expand(det_t - pt.LC() * c**4) == 0,
        f"A2 span dets are {pj.LC()} c^2 and {pt.LC()} c^4")
require(pj.LC() == sp.Rational(298980605952, 165695302703125)
        and pt.LC() == sp.Rational(-2778946464, 75418890625),
        "A2 the leading coefficients are the rationals stated in the attempt")

# ---------------------------------------------------------------- W3 at the axis and at the generic rational q
cc = sp.Rational(4, 5)
trips = {
    0: [(cc, 0, 0), (cc, sp.Rational(3, 5), 0), (cc, 0, sp.Rational(3, 5))],
    1: [(cc, sp.Rational(3, 5), 0), (cc, sp.Rational(3, 5), sp.Rational(4, 5)), (cc, sp.Rational(4, 5), 0)],
    2: [(cc, 0, sp.Rational(3, 5)), (cc, sp.Rational(4, 5), sp.Rational(3, 5)), (cc, 0, sp.Rational(4, 5))],
}
dets = [sp.Matrix(trips[j]).det() for j in range(3)]
require(dets == [sp.Rational(36, 125), sp.Rational(-16, 125), sp.Rational(16, 125)],
        f"B1 three axis pairs per component are independent (dets {dets})")

half = [(sp.Rational(4, 5), sp.Rational(3, 5)), (sp.Rational(12, 13), sp.Rational(5, 13)),
        (sp.Rational(15, 17), sp.Rational(8, 17))]


def pauli(v):
    return sp.Matrix([[v[2], v[0] - sp.I * v[1]], [v[0] + sp.I * v[1], -v[2]]])


f = sp.symbols("f1:4")
fs = pauli(f)
eqs = []
species_ok = None
for choice in range(8):
    s = [half[a][0] if (choice >> a) & 1 else half[a][1] for a in range(3)]
    spn = [half[a][0] if (choice >> a) & 1 else -half[a][1] for a in range(3)]
    e2 = sum(x * x for x in s)
    X = e2 * fs + pauli(spn) * fs * pauli(s)
    Y = pauli(spn) * fs + fs * pauli(s)
    entries = [sp.expand(z) for z in list(X) + list(Y)]
    if choice == 0:
        species_ok = all(sp.expand(z.subs({f[a]: half[a][1] for a in range(3)})) == 0 for z in entries)
    else:
        eqs.extend(entries)
rank_m = sp.Matrix([[sp.expand(z).coeff(fv) for fv in f] for z in eqs]).rank()
require(rank_m == 3 and species_ok,
        "B2 generic rational q: seven per-component pairs give rank 3, and the species point accepts f parallel to sin(q/2)")

# shears span Sym(3); opposite axes intersect only at 0
shears = []
for c_ax in range(3):
    for w in range(3):
        m = sp.zeros(3)
        m[c_ax, w] += 1
        m[w, c_ax] += 1
        shears.append(sp.Matrix([m[a, b] for a in range(3) for b in range(a, 3)]))
require(sp.Matrix.hstack(*shears).rank() == 6, "B limit: the symmetrized rank-one updates span Sym(3), so sym P(0)=0")
require(all(
    sp.Matrix.hstack(
        sp.Matrix([1 if i == c_ax else 0 for i in range(3)]),
        sp.Matrix([1 if i == d else 0 for i in range(3)]),
    ).rank() == 2
    for c_ax in range(3) for d in range(c_ax + 1, 3)),
    "C limit: e_c⊗C^3 meets e_d⊗C^3 only at 0 when c≠d, so a shear is annihilated and ΛR(0) cannot be 1")

# ---------------------------------------------------------------- transposed law, symbols
k, kp, q = sp.symbols("k kp q", real=True)
ident = sp.simplify(
    sp.sin(k - kp) * (sp.sin(2 * k) + sp.sin(2 * kp)) / 2
    - sp.cos(k - kp) * (sp.sin(k) ** 2 - sp.sin(kp) ** 2)
)
require(ident == 0, "D1 with q=k-k', sin q (P(k)+P(k')) = cos q (sin^2 k - sin^2 k')")
phi_d = sp.simplify((1 + sp.exp(-sp.I * q)) / 2 * (sp.exp(sp.I * q) - 1) - sp.I * sp.sin(q))
require(phi_d == 0, "D3 symbol of phi_j d_j along its own axis is i sin q")
# sum_j prod_{l≠j} cos q_l * sin q_j * (P_j+P_j') = (prod cos) (|s|^2-|s'|^2)
ks = sp.symbols("k1:4", real=True)
kps = sp.symbols("kp1:4", real=True)
qs = [ks[j] - kps[j] for j in range(3)]
term = 0
for j in range(3):
    prod = 1
    for l in range(3):
        if l != j:
            prod *= sp.cos(qs[l])
    term += prod * sp.sin(qs[j]) * (sp.sin(ks[j]) * sp.cos(ks[j]) + sp.sin(kps[j]) * sp.cos(kps[j]))
want = sp.prod([sp.cos(qs[l]) for l in range(3)]) * (
    sum(sp.sin(ks[j]) ** 2 for j in range(3)) - sum(sp.sin(kps[j]) ** 2 for j in range(3))
)
require(sp.simplify(term - want) == 0, "D1 the transposed weight collapses to (prod cos q)(|s|^2-|s'|^2)")

# finite stencil of K on the first reflection state, at the origin and its neighbours
def field_C(g, a, x):
    return (g(shift(x, a, 1)) + g(shift(x, a, -1))) / 2


def transposed(st, mom, a, x):
    def raw(j, y):
        return current(st, a, j, y, mom)

    acc = F(0)
    for j in range(3):
        def layer(y, j=j):
            return raw(j, shift(y, j, 1)) - raw(j, shift(y, j, -1))

        g = layer
        for l in range(3):
            if l != j:
                prev = g
                g = lambda y, prev=prev, l=l: field_C(prev, l, y)
        acc += g(x)
    return acc


k_bad = []
j_nonzero = 0
for x in [(0, 0, 0), (1, 0, 0), (0, 1, -1)]:
    for a in range(3):
        if transposed(st0, apply_P, a, x) != 0:
            k_bad.append((x, a))
        if transposed(st0, apply_S, a, x) != 0:
            j_nonzero += 1
require(not k_bad and j_nonzero > 0,
        f"D2 on the reflection state, the transposed stencil of K vanishes and the same stencil of J does not ({j_nonzero} hits)")

# ---------------------------------------------------------------- block 62 static kernel
hs = sp.symbols("h11 h22 h33 h12 h13 h23")
h = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
kernel_ok = True
for pv in [(1, 0, 0), (1, 2, 2), (sp.Rational(2, 5), sp.Rational(1, 3), sp.Rational(-3, 7))]:
    p = sp.Matrix(pv)
    p2 = (p.T * p)[0]
    form = (-(p2 / 4) * (h.T * h).trace() + sp.Rational(1, 2) * ((h * p).T * (h * p))[0]
            - sp.Rational(1, 2) * (p.T * h * p)[0] * h.trace() + (p2 / 4) * h.trace() ** 2)
    hess = sp.hessian(form, hs)
    gauges = []
    for b in range(3):
        eta = sp.Matrix([1 if t == b else 0 for t in range(3)])
        g = p * eta.T + eta * p.T
        gauges.append(sp.Matrix([g[0, 0], g[1, 1], g[2, 2], g[0, 1], g[0, 2], g[1, 2]]))
    kernel_ok = kernel_ok and hess.rank() == 3 and sp.Matrix.hstack(*gauges).rank() == 3
    kernel_ok = kernel_ok and all((hess * g).is_zero_matrix for g in gauges)
require(kernel_ok, "D4 at three nonzero p the static hessian has rank 3 and kernel the relabelling directions")

# plain transfer pairing on the first reflection state, xi = e_1 at the origin
def fwd(field, a):
    out = {}
    for x, v in field.items():
        out[x] = out.get(x, F(0)) - v
        y = shift(x, a, -1)
        out[y] = out.get(y, F(0)) + v
    return {x: v for x, v in out.items() if v != 0}


xi = [{(0, 0, 0): F(1)}, {}, {}]
pairing = F(0)
for a in range(3):
    for j in range(3):
        piece = {}
        for part in (fwd(xi[j], a), fwd(xi[a], j)):
            for x, v in part.items():
                piece[x] = piece.get(x, F(0)) + v / 2
        for x, v in piece.items():
            pairing += v * theta(st0, a, j, x)
require(pairing == F(-1152, 625), f"B3 plain transfer on s=(4/5,3/5,0), xi_1=delta_0, pairing {pairing}")

xi2 = [{}, {(0, 0, 0): F(1)}, {}]
pairing_j = F(0)
conserved = F(0)
for a in range(3):
    for j in range(3):
        piece = {}
        for part in (fwd(xi2[j], a), fwd(xi2[a], j)):
            for x, v in part.items():
                piece[x] = piece.get(x, F(0)) + v / 2
        for x, v in piece.items():
            pairing_j += v * current(st0, a, j, x, apply_S)
        for x, v in fwd(xi2[j], a).items():
            conserved += v * current(st0, a, j, x, apply_S)
require(conserved == 0 and pairing_j == F(-1728, 3125),
        f"C1 conservation pairing {conserved}, plain bond realisation pairing {pairing_j}")

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0])
else:
    print("HIT: confirmed - site and nearest-bond placements of S cannot source the symmetric member; the two-step current K can")
    print("SUMMARY: confirmed - reflection responses, the axis span, W3 rank 3, the transposed identity for K, "
          "and the plain-transfer pairings -1152/625 and -1728/3125.")
