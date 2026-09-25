#!/usr/bin/env python3
"""check.py for J:derive:the-exchange-sign-at-fourth-order-in-the-crowd:a1 (worker w-macbookpro9927a-je6b5, claude-opus-5-5).

Every finite claim of ATTEMPT.md is checked with exact arithmetic: Fraction polynomials, sympy, Gaussian integers
(2H has Gaussian-integer entries, so complex128 carries every product here exactly and gi() asserts it), and
mpmath interval arithmetic for the square-root comparisons.

Families
  Q  quoted definitions pinned by commit and SHA-256 (blocks 54, 78, 80, 85 as landed; attempt #8642; the task text)
  A  one-record moments: H(k)^2 = sum sin^2 k_a, m2 = 3/2, m4 = 21/8, kappa4 = -33/8; no closed 3-hop process
  C  linked-cluster cumulants per site on Z^3, both composition signs; the sign part; jam; degree; plaquette origin
  V  brute-force torus traces against the series: 2D side 5 (N = 1..4), 3D side 5 (N = 1, 2 sparse; N = 3 by orbits)
  L  fixed filling: the Legendre correction, its O(1/V) check, and the free-energy and energy differences
  B  alternation of bond rates (all axes, one axis) and a clock modulation: exact coefficients and sign parts
  G  ground energy: hard-core-boson trial identity, the 8^3 certificates, the thermodynamic-limit threshold
"""
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as F
from math import comb

import numpy as np
import scipy.sparse as sps
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


def gi(z):
    r, i = round(z.real), round(z.imag)
    assert abs(z.real - r) < 1e-9 and abs(z.imag - i) < 1e-9
    return r, i


# ------------------------------------------------------------------ Q: pinned sources
SRC = [
    ("block54", "c3f8c47a58bfba48c1d9e030d6d79ecda00a294e",
     "docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES"
     "_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     "f6036ab9a00783efa4bd4a1c031a3ad777e65d94c3d858d405bc813493fb9431",
     ["Define (T_e psi)(x)=psi(x-e), D_j=(i/2)(T_j-T_j^dagger), and H=sum_e A_e T_e, including e=0."]),
    ("block78", "7445cc7a50e2c7631d70dc8d9a065d0653ffa6ef",
     "docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE"
     "_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md",
     "1304da384ff3e6a18605271e5259195cb3e7dcd65d4c8bac4d330aa48f6062ca",
     ["compressed by the fixed position projector P removing configurations with equal sites. This compression, "
      "tensor-product space and exchange rule are supplied model choices."]),
    ("block80", "7445cc7a50e2c7631d70dc8d9a065d0653ffa6ef",
     "docs/ADMISSIBILITY_RULE_MANY_RECORDS_UNDER_EXCLUSION_SOURCE_IS_THE_PROJECTED_DENSITY_CHESSBOARD_INVISIBLE_INTERACTING"
     "_SEA_STIFFENS_CLOCKS_OPPOSITELY_BOUNDED_THEOREM_NOTE_2026-09-22.md",
     "3167d7fd450738453e33795768b1e4359f086d169aa5b92cd61c89b13430f16e",
     ["no interacting-sea stiffness claim is retained", "Let H_w=phi sigma3 S phi on a finite ring, phi_x>0, u_x=2 log phi_x"]),
    ("block85", "fbe9f0f0154402d8afa07a8d12c920df2d9d0848",
     "docs/ADMISSIBILITY_RULE_THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS_FROM_AN_ALTERNATION_OF_THE_BOND_RATES_ITS_GROUND_ENERGY"
     "_NEVER_RISES_THE_JAM_IS_BLIND_BOUNDED_THEOREM_NOTE_2026-09-22.md",
     "7b52b254cc5f01968d825258488a52a58a03e87a6f9fb68656f41a706832d9cf",
     ["The supplied one-particle pure hop has bond amplitudes 1+delta(-1)^x_j.",
      "No derivative or quadratic susceptibility follows from concavity, and a cusp is allowed."]),
    ("attempt8642", "043d41713d742505694a54421afff2ba37a5dda1",
     "probes/work/derive/the-exchange-sign-from-the-coin/w-macbookpro90c72-j3430/ATTEMPT.md",
     "c79428097274d29eb9fef76f29fb1970881b720c362e29259892806d69fa162f",
     ["= tr(P H₂⁴) = −8` per plaquette"]),
]
TASKQ = ("92a2f08fad1997e2571982fd06dfaeb7e3dacf58", "J:derive:the-exchange-sign-at-fourth-order-in-the-crowd:a1",
         ["(a) The fourth-order cluster expansion of the crowd's ground energy per site at fixed filling on Z^3, both signs, "
          "exact coefficients; which sign lowers it.",
          "(b) The same for the clock stiffness (block 80) and the bond-rate alternation's coefficient (block 85): does the "
          "sign change either at fourth order?", "HIT: (a) exact."])


