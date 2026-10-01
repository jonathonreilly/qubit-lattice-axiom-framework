#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: the exact charge of every touching in the three node families, for all couplings.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J_x = J_y = 1, J_z = J (0 < J < 2), odd term kappa > 0, four-site Bloch matrix H(f) = i M(f). The landed certificate note gives three
exact families of zero-energy touchings of the middle bands: (i) the line nodes (x, 1-x, 0), (1-x, x, 0); (ii) four nodes on
f1 + f2 = 1 for kappa_c < kappa < kappa_h; (iii) four nodes (f3 + g, f3 - g, f3) for kappa > kappa_h. A node's coordinates z_j =
e^{2 pi i f_j} lie in a tower of quadratic extensions of Q(kappa, J); complex conjugation of the node is the automorphism z -> 1/z,
so imaginary parts are read off exactly. The chirality is sign T, T = Im Tr(P d1H P d2H P d3H) = 2 det V (the landed convention),
with P = Pt/e2(M), Pt = M^2 - tr(M) M + e2(M) I the kernel projector, d_jH = -2 pi N_j, N_j = z_j dM/dz_j.
Checks (exact symbolic arithmetic; no floating point): at every node of each family tr M = 0, M Pt = 0, Pt^2 = e2 Pt, tr Pt = 2 e2
(a double zero level); closed forms of T per family and the signs of their factors on each family's domain; the birth, handover and
ordering identities; exact per-coupling tower arithmetic at several hundred rational couplings; agreement with the landed chirality
strings. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 600
RESULTS = []
T0 = time.time()


AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])       # rows: primitive translations of the site and colour rules
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out



# ---------------------------------------------------------------------------------------------- network terms (symbolic tags)
_T = terms((1.0, 1.0, 7.0), 0.3)          # amplitudes 2 (x, y), 14 (z), 0.6 (kappa) tag the three classes
KIND = {2.0: "xy", 14.0: "z", 0.6: "odd"}
TERMS = [(int(a), int(b), tuple(int(x) for x in n), KIND[round(float(t), 9)]) for (a, b, n, t) in _T]
assert len(TERMS) == 18


def amplitude(kind, kap, J, one):
    return {"xy": 2 * one, "z": 2 * J, "odd": 2 * kap}[kind]


# ---------------------------------------------------------------------------------------------- tower of quadratic extensions
class Tower:
    """Tower F < E1 < E2 < ... ; a level-k element is x0 + x1 g_k with x_i in level k-1 and g_k^2 = r1 g_k + r0.
    kind 'circle': g^2 = p g - 1 (g = e^{2 pi i f}, p = 2 cos 2 pi f), conjugation g -> p - g = 1/g.
    kind 'real':   g^2 = r0 (a real radical), conjugation fixes g."""

    def __init__(self, F_zero, F_one, F_from_int):
        self.F0, self.F1, self.fi = F_zero, F_one, F_from_int
        self.levels = []

    def add_level(self, kind, p=None, r0=None):
        base = self.levels[-1] if self.levels else None
        tw = self
        if kind == "circle":
            R1, R0 = p, -1
        else:
            R1, R0 = 0, r0

        class E:
            __slots__ = ("x0", "x1")
            KIND = kind
            P = p
            BASE = base
            RR1, RR0 = R1, R0

            def __init__(s, x0, x1):
                s.x0, s.x1 = x0, x1

            @classmethod
            def lift(cls, x):
                if type(x) is cls:
                    return x
                if cls.BASE is None:
                    if isinstance(x, int):
                        x = tw.fi(x)
                    return cls(x, tw.F0)
                return cls(cls.BASE.lift(x), cls.BASE.zero())

            @classmethod
            def zero(cls):
                return cls(cls.BASE.zero() if cls.BASE else tw.F0, cls.BASE.zero() if cls.BASE else tw.F0)

            @classmethod
            def one(cls):
                return cls(cls.BASE.one() if cls.BASE else tw.F1, cls.BASE.zero() if cls.BASE else tw.F0)

            @classmethod
            def gen(cls):
                return cls(cls.BASE.zero() if cls.BASE else tw.F0, cls.BASE.one() if cls.BASE else tw.F1)

            def __add__(s, o):
                o = type(s).lift(o)
                return type(s)(s.x0 + o.x0, s.x1 + o.x1)

            __radd__ = __add__

            def __neg__(s):
                return type(s)(-s.x0, -s.x1)

            def __sub__(s, o):
                o = type(s).lift(o)
                return type(s)(s.x0 - o.x0, s.x1 - o.x1)

            def __rsub__(s, o):
                return type(s).lift(o) - s

            def __mul__(s, o):
                cls = type(s)
                if type(o) is not cls:
                    return cls(s.x0 * o, s.x1 * o)          # scalar or lower-level factor: componentwise
                a0, a1, b0, b1 = s.x0, s.x1, o.x0, o.x1
                c11 = a1 * b1
                return cls(a0 * b0 + c11 * cls.RR0, a0 * b1 + a1 * b0 + c11 * cls.RR1)

            __rmul__ = __mul__

            def sigma(s):
                cls = type(s)
                u0 = s.x0.sigma() if _is_E(s.x0) else s.x0
                u1 = s.x1.sigma() if _is_E(s.x1) else s.x1
                if cls.KIND == "circle":
                    return cls(u0 + u1 * cls.P, -u1)        # x0 + x1 (p - g)
                return cls(u0, u1)

            def coords(s):
                out = []
                for part in (s.x0, s.x1):
                    out += part.coords() if _is_E(part) else [part]
                return out

        self.levels.append(E)
        return E

    def top(self):
        return self.levels[-1]


