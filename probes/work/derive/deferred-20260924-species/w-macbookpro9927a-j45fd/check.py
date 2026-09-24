#!/usr/bin/env python3
"""Deferred-science recovery, species (first pass): checks for ATTEMPT.md, worker w-macbookpro9927a-j45fd (claude-opus-5-5).

Residual worked (PR8602, block 70, deferred CHECKER item 2 and control W2): the exact static multiplicity of the walk's levels in
varying fields on even tori. Objects as landed on origin/main (block 70 note): (T psi)(x) = psi(x - e), S = (i/2)(T - T^dag),
C = (T + T^dag)/2, P = S C; H = sum_a sigma_a S_a; the exchange maps V_n = R_n U_n, U_n = (-1)^(n.x), R_n the coin matrix of the
half turn rho_n = s_n D_n (identity for n = 000, 111); Theta = sigma_2 followed by complex conjugation. Everything is exact:
Gaussian rationals for operator identities, characteristic polynomials over F_p (p = 1 mod 4) as certificates.
"""
from __future__ import annotations

import hashlib
import json
import random
import subprocess
import time
from fractions import Fraction as Fr

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


MAIN_NOTE = ("docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_"
             "BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md")
MAIN_SHA = "0e6ad82850"
HEAD8602 = "8b4eccab5cb0cda8a42b254cd9af8261e2cde203"
P8602 = ".claude/science/physics-loops/admissibility-induced-law-20260906/"
SOURCES = [   # (path under P8602, manifest sha256) - deferred sources of PR8602 used here
    ("CHECKER_block70_findings.md", "fbb5fe114b5b"),
    ("RESULTS_block70.md", "c6ac06d3509b"),
    ("specs/supervisor_control_block70_species_exchange.py", "de4c3912baff"),
    ("specs/supervisor_control_block70_species_exchange.out.txt", "a9eb88ca3f2f"),
]
QUOTES = [
    ("main", "so every eigenvalue of a finite static Hermitian member is at least doubly degenerate"),
    ("main", "This is not eightfold eigenspace degeneracy or a count of linearly independent states."),
    ("main", "With rates and reach-three strains in any configuration, the three nonidentity even maps commute with the generator"),
    ("checker", "the supervisor expected a further doubling of levels beyond the reversal of motion's. Executed multiplicity is two in "
                "every case."),
    ("out", "rates + reach-three strain  : {2: 216}"),
    ("frozen", "the sixteen branches (eight species, two signs of the energy) fall into two classes of eight exact copies"),
]


def family_q() -> None:
    bad = []
    b = json.load(open("probes/work/deferred-science-20260924/batch-08.json"))
    manifest = {s["path"]: s for s in b["sources"] if s["pr"] == 8602}
    texts = {}
    for path, sha12 in SOURCES:
        s = manifest[P8602 + path]
        data = subprocess.run(["git", "show", f"{HEAD8602}:{P8602 + path}"], capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != s["sha256"] or not s["sha256"].startswith(sha12):
            bad.append(path)
        texts[path] = data.decode()
    texts["main"] = subprocess.run(["git", "show", f"{MAIN_SHA}:{MAIN_NOTE}"], capture_output=True, text=True).stdout
    texts["frozen"] = subprocess.run(["git", "show", f"{HEAD8602}:{MAIN_NOTE}"], capture_output=True, text=True).stdout
    key = {"checker": "CHECKER_block70_findings.md", "out": "specs/supervisor_control_block70_species_exchange.out.txt"}
    for tag, q in QUOTES:
        if q not in texts[key.get(tag, tag)]:
            bad.append(f"quote:{tag}")
    st = json.load(open("probes/work/derive/deferred-20260924-species/w-macbookpro9927a-j45fd/RECOVERY_STATUS.json"))
    allsrc = {(x["pr"], x["path"]): x for x in b["sources"]}
    for e in st["source_groups_inspected"]:
        m = allsrc[(e["pr"], e["path"])]
        data = subprocess.run(["git", "show", f"{m['head']}:{m['path']}"], capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != m["sha256"] or e["sha256"] != m["sha256"] or e["head"] != m["head"]:
            bad.append("status:" + e["path"].split("/")[-1])
    f = next(x for x in b["findings"] if x["id"] == "U8-R1")
    if "distinguish formal branch-label orbits from static finite eigenvalue doubling" not in f["resolution"]:
        bad.append("U8-R1")
    check("Q", not bad, "origin/main 0e6ad82850 block 70 (T3(a), T3(b)), the frozen head 8b4eccab5c (T3's 'two classes of eight exact "
          "copies'), review finding U8-R1, the four deferred PR8602 sources (checker item 2: 'Executed multiplicity is two in every "
          f"case'; control W2 '{{2: 216}}') and all {len(st['source_groups_inspected'])} sources listed in RECOVERY_STATUS.json "
          f"re-fetched from their frozen heads with SHA256 equal to the manifest"
          f"{'; bad ' + str(bad) if bad else ''}")


# ---------------------------------------------------------------- exact sparse operators over Q(i)
def gm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def ga(a, b):
    return (a[0] + b[0], a[1] + b[1])


Z0 = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))
I = (Fr(0), Fr(1))