def git_show(spec):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes in SRC:
        b = git_show(f"{c}:{p}")
        if b is None:
            rep("Q", False, f"{tag} unreadable at {c[:8]}")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json")
    what = next((t.get("what", "") for t in json.loads(b.decode()) if t.get("id") == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg) + ". Landed narrowings: block 80 keeps no interacting-sea stiffness, block 85 no quadratic "
                                   "susceptibility; (b) is answered for new fourth-order cluster coefficients, not those withdrawn claims")


# ------------------------------------------------------------------ cluster machinery (dimension d)
SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]


def unit(d, a):
    return tuple(1 if i == a else 0 for i in range(d))


def vadd(x, e, s=1):
    return tuple(x[i] + s * e[i] for i in range(len(x)))


def bsites(b, d):
    return (b[0], vadd(b[0], unit(d, b[1])))


def connected_sets(anchor, d, maxsize=4):
    out = {frozenset([anchor])}
    frontier = [frozenset([anchor])]
    for _ in range(2, maxsize + 1):
        new = []
        for S in frontier:
            sites = {s for b in S for s in bsites(b, d)}
            cand = {(s, a) for s in sites for a in range(d)} | {(vadd(s, unit(d, a), -1), a) for s in sites for a in range(d)}
            for b in cand:
                if b not in S and (S | {b}) not in out:
                    out.add(S | {b})
                    new.append(S | {b})
        frontier = new
    return out


class Local:
    """Local Fock space on the sites of a bond set: 0 empty, 1 up, 2 down; eps = -1 uses Jordan-Wigner signs."""

    def __init__(self, sites, d):
        self.sites, self.d, self.n = list(sites), d, len(sites)
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.states = list(itertools.product(range(3), repeat=self.n))
        self.sidx = {st: i for i, st in enumerate(self.states)}
        self.occ = [sum(1 for v in st if v) for st in self.states]

    def hop2(self, b, eps):  # 2h_b: <x|2H|x+e> = -i sigma, <x+e|2H|x> = +i sigma  (block 54's D_j with coin sigma_j)
        x, y = bsites(b, self.d)
        ix, iy = self.idx[x], self.idx[y]
        rows, cols, vals = [], [], []
        for st in self.states:
            for (src, dst, coef) in ((iy, ix, -1j), (ix, iy, 1j)):
                if st[src] and not st[dst]:
                    for alpha in range(2):
                        amp = coef * SIG[b[1]][alpha, st[src] - 1]
                        if amp == 0:
                            continue
                        new = list(st)
                        new[src], new[dst] = 0, alpha + 1
                        lo, hi = min(src, dst), max(src, dst)
                        sign = -1 if (eps == -1 and sum(1 for k in range(lo + 1, hi) if st[k]) % 2) else 1
                        rows.append(self.sidx[tuple(new)])
                        cols.append(self.sidx[st])
                        vals.append(sign * amp)
        N = len(self.states)
        return sps.csr_matrix((vals, (rows, cols)), shape=(N, N))

    def expect(self, M, scale):  # product-state expectation as a monomial polynomial in rho (Fraction list)
        acc = {}
        for i, v in enumerate(M.diagonal()):
            if v == 0:
                continue
            re, im = gi(v)
            assert im == 0
            acc[self.occ[i]] = acc.get(self.occ[i], 0) + F(re, 2 ** self.occ[i])
        r = [F(0)] * (self.n + 1)
        for k, c in acc.items():
            for j in range(self.n - k + 1):
                r[k + j] += c / scale * comb(self.n - k, j) * (-1) ** j
        return ptrim(r)


def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def padd(p, q, s=1):
    r = [F(0)] * max(len(p), len(q))
    for i, a in enumerate(p):
        r[i] += a
    for i, b in enumerate(q):
        r[i] += s * b
    return r


SEQ_CACHE = {}