def _is_E(x):
    return hasattr(x, "x0") and hasattr(x, "x1")


def _zero(x):
    if _is_E(x):
        return _zero(x.x0) and _zero(x.x1)
    return x == 0


# ---------------------------------------------------------------------------------------------- matrices of tower elements
def mat_zero(Z):
    return [[Z for _ in range(4)] for _ in range(4)]


def mmul(A, B):
    return [[sum((A[r][k] * B[k][c] for k in range(1, 4)), A[r][0] * B[0][c]) for c in range(4)] for r in range(4)]


def madd(A, B):
    return [[A[r][c] + B[r][c] for c in range(4)] for r in range(4)]


def mscale(A, s):
    return [[A[r][c] * s for c in range(4)] for r in range(4)]


def mtrace(A):
    return A[0][0] + A[1][1] + A[2][2] + A[3][3]


def M_and_N(zpows, kap, J, one, zero_el):
    """M (real-coefficient Laurent matrix, H = iM) and N_j = z_j dM/dz_j as 4x4 matrices of tower elements.
    zpows[j][e] = z_j^e for e in -2..2 (tower elements)."""
    M = [[zero_el for _ in range(4)] for _ in range(4)]
    N = [[[zero_el for _ in range(4)] for _ in range(4)] for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        t = amplitude(kind, kap, J, one)
        mon = zpows[0][n[0]] * zpows[1][n[1]] * zpows[2][n[2]]
        mon_inv = zpows[0][-n[0]] * zpows[1][-n[1]] * zpows[2][-n[2]]
        M[a][b] = M[a][b] + mon * t
        M[b][a] = M[b][a] - mon_inv * t
        for j in range(3):
            if n[j]:
                N[j][a][b] = N[j][a][b] + mon * (t * n[j])
                N[j][b][a] = N[j][b][a] + mon_inv * (t * n[j])          # d/dlog z of  -t z^{-n}  =  + n t z^{-n}
    return M, N


def e2_of(M):
    s = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    for i in range(4):
        for j in range(i + 1, 4):
            if (i, j) != (0, 1):
                s = s + (M[i][i] * M[j][j] - M[i][j] * M[j][i])
    return s


def chirality_data(M, N, one_el):
    """Returns dict: e1M, e2M, Pt (matrix), R = Tr(Pt N1 Pt N2 Pt N3)."""
    M2 = mmul(M, M)
    e1 = mtrace(M)
    e2 = e2_of(M)
    Pt = [[M2[r][c] - e1 * M[r][c] + (e2 if r == c else 0 * e2) for c in range(4)] for r in range(4)]
    X1 = mmul(Pt, N[0]); X2 = mmul(Pt, N[1]); X3 = mmul(Pt, N[2])
    Y = mmul(X1, X2)
    R = sum((Y[r][k] * X3[k][r] for r in range(4) for k in range(4)), 0 * e2)
    return dict(e1=e1, e2=e2, Pt=Pt, R=R, M2=M2)


def odd_part(R):
    return (R - R.sigma()) * 1      # 2 * R_odd  (caller divides by 2)


def exact_sign(p, q, D):
    """sign(p + q sqrt(D)), D >= 0 rational, exact."""
    p, q, D = Fr(p), Fr(q), Fr(D)
    if D == 0 or q == 0:
        return (p > 0) - (p < 0)
    if p >= 0 and q >= 0:
        return 1 if (p > 0 or q > 0) else 0
    if p <= 0 and q <= 0:
        return -1
    # opposite signs: compare p^2 with q^2 D
    lhs, rhs = p * p, q * q * D
    if lhs == rhs:
        return 0
    return (1 if p > 0 else -1) if lhs > rhs else (1 if q > 0 else -1)


def _powers(gens, inv, one):
    def pw(g, gi, e):
        r = one
        for _ in range(abs(e)):
            r = r * (g if e > 0 else gi)
        return r
    return [{e: pw(g, gi, e) for e in range(-2, 3)} for g, gi in zip(gens, inv)]


def _identities(M, Pt, e1, e2):
    MP = mmul(M, Pt); PP = mmul(Pt, Pt)
    return (all(c == 0 for c in e1.coords()) and all(all(c == 0 for c in MP[r][q].coords()) for r in range(4) for q in range(4))
            and all(all(c == 0 for c in (PP[r][q] - e2 * Pt[r][q]).coords()) for r in range(4) for q in range(4))
            and all(c == 0 for c in (mtrace(Pt) - e2 * 2).coords()))


def families(J, kap):
    J, kap = Fr(J), Fr(kap)
    u = kap * kap
    uc = J * (J + 2) / (4 * (4 + 2 * J - J * J)); uh = J / (4 * (2 - J))
    out = {"uc": uc, "uh": uh}
    # ---- line
    T1 = Tower(Fr(0), Fr(1), Fr)
    disc = 1 + 8 * u + 16 * u * u - 4 * u * J * J
    Ed = T1.add_level("real", r0=disc)
    cL = (Ed.one() - Ed.gen()) * (1 / (4 * u))
    Ez = T1.add_level("circle", p=cL * 2)
    z = Ez.gen(); one = Ez.one(); zi = Ez.lift(cL * 2) - z
    M, N = M_and_N(_powers([z, zi, one], [zi, z, one], one), kap, J, one, Ez.zero())
    d = chirality_data(M, N, one)
    co = d["R"].coords()
    a_sign = exact_sign(co[2], co[3], disc)           # R = a (z - c): Im R = a sin 2 pi x, x in (0, 1/2) for z = e^{2 pi i x}
    out["line"] = dict(ok=_identities(M, d["Pt"], d["e1"], d["e2"]), chir_plus=-a_sign, e2=d["e2"].coords()[0], disc=disc)
    # ---- plane (ii)
    if uc < u < uh:
        T2 = Tower(Fr(0), Fr(1), Fr)
        c1 = 1 - J / (4 * u); c3 = (J + 2) / (4 * u) - (4 + J - J * J) / J
        Ez2 = T2.add_level("circle", p=2 * c1); Ew2 = T2.add_level("circle", p=2 * c3)
        zz = Ew2.lift(Ez2.gen()); ww = Ew2.gen(); one2 = Ew2.one()
        ziz = (2 * c1) - zz; wwi = (2 * c3) - ww
        pz = _powers([zz, ziz, ww], [ziz, zz, wwi], one2)
        pz = [pz[0], {e: pz[0][-e] for e in range(-2, 3)}, pz[2]]
        M, N = M_and_N(pz, kap, J, one2, Ew2.zero())
        d = chirality_data(M, N, one2)
        co = d["R"].coords()
        out["ii"] = dict(ok=_identities(M, d["Pt"], d["e1"], d["e2"]) and co[2] == 0 and co[3] == 0,
                         chir_plus=-((co[1] > 0) - (co[1] < 0)), e2=d["e2"].coords()[0])
    # ---- plane (iii)
    if u > uh:
        T3 = Tower(Fr(0), Fr(1), Fr)
        sig0 = 5 * J * J + 8 * J + J * (J + 2) / u
        Es = T3.add_level("real", r0=sig0)
        sg = Es.gen()
        Ew3 = T3.add_level("circle", p=Es.lift(J + 2) - sg)
        Ey3 = T3.add_level("circle", p=sg - Es.lift(3 * J + 2))
        w3 = Ey3.lift(Ew3.gen()); y3 = Ey3.gen(); one3 = Ey3.one()
        wi3 = Ey3.lift(Es.lift(J + 2) - sg) - w3
        yi3 = Ey3.lift(sg - Es.lift(3 * J + 2)) - y3
        pz = _powers([w3 * y3, w3 * yi3, w3], [wi3 * yi3, wi3 * y3, wi3], one3)
        M, N = M_and_N(pz, kap, J, one3, Ey3.zero())
        d = chirality_data(M, N, one3)
        co = d["R"].coords()
        e2c = d["e2"].coords()
        out["iii"] = dict(ok=_identities(M, d["Pt"], d["e1"], d["e2"]) and co[2] == 0 and co[3] == 0 and co[6] == 0 and co[7] == 0,
                          chir_g_positive=-exact_sign(co[4], co[5], sig0), e2_sign=exact_sign(e2c[0], e2c[1], sig0), sig0=sig0)
    return out


def predicted(J, kap):
    """chirality strings in the landed runner's node order, from the closed forms (signs of F1, F2 only)."""
    J, kap = Fr(J), Fr(kap)
    u = kap * kap
    uc = J * (J + 2) / (4 * (4 + 2 * J - J * J)); uh = J / (4 * (2 - J))
    F2 = J * (J + 2) - 4 * u * (4 + 2 * J - J * J)
    s = lambda v: "+" if v > 0 else "-"
    line = s(F2) + ("-" if F2 > 0 else "+")                                  # (x, 1-x, 0), (1-x, x, 0)
    if u < uc:
        return line
    if u < uh:
        return line + "++--"                                                 # (xo,1-xo,fo),(xo,1-xo,1-fo),(1-xo,xo,fo),(1-xo,xo,1-fo)
    return line + "-+-+"                                                     # (sf,sg) = (+,+), (+,-), (-,+), (-,-): charge = -sg


def from_tower(J, kap):
    """the same string computed from the exact tower arithmetic."""
    f = families(J, kap)
    line = ("+" if f["line"]["chir_plus"] > 0 else "-")
    line = line + ("-" if line == "+" else "+")
    s = line
    if "ii" in f:
        p = "+" if f["ii"]["chir_plus"] > 0 else "-"
        q = "-" if p == "+" else "+"
        s += p + p + q + q
    if "iii" in f:
        p = "+" if f["iii"]["chir_g_positive"] > 0 else "-"        # nodes with sin 2 pi g > 0 (sg = +1)
        q = "-" if p == "+" else "+"
        s += p + q + p + q
    ok = f["line"]["ok"] and f.get("ii", {"ok": True})["ok"] and f.get("iii", {"ok": True})["ok"] and f.get("iii", {"e2_sign": 1})["e2_sign"] > 0
    return s, ok


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""), flush=True)