class Op:
    def __init__(self, n, d=None):
        self.n = n
        self.d = d or {}

    def add_to(self, i, j, v):
        w = ga(self.d.get((i, j), Z0), v)
        if w == Z0:
            self.d.pop((i, j), None)
        else:
            self.d[(i, j)] = w

    def __add__(self, o):
        r = Op(self.n, dict(self.d))
        for k, v in o.d.items():
            r.add_to(k[0], k[1], v)
        return r

    def scale(self, c):
        return Op(self.n, {k: gm(c, v) for k, v in self.d.items() if gm(c, v) != Z0})

    def __sub__(self, o):
        return self + o.scale((Fr(-1), Fr(0)))

    def __matmul__(self, o):
        rows = {}
        for (i, k), v in self.d.items():
            rows.setdefault(i, []).append((k, v))
        cols = {}
        for (k, j), v in o.d.items():
            cols.setdefault(k, []).append((j, v))
        r = Op(self.n)
        for i, lst in rows.items():
            for k, v in lst:
                for j, u in cols.get(k, []):
                    r.add_to(i, j, gm(v, u))
        return r

    def conj(self):
        return Op(self.n, {k: (v[0], -v[1]) for k, v in self.d.items()})

    def zero(self):
        return not self.d


PAULI = {1: {(0, 1): ONE, (1, 0): ONE}, 2: {(0, 1): (Fr(0), Fr(-1)), (1, 0): I}, 3: {(0, 0): ONE, (1, 1): (Fr(-1), Fr(0))}}


class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = [(a, b, c) for a in range(L[0]) for b in range(L[1]) for c in range(L[2])]
        self.idx = {x: i for i, x in enumerate(self.sites)}
        self.N = len(self.sites)

    def mv(self, x, a, k):
        y = list(x)
        y[a] = (y[a] + k) % self.L[a]
        return tuple(y)

    def site_op(self, entries):          # entries: {(x, y): gauss} on sites -> Op on sites x spin (spin identity)
        o = Op(2 * self.N)
        for (x, y), v in entries.items():
            for s in (0, 1):
                o.add_to(2 * self.idx[x] + s, 2 * self.idx[y] + s, v)
        return o

    def kron(self, entries, c):          # site entries (x,y) times Pauli c (or a 2x2 dict)
        P = PAULI[c] if isinstance(c, int) else c
        o = Op(2 * self.N)
        for (x, y), v in entries.items():
            for (s, t), u in P.items():
                o.add_to(2 * self.idx[x] + s, 2 * self.idx[y] + t, gm(v, u))
        return o

    def T(self, a, k=1):                 # (T^k psi)(x) = psi(x - k e_a)
        return {(x, self.mv(x, a, -k)): ONE for x in self.sites}

    def S(self, a):                      # (i/2)(T - T^dag)
        e = {}
        for x in self.sites:
            e[(x, self.mv(x, a, -1))] = ga(e.get((x, self.mv(x, a, -1)), Z0), (Fr(0), Fr(1, 2)))
            e[(x, self.mv(x, a, 1))] = ga(e.get((x, self.mv(x, a, 1)), Z0), (Fr(0), Fr(-1, 2)))
        return {k: v for k, v in e.items() if v != Z0}

    def P(self, a):                      # S C = (i/4)(T^2 - T^-2)
        e = {}
        for x in self.sites:
            for k, c in ((-2, Fr(1, 4)), (2, Fr(-1, 4))):
                y = self.mv(x, a, k)
                e[(x, y)] = ga(e.get((x, y), Z0), (Fr(0), c))
        return {k: v for k, v in e.items() if v != Z0}

    def Cf(self, a, f):                  # (C_a[f] psi)(x) = (f(x,x+e) psi(x+e) + f(x-e,x) psi(x-e))/2, f on bonds (x, x+e)
        e = {}
        for x in self.sites:
            y, z = self.mv(x, a, 1), self.mv(x, a, -1)
            e[(x, y)] = ga(e.get((x, y), Z0), (f[(x, a)] / 2, Fr(0)))
            e[(x, z)] = ga(e.get((x, z), Z0), (f[(z, a)] / 2, Fr(0)))
        return {k: v for k, v in e.items() if v != Z0}