def sequences(d, eps):
    """List of (kind, set, seq, poly): kind 'm2' for <h h> of an anchored bond, 'K' for the connected fourth cumulant term
    K = <h1h2h3h4> - <h1h2><h3h4> - <h1h3><h2h4> - <h1h4><h2h3> of every sequence starting at an anchored bond."""
    if (d, eps) in SEQ_CACHE:
        return SEQ_CACHE[(d, eps)]
    out = []
    for a0 in range(d):
        anchor = (tuple([0] * d), a0)
        for S in connected_sets(anchor, d, 4):
            loc = Local(sorted({s for b in S for s in bsites(b, d)}), d)
            H2 = {b: loc.hop2(b, eps) for b in S}
            pc = {}

            def pair(b, bb):
                if (b, bb) not in pc:
                    pc[(b, bb)] = loc.expect(H2[b] @ H2[bb], 4)
                return pc[(b, bb)]
            if len(S) == 1:
                out.append(("m2", S, (anchor, anchor), pair(anchor, anchor)))
            for rest in itertools.product(sorted(S), repeat=3):
                seq = (anchor,) + rest
                if set(seq) != set(S):
                    continue
                K = loc.expect(H2[seq[0]] @ H2[seq[1]] @ H2[seq[2]] @ H2[seq[3]], 16)
                for (i, j, k, l) in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
                    K = padd(K, pmul(pair(seq[i], seq[j]), pair(seq[k], seq[l])), -1)
                K = ptrim(K)
                if any(K):
                    out.append(("K", S, seq, K))
    SEQ_CACHE[(d, eps)] = out
    return out


def cumulants(d, eps):
    c2, c4 = [F(0)], [F(0)]
    for kind, S, seq, poly in sequences(d, eps):
        if kind == "m2":
            c2 = padd(c2, poly)
        else:
            c4 = padd(c4, poly)
    return ptrim(c2), ptrim(c4)


RHO, Z = sp.symbols("rho z")


def to_sp(p):
    return sp.expand(sum(sp.Rational(c.numerator, c.denominator) * RHO ** k for k, c in enumerate(p)))


def is_plaquette(S, d):
    sites = {s for b in S for s in bsites(b, d)}
    return len(S) == 4 and len(sites) == 4


# ------------------------------------------------------------------ A: one record
def fam_A():
    ok = True
    k = sp.symbols("k1:4", real=True)
    Hk = sum((sp.sin(k[a]) * sp.Matrix(SIG[a].tolist()).applyfunc(sp.nsimplify) for a in range(3)), sp.zeros(2))
    ok &= sp.simplify(Hk * Hk - sp.eye(2) * sum(sp.sin(x) ** 2 for x in k)) == sp.zeros(2)
    s2, s4 = sp.Rational(1, 2), sp.Rational(3, 8)          # averages of sin^2, sin^4 over the circle
    x = sp.symbols("x")
    ok &= sp.integrate(sp.sin(x) ** 2, (x, 0, 2 * sp.pi)) / (2 * sp.pi) == s2
    ok &= sp.integrate(sp.sin(x) ** 4, (x, 0, 2 * sp.pi)) / (2 * sp.pi) == s4
    m2 = 3 * s2
    m4 = 3 * s4 + 6 * s2 * s2
    ok &= m2 == sp.Rational(3, 2) and m4 == sp.Rational(21, 8) and m4 - 3 * m2 ** 2 == sp.Rational(-33, 8)
    # no closed 3-hop process: every hop changes the total coordinate parity of the records
    zero3 = True
    for eps in (1, -1):
        for a0 in range(3):
            anchor = ((0, 0, 0), a0)
            for S in connected_sets(anchor, 3, 3):
                loc = Local(sorted({s for b in S for s in bsites(b, 3)}), 3)
                H2 = {b: loc.hop2(b, eps) for b in S}
                for rest in itertools.product(sorted(S), repeat=2):
                    if set((anchor,) + rest) == set(S):
                        zero3 &= not any(loc.expect(H2[anchor] @ H2[rest[0]] @ H2[rest[1]], 8))
    ok &= zero3
    rep("A", ok, "one record: H(k)^2 = sum_a sin^2 k_a, m2 = 3/2, m4 = 21/8, kappa4 = -33/8 (block 54's D_j with coin "
                 "sigma_j); every 3-hop product on Z^3 has zero diagonal (odd cumulants vanish), both signs")


# ------------------------------------------------------------------ C: cumulants on Z^3
C3 = {}