Fld, kF, JF = sp.field("k,J", sp.QQ)
k, J, u = sp.symbols("k J u", positive=True)          # u = kappa^2
ex = lambda e: sp.sympify(e.as_expr()).subs({sp.Symbol("k"): k, sp.Symbol("J"): J})
zero_tower = lambda E, coords: all(c == 0 for c in coords)
SAVE = {}


def powers(gens, inv, one):
    def pw(g, gi, e):
        r = one
        for _ in range(abs(e)):
            r = r * (g if e > 0 else gi)
        return r
    return [{e: pw(g, gi, e) for e in range(-2, 3)} for g, gi in zip(gens, inv)]


def node_identities(tag, M, N, one):
    d = chirality_data(M, N, one)
    e1, e2, R, Pt = d["e1"], d["e2"], d["R"], d["Pt"]
    MP = mmul(M, Pt); PP = mmul(Pt, Pt)
    ok_e1 = all(c == 0 for c in e1.coords())
    ok_MP = all(all(c == 0 for c in MP[r][q].coords()) for r in range(4) for q in range(4))
    ok_PP = all(all(c == 0 for c in (PP[r][q] - e2 * Pt[r][q]).coords()) for r in range(4) for q in range(4))
    ok_tr = all(c == 0 for c in (mtrace(Pt) - e2 * 2).coords())
    check(f"{tag}: tr M = 0, M Pt = 0, Pt^2 = e2 Pt, tr Pt = 2 e2 (so P = Pt/e2 is a rank-two projector onto ker H: a double zero "
          "level; tr H = 0 and e2(H) = -e2(M) = -tr(H^2)/2 < 0 put the outer levels at +-sqrt(e2(M)))", ok_e1 and ok_MP and ok_PP and ok_tr,
          f"e1 {ok_e1}, MPt {ok_MP}, PtPt {ok_PP}, trPt {ok_tr}")
    return d