def emul(A, B):
    """product of site-entry dicts"""
    rows = {}
    for (x, y), v in A.items():
        rows.setdefault(x, []).append((y, v))
    cols = {}
    for (y, z), v in B.items():
        cols.setdefault(y, []).append((z, v))
    r = {}
    for x, lst in rows.items():
        for y, v in lst:
            for z, u in cols.get(y, []):
                r[(x, z)] = ga(r.get((x, z), Z0), gm(v, u))
    return {k: v for k, v in r.items() if v != Z0}


def eadd(A, B, c=ONE):
    r = dict(A)
    for k, v in B.items():
        r[k] = ga(r.get(k, Z0), gm(c, v))
    return {k: v for k, v in r.items() if v != Z0}


def walk(t, strain=None, reach=3, frame=None):
    """sum_a sigma_a (S_a + sum_j (1/2){C_a[B_a^j], X_j}), X = P (reach three) or S (reach two); or block 62's frame."""
    H = Op(2 * t.N)
    if frame is not None:
        for j in range(3):
            Sj = t.S(j)
            for a in range(3):
                Ed = {(x, x): (frame[(x, j, a)], Fr(0)) for x in t.sites}
                anti = eadd(emul(Ed, Sj), emul(Sj, Ed))
                H = H + t.kron({k: (v[0] / 2, v[1] / 2) for k, v in anti.items()}, a + 1)
        return H
    for a in range(3):
        ent = t.S(a)
        if strain is not None:
            for j in range(3):
                X = t.P(j) if reach == 3 else t.S(j)
                if not X:
                    continue
                Cb = t.Cf(a, {k: strain[(k[0], a, j)] for k in [(x, a) for x in t.sites]})
                anti = eadd(emul(Cb, X), emul(X, Cb))
                ent = eadd(ent, {k: (v[0] / 2, v[1] / 2) for k, v in anti.items()})
        H = H + t.kron(ent, a + 1)
    return H


def rates(t, H, phi):
    Ph = Op(2 * t.N, {(2 * i + s, 2 * i + s): (phi[x], Fr(0)) for x, i in t.idx.items() for s in (0, 1)})
    return Ph @ H @ Ph


RN = {(0, 0, 0): None, (1, 1, 1): None, (1, 1, 0): 3, (1, 0, 1): 2, (0, 1, 1): 1, (1, 0, 0): 1, (0, 1, 0): 2, (0, 0, 1): 3}


def V(t, n):
    U = {(x, x): (Fr((-1) ** (n[0] * x[0] + n[1] * x[1] + n[2] * x[2])), Fr(0)) for x in t.sites}
    c = RN[n]
    return t.site_op(U) if c is None else t.kron(U, c)


def theta_conj(t, O):
    """Theta O Theta^-1 = sigma_2 conj(O) sigma_2."""
    S2 = t.kron({(x, x): ONE for x in t.sites}, 2)
    return S2 @ O.conj() @ S2


def family_a(t, fields) -> None:
    ok = True
    Vs = {n: V(t, n) for n in RN}
    Id = t.site_op({(x, x): ONE for x in t.sites})
    ev = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
    ok &= all((Vs[n] @ Vs[n] - Id).zero() for n in RN)
    ok &= all((Vs[a] @ Vs[b] + Vs[b] @ Vs[a]).zero() for a in ev for b in ev if a < b)
    ok &= (Vs[(1, 1, 0)] @ Vs[(0, 1, 1)] - Vs[(1, 0, 1)].scale(I)).zero()
    new_anti = all((theta_conj(t, Vs[n]) + Vs[n]).zero() for n in ev)
    Hw = fields["rates"]
    s = {n: (-1) ** (n[0] + n[1] + n[2]) for n in RN}
    ok &= all((Vs[n] @ Hw @ Vs[n] - Hw.scale((Fr(s[n]), Fr(0)))).zero() for n in RN)
    ok &= all((theta_conj(t, H) - H).zero() for H in fields.values())
    ok &= new_anti
    check("A", ok, f"torus {t.L}, rational fields: V_n^2 = 1, the three even maps pairwise anticommute, V_110 V_011 = i V_101, "
          "V_n H V_n = s_n H in a varying rate field (all eight n), Theta commutes with the walk in rate, reach-two and frame fields; "
          "and (new) Theta V_n Theta^-1 = -V_n for each even map: the reversal anticommutes with the three species symmetries (the "
          "reach-three strain vanishes on a side of 4, since there T^2 = T^-2; it is checked on 6x4x4 in W)")