def fam_C():
    ok = True
    for eps in (1, -1):
        C3[eps] = cumulants(3, eps)
    c2p, c4p = map(to_sp, C3[1])
    c2m, c4m = map(to_sp, C3[-1])
    r = RHO
    ok &= sp.expand(c2p - sp.Rational(3, 2) * r * (1 - r)) == 0 and sp.expand(c2m - c2p) == 0
    ok &= sp.expand(c4p - r * (1 - r) / 8 * (21 - 198 * r + 207 * r ** 2)) == 0
    ok &= sp.expand(c4m - r * (1 - r) / 8 * (21 - 150 * r + 159 * r ** 2)) == 0
    ok &= sp.expand(c4p - c4m + 6 * r ** 2 * (1 - r) ** 2) == 0
    ok &= c4p.subs(r, 1) == 0 and c4m.subs(r, 1) == 0 and sp.degree(c4p, r) <= 4 and sp.degree(c4m, r) <= 4
    ok &= sp.Poly(c4p, r).coeff_monomial(r) == sp.Rational(21, 8)
    # the sign enters only through plaquettes (per sequence); bond sets with five sites contribute nothing
    Kp = {q: poly for kind, S, q, poly in sequences(3, 1) if kind == "K"}
    Km = {q: poly for kind, S, q, poly in sequences(3, -1) if kind == "K"}
    sets = {q: S for kind, S, q, poly in sequences(3, 1) + sequences(3, -1) if kind == "K"}
    ok &= all(ptrim(Kp.get(q, [F(0)])) == ptrim(Km.get(q, [F(0)])) for q, S in sets.items() if not is_plaquette(S, 3))
    ok &= all(len({s for b in S for s in bsites(b, 3)}) <= 4 for S in sets.values())
    ok &= any(is_plaquette(S, 3) and ptrim(Kp.get(q, [F(0)])) != ptrim(Km.get(q, [F(0)])) for q, S in sets.items())
    nseq = sum(1 for x in sequences(3, 1) if x[0] == "K")
    rep("C", ok, f"Z^3 per site ({nseq} connected 4-sequences): c2 = (3/2)rho(1-rho); c4(+) = rho(1-rho)(21-198rho+207rho^2)/8, "
                 "c4(-) = rho(1-rho)(21-150rho+159rho^2)/8; c4(+) - c4(-) = -6rho^2(1-rho)^2, all of it from plaquettes; "
                 "five-site sets give 0; c4(1) = 0 (jam); O(rho) = 21/8")


# ------------------------------------------------------------------ V: brute-force validations
def torus_traces(L, d, N, eps):
    sites = list(itertools.product(range(L), repeat=d))
    V = len(sites)
    sidx = {s: i for i, s in enumerate(sites)}
    basis = []
    for X in itertools.combinations(range(V), N):
        for cs in itertools.product((1, 2), repeat=N):
            st = [0] * V
            for x, c in zip(X, cs):
                st[x] = c
            basis.append(tuple(st))
    bidx = {st: i for i, st in enumerate(basis)}
    rows, cols, vals = [], [], []
    for j, st in enumerate(basis):
        for y in (x for x in range(V) if st[x]):
            for a in range(d):
                for sg in (1, -1):
                    x = sidx[tuple((sites[y][i] + (sg if i == a else 0)) % L for i in range(d))]
                    if st[x]:
                        continue
                    for alpha in range(2):
                        amp = (1j if sg == 1 else -1j) * SIG[a][alpha, st[y] - 1]
                        if amp == 0:
                            continue
                        new = list(st)
                        new[y], new[x] = 0, alpha + 1
                        lo, hi = min(x, y), max(x, y)
                        sign = -1 if (eps == -1 and sum(1 for k in range(lo + 1, hi) if st[k]) % 2) else 1
                        rows.append(bidx[tuple(new)])
                        cols.append(j)
                        vals.append(sign * amp)
    D = len(basis)
    H = sps.csr_matrix((vals, (rows, cols)), shape=(D, D))
    assert abs(H - H.conj().T).max() < 1e-12
    t2 = gi(complex(H.multiply(H.T).sum()))[0]
    t4 = 0
    for s0 in range(0, D, 4000):
        Y = H @ (H @ sps.identity(D, format="csc", dtype=complex)[:, s0:s0 + 4000])
        t4 += (abs(Y.data) ** 2).sum()
    return t2, round(t4)