# ======================================================================================================== family (i): line
T1 = Tower(Fld.zero, Fld.one, lambda n: Fld(n))
disc_F = 1 + 8 * kF ** 2 + 16 * kF ** 4 - 4 * kF ** 2 * JF ** 2
Ed = T1.add_level("real", r0=disc_F)
dgen = Ed.gen()
cL = (Ed.one() - dgen) * (1 / (4 * kF ** 2))
Ez = T1.add_level("circle", p=cL * 2)
zL = Ez.gen(); oneL = Ez.one(); ziL = Ez.lift(cL * 2) - zL
chk = cL * cL * (4 * kF ** 2) - cL * 2 + Ed.lift(JF ** 2 - 4 * kF ** 2 - 2)
check("line (i): c = (1 - d)/(4k^2) solves 4k^2 c^2 - 2c + J^2 - 4k^2 - 2 = 0 identically in (k, J)", all(x == 0 for x in chk.coords()))
zpL = powers([zL, ziL, oneL], [ziL, zL, oneL], oneL)
M, N = M_and_N(zpL, kF, JF, oneL, Ez.zero())
dL = node_identities("line (i)", M, N, oneL)
rc = [ex(c) for c in dL["R"].coords()]               # basis 1, d, z, d z
e2L = sp.factor(ex(dL["e2"].coords()[0]))
check("line (i): e2(M) = 16 J^2 (outer levels +-4J)", sp.simplify(e2L - 16 * J ** 2) == 0 and all(c == 0 for c in dL["e2"].coords()[1:]), f"e2 = {e2L}")
disc = 1 + 8 * u + 16 * u ** 2 - 4 * u * J ** 2
U_ = 8 * J * u + J + 8 * u + 2
V_ = 8 * J ** 3 * u ** 2 + 2 * J ** 3 * u + 4 * J ** 2 * u - 32 * J * u ** 2 - 12 * J * u - J - 32 * u ** 2 - 16 * u - 2
F1 = J - 4 * (2 - J) * u                              # kappa_h^2 = J/(4(2-J)) is its root in u
F2 = J * (J + 2) - 4 * u * (4 + 2 * J - J ** 2)       # kappa_c^2 = J(J+2)/(4(4+2J-J^2)) is its root in u
sub_u = lambda e: sp.expand(sp.sympify(e).subs(k, sp.sqrt(u)))
pref_L = 4096 * J ** 3 / k ** 3
r2_ok = sp.simplify(rc[2] - pref_L * disc.subs(u, k ** 2) * U_.subs(u, k ** 2)) == 0
r3_ok = sp.simplify(rc[3] - pref_L * V_.subs(u, k ** 2)) == 0
check("line (i): Im Tr(Pt N1 Pt N2 Pt N3) = a sin 2 pi x with a = (4096 J^3 d/k^3)(d U + V), U = 8Jk^2 + J + 8k^2 + 2, "
      "V = 8J^3k^4 + 2J^3k^2 + 4J^2k^2 - 32Jk^4 - 12Jk^2 - J - 32k^4 - 16k^2 - 2 (coefficients of z and d z of the exact trace)", r2_ok and r3_ok)
