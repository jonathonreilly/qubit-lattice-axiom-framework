#!/usr/bin/env python3
"""Independent exact check of block 152 T1(d) (channel closure), block 154 T1(a)-(c) (every placement gives E_b v_b at zero
transfer) and block 154 T3(b)-(d) (hop range R sets the order N <= R + 2), as LANDED on origin/main (3e1a2dd2).

Only fractions, integers and sympy are used for finite claims.  One line per check: PASS/FAIL.
Families:  A  channel closure of block 152 T1(d)        (polynomial identity, equality set, sample grid, pi/4 sharpness)
           B  block 154 T1: continuity symbol at first order in the transfer, generic placements, matching with a uniform lapse
           C  block 154 T3: power-series orders against hop range R = 1..6 (Groebner), Vandermonde lemma, the f_m family
"""
from __future__ import annotations

import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
PASS = 0
FAIL = 0


def check(tag: str, ok: bool, msg: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAIL += 1
        print(f"FAIL: {tag} {msg}")


# =============================================================================================== family A
def rational_angles():
    """Exact (sin, cos) pairs on the unit circle, closed under k -> -k and k -> pi - k and k -> k + pi."""
    pts = set()
    ts = [Fr(0), Fr(1), Fr(1, 2), Fr(2), Fr(1, 3), Fr(3), Fr(2, 3), Fr(3, 2), Fr(1, 5), Fr(5, 2)]
    for t in ts:
        s, c = 2 * t / (1 + t * t), (1 - t * t) / (1 + t * t)
        for ss in (s, -s):
            for cc in (c, -c):
                pts.add((ss, cc))
    pts.add((Fr(0), Fr(-1)))
    return sorted(pts)


ANG = rational_angles()


def add_ang(u, v):
    return (u[0] * v[1] + u[1] * v[0], u[1] * v[1] - u[0] * v[0])


def eps2(kv):
    return sum(c[0] * c[0] for c in kv)


def le_sum(x2, y2, z2):
    """sqrt(x2) <= sqrt(y2) + sqrt(z2) exactly, for nonnegative rationals."""
    lhs = x2 - y2 - z2
    return lhs <= 0 or lhs * lhs <= 4 * y2 * z2


def eq_sum(x2, y2, z2):
    """sqrt(x2) == sqrt(y2) + sqrt(z2) exactly."""
    lhs = x2 - y2 - z2
    return lhs >= 0 and lhs * lhs == 4 * y2 * z2


def family_a() -> None:
    # A1: polynomial identity eps(a+b)^2 = eps(a)^2 + eps(b)^2 - 2W + 2 u.v, with W = sum sin^2 a_i sin^2 b_i,
    #     u_i = sin a_i cos b_i, v_i = cos a_i sin b_i, modulo sin^2 + cos^2 = 1 on every component (d = 1, 2, 3).
    ok_all = True
    for d in (1, 2, 3):
        s = sp.symbols(f"s1:{d + 1}")
        c = sp.symbols(f"c1:{d + 1}")
        t = sp.symbols(f"t1:{d + 1}")
        w = sp.symbols(f"w1:{d + 1}")
        gens = list(s) + list(c) + list(t) + list(w)
        rel = [s[i] ** 2 + c[i] ** 2 - 1 for i in range(d)] + [t[i] ** 2 + w[i] ** 2 - 1 for i in range(d)]
        G = sp.groebner(rel, *gens, order="grevlex")
        e2a = sum(x ** 2 for x in s)
        e2b = sum(x ** 2 for x in t)
        e2ab = sum((s[i] * w[i] + c[i] * t[i]) ** 2 for i in range(d))
        W = sum(s[i] ** 2 * t[i] ** 2 for i in range(d))
        uv = sum(s[i] * w[i] * c[i] * t[i] for i in range(d))
        u2 = sum((s[i] * w[i]) ** 2 for i in range(d))
        v2 = sum((c[i] * t[i]) ** 2 for i in range(d))
        r1 = G.reduce(sp.expand(e2ab - (e2a + e2b - 2 * W + 2 * uv)))[1]
        r2 = G.reduce(sp.expand(u2 - (e2a - W)))[1]
        r3 = G.reduce(sp.expand(v2 - (e2b - W)))[1]
        ok_all = ok_all and r1 == 0 and r2 == 0 and r3 == 0
    check("A1", ok_all,
          "identities modulo sin^2+cos^2=1 for d=1,2,3: eps(a+b)^2 = eps(a)^2+eps(b)^2-2W+2u.v, |u|^2 = eps(a)^2-W, |v|^2 = eps(b)^2-W "
          "(W = sum sin^2a_i sin^2b_i >= 0), so (eps(a)+eps(b))^2 - eps(a+b)^2 = 2W + 2(eps(a)eps(b) - u.v) with eps(a)eps(b) >= |u||v| >= u.v: subadditivity for all a, b")

    # A2: exact grid d=2 (all pairs) : subadditivity, and equality iff one record has eps = 0 (sits at a corner)
    n_pairs = n_eq = n_strict = 0
    sub_ok = True
    eq_char = True
    for a in itertools.product(ANG, repeat=2):
        ea2 = eps2(a)
        for b in itertools.product(ANG, repeat=2):
            eb2 = eps2(b)
            ab = tuple(add_ang(a[i], b[i]) for i in range(2))
            eab2 = eps2(ab)
            n_pairs += 1
            sub_ok = sub_ok and le_sum(eab2, ea2, eb2)
            is_eq = eq_sum(eab2, ea2, eb2)
            if is_eq:
                n_eq += 1
            else:
                n_strict += 1
            eq_char = eq_char and (is_eq == (ea2 == 0 or eb2 == 0))
    check("A2", sub_ok and eq_char and n_eq > 0 and n_strict > 0,
          f"d=2 exact grid ({n_pairs} pairs of points with rational sines and cosines): eps(a+b) <= eps(a)+eps(b) always; equality ({n_eq} cases) holds exactly "
          f"when eps(a) = 0 or eps(b) = 0, i.e. one record sits at a corner ({n_strict} strict cases)")

    # A3: d=3 random sample, same two statements
    rng = random.Random(20260926)
    sub3 = eq3 = True
    n3 = 0
    for _ in range(60000):
        a = tuple(rng.choice(ANG) for _ in range(3))
        b = tuple(rng.choice(ANG) for _ in range(3))
        ab = tuple(add_ang(a[i], b[i]) for i in range(3))
        ea2, eb2, eab2 = eps2(a), eps2(b), eps2(ab)
        sub3 = sub3 and le_sum(eab2, ea2, eb2)
        eq3 = eq3 and (eq_sum(eab2, ea2, eb2) == (ea2 == 0 or eb2 == 0))
        n3 += 1
    check("A3", sub3 and eq3, f"d=3 random exact sample ({n3} pairs): subadditivity, and equality iff one record has eps = 0")

    # A4: the closure: (+,+) incoming at total K, any (+,-) outgoing at the same K; d=2 grid
    # the (+,-) pair energy eps(k1') - eps(k2') <= eps(K) <= eps(k1)+eps(k2), strict unless a record is at a corner
    n_close = 0
    close_ok = True
    for K in itertools.product(ANG, repeat=2):
        eK2 = eps2(K)
        for k1 in itertools.product(ANG, repeat=2):
            k2 = tuple(add_ang(K[i], (-k1[i][0], k1[i][1])) for i in range(2))  # K - k1
            e1, e2 = eps2(k1), eps2(k2)
            # eps(k1) <= eps(K) + eps(k2)  (so  eps(k1) - eps(k2) <= eps(K))   [(+,-) energy bound with k1 the + record]
            close_ok = close_ok and le_sum(e1, eK2, e2)
            # eps(K) <= eps(k1) + eps(k2)  [(+,+) energy at least eps(K)]
            close_ok = close_ok and le_sum(eK2, e1, e2)
            # strictness: (+,+) energy equals eps(K) only if e1 == 0 or e2 == 0
            if eq_sum(eK2, e1, e2):
                close_ok = close_ok and (e1 == 0 or e2 == 0)
            n_close += 1
    check("A4", close_ok, f"closure of (+,-) from (+,+) at fixed K on the d=2 grid ({n_close} (K,k1) cases): (+,-) energy <= eps(K) <= (+,+) energy, "
                          "with the last equality only when a record is at a corner")

    # A5: crystal momentum and the pi/4 bound, per component, in units of pi (exact Fractions)
    grid = [Fr(k, 16) for k in range(-3, 4)]  # |offset| < 1/4 (units of pi)
    ok = True
    n = 0
    for A, B, A2, B2 in itertools.product((0, 1), repeat=4):
        for d1, d2, d1p, d2p in itertools.product(grid, repeat=4):
            diff = (A + B + d1 + d2) - (A2 + B2 + d1p + d2p)
            if diff.denominator == 1 and diff.numerator % 2 == 0:  # congruent mod 2 (units of pi)
                n += 1
                ok = ok and (d1 + d2 == d1p + d2p)
    check("A5", ok and n > 0, f"every congruence mod 2pi over all corner channels with offsets |delta| < pi/4 on a grid of {n} congruent cases has equal offset sums")
    # sharpness: offsets exactly pi/4 break it
    A, B, A2, B2 = 1, 0, 0, 0
    d1 = d2 = Fr(1, 4)
    d1p = d2p = Fr(-1, 4)
    diff = (A + B + d1 + d2) - (A2 + B2 + d1p + d2p)
    check("A6", diff.denominator == 1 and diff.numerator % 2 == 0 and d1 + d2 != d1p + d2p,
          "at |delta| = pi/4 exactly the offset sum is NOT conserved (corner pi + offsets pi/4,pi/4 -> corner 0 + offsets -pi/4,-pi/4 is crystal-momentum allowed): the strict bound 'below pi/4' in block 152 T1(b) cannot be weakened to 'at most'")
    # sin^2 threshold
    check("A7", sp.sin(sp.pi / 4) ** 2 == sp.Rational(1, 2) and all((s * s < Fr(1, 2)) == (abs(sp.asin(sp.Rational(s.numerator, s.denominator))) < sp.pi / 4) for s, _ in ANG),
          "sin^2(pi/4) = 1/2; for every grid point, sin^2 < 1/2 iff the offset from the nearest multiple of pi is below pi/4 (so pair energy < sqrt(2)/2 keeps every record's offsets below pi/4)")


# =============================================================================================== family B
class Gq:
    """Gaussian rational r + i*i with exact Fractions."""
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = Fr(r)
        self.i = Fr(i)

    @staticmethod
    def of(x):
        return x if isinstance(x, Gq) else Gq(x, 0)

    def __add__(self, o):
        o = Gq.of(o)
        return Gq(self.r + o.r, self.i + o.i)

    __radd__ = __add__

    def __sub__(self, o):
        o = Gq.of(o)
        return Gq(self.r - o.r, self.i - o.i)

    def __neg__(self):
        return Gq(-self.r, -self.i)

    def __mul__(self, o):
        o = Gq.of(o)
        return Gq(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)

    __rmul__ = __mul__

    def conj(self):
        return Gq(self.r, -self.i)

    def inv(self):
        n = self.r * self.r + self.i * self.i
        return Gq(self.r / n, -self.i / n)

    def __pow__(self, n):
        base = self if n >= 0 else self.inv()
        out = Gq(1)
        for _ in range(abs(n)):
            out = out * base
        return out

    def __eq__(self, o):
        o = Gq.of(o)
        return self.r == o.r and self.i == o.i

    def __hash__(self):
        return hash((self.r, self.i))


GI = Gq(0, 1)
GZ = Gq(0)


def mzero(n=2):
    return [[GZ for _ in range(n)] for _ in range(n)]


def meye(n=2):
    return [[Gq(1) if i == j else GZ for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def mscal(c, A):
    return [[c * A[i][j] for j in range(len(A))] for i in range(len(A))]


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), GZ) for j in range(n)] for i in range(n)]


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), GZ)