def orbit_t4(L, N, eps):
    """tr((2H)^4) on the L^3 torus: (V/N) x sum over basis states with a record at site 0 of |(2H)^2 e_s|^2."""
    sites = list(itertools.product(range(L), repeat=3))
    V = len(sites)
    sidx = {s: i for i, s in enumerate(sites)}
    nb = [[(sidx[tuple((s[i] + (sg if i == a else 0)) % L for i in range(3))], a, 1j if sg == 1 else -1j)
           for a in range(3) for sg in (1, -1)] for s in sites]

    def apply(vec):
        out = {}
        for st, amp in vec.items():
            occ = dict(st)
            for y, cy in st:
                for (x, a, coef) in nb[y]:
                    if x in occ:
                        continue
                    for alpha in range(2):
                        m = SIG[a][alpha, cy - 1]
                        if m == 0:
                            continue
                        lo, hi = min(x, y), max(x, y)
                        sign = -1 if (eps == -1 and sum(1 for (w, _) in st if lo < w < hi) % 2) else 1
                        new = tuple(sorted([(w, c) for (w, c) in st if w != y] + [(x, alpha + 1)]))
                        out[new] = out.get(new, 0) + sign * coef * m * amp
        return out
    tot = 0
    for rest in itertools.combinations(range(1, V), N - 1):
        for coins in itertools.product((1, 2), repeat=N):
            v = apply(apply({tuple(zip((0,) + rest, coins)): 1}))
            tot += sum(abs(c) ** 2 for c in v.values())
    return F(round(tot)) * V / N


def series_traces(c2, c4, V, N):
    rho = 2 * Z / (1 + 2 * Z)
    C2 = to_sp(c2).subs(RHO, rho)
    C4 = to_sp(c4).subs(RHO, rho)
    e2 = sp.Poly(sp.expand(sp.cancel((1 + 2 * Z) ** V * V * C2)), Z).coeff_monomial(Z ** N)
    e4 = sp.Poly(sp.expand(sp.cancel((1 + 2 * Z) ** V * (V * C4 + 3 * V ** 2 * C2 ** 2))), Z).coeff_monomial(Z ** N)
    return 4 * e2, 16 * e4


def fam_V():
    ok, out = True, []
    for eps in (1, -1):
        c2, c4 = cumulants(2, eps)
        for N in (1, 2, 3, 4):
            p2, p4 = series_traces(c2, c4, 25, N)
            t2, t4 = torus_traces(5, 2, N, eps)
            ok &= (p2 == t2 and p4 == t4)
        out.append(f"2D eps={eps:+d}: c4 = {'; '.join(str(x) for x in c4)}")
    t3 = []
    for eps in (1, -1):
        c2, c4 = C3[eps]
        for N in (1, 2):
            p2, p4 = series_traces(c2, c4, 125, N)
            t2, t4 = torus_traces(5, 3, N, eps)
            ok &= (p2 == t2 and p4 == t4)
            if N == 2:
                t3.append(t4)
        p2, p4 = series_traces(c2, c4, 125, 3)
        b4 = orbit_t4(5, 3, eps)
        ok &= p4 == b4
        t3.append(int(b4))
    ok &= t3[0] == 9135000 and t3[2] == 9183000
    rep("V", ok, "exact brute-force tr((2H)^2), tr((2H)^4) equal the series on the 5x5 torus for N = 1..4 and on the 5^3 torus "
                 f"for N = 1, 2, 3, both signs (5^3, N = 2: {t3[0]} and {t3[2]}, i.e. 9135/496 and 9183/496 per state as in "
                 f"#8642; N = 3: {t3[1]} and {t3[3]}); " + "; ".join(out))