def family_c() -> None:
    import itertools
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]
    def mm(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    def neg(a):
        return [[-v for v in r] for r in a]
    def conj(a):
        return [[complex(v).conjugate() for v in r] for r in a]
    def J(a):          # J a J^-1 with J = sigma_y K: sigma_y conj(a) sigma_y
        return mm(mm(sy, conj(a)), sy)
    v1, v2, v3 = sz, sx, neg(sy)
    idm = [[1, 0], [0, 1]]
    ok = all(mm(v, v) == idm for v in (v1, v2, v3))
    ok &= all(mm(a, b) == neg(mm(b, a)) for a, b in itertools.combinations((v1, v2, v3), 2))
    ok &= mm(v1, v3) == [[1j * x for x in r] for r in v2]
    ok &= all(J(v) == neg(v) for v in (v1, v2, v3))
    ok &= mm(sy, conj(sy)) == neg(idm)                     # J^2 = -1, as Theta^2 = -1
    check("C", ok, "the 2-dimensional corepresentation V_110 -> sigma_z, V_101 -> sigma_x, V_011 -> -sigma_y, Theta -> sigma_y K obeys "
          "every relation of the symmetries (involutions, pairwise anticommuting, V_110 V_011 = i V_101, Theta anticommuting with each, "
          "Theta^2 = -1): on an eigenspace C^2 (x) W, Theta = (sigma_y K) (x) Theta_W with Theta_W^2 = +1, so W carries a real "
          "structure and symmetry forces multiplicity 2, not 4 or 8")


# ---------------------------------------------------------------- characteristic polynomials over F_p as certificates
PRIME = 1000033        # prime, = 1 mod 4


def sqrt_minus_one(p):
    for g in range(2, 200):
        r = pow(g, (p - 1) // 4, p)
        if r * r % p == p - 1:
            return r
    raise ValueError


def to_mod(v, p, r):
    re = v[0].numerator * pow(v[0].denominator, p - 2, p)
    im = v[1].numerator * pow(v[1].denominator, p - 2, p)
    return (re + r * im) % p


def charpoly_mod(M, p):
    n = len(M)
    A = [row[:] for row in M]
    for k in range(n - 2):
        piv = next((i for i in range(k + 1, n) if A[i][k] % p), None)
        if piv is None:
            continue
        if piv != k + 1:
            A[piv], A[k + 1] = A[k + 1], A[piv]
            for row in A:
                row[piv], row[k + 1] = row[k + 1], row[piv]
        inv = pow(A[k + 1][k], p - 2, p)
        for i in range(k + 2, n):
            if A[i][k] % p:
                t = A[i][k] * inv % p
                ri, rk = A[i], A[k + 1]
                for j in range(n):
                    ri[j] = (ri[j] - t * rk[j]) % p
                for row in A:
                    row[k + 1] = (row[k + 1] + t * row[i]) % p
    P = [[1]]
    for m in range(1, n + 1):
        cur = [0] + P[m - 1]
        h = A[m - 1][m - 1]
        cur = [(c - h * (P[m - 1][i] if i < len(P[m - 1]) else 0)) % p for i, c in enumerate(cur)]
        prod = 1
        for i in range(m - 1, 0, -1):
            prod = prod * A[i][i - 1] % p
            coef = A[i - 1][m - 1] * prod % p
            if coef:
                for d, c in enumerate(P[i - 1]):
                    cur[d] = (cur[d] - coef * c) % p
        P.append(cur)
    return P[n]


def ptrim(a):
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def pmod(a, b, p):
    a = ptrim(a[:])
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and any(a):
        c = a[-1] * inv % p
        s = len(a) - len(b)
        for i, bi in enumerate(b):
            a[s + i] = (a[s + i] - c * bi) % p
        a = ptrim(a)
        if len(a) < len(b):
            break
    return a


def pgcd(a, b, p):
    a, b = ptrim(a), ptrim(b)
    while any(b):
        a, b = b, pmod(a, b, p)
    inv = pow(a[-1], p - 2, p)
    return [c * inv % p for c in a]


def deriv(a, p):
    return [i * a[i] % p for i in range(1, len(a))] or [0]


def dense(H, rows, p, r):
    pos = {v: i for i, v in enumerate(rows)}
    M = [[0] * len(rows) for _ in rows]
    for (i, j), v in H.d.items():
        if i in pos and j in pos:
            M[pos[i]][pos[j]] = to_mod(v, p, r)
    return M


def reduced_rows(t):
    """basis vectors of the +1 eigenspace of V_110 = sigma_3 (-1)^(x1+x2): V_110 is diagonal, so the block is a principal submatrix."""
    return [2 * i + s for x, i in t.idx.items() for s in (0, 1) if (1 if s == 0 else -1) * (-1) ** (x[0] + x[1]) == 1]


def cert_reduced(t, H, p, r):
    """(multiplicity of the root 0, degree of the rest, degree of gcd(rest, rest')) for the V_110 = +1 block."""
    rows = reduced_rows(t)
    f = charpoly_mod(dense(H, rows, p, r), p)
    m = 0
    while f[0] % p == 0:
        f, m = f[1:], m + 1
    g = pgcd(f, deriv(f, p), p)
    return m, len(f) - 1, len(g) - 1


def cert_kramers(t, H, p, r):
    f = charpoly_mod(dense(H, list(range(2 * t.N)), p, r), p)
    g = pgcd(f, deriv(f, p), p)
    gg = pgcd(g, deriv(g, p), p)
    sq = [0] * (2 * len(g) - 1)
    for i, a in enumerate(g):
        for j, b in enumerate(g):
            sq[i + j] = (sq[i + j] + a * b) % p
    return len(f) - 1, len(g) - 1, len(gg) - 1, ptrim(sq) == ptrim(f)


def family_w(t4, t6, fields4, H6, phi) -> None:
    p = PRIME
    r = sqrt_minus_one(p)
    ev = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
    V6 = {n: V(t6, n) for n in ev}
    comm6 = all((V6[n] @ H6 - H6 @ V6[n]).zero() for n in ev) and (theta_conj(t6, H6) - H6).zero() and \
        not (H6 - walk(t6)).zero() and (V6[(1, 1, 0)] @ V6[(1, 0, 1)] + V6[(1, 0, 1)] @ V6[(1, 1, 0)]).zero()
    m1, d1, g1 = cert_reduced(t4, fields4["rates"], p, r)
    m2, d2, g2 = cert_reduced(t6, H6, p, r)
    d3, g3, gg3, sq3 = cert_kramers(t4, fields4["frame"], p, r)
    d4, g4, gg4, sq4 = cert_kramers(t4, fields4["reach2"], p, r)
    # the rate field keeps the free walk's kernel exactly: H_w (Phi^-1 psi) = Phi H psi = 0 for the 16 zero modes k in {0, pi}^3
    Hw = fields4["rates"]
    kern_ok = True
    for k in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]:
        for sp in (0, 1):
            vec = {2 * t4.idx[x] + sp: (Fr((-1) ** (k[0] * x[0] + k[1] * x[1] + k[2] * x[2])) / phi[x], Fr(0)) for x in t4.sites}
            out = {}
            for (i, j), v in Hw.d.items():
                if j in vec:
                    out[i] = ga(out.get(i, Z0), gm(v, vec[j]))
            kern_ok &= all(v == Z0 for v in out.values())
    ok = (m1, d1, g1) == (8, 56, 0) and (m2, d2, g2) == (0, 96, 0) and (d3, g3, gg3, sq3) == (128, 64, 0, True) and \
        (d4, g4, gg4, sq4) == (128, 64, 0, True) and kern_ok and comm6
    check("W", ok, f"certificates over F_{p} (i -> {r}): a varying rate field on 4x4x4: the V_110 = +1 block has characteristic "
          f"polynomial E^{m1} q(E), q of degree {d1} squarefree (gcd with q' of degree {g1}) with q(0) != 0, and V_101 maps the block "
          f"onto the -1 block: 56 nonzero levels each of multiplicity exactly 2, and the zero level of multiplicity 16, which is exact "
          f"for every rate field (the 16 free zero modes, k in {{0, pi}}^3 times two coin states, divided by Phi = w^(1/2) are killed "
          f"by Phi H Phi: checked exactly); a varying reach-three strain on 6x4x4 (nonzero there, commuting with the even maps and "
          f"Theta: checked exactly): block of degree {d2} squarefree, no zero root; "
          f"frame and reach-two strain on 4x4x4, where no species map is a symmetry: characteristic polynomial of degree {d3} equal to "
          f"q^2, q of degree {g3} squarefree (and the same for reach two): every level exactly doubled")


def family_u(t4) -> None:
    p = PRIME
    r = sqrt_minus_one(p)
    H = walk(t4)
    f = charpoly_mod(dense(H, list(range(2 * t4.N)), p, r), p)
    def pw(a, b):
        out = [1]
        for _ in range(b):
            nxt = [0] * (len(out) + len(a) - 1)
            for i, x in enumerate(out):
                for j, y in enumerate(a):
                    nxt[i + j] = (nxt[i + j] + x * y) % p
            out = nxt
        return out
    def mul(a, b):
        return pw(a, 1) if False else [sum(a[i] * b[k - i] for i in range(len(a)) if 0 <= k - i < len(b)) % p
                                      for k in range(len(a) + len(b) - 1)]
    target = mul(mul(mul(pw([0, 1], 16), pw([p - 1, 0, 1], 24)), pw([p - 2, 0, 1], 24)), pw([p - 3, 0, 1], 8))
    ok = ptrim(f) == ptrim(target)
    check("U", ok, "the uniform walk on the 4x4x4 torus (the formal branch-label setting) has characteristic polynomial "
          "E^16 (E^2 - 1)^24 (E^2 - 2)^24 (E^2 - 3)^8 over F_p: levels of multiplicity 16, 24, 24, 8 (momentum and species labels "
          "together); a varying field lifts all of it to exact doubling")


def main() -> None:
    t0 = time.time()
    family_q()
    rnd = random.Random(20260924)
    t4 = Torus((4, 4, 4))
    phi = {x: Fr(rnd.randint(5, 15), 10) for x in t4.sites}
    H0 = walk(t4)
    strain4 = {(x, a, j): Fr(rnd.randint(-4, 4), 10) for x in t4.sites for a in range(3) for j in range(3)}
    frame4 = {(x, j, a): (Fr(1) if a == j else Fr(0)) + Fr(rnd.randint(-3, 3), 10) for x in t4.sites for j in range(3) for a in range(3)}
    t6 = Torus((6, 4, 4))
    strain6 = {(x, a, j): Fr(rnd.randint(-4, 4), 10) for x in t6.sites for a in range(3) for j in range(3)}
    fields4 = {"rates": rates(t4, H0, phi), "reach3": walk(t4, strain4, 3), "reach2": walk(t4, strain4, 2),
               "frame": walk(t4, frame=frame4)}
    family_a(t4, fields4)
    t6fields = walk(t6, strain6, 3)
    family_c()
    family_w(t4, t6, fields4, t6fields, phi)
    family_u(t4)
    print("\n".join(OUT))
    print(f"families Q A C W U (all exact): {len(OUT) - len(FAILS)}/{len(OUT)} ok, {time.time() - t0:.0f} s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PARTIAL recovered PR8602's deferred finite observation ('executed multiplicity is two in every case') as an exact "
          "statement: Theta anticommutes with the three even species maps, so the symmetry of the walk in rate and reach-three fields "
          "has a 2-dimensional irreducible corepresentation and forces only doubling; certified rational fields of all four kinds have "
          "every nonzero level exactly doubled; rate fields keep the eight species' 16 zero modes exactly (kernel Phi^-1 ker H); the "
          "uniform walk on 4^3 has multiplicities 16, 24, 24, 8")
    print("HIT: on even tori the reversal Theta = sigma_2 K anticommutes with each of block 70's even species maps V_110, V_101, V_011; "
          "with their own relations this makes the symmetry of the walk in any varying rate or reach-three field a 2-dimensional "
          "irreducible corepresentation (V -> sigma_z, sigma_x, -sigma_y, Theta -> sigma_y K), so symmetry forces levels of even "
          "multiplicity and never a four- or eightfold level; certified over F_1000033, rational rate (4x4x4), reach-three (6x4x4), "
          "frame and reach-two (4x4x4) fields have every nonzero level exactly doubled, while every positive rate field keeps the 16 "
          "zero modes of the eight species exactly (ker Phi H Phi = Phi^-1 ker H), against 16, 24, 24, 8 for the uniform walk")


if __name__ == "__main__":
    main()