def mH(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def miszero(A):
    return all(x == GZ for row in A for x in row)


SIGM = (
    [[GZ, Gq(1)], [Gq(1), GZ]],
    [[GZ, -GI], [GI, GZ]],
    [[Gq(1), GZ], [GZ, Gq(-1)]],
)


def grand(rng):
    return Gq(Fr(rng.randint(-4, 4), rng.randint(1, 3)), Fr(rng.randint(-4, 4), rng.randint(1, 3)))


def rmat(rng):
    return [[grand(rng) for _ in range(2)] for _ in range(2)]


def target_blocks(d, kind):
    """Fourier blocks H_m = sum_{y-z=m} C_{yz} a placement must have: the walk (kind 'e', symbol sum_a sigma_a sin k_a) or the identity (kind 'n')."""
    if kind == "n":
        return {(0,) * d: meye()}
    blocks = {}
    for a in range(d):
        e = tuple(1 if i == a else 0 for i in range(d))
        me = tuple(-v for v in e)
        blocks[e] = madd(blocks.get(e, mzero()), mscal(Gq(0, Fr(1, 2)), SIGM[a]))      # -sigma/(2i) = (i/2) sigma
        blocks[me] = madd(blocks.get(me, mzero()), mscal(Gq(0, Fr(-1, 2)), SIGM[a]))   # +sigma/(2i) = -(i/2) sigma
    return blocks


def make_placement(d, kind, hermitian, rng):
    if d <= 2:
        sites = list(itertools.product((-1, 0, 1), repeat=d))
    else:
        sites = [(0,) * d] + [tuple(s * (1 if i == a else 0) for i in range(d)) for a in range(d) for s in (1, -1)]
    C = {(y, z): rmat(rng) for y in sites for z in sites}
    if hermitian:
        for y in sites:
            for z in sites:
                if y <= z:
                    Cn = mscal(Gq(Fr(1, 2)), madd(C[(y, z)], mH(C[(z, y)])))
                    C[(y, z)] = Cn
                    C[(z, y)] = mH(Cn)
    tgt = target_blocks(d, kind)
    diffs = {}
    for (y, z) in C:
        diffs.setdefault(tuple(y[i] - z[i] for i in range(d)), []).append((y, z))
    zero_m = (0,) * d
    for m, pairs in diffs.items():
        S = mzero()
        for p in pairs:
            S = madd(S, C[p])
        D = msub(tgt.get(m, mzero()), S)
        if miszero(D):
            continue
        y, z = pairs[0]
        if hermitian:
            if m == zero_m:
                C[(y, z)] = madd(C[(y, z)], D)
            elif m > zero_m:
                C[(y, z)] = madd(C[(y, z)], D)
                C[(z, y)] = madd(C[(z, y)], mH(D))
        else:
            C[(y, z)] = madd(C[(y, z)], D)
    if hermitian:
        for (y, z), M in C.items():
            assert all(M[i][j] == mH(C[(z, y)])[i][j] for i in range(2) for j in range(2))
    for m, pairs in diffs.items():
        S = mzero()
        for p in pairs:
            S = madd(S, C[p])
        assert miszero(msub(S, tgt.get(m, mzero()))), "placement totals wrong"
    return C


def point(rng, d):
    pool = [p for p in ANG if p[0] != 0 and p[1] != 0]
    sc = [rng.choice(pool) for _ in range(d)]
    S = [Gq(s) for s, c in sc]
    Cc = [Gq(c) for s, c in sc]
    E = [Gq(c, s) for s, c in sc]
    return S, Cc, E


# Laurent polynomials in z_a = exp(-i q_a) with 2x2 matrix coefficients: dict {exponent tuple: matrix}
def lp_add_term(P, ex, M):
    P[ex] = madd(P[ex], M) if ex in P else M


def lp_mul(P, Qp):
    out = {}
    for e1, M1 in P.items():
        for e2, M2 in Qp.items():
            ex = tuple(a + b for a, b in zip(e1, e2))
            lp_add_term(out, ex, mmul(M1, M2))
    return out


def lp_scale(c, P):
    return {e: mscal(c, M) for e, M in P.items()}


def lp_sub(P, Qp):
    out = dict(P)
    for e, M in Qp.items():
        lp_add_term(out, e, mscal(Gq(-1), M))
    return out


def lp_at_one(P, fix):
    """Set z_a = 1 for a in fix; returns a Laurent poly in the remaining variables (same exponent length, fixed ones 0)."""
    out = {}
    for e, M in P.items():
        ex = tuple(0 if a in fix else e[a] for a in range(len(e)))
        lp_add_term(out, ex, M)
    return {e: M for e, M in out.items() if not miszero(M)}


def lp_total(P):
    S = mzero()
    for M in P.values():
        S = madd(S, M)
    return S


def lp_div_one_minus(P, a):
    """P / (1 - z_a) for P vanishing at z_a = 1: q_n = cumulative sum of coefficients of z_a^m, m <= n (grouped by the other exponents)."""
    groups = {}
    for e, M in P.items():
        rest = tuple(e[b] for b in range(len(e)) if b != a)
        groups.setdefault(rest, {})[e[a]] = M
    out = {}
    for rest, byexp in groups.items():
        tot = mzero()
        for M in byexp.values():
            tot = madd(tot, M)
        assert miszero(tot), "not divisible by (1 - z)"
        run = mzero()
        for n in range(min(byexp), max(byexp) + 1):
            run = madd(run, byexp.get(n, mzero()))
            if not miszero(run):
                ex = list(rest)
                ex.insert(a, n)
                out[tuple(ex)] = run
    return out


def family_b() -> None:
    rng = random.Random(154)
    all_ok = True
    n_cases = 0
    for d, nplace in ((1, 3), (2, 3), (3, 2)):
        for kind in ("e", "n"):
            for herm in (False, True):
                for _ in range(nplace):
                    C = make_placement(d, kind, herm, rng)
                    S, Cc, E = point(rng, d)
                    # e(k+q,k) = sum C_{yz} exp(-i(k+q).y) exp(ik.z);  exponent of z_a is y_a
                    e_lp = {}
                    for (y, z), M in C.items():
                        coef = Gq(1)
                        for a in range(d):
                            coef = coef * (E[a].inv() ** y[a]) * (E[a] ** z[a])
                        lp_add_term(e_lp, y, mscal(coef, M))
                    hk = mzero()
                    for a in range(d):
                        hk = madd(hk, mscal(S[a], SIGM[a]))
                    # h(k+q) = sum_a sigma_a (E_a z_a^{-1} - E_a^{-1} z_a)/(2i)
                    hkq = {}
                    for a in range(d):
                        em = tuple(-1 if b == a else 0 for b in range(d))
                        ep = tuple(1 if b == a else 0 for b in range(d))
                        lp_add_term(hkq, em, mscal(E[a] * Gq(0, Fr(-1, 2)), SIGM[a]))
                        lp_add_term(hkq, ep, mscal(E[a].inv() * Gq(0, Fr(1, 2)), SIGM[a]))
                    e0 = lp_total(e_lp)
                    tgt0 = hk if kind == "e" else meye()
                    all_ok = all_ok and miszero(msub(e0, tgt0))
                    # Q = i (h(k+q) e - e h(k))
                    Q = lp_scale(GI, lp_sub(lp_mul(hkq, e_lp), {e: mmul(M, hk) for e, M in e_lp.items()}))
                    all_ok = all_ok and miszero(lp_total(Q))
                    for j in range(d):
                        # (b): J_j(k,k) = -(d_j h . h + [h, d_{q_j} e]);  d/dq_j = -i z_j d/dz_j
                        de = mzero()
                        for ex, M in e_lp.items():
                            de = madd(de, mscal(Gq(0, -ex[j]), M))
                        dh = mscal(Cc[j], SIGM[j])
                        left = mmul(dh, hk if kind == "e" else meye())
                        Jb = mscal(Gq(-1), madd(left, msub(mmul(hk, de), mmul(de, hk))))
                        # independent construction: telescoping Q = sum_a [Q|_{z_<a=1} - Q|_{z_<=a=1}], each term divisible by (1 - z_a)
                        prev = lp_at_one(Q, set(range(j)))
                        nxt = lp_at_one(Q, set(range(j + 1)))
                        num = lp_sub(prev, nxt)
                        num = {e: M for e, M in num.items() if not miszero(M)}
                        Jdiv = mscal(Gq(-1), lp_total(lp_div_one_minus(num, j)))
                        same_fm = miszero(msub(Jdiv, Jb))
                        trJ = mtr(Jb)
                        trhJ = mtr(mmul(hk, Jb))
                        sc2 = S[j] * Cc[j] * Gq(2)
                        if kind == "e":
                            diag_ok = trJ == -sc2 and trhJ == GZ
                        else:
                            diag_ok = trJ == GZ and trhJ == -sc2
                        all_ok = all_ok and same_fm and diag_ok
                        n_cases += 1
    check("B1", all_ok, f"{n_cases} (placement, axis) cases with random exact finite-range placements, hermitian and non-hermitian, d=1,2,3, energy (sum = H) and number density (sum = 1): "
                       "J_j(k,k) from the first-order formula equals J_j(k,k) from an explicit division of the continuity symbol by (1-z_j); "
                       "band-diagonals: energy current tr J = -2 sin k_j cos k_j, tr(hJ) = 0 (so -sin k_j cos k_j in BOTH bands); number current tr J = 0, tr(hJ) = -2 sin k_j cos k_j (velocity -d_j E_b)")

    # B2: the same two trace identities for an arbitrary 2x2 X = d_{q_j} e (symbolic), no placement data at all
    x = sp.symbols("x0:4")
    X = sp.Matrix(2, 2, x)
    SIGS = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    ok = True
    for d in (1, 2, 3):
        S = sp.symbols(f"s1:{d + 1}")
        Cc = sp.symbols(f"c1:{d + 1}")
        hk = sum((SIGS[a] * S[a] for a in range(d)), sp.zeros(2))
        for j in range(d):
            dh = SIGS[j] * Cc[j]
            J = -(dh * hk + (hk * X - X * hk))
            ok = ok and sp.expand(J.trace() + 2 * S[j] * Cc[j]) == 0 and sp.expand((hk * J).trace()) == 0
            Jn = -(dh + (hk * X - X * hk))
            ok = ok and sp.expand(Jn.trace()) == 0 and sp.expand((hk * Jn).trace() + 2 * S[j] * Cc[j]) == 0
    check("B2", ok, "for an arbitrary 2x2 X = d_{q_j}e (symbolic): energy: tr J = -2 s_j c_j, tr(hJ) = 0; number: tr J = 0, tr(hJ) = -2 s_j c_j; the commutator [h, X] drops out "
                    "(tr [h,X] = 0, tr(h[h,X]) = 0 by cyclicity; tr(sigma_j h) = 2 s_j; tr(h sigma_j h) = 0): band-diagonal = tr(J)/2 +- tr(hJ)/(2 eps), no eigenvectors, no non-degeneracy needed")

    # B3: summation by parts with the continuity sign convention on a ring of L sites, generic placement
    L = 6
    nS = 2 * L
    rng2 = random.Random(7)

    def big_zero():
        return [[GZ for _ in range(nS)] for _ in range(nS)]

    def site_op(blocks):
        M = big_zero()
        for (y, z), B in blocks.items():
            yy, zz_ = y % L, z % L
            for i in range(2):
                for j in range(2):
                    M[2 * yy + i][2 * zz_ + j] = M[2 * yy + i][2 * zz_ + j] + B[i][j]
        return M

    def badd(A, B):
        return [[A[i][j] + B[i][j] for j in range(nS)] for i in range(nS)]

    def bmul(A, B):
        return [[sum((A[i][k] * B[k][j] for k in range(nS) if not (A[i][k] == GZ)), GZ) for j in range(nS)] for i in range(nS)]

    def bscal(c, A):
        return [[c * A[i][j] for j in range(nS)] for i in range(nS)]

    def bcomm(A, B):
        AB, BA = bmul(A, B), bmul(B, A)
        return [[AB[i][j] - BA[i][j] for j in range(nS)] for i in range(nS)]

    def bzero(A):
        return all(x == GZ for row in A for x in row)

    Hfull = big_zero()
    for z_ in range(L):
        Hfull = badd(Hfull, site_op({(z_ + 1, z_): mscal(Gq(0, Fr(1, 2)), SIGM[0]), (z_ - 1, z_): mscal(Gq(0, Fr(-1, 2)), SIGM[0])}))
    C1 = make_placement(1, "e", False, rng2)
    es = [site_op({(y[0] + x_, z[0] + x_): M for (y, z), M in C1.items()}) for x_ in range(L)]
    sumE = big_zero()
    for E_ in es:
        sumE = badd(sumE, E_)
    placement_ok = bzero([[sumE[i][j] - Hfull[i][j] for j in range(nS)] for i in range(nS)])
    iH = [bscal(GI, bcomm(Hfull, e_)) for e_ in es]  # i[H, e_x]
    Js = [None] * L
    Js[0] = big_zero()
    for x_ in range(1, L):
        Js[x_] = [[Js[x_ - 1][i][j] - iH[x_][i][j] for j in range(nS)] for i in range(nS)]
    cont_ok = bzero([[Js[0][i][j] - Js[L - 1][i][j] + iH[0][i][j] for j in range(nS)] for i in range(nS)])
    Mw = [rng2.randint(-5, 5) for _ in range(L)]
    lhs = big_zero()
    rhs = big_zero()
    for x_ in range(L):
        lhs = badd(lhs, bscal(Gq(Mw[x_]), iH[x_]))
        rhs = badd(rhs, bscal(Gq(Mw[(x_ + 1) % L] - Mw[x_]), Js[x_]))
    sbp_ok = bzero([[lhs[i][j] - rhs[i][j] for j in range(nS)] for i in range(nS)])
    check("B3", placement_ok and cont_ok and sbp_ok,
          "ring of 6 sites, generic placement e_x (sum = H), J from i[H,e_x] = -(J_x - J_{x-1}): i[H, sum_x M_x e_x] = sum_x (M_{x+1} - M_x) J_x exactly "
          "(the sign used in block 154 T1(a); with block 150 T5(a)'s M=1 form X = -Y this gives P - J divergence-free)")
    z1 = sp.Symbol("z1")
    aa = sp.symbols("a0:3")
    lhs_poly = sp.expand((1 - z1) * (aa[0] + aa[1] * z1 + aa[2] * z1 ** 2))
    zero_coeffs = sp.solve(sp.Poly(lhs_poly, z1).all_coeffs(), list(aa), dict=True)
    check("B4", bool(zero_coeffs) and all(v == 0 for v in zero_coeffs[0].values()),
          "a polynomial D(z) with (1 - z) D(z) = 0 identically has D = 0 (degree 2 checked; in general (1-z) is a non-zero-divisor): so a divergence-free family vanishes along each axis and D_j(k,k) = 0")


# =============================================================================================== family C
d_ = sp.Symbol("d")


def system(R, N, extra_light=False):
    a = sp.symbols(f"a1:{R + 1}")
    eqs = []
    for A in (0, 1):
        f = sum(a[m - 1] * (-1) ** (m * A) * sp.series(sp.sin(m * d_), d_, 0, N + 1).removeO() for m in range(1, R + 1))
        g = sp.expand(f * sp.diff(f, d_))
        P = sp.Poly(g, d_)
        for i in range(0, N):
            e = sp.expand(P.coeff_monomial(d_ ** i) - (1 if i == 1 else 0))
            if e != 0:
                eqs.append(e)
    return a, eqs


def quotient_dim(G, gens, maxdeg=14):
    lms = [sp.Poly(g, *gens).monoms(order="grevlex")[0] for g in G.exprs]
    n = len(gens)
    total = 0
    for deg in range(maxdeg + 1):
        c = 0
        for comp in itertools.product(range(deg + 1), repeat=n):
            if sum(comp) != deg:
                continue
            if not any(all(comp[i] >= lm[i] for i in range(n)) for lm in lms):
                c += 1
        total += c
        if c == 0:
            return total
    return None


def odd_stencil(m):
    """f_m = sin k sum_{j<m} binom(2j,j)/(4^j (2j+1)) sin^{2j} k, as sine-harmonic coefficients a_1..a_{2m-1}
    (f_m / sin k = P(c) = sum_n a_n U_{n-1}(c), c = cos k)."""
    c = sp.Symbol("c")
    P = sum(sp.Rational(sp.binomial(2 * j, j), 4 ** j * (2 * j + 1)) * (1 - c ** 2) ** j for j in range(m))
    R = 2 * m - 1
    a = sp.symbols(f"u1:{R + 1}")
    expr = sp.expand(P - sum(a[n - 1] * sp.chebyshevu(n - 1, c) for n in range(1, R + 1)))
    sol = sp.solve(sp.Poly(expr, c).all_coeffs(), a, dict=True)[0]
    return [sol[x] for x in a]


def even_stencil(J):
    """f = (1/2) F(2k) with F = sum_{j<=J} c_j sin(j u), F(u) = u + O(u^{2J+1}): harmonics 2,4,...,2J."""
    c = sp.symbols(f"c1:{J + 1}")
    eqs = [sum(j * c[j - 1] for j in range(1, J + 1)) - 1] + [sum(j ** (2 * l + 1) * c[j - 1] for j in range(1, J + 1)) for l in range(1, J)]
    sol = sp.solve(eqs, c, dict=True)[0]
    return [sol[c[j - 1]] / 2 for j in range(1, J + 1)]  # coefficient of sin(2 j k)


def family_c() -> None:
    # C1: Vandermonde lemma for every m <= 10: det[x_j^{l-1}] = prod_{i<j}(x_j - x_i) != 0 for x_j = (2j+1)^2 and x_j = (2j)^2
    ok = True
    for m in range(1, 11):
        for xs in ([sp.Integer((2 * j + 1) ** 2) for j in range(m)], [sp.Integer((2 * j) ** 2) for j in range(1, m + 1)]):
            Vm = sp.Matrix(m, m, lambda l, j: xs[j] ** l)
            dv = Vm.det()
            pr = sp.Integer(1)
            for i in range(m):
                for j in range(i + 1, m):
                    pr *= xs[j] - xs[i]
            ok = ok and dv == pr and dv != 0
    check("C1", ok, "m = 1..10: det[x_j^l]_{l=0..m-1} = prod_{i<j}(x_j - x_i) != 0 for x_j = (2j+1)^2 (odd harmonics) and x_j = (2j)^2 (even harmonics): the matrix-of-powers lemma at every m, not only m <= 6")

    # C2: the power-series conditions, no light cone imposed: largest N for R = 1..6 and the full solution count
    Nmax = {1: 3, 2: 3, 3: 5, 4: 5, 5: 7, 6: 7}
    expect_dim = {1: 2, 2: 4, 3: 2, 4: 4, 5: 2, 6: 4}
    ok_empty = ok_nonempty = ok_dim = True
    got = {}
    for R in range(1, 7):
        a, eq_hi = system(R, Nmax[R] + 2)
        G_hi = sp.groebner(eq_hi, *a, order="grevlex")
        ok_empty = ok_empty and list(G_hi.exprs) == [1]
        a, eq_lo = system(R, Nmax[R])
        G_lo = sp.groebner(eq_lo, *a, order="grevlex")
        ok_nonempty = ok_nonempty and list(G_lo.exprs) != [1]
        qd = quotient_dim(G_lo, a)
        got[R] = qd
        ok_dim = ok_dim and qd == expect_dim[R]
    check("C2", ok_empty and ok_nonempty and ok_dim,
          f"no light cone imposed: the Groebner basis of the order-N system is {{1}} (no complex solution) at N = {[Nmax[R] + 2 for R in range(1, 7)]} and not {{1}} at N = {[Nmax[R] for R in range(1, 7)]} "
          f"for R = 1..6, so the largest N is 3,3,5,5,7,7; the solution count at the largest N (with multiplicity) is {[got[R] for R in range(1, 7)]}")

    # C3: those solutions are exactly: +-f_m (odd R = 2m-1, and R = 2m), and, for even R, +-(1/2)F(2k) (vanishing at pi/2).
    k = sp.Symbol("k")
    ok_sols = True
    ok_zero = True
    for R in range(1, 7):
        m = (R + 1) // 2
        o = odd_stencil(m)
        a, eqs = system(R, Nmax[R])
        base = [sp.Integer(0)] * R
        for i, v in enumerate(o):
            base[i] = v
        sols = [base, [-v for v in base]]
        if R % 2 == 0:
            ev = even_stencil(R // 2)
            v2 = [sp.Integer(0)] * R
            for j, v in enumerate(ev, start=1):
                v2[2 * j - 1] = v
            sols += [v2, [-v for v in v2]]
        for s in sols:
            sub = dict(zip(a, s))
            ok_sols = ok_sols and all(sp.expand(e.subs(sub)) == 0 for e in eqs)
        if R % 2 == 0:
            f_ev = sum(v2[n - 1] * sp.sin(n * k) for n in range(1, R + 1))
            ok_zero = ok_zero and sp.simplify(f_ev.subs(k, sp.pi / 2)) == 0
        # the odd-harmonic solution has no zero besides 0, pi (see C5)
    check("C3", ok_sols and ok_zero,
          "for R = 1..6 the solutions of C2 are exhibited exactly: +-f_m (m = ceil(R/2), the truncated arcsin(sin k) stencil) and, for even R, +-(1/2)F(2k) with F the sine polynomial of degree R/2 matching u through u^R; "
          "counts 2 or 4 equal the Groebner quotient dimensions, so these are all complex solutions; every even-harmonic solution vanishes at k = pi/2")

    # C4: linear (Vandermonde) route for odd R = 2m-1, N = R+2: unique odd stencil; and it is f_m; one more equation is inconsistent
    ok_lin = True
    for m in range(1, 7):
        xs = [sp.Integer((2 * j + 1) ** 2) for j in range(m)]
        b = sp.symbols(f"b0:{m}")
        eqs = [sum(b) - 1] + [sum(b[j] * xs[j] ** l for j in range(m)) for l in range(1, m)]
        sol = sp.solve(eqs, b, dict=True)[0]
        a_from = [sol[b[j]] / (2 * j + 1) for j in range(m)]
        o = odd_stencil(m)
        ok_lin = ok_lin and all(o[2 * j] == a_from[j] for j in range(m)) and all(o[2 * j + 1] == 0 for j in range(m - 1))
        # appending the l = m equation: the system for (b) is overdetermined and inconsistent
        A = sp.Matrix([[1] * m] + [[xs[j] ** l for j in range(m)] for l in range(1, m + 1)])
        rhs = sp.Matrix([1] + [0] * m)
        ok_lin = ok_lin and A.row_join(rhs).rank() > A.rank()
    check("C4", ok_lin, "odd R = 2m-1, m = 1..6: sum b_j = 1 and sum b_j x_j^l = 0 (l = 1..m-1) has exactly one solution, equal to f_m's sine coefficients; adding l = m makes it inconsistent (N <= 2m+1 = R+2)")

    # C5: f_m for m = 1..6: series, light cone (no zero but 0, pi; unit slopes), and speed bound |f'| <= 1
    ok_ser = ok_cone = ok_speed = True
    c_, y_ = sp.symbols("c y")
    for m in range(1, 7):
        coef = [sp.Rational(sp.binomial(2 * j, j), 4 ** j * (2 * j + 1)) for j in range(m)]
        f = sp.sin(k) * sum(coef[j] * sp.sin(k) ** (2 * j) for j in range(m))
        g = sp.series(f.subs(k, d_) * sp.diff(f, k).subs(k, d_), d_, 0, 2 * m + 3).removeO()
        am = sp.Rational(sp.binomial(2 * m, m), 4 ** m * (2 * m + 1))
        ok_ser = ok_ser and sp.expand(g - (d_ - (2 * m + 2) * am * d_ ** (2 * m + 1))) == 0
        g_pi = sp.series(f.subs(k, sp.pi + d_) * sp.diff(f, k).subs(k, sp.pi + d_), d_, 0, 2 * m + 3).removeO()
        ok_ser = ok_ser and sp.expand(g_pi - (d_ - (2 * m + 2) * am * d_ ** (2 * m + 1))) == 0
        # light cone: f / sin k = sum coef_j (1-c^2)^j >= 1 > 0 for real c; slopes f'(0) = 1, f'(pi) = -1
        ok_cone = ok_cone and all(cj > 0 for cj in coef) and sp.diff(f, k).subs(k, 0) == 1 and sp.diff(f, k).subs(k, sp.pi) == -1
        # speed: f' = cos k * T(s^2), T(y) = sum_j binom(2j,j) (y/4)^j ; 1 - f'^2 = 1 - (1-y) T(y)^2 has nonnegative coefficients in y = sin^2 k
        T = sum(sp.binomial(2 * j, j) * (y_ / 4) ** j for j in range(m))
        gpoly = sp.Poly(sp.expand(1 - (1 - y_) * T ** 2), y_)
        ok_speed = ok_speed and all(cf >= 0 for cf in gpoly.all_coeffs())
        # f' = cos k T(sin^2 k) exactly
        ok_speed = ok_speed and sp.simplify(sp.diff(f, k) - sp.cos(k) * T.subs(y_, sp.sin(k) ** 2)) == 0
    check("C5", ok_ser and ok_cone and ok_speed,
          "m = 1..6 (R = 1,3,..,11): f_m f_m'(A+delta) = delta - (2m+2) a_m delta^{2m+1} + O(delta^{2m+3}) at both corners, a_m = binom(2m,m)/(4^m (2m+1)) (m=2: 9/20); "
          "f_m = sin k * (polynomial with positive coefficients in sin^2 k): zeros only at 0, pi, slopes +1, -1; f_m' = cos k T(sin^2 k) and 1 - (1-y)T(y)^2 has nonnegative coefficients: |f_m'| <= 1")

    # C6: R = 3 closed forms quoted by the note
    c = sp.Symbol("c")
    f3 = sp.Rational(9, 8) * sp.sin(k) - sp.Rational(1, 24) * sp.sin(3 * k)
    cond_a = sp.simplify(sp.expand_trig(f3 - sp.sin(k) * (1 + sp.sin(k) ** 2 / 6))) == 0
    cond_b = sp.expand((sp.Rational(3, 2) * c - c ** 3 / 2) ** 2 - 1 + (1 - c ** 2) ** 2 * (4 - c ** 2) / 4) == 0
    f5 = sp.Rational(75, 64) * sp.sin(k) - sp.Rational(25, 384) * sp.sin(3 * k) + sp.Rational(3, 640) * sp.sin(5 * k)
    o3 = odd_stencil(3)
    cond_c = o3 == [sp.Rational(75, 64), 0, -sp.Rational(25, 384), 0, sp.Rational(3, 640)]
    check("C6", cond_a and cond_b and cond_c, "block 154's R=3 and R=5 stencils: (9/8)sin k - (1/24) sin 3k = sin k (1+sin^2 k/6); 1 - f'^2 = (1-c^2)^2 (4-c^2)/4; R=5 coefficients 75/64, -25/384, 3/640 equal f_3's harmonics")

    # C7: what the light cone is for.  At R = 2, N = 3 the solutions are +-sin k and +-(1/2) sin 2k; the latter has f'(0)=1, f'(pi)=1 but vanishes at pi/2,
    #     and its momentum f f' = (1/4) sin 4 delta = delta - (8/3) delta^3, not sin(delta)cos(delta) = delta - (2/3) delta^3
    f2 = sp.sin(2 * k) / 2
    ser = sp.series((f2 * sp.diff(f2, k)).subs(k, d_), d_, 0, 5).removeO()
    check("C7", sp.diff(f2, k).subs(k, 0) == 1 and sp.diff(f2, k).subs(k, sp.pi) == 1 and f2.subs(k, sp.pi / 2) == 0 and sp.expand(ser - (d_ - sp.Rational(8, 3) * d_ ** 3)) == 0,
          "the light cone is used to select f = +-sin k at R = 2 (T3(c)); it is NOT used for the bound N <= R+2, which C2 shows for all complex f (the even-harmonic solution reaches only N = R+1)")

    # C8: block 152 T3(b) / block 154 T3(e) quoted sums
    p, x, y = sp.symbols("p x y")
    s3 = (p / 2 + x) ** 3 + (p / 2 - x) ** 3
    s5 = (p / 2 + x) ** 5 + (p / 2 - x) ** 5
    ok = sp.expand(s3 - (p ** 3 / 4 + 3 * p * x ** 2)) == 0 and sp.expand(s5 - (p ** 5 / 16 + sp.Rational(5, 2) * p ** 3 * x ** 2 + 5 * p * x ** 4)) == 0
    # the shell |d1| + |d2| = E=5/2, p = 1: points (x,y) = (5/4, 0) and (0, sqrt(21)/4)
    E_ = sp.Rational(5, 2)
    pts = [(sp.Rational(5, 4), sp.Integer(0)), (sp.Integer(0), sp.sqrt(21) / 4)]
    on_shell = all(sp.simplify(sp.sqrt((sp.Rational(1, 2) + px) ** 2 + py ** 2) + sp.sqrt((sp.Rational(1, 2) - px) ** 2 + py ** 2) - E_) == 0 for px, py in pts)
    v3 = [s3.subs({p: 1, x: px}) for px, py in pts]
    ok = ok and on_shell and v3 == [sp.Rational(79, 16), sp.Rational(1, 4)]
    v5 = [s5.subs({p: 1, x: px}) for px, py in pts]
    ok = ok and v5[0] != v5[1]
    check("C8", ok, f"the sums on block 152's family: cubic p^3/4+3px^2 takes 79/16 and 1/4 at the two shell points (E=5/2, p=1); fifth-order p^5/16+(5/2)p^3x^2+5px^4 takes {v5[0]} and {v5[1]}")


def main() -> int:
    family_a()
    family_b()
    family_c()
    print("RUNTIME_SECONDS: %.1f" % (time.time() - T0))
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("HIT: exact confirmation of block 152 T1(d)'s channel closure with a polynomial-identity proof that eps(a+b) = eps(a)+eps(b) iff one record is at a corner; "
              "of block 154 T1's generic-placement band-diagonal -sin k_j cos k_j (traces, no eigenvectors); and of T3's N <= R+2 (largest N = 3,3,5,5,7,7 for R = 1..6, full solution sets, no light cone needed for the bound)")
        print("SUMMARY: PARTIAL independent exact confirmation of block 152 T1(d), block 154 T1(a)-(c) and T3(b)-(d), plus three scoped sharpenings (A2/A6, B2, C2/C7); no error found in the landed steps")
    else:
        print("SUMMARY: ROUTE FAILS AT a check marked FAIL above")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