# ------------------------------------------------------------------ L: fixed filling
def fam_L():
    ok = True
    r, t, b = RHO, sp.symbols("t"), sp.symbols("beta")
    c2 = to_sp(C3[1][0])
    Cc = {}
    for eps in (1, -1):
        c4 = to_sp(C3[eps][1])
        # Legendre transform of g(t) = log(1+2e^t) + b^2 c2/2 + b^4 c4/24 at fixed rho, to order b^4
        rho_t = 2 * sp.exp(t) / (1 + 2 * sp.exp(t))
        g0pp = sp.simplify(sp.diff(rho_t, t))
        dc2 = sp.diff(c2, r) * r * (1 - r)
        corr = sp.simplify(3 * dc2 ** 2 / (r * (1 - r)))
        ok &= sp.simplify(g0pp - rho_t * (1 - rho_t)) == 0
        Cc[eps] = sp.factor(sp.expand(c4 - corr))
    ok &= sp.expand(Cc[1] + sp.Rational(3, 8) * r * (1 - r) * (11 - 6 * r + 3 * r ** 2)) == 0
    ok &= sp.expand(Cc[-1] + sp.Rational(3, 8) * r * (1 - r) * (11 - 22 * r + 19 * r ** 2)) == 0
    ok &= sp.expand(Cc[1] - Cc[-1] + 6 * r ** 2 * (1 - r) ** 2) == 0
    ok &= sp.limit(Cc[1] / r, r, 0) == sp.Rational(-33, 8)
    # O(1/V) convergence of the exact canonical kappa4/V extracted from the validated series (rho = 1/4)
    ratios = []
    for eps in (1, -1):
        c4 = to_sp(C3[eps][1])
        pred = Cc[eps].subs(r, sp.Rational(1, 4))
        diffs = []
        for V in (400, 800, 1600):
            N = V // 4
            vals = []
            for expr in (V * c2 / 2, V * c4 / 24 + V ** 2 * c2 ** 2 / 8):
                e = sp.together(expr.subs(r, 2 * Z / (1 + 2 * Z)))
                num, den = sp.fraction(e)
                kp = sp.degree(den, Z)
                const = sp.Poly(den, Z).LC() / 2 ** kp
                num = sp.Poly(sp.expand(num), Z)
                s = sum(sp.Rational(c) * comb(V - kp, N - j) * 2 ** (N - j) for (j,), c in num.terms() if 0 <= N - j <= V - kp)
                vals.append(s / const)
            Z0 = comb(V, N) * 2 ** N
            a2, a4 = vals[0] / Z0, vals[1] / Z0
            diffs.append(24 * (a4 - a2 * a2 / 2) / V - pred)
        ratios.append([diffs[i] / diffs[i + 1] for i in range(2)])
        ok &= all(abs(q - 2) < sp.Rational(1, 50) for q in ratios[-1])
    df = sp.expand(-(b ** 3 / 24) * (Cc[-1] - Cc[1]))
    du = sp.expand(-(b ** 3 / 6) * (Cc[-1] - Cc[1]))
    ok &= sp.expand(df + b ** 3 * r ** 2 * (1 - r) ** 2 / 4) == 0 and sp.expand(du + b ** 3 * r ** 2 * (1 - r) ** 2) == 0
    rep("L", ok, "fixed filling (Legendre, correction 3(d_t c2)^2/(d_t rho) = (27/4)rho(1-rho)(1-2rho)^2): C4(+) = "
                 "-(3/8)rho(1-rho)(11-6rho+3rho^2), C4(-) = -(3/8)rho(1-rho)(11-22rho+19rho^2), low-density limit -33/8 per record; "
                 f"exact canonical kappa4/V - C4 at V = 400, 800, 1600 halves (ratios {[[round(float(q), 4) for q in x] for x in ratios]}); "
                 "f(-) - f(+) = -(beta^3/4)rho^2(1-rho)^2, u(-) - u(+) = -beta^3 rho^2(1-rho)^2 + O(beta^5)")