# constant part is -a c, i.e. R = a (z - c): the trace is a real multiple of (z - c) = i sin 2 pi x
cc_ = sp.symbols("cc")
const_part = sp.expand(rc[0] + rc[1] * sp.Symbol("dd"))
a_expr = rc[2] + rc[3] * sp.Symbol("dd")
cL_expr = (1 - sp.Symbol("dd")) / (4 * k ** 2)
rem = sp.rem(sp.Poly(sp.expand(const_part + a_expr * cL_expr), sp.Symbol("dd")), sp.Poly(sp.Symbol("dd") ** 2 - disc.subs(u, k ** 2), sp.Symbol("dd")))
check("line (i): the constant part of the trace equals -a c (trace = a (z - c), so Im = a sin 2 pi x exactly)", sp.simplify(rem.as_expr()) == 0)
N_line = 4 * J ** 3 * u ** 2 * (J + 2) * (4 * u + 1) * F2
check("line (i): (V + dU)(V - dU) = V^2 - d^2 U^2 = 4 J^3 k^4 (J+2)(4k^2+1) F2, F2 = J(J+2) - 4k^2(4 + 2J - J^2) (exact identity)",
      sp.expand(V_ ** 2 - disc * U_ ** 2 - N_line) == 0)
d_pos = sp.expand(disc - (4 * u - 1) ** 2 - 4 * u * (4 - J ** 2)) == 0
check("line (i): d^2 - (4k^2 - 1)^2 = 4k^2 (4 - J^2) > 0 for 0 < J < 2, so d > |4k^2 - 1| >= 0; also (1 + 4k^2)^2 - d^2 = 4k^2 J^2 > 0 "
      "hence c = (1 - d)/(4k^2) lies in (-1, 1): two line nodes for every kappa > 0, 0 < J < 2",
      d_pos and sp.expand((1 + 4 * u) ** 2 - disc - 4 * u * J ** 2) == 0)
P_big = sp.expand((4 * u - 1) * U_ - V_)
P_big_ok = sp.expand(P_big - (8 * (8 + 8 * J - J ** 3) * u ** 2 + 2 * (J + 2) ** 2 * (2 - J) * u)) == 0
P_small = sp.expand((1 - 4 * u) * U_ - V_)
P_small_ok = sp.expand(P_small - (2 * (J + 2) + 4 * (J + 1) * (4 - J ** 2) * u + 2 * J ** 3 * u * (1 - 4 * u))) == 0
check("line (i): d U - V > 0 on the whole domain: (4u-1)U - V = 8(8+8J-J^3)u^2 + 2(J+2)^2(2-J)u > 0 (u >= 1/4) and "
      "(1-4u)U - V = 2(J+2) + 4(J+1)(4-J^2)u + 2J^3 u (1-4u) > 0 (u < 1/4), with d >= |4u - 1| (identities, J in (0,2))",
      P_big_ok and P_small_ok and sp.expand(8 + 8 * J - J ** 3 - (8 + 8 * J - 2 * J ** 2) - (2 * J ** 2 - J ** 3)) == 0)
# T for the node (x, 1-x, 0), x in (0, 1/2):  T = -(2 pi)^3 a sin(2 pi x)/e2^3, e2 = 16 J^2
dd = sp.Symbol("dd")
Uk, Vk, Fk2 = U_.subs(u, k ** 2), V_.subs(u, k ** 2), F2.subs(u, k ** 2)
lhs = -8 * sp.pi ** 3 * pref_L * dd * (dd * Uk + Vk) / (16 * J ** 2) ** 3 * (dd * Uk - Vk) - 32 * sp.pi ** 3 * k * dd * (J + 2) * (4 * k ** 2 + 1) * Fk2
rem2 = sp.rem(sp.Poly(sp.together(sp.expand(lhs * k ** 3 * J ** 3)), dd), sp.Poly(dd ** 2 - disc.subs(u, k ** 2), dd))
check("line (i): T(x, 1-x, 0)/sin(2 pi x) = -8 pi^3 a/(16 J^2)^3 = 32 pi^3 k d (J+2)(4k^2+1) F2/(d U - V) (use d^2 = disc and (V+dU)(V-dU) = N)",
      sp.simplify(rem2.as_expr()) == 0)
SAVE["line"] = dict(r=[str(c) for c in rc], e2=str(e2L))

# ======================================================================================================== family (ii)
T2 = Tower(Fld.zero, Fld.one, lambda n: Fld(n))
c1F = 1 - JF / (4 * kF ** 2); c3F = (JF + 2) / (4 * kF ** 2) - (4 + JF - JF ** 2) / JF
Ez2 = T2.add_level("circle", p=2 * c1F)
Ew2 = T2.add_level("circle", p=2 * c3F)
z2g = Ew2.lift(Ez2.gen()); w2g = Ew2.gen(); one2 = Ew2.one()
zi2 = (2 * c1F) - z2g; wi2 = (2 * c3F) - w2g
zp2 = powers([z2g, zi2, w2g], [zi2, z2g, wi2], one2)         # (z1, z2, z3) = (z, 1/z, w)  and the third entry w
zp2 = [zp2[0], {e: zp2[0][-e] for e in range(-2, 3)}, zp2[2]]
M, N = M_and_N(zp2, kF, JF, one2, Ew2.zero())
d2 = node_identities("plane (ii)", M, N, one2)
co2 = [ex(c) for c in d2["R"].coords()]                      # basis 1, z, w, z w
e2_ii = sp.factor(ex(d2["e2"].coords()[0]))
check("plane (ii): e2(M) = 4 (8k^2 - J)(J+2)/k^2", sp.simplify(e2_ii - 4 * (8 * k ** 2 - J) * (J + 2) / k ** 2) == 0 and all(c == 0 for c in d2["e2"].coords()[1:]), f"e2 = {e2_ii}")
a_ii = 128 * (8 * k ** 2 - J) ** 3 * (J + 1) * (J + 2) ** 2 * F1.subs(u, k ** 2) * F2.subs(u, k ** 2) / (J * k ** 7)
c1s = 1 - J / (4 * k ** 2)
check("plane (ii): the exact trace is R = a (z - c1) with NO w part: coefficients of w and z w vanish, and "
      "a = 128 (8k^2 - J)^3 (J+1)(J+2)^2 F1 F2/(J k^7), F1 = J - 4(2-J)k^2, F2 = J(J+2) - 4k^2(4+2J-J^2)",
      co2[2] == 0 and co2[3] == 0 and sp.simplify(co2[1] - a_ii) == 0 and sp.simplify(co2[0] + a_ii * c1s) == 0)
T_ii = -16 * sp.pi ** 3 * (J + 1) * F1.subs(u, k ** 2) * F2.subs(u, k ** 2) / (k * J * (J + 2))
check("plane (ii): T(x, 1-x, +-f3) = -(2 pi)^3 a sin(2 pi x)/e2^3 = -16 pi^3 (J+1) F1 F2 sin(2 pi x)/(k J (J+2)), x in (0, 1/2)",
      sp.simplify(-8 * sp.pi ** 3 * a_ii / (4 * (8 * k ** 2 - J) * (J + 2) / k ** 2) ** 3 - T_ii) == 0)
# existence domain of (ii)
c3s = (J + 2) / (4 * u) - (4 + J - J ** 2) / J
ok_dom = (sp.simplify(1 - c3s + F2 / (4 * J * u)) == 0 and sp.simplify(1 + c3s - (J + 2) * F1 / (4 * J * u)) == 0
          and sp.simplify((1 - c1s.subs(k, sp.sqrt(u))) - J / (4 * u)) == 0 and sp.simplify((1 + c1s.subs(k, sp.sqrt(u))) - (8 * u - J) / (4 * u)) == 0
          and sp.expand((8 * u - J) * (4 + 2 * J - J ** 2) - (-2 * F2 + J ** 3)) == 0)
check("plane (ii): 1 - c3 = -F2/(4Ju), 1 + c3 = (J+2)F1/(4Ju), 1 - c1 = J/(4u), 1 + c1 = (8u - J)/(4u), (8u - J)(4+2J-J^2) = J^3 - 2 F2: "
      "so for 0 < J < 2 the nodes are real and distinct exactly when F2 < 0 < F1, i.e. kappa_c < kappa < kappa_h (then 8k^2 > J)", ok_dom)
sin_ii = sp.sqrt(J * (8 * u - J)) / (4 * u)
check("plane (ii): 1 - c1^2 = J(8u - J)/(16u^2), so sin 2 pi x = sqrt(J(8k^2 - J))/(4k^2) and T(x, 1-x, +-f3) = -4 pi^3 (J+1) F1 F2 sqrt(J(8k^2 - J))/(k^3 J (J+2))",
      sp.simplify((1 - c1s ** 2).subs(k, sp.sqrt(u)) - J * (8 * u - J) / (16 * u ** 2)) == 0
      and sp.simplify((T_ii * sin_ii.subs(u, k ** 2)).subs(k, k) - (-4 * sp.pi ** 3 * (J + 1) * F1.subs(u, k ** 2) * F2.subs(u, k ** 2) * sp.sqrt(J * (8 * k ** 2 - J)) / (k ** 3 * J * (J + 2)))) == 0)
SAVE["ii"] = dict(r=[str(c) for c in co2], e2=str(e2_ii))

# ======================================================================================================== family (iii)
T3 = Tower(Fld.zero, Fld.one, lambda n: Fld(n))
sig0F = 5 * JF ** 2 + 8 * JF + JF * (JF + 2) / kF ** 2
Es = T3.add_level("real", r0=sig0F)
sg = Es.gen()
Ew3 = T3.add_level("circle", p=Es.lift(JF + 2) - sg)
Ey3 = T3.add_level("circle", p=sg - Es.lift(3 * JF + 2))
w3 = Ey3.lift(Ew3.gen()); y3 = Ey3.gen(); one3 = Ey3.one()
wi3 = Ey3.lift(Es.lift(JF + 2) - sg) - w3
yi3 = Ey3.lift(sg - Es.lift(3 * JF + 2)) - y3
zp3 = powers([w3 * y3, w3 * yi3, w3], [wi3 * yi3, wi3 * y3, wi3], one3)
M, N = M_and_N(zp3, kF, JF, one3, Ey3.zero())
d3 = node_identities("plane (iii)", M, N, one3)
co3 = [ex(c) for c in d3["R"].coords()]                      # index 4 e_y + 2 e_w + e_s; basis 1, s, w, s w, y, s y, w y, s w y
s_ = sp.Symbol("s")
check("plane (iii): the exact trace has NO w and NO w y part: R = (r0 + r1 s) + (r4 + r5 s) y (coordinates 2, 3, 6, 7 vanish)",
      co3[2] == 0 and co3[3] == 0 and co3[6] == 0 and co3[7] == 0)