# ------------------------------------------------------------------ B: alternation and clock modulation
def fam_B():
    ok = True
    dl = sp.symbols("delta")
    kv = sp.symbols("k1:4")
    res = {}
    for eps in (1, -1):
        seqs = sequences(3, eps)
        out = {}
        for axes, tag in (({0, 1, 2}, "all"), ({0}, "one")):
            c2 = 0
            c4 = 0
            for X in itertools.product((0, 1), repeat=3):
                for kind, S, seq, poly in seqs:
                    w = 1
                    for (x, a) in seq:
                        if a in axes:
                            w *= 1 + dl * (-1) ** ((x[a] + X[a]) % 2)
                    if kind == "m2":
                        c2 += w * to_sp(poly)
                    else:
                        c4 += w * to_sp(poly)
            out[tag] = (sp.expand(c2 / 8), sp.expand(c4 / 8))
        x2 = 0
        x4 = 0
        for kind, S, seq, poly in seqs:
            A = {}
            for bnd in seq:
                for s in bsites(bnd, 3):
                    A[s] = A.get(s, 0) + sp.Rational(1, 2)
            tot = sum(A.values())
            quad = sum(A[s] * A[s2] * sum(kv[i] * (s[i] - s2[i]) for i in range(3)) ** 2 for s in A for s2 in A)
            val = sp.Rational(1, 4) * (tot ** 2 - quad / 2)
            if kind == "m2":
                x2 += val * to_sp(poly)
            else:
                x4 += val * to_sp(poly)
        out["clock"] = (sp.expand(x2), sp.expand(x4))
        res[eps] = out
    r = RHO
    K2 = sum(x ** 2 for x in kv)
    ok &= sp.expand(res[1]["all"][0] - sp.Rational(3, 2) * r * (1 - r) * (1 + dl ** 2)) == 0
    ok &= sp.expand(res[1]["all"][1] - res[-1]["all"][1] + 6 * r ** 2 * (1 - r) ** 2 * (1 + dl ** 2) ** 2) == 0
    ok &= sp.expand(res[1]["one"][1] - res[-1]["one"][1] + 2 * r ** 2 * (1 - r) ** 2 * (3 + 2 * dl ** 2)) == 0
    ok &= sp.expand(res[1]["all"][1] - 3 * r * (1 - r) / 8 * ((69 * r ** 2 - 66 * r + 7) * (1 + dl ** 4)
                                                               + (114 * r ** 2 - 108 * r + 10) * dl ** 2)) == 0
    ok &= sp.expand(res[1]["clock"][0] - r * (1 - r) * (12 - K2) / 8) == 0
    ok &= sp.expand(res[1]["clock"][1] - 3 * r * (1 - r) / 8 * ((276 * r ** 2 - 264 * r + 28) - (36 * r ** 2 - 34 * r + 3) * K2)) == 0
    ok &= sp.expand(res[1]["clock"][1] - res[-1]["clock"][1] - 4 * r ** 2 * (1 - r) ** 2 * (K2 - 6)) == 0
    al4 = sp.Poly(res[-1]["all"][1], dl).coeff_monomial(dl ** 2)
    ck4 = sp.Poly(res[-1]["clock"][1], *kv).coeff_monomial(kv[0] ** 2)
    rep("B", ok, "alternation 1+delta(-1)^x_a on all axes: c2 = (3/2)rho(1-rho)(1+delta^2); c4(+) = (3rho(1-rho)/8)[(69rho^2-66rho+7)"
                 "(1+delta^4) + (114rho^2-108rho+10)delta^2]; c4(+) - c4(-) = -6rho^2(1-rho)^2(1+delta^2)^2 (delta^2 part "
                 "-12rho^2(1-rho)^2); one axis: -2rho^2(1-rho)^2(3+2delta^2); clock u = eta cos(k.x), eta^2 terms: chi2 = "
                 "rho(1-rho)(12-|k|^2)/8, chi4(+) = (3rho(1-rho)/8)[(276rho^2-264rho+28) - (36rho^2-34rho+3)|k|^2], "
                 f"chi4(+) - chi4(-) = 4rho^2(1-rho)^2(|k|^2 - 6); for eps=-1 the delta^2 coefficient is {sp.factor(al4)} and the "
                 f"k_1^2 coefficient {sp.factor(ck4)}")


# ------------------------------------------------------------------ G: ground energy
def trial_energy(L, N, chi):
    sites = list(itertools.product(range(L), repeat=3))
    V = len(sites)
    sid = {s: i for i, s in enumerate(sites)}
    amp = {}
    for X in itertools.combinations(range(V), N):
        p = 1
        for x in X:
            p *= 1j ** (sum(sites[x]) % 4)
        for coins in itertools.product((0, 1), repeat=N):
            c = p
            for q in coins:
                c *= chi[q]
            amp[(X, coins)] = c
    E2 = 0
    for (X, coins), a in amp.items():
        occ = set(X)
        for idx, y in enumerate(X):
            for ax in range(3):
                for sg in (1, -1):
                    t = list(sites[y])
                    t[ax] = (t[ax] + sg) % L
                    x = sid[tuple(t)]
                    if x in occ:
                        continue
                    for al in (0, 1):
                        m = SIG[ax][al, coins[idx]]
                        if m == 0:
                            continue
                        nX, nC = list(X), list(coins)
                        nX[idx], nC[idx] = x, al
                        o = sorted(range(N), key=lambda j: nX[j])
                        E2 += amp[(tuple(nX[j] for j in o), tuple(nC[j] for j in o))].conjugate() * (1j if sg == 1 else -1j) * m * a
    er, ei = gi(E2)
    nr = gi(complex(sum(abs(v) ** 2 for v in amp.values())))[0]
    Mq = sum(np.conj(chi[i]) * (SIG[0] + SIG[1] + SIG[2])[i, j] * chi[j] for i in range(2) for j in range(2))
    qr, qi = gi(Mq)
    cc = gi(complex(sum(abs(c) ** 2 for c in chi)))[0]
    return ei == 0 and qi == 0 and F(er, 2 * nr) == F(N * (V - N), V - 1) * F(qr, cc)