W_ = 5 * J * k ** 2 + 8 * k ** 2 + J + 2
pref3 = 4096 * J ** 2 * (J + 1) * (J + 2) / k ** 3
G0 = sp.cancel(co3[4] / pref3); G1 = sp.cancel(co3[5] / pref3)
Q4 = sp.cancel(G0 / (-J * W_)); Q5 = sp.cancel(G1 / k ** 2)
Q4p = sp.Poly(sp.expand(Q4), J, k); Q5p = sp.Poly(sp.expand(Q5), J, k)
check("plane (iii): b = r4 + r5 s with r4 = -pref J W Q4, r5 = pref k^2 Q5, pref = 4096 J^2 (J+1)(J+2)/k^3, W = 5Jk^2 + 8k^2 + J + 2; "
      "Q4, Q5 are polynomials in J, k^2 with strictly positive coefficients (so Q4, Q5 > 0 for J, k > 0)",
      all(c > 0 for c in Q4p.coeffs()) and all(c > 0 for c in Q5p.coeffs())
      and all(m[1] % 2 == 0 for m in Q4p.monoms()) and all(m[1] % 2 == 0 for m in Q5p.monoms()),
      f"{len(Q4p.coeffs())} and {len(Q5p.coeffs())} terms, min coefficients {min(Q4p.coeffs())}, {min(Q5p.coeffs())}")
sig0 = J * W_ / k ** 2
check("plane (iii): s^2 = 5J^2 + 8J + J(J+2)/k^2 = J W/k^2", sp.simplify(5 * J ** 2 + 8 * J + J * (J + 2) / k ** 2 - sig0) == 0)
Wf = 4 * J ** 2 * u + J ** 2 + 4 * J * u + 2 * J + 4 * u + 1
Norm_b = J * (J + 2) * (4 * u + 1) * (4 * J * u - J + 8 * u) ** 2 * F1 * (4 * J * u - J - 8 * u - 2) ** 2 * W_.subs(k, sp.sqrt(u)) * Wf ** 3
norm_lhs = sp.expand((G0 ** 2 - G1 ** 2 * sig0).subs(k, sp.sqrt(u)))
check("plane (iii): Norm(b)/pref^2 = (r4^2 - r5^2 s^2)/pref^2 = J (J+2)(4u+1) (4Ju - J + 8u)^2 F1 (4Ju - J - 8u - 2)^2 W (4J^2u + J^2 + 4Ju + 2J + 4u + 1)^3, "
      "u = k^2 (exact identity); F1 = J - 4(2-J)u < 0 exactly when kappa > kappa_h", sp.expand(norm_lhs - sp.expand(Norm_b)) == 0)
sg2 = sig0.subs(k, sp.sqrt(u))
ok_dom3 = sp.simplify((J + 4) ** 2 - sg2 + (J + 2) * F1 / u) == 0
ok_dom3 &= sp.simplify(sg2 - J ** 2 - (4 * J ** 2 + 8 * J + J * (J + 2) / u)) == 0
ok_dom3 &= sp.simplify(sg2 - 9 * J ** 2 - (4 * J * (2 - J) + J * (J + 2) / u)) == 0
ok_dom3 &= sp.simplify((3 * J + 4) ** 2 - sg2 - (J + 2) * (4 * (J + 2) - J / u)) == 0
check("plane (iii): with s = +sqrt(s^2): s^2 - J^2 = 4J^2 + 8J + J(J+2)/u > 0, (J+4)^2 - s^2 = -(J+2)F1/u, s^2 - 9J^2 = 4J(2-J) + J(J+2)/u > 0, "
      "(3J+4)^2 - s^2 = (J+2)(4(J+2) - J/u): so cos 2 pi f3 = (J+2-s)/2 and cos 2 pi g = -J - cos 2 pi f3 are both in (-1, 1) "
      "exactly when F1 < 0 (kappa > kappa_h), given 4(J+2)u > J which F1 < 0 implies", ok_dom3)
# e2(M) > 0 in (iii): structural
e2_3 = [sp.factor(ex(c)) for c in d3["e2"].coords()]
check("plane (iii): e2(M) = e0 + e1 s with e2(M) = -tr(M^2)/2 = sum |H_ij|^2/2 > 0 (tr M = 0 exactly, so no sign question); e2 lies in Q(k,J)(s)",
      all(c == 0 for c in d3["e2"].coords()[2:]))
SAVE["iii"] = dict(r=[str(c) for c in co3], e2=[str(c) for c in e2_3])

# ======================================================================================================== signs
# The sign statements follow from the identities above:
#   line (i):   T = 32 pi^3 k d (J+2)(4k^2+1) F2 sin(2 pi x)/(dU - V), dU - V > 0, everything else > 0     => sign T = sign F2 (x < 1/2)
#   plane (ii): T = -16 pi^3 (J+1) F1 F2 sin(2 pi x)/(k J (J+2)),  F1 > 0 > F2 on kappa_c < kappa < kappa_h => sign T = sign sin 2 pi x
#   plane (iii): T = -8 pi^3 b sin(2 pi g)/e2^3, b > 0 (Norm(b) < 0, r5 > 0), e2 > 0                          => sign T = -sign sin 2 pi g
# and are re-checked below by exact arithmetic at rational couplings (a genuine, independent exact computation per coupling).
grid_J = [Fr(j, 5) for j in range(1, 10)] + [Fr(1, 20), Fr(19, 10), Fr(39, 20)]
grid_k0 = sorted({Fr(m, 20) for m in range(1, 61)} | {Fr(49, 100), Fr(51, 100), Fr(387, 1000), Fr(3873, 10000)})
bad, regimes, npts = [], {"I": 0, "II": 0, "III": 0}, 0
for Jr in grid_J:
    uc_ = Jr * (Jr + 2) / (4 * (4 + 2 * Jr - Jr * Jr)); uh_ = Jr / (4 * (2 - Jr))
    mid = Fr(((float(uc_) + float(uh_)) / 2) ** 0.5).limit_denominator(2000)       # a rational kappa inside the (ii) window
    assert uc_ < mid * mid < uh_
    for kr in sorted(set(grid_k0) | {mid}):
        u_ = kr * kr
        if u_ == uc_ or u_ == uh_:
            continue
        got, ok = from_tower(Jr, kr)
        npts += 1
        regimes["I" if u_ < uc_ else ("II" if u_ < uh_ else "III")] += 1
        if (not ok) or got != predicted(Jr, kr):
            bad.append((Jr, kr, got, predicted(Jr, kr), ok))
check(f"exact tower arithmetic at {npts} rational couplings (J in [1/20, j/5 for j = 1..9, 19/10, 39/20]; kappa on a 1/20 grid up to 3, plus a point inside the (ii) window for each J and points beside kappa_c, kappa_h at J = 1; "
      f"regimes {regimes}): every node identity (tr M = 0, kernel projector, no w / w y parts, e2 > 0) holds and the exact chirality string equals the closed-form "
      "prediction (line +-/-+ by sign F2; (ii) ++-- ; (iii) -+-+)", not bad, f"{len(bad)} mismatches {bad[:3]}")
# explicit root-count statement for the line node ordering: sin(2 pi x) > 0 for x in (0, 1/2)
# save formulas for the numerical cross-check script
# exact boundary points: birth at kappa_c and handover at kappa_h
uc = J * (J + 2) / (4 * (4 + 2 * J - J ** 2)); uh = J / (4 * (2 - J))
c0 = (J - 2) * (J + 1) / (J + 2)
dc = 1 - 4 * uc * c0
check("birth at kappa_c: at u = kappa_c^2 the line cosine c = (1 - d)/(4u) equals c1 = (J-2)(J+1)/(J+2) (d_c = (4+4J-J^3)/(4+2J-J^2) > 0) and c3 = 1, "
      "so the four (ii) nodes are born from the two line nodes",
      sp.simplify(dc - (4 + 4 * J - J ** 3) / (4 + 2 * J - J ** 2)) == 0 and sp.simplify(disc.subs(u, uc) - dc ** 2) == 0
      and sp.simplify(c1s.subs(k, sp.sqrt(uc)) - c0) == 0 and sp.simplify(c3s.subs(u, uc) - 1) == 0)
check("handover at kappa_h: at u = kappa_h^2, c3 = -1, c1 = J - 1, and in (iii) s = J + 4 (cos 2 pi f3 = -1, cos 2 pi g = 1 - J)",
      sp.simplify(c3s.subs(u, uh) + 1) == 0 and sp.simplify(c1s.subs(k, sp.sqrt(uh)) - (J - 1)) == 0 and sp.simplify(sig0.subs(k, sp.sqrt(uh)) - (J + 4) ** 2) == 0)
check("ordering: kappa_h^2 - kappa_c^2 = J^2/(2(2-J)(4+2J-J^2)) > 0 for 0 < J < 2 (4 + 2J - J^2 = 5 - (J-1)^2 > 4), so the three kappa ranges are non-empty and ordered",
      sp.simplify(uh - uc - J ** 2 / (2 * (2 - J) * (4 + 2 * J - J ** 2))) == 0 and sp.expand(4 + 2 * J - J ** 2 - (5 - (J - 1) ** 2)) == 0)
# the landed interval certificate's chirality strings at its thirteen couplings (cache of the landed 2026-09-26 certificate)
LANDED = {("1", "1/10"): "+-", ("1", "3/10"): "+-", ("1", "7/20"): "+-", ("1", "9/20"): "-+++--", ("1", "12/25"): "-+++--",
          ("1", "3/5"): "-+-+-+", ("1", "4/5"): "-+-+-+", ("1", "1"): "-+-+-+", ("1/2", "1/5"): "+-", ("1/2", "2/5"): "-+-+-+",
          ("3/2", "2/5"): "+-", ("3/2", "7/10"): "-+++--", ("3/2", "1"): "-+-+-+"}
agree = {key: (predicted(Fr(key[0]), Fr(key[1])), from_tower(Fr(key[0]), Fr(key[1]))[0]) for key in LANDED}
check("the closed-form charge strings and the exact per-coupling strings equal the landed interval certificate's chirality strings at "
      "all thirteen landed couplings", all(v[0] == LANDED[kk] and v[1] == LANDED[kk] for kk, v in agree.items()),
      f"{sum(v[0] == LANDED[kk] for kk, v in agree.items())}/13 closed form, {sum(v[1] == LANDED[kk] for kk, v in agree.items())}/13 per-coupling")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")