def fam_G():
    from mpmath import iv
    ok = True
    ok &= all(trial_energy(4, N, chi) for N, chi in ((2, (2, 1 + 1j)), (2, (1, 0)), (3, (1, 3 - 2j))))
    ev = sp.Matrix(SIG[0] + SIG[1] + SIG[2]).applyfunc(sp.nsimplify).eigenvals()
    ok &= set(ev) == {sp.sqrt(3), -sp.sqrt(3)}
    iv.dps = 40
    vals = [F(0), F(1, 2), F(1), F(1, 2), F(0), F(1, 2), F(1), F(1, 2)]    # sin^2(2 pi j/8)
    cnt = {}
    for a in vals:
        for b2 in vals:
            for c in vals:
                cnt[a + b2 + c] = cnt.get(a + b2 + c, 0) + 1
    levels = sorted(cnt.items(), key=lambda q: -q[0])
    ok &= levels[:3] == [(F(3), 8), (F(5, 2), 48), (F(2), 120)]
    V = 512
    cert = []
    for N in range(1, 61):
        tot, left = iv.mpf(0), N
        for val, m in levels:
            take = min(m, left)
            tot += take * iv.sqrt(iv.mpf(val.numerator) / val.denominator)
            left -= take
            if left == 0:
                break
        margin = -tot + iv.sqrt(3) * iv.mpf(N * (V - N)) / (V - 1)
        if margin.a > 0:
            cert.append(N)
    ok &= cert == list(range(11, 36))
    A = sp.pi / 6 * (2 * sp.sqrt(3)) ** sp.Rational(3, 2)
    rho_star = (sp.Rational(3, 5) * A ** sp.Rational(-2, 3) / sp.sqrt(3)) ** 3
    ok &= 0.0036 < float(rho_star) < 0.0037
    rep("G", ok, "hard-core-boson trial state (every record in the k0 = (pi/2)^3 plane wave with spinor chi) has energy exactly "
                 "N(V-N)/(V-1) chi'(sigma1+sigma2+sigma3)chi/chi'chi (4^3, N = 2, 3, three spinors); lowest value -sqrt3, so "
                 "E0(+) <= -sqrt3 N(V-N)/(V-1) when 4 | L; free fermions bound E0(-) from below; on 8^3 (shells |d|^2 = 3, 5/2, 2 "
                 f"with 8, 48, 120 states) interval arithmetic certifies E0(+) < E0(-) for N = {cert[0]}..{cert[-1]}; thermodynamic "
                 f"limit: the symmetric rule is strictly lower for rho < ((3/5)A^(-2/3)/sqrt3)^3 = {float(rho_star):.5f}, "
                 "A = (pi/6)(2sqrt3)^(3/2)")


if __name__ == "__main__":
    for fam in (fam_Q, fam_A, fam_C, fam_V, fam_L, fam_B, fam_G):
        fam()
    print(f"runtime {time.time() - T0:.0f}s; failed families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT check families {sorted(set(FAILS))}")
        sys.exit(1)
    print("SUMMARY: PARTIAL exact: the fourth-order linked-cluster (high-temperature) coefficients of the crowd on Z^3 at fixed "
          "filling, both composition signs: C2 = (3/2)rho(1-rho), C4(+/-) = -(3/8)rho(1-rho)(11-14rho+11rho^2 +/- 8rho(1-rho)); "
          "the sign enters first through plaquette exchanges, C4(+) - C4(-) = -6rho^2(1-rho)^2, so at that order the "
          "antisymmetric rule has the lower free energy and energy; the ground energy at low filling is lower for the symmetric "
          "rule (certified on 8^3 for 11 <= N <= 35 and for rho < 0.00365).")
    print("HIT: (a) exact, hop amplitude 1/2: per site at fixed filling, log Z/V = s(rho) + beta^2 C2/2 + beta^4 C4/24 + O(beta^6) "
          "with C2 = (3/2)rho(1-rho), C4(+) = -(3/8)rho(1-rho)(11-6rho+3rho^2), C4(-) = -(3/8)rho(1-rho)(11-22rho+19rho^2); the "
          "antisymmetric rule lowers f by (beta^3/4)rho^2(1-rho)^2; (b) the sign also moves the fourth-order alternation "
          "coefficient (delta^2 part -12rho^2(1-rho)^2, all axes) and the clock-gradient coefficient (4rho^2(1-rho)^2|k|^2); "
          "but the ground-state order is the reverse at low filling: E0(+) <= -sqrt3 N(V-N)/(V-1) < E0(-) on 8^3 for N = 11..35.")
