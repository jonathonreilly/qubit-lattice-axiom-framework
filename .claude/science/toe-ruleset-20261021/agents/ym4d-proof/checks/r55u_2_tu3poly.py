#!/usr/bin/env python3
"""r55u_2_tu3poly.py -- REVIEW55_TUNIF check r55u_2 (criteria: checks/r55u_2_criteria.md, written first).
Independent exact implementation of TUNIF Lemma TU-2 / Theorem TU-3 with z_1, z_2 SYMBOLIC (bivariate polynomials
in Z1, Z2 over Fraction). Imports nothing from the lane."""
from fractions import Fraction as Fr
from itertools import product, combinations
import random, sys

# ---------- bivariate polynomials {(i, j): coeff} for Z1^i Z2^j ----------
def P(c=0):
    return {} if c == 0 else {(0, 0): Fr(c)}
def padd(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, Fr(0)) + s * v
        if r[k] == 0: del r[k]
    return r
def pscale(p, c):
    return {} if c == 0 else {k: v * c for k, v in p.items()}
def pmulvar(p, var):              # var 0 -> Z1, 1 -> Z2
    return {((i + 1, j) if var == 0 else (i, j + 1)): v for (i, j), v in p.items()}
def peval1(p, var):               # set Z_var := 1
    r = {}
    for (i, j), v in p.items():
        k = (0, j) if var == 0 else (i, 0)
        r[k] = r.get(k, Fr(0)) + v
        if r[k] == 0: del r[k]
    return r
def pdivZm1(p, var):
    """Divide p by (Z_var - 1). Returns (quotient, remainder) with remainder = p|_{Z_var = 1}."""
    # group by the power of Z_var
    groups = {}
    for (i, j), v in p.items():
        e, other = (i, j) if var == 0 else (j, i)
        groups.setdefault(e, {})[other] = v
    if not groups:
        return {}, {}
    n = max(groups)
    def mono(e, other):
        return (e, other) if var == 0 else (other, e)
    q = {}
    carry = {}                     # b_{e-1} = c_e + b_e ; coefficients are polys in the other variable (dict other->v)
    for e in range(n, 0, -1):
        ce = groups.get(e, {})
        b = dict(ce)
        for o, v in carry.items():
            b[o] = b.get(o, Fr(0)) + v
        b = {o: v for o, v in b.items() if v != 0}
        for o, v in b.items():
            q[mono(e - 1, o)] = v
        carry = b
    rem = dict(groups.get(0, {}))
    for o, v in carry.items():
        rem[o] = rem.get(o, Fr(0)) + v
    rem = {mono(0, o): v for o, v in rem.items() if v != 0}
    return q, rem

# ---------- fields on the cell (Z/l)^d ----------
class Cell:
    def __init__(self, d, l, ztail):
        self.d, self.l = d, l
        self.ztail = ztail          # numeric twists for directions 2..d-1 (0-based)
        self.U = list(product(range(l), repeat=d))
    def zero(self):
        return {u: {} for u in self.U}
    def shift(self, u, mu):
        v = list(u); v[mu] = (v[mu] + 1) % self.l; return tuple(v)
    def D(self, g, mu):
        out = {}
        for u in self.U:
            h = g[self.shift(u, mu)]
            if u[mu] == self.l - 1:
                h = pmulvar(h, mu) if mu < 2 else pscale(h, self.ztail[mu - 2])
            out[u] = padd(h, g[u], -1)
        return out
    def sigma(self, g, mu):
        out = {}
        for u in self.U:
            s = {}
            for i in range(self.l):
                v = list(u); v[mu] = i
                s = padd(s, g[tuple(v)])
            out[u] = s
        return out
    def theta(self, g, mu):
        out = {}
        for u in self.U:
            s = {}
            for i in range(u[mu]):
                v = list(u); v[mu] = i
                s = padd(s, g[tuple(v)])
            out[u] = s
        return out
    def curl(self, b):
        return {(a, c): {u: padd(self.D(b[c], a)[u], self.D(b[a], c)[u], -1) for u in self.U}
                for a, c in combinations(range(self.d), 2)}

def fld_eq(f, g, U):
    return sum(1 for u in U if padd(f[u], g[u], -1))

def Fget(F, a, b, U):
    if a < b: return F[(a, b)]
    return {u: pscale(F[(b, a)][u], -1) for u in U}

def tu3(C, F, mode="spread"):
    """Run TU-3. Returns dict of counts."""
    U, d, l = C.U, C.d, C.l
    res = {"rem": 0, "phi": 0, "tu2i": 0, "dmu": 0, "eqn": 0, "closed": 0}
    # closedness of input
    for a, b, c in combinations(range(d), 3):
        t1 = C.D(Fget(F, b, c, U), a); t2 = C.D(Fget(F, a, c, U), b); t3 = C.D(Fget(F, a, b, U), c)
        res["closed"] += sum(1 for u in U if padd(padd(t1[u], t2[u], -1), t3[u]))
    Om = {b: {u: peval1(v, 0) for u, v in C.sigma(F[(0, b)], 0).items()} for b in range(1, d)}
    s2 = C.sigma(Om[1], 1)
    phi = {u: peval1(v, 1) for u, v in s2.items()}
    res["phi"] = sum(1 for u in U if phi[u])
    for b, c in combinations(range(1, d), 2):
        res["tu2i"] += fld_eq(C.D(Om[c], b), C.D(Om[b], c), U)
    q2 = {}
    for u in U:
        q, r = pdivZm1(s2[u], 1)
        if r: res["rem"] += 1
        q2[u] = q
    th2 = C.theta(Om[1], 1)
    mu = {u: padd(th2[u], q2[u]) for u in U}
    for b in range(1, d):
        res["dmu"] += fld_eq(C.D(mu, b), Om[b], U)
    if mode == "spread":
        b1 = {u: pscale(mu[u], Fr(-1, l)) for u in U}
    elif mode == "concentrated":
        b1 = {u: (pscale(mu[u], -1) if u[0] == 0 else {}) for u in U}
    else:
        b1 = C.zero()
    bb = {0: b1}
    for b in range(1, d):
        Db1 = C.D(b1, b)
        G = {u: padd(F[(0, b)][u], Db1[u]) for u in U}
        sG = C.sigma(G, 0)
        thG = C.theta(G, 0)
        out = {}
        for u in U:
            q, r = pdivZm1(sG[u], 0)
            if r: res["rem"] += 1
            out[u] = padd(thG[u], q)
        bb[b] = out
    cu = C.curl(bb)
    for key in cu:
        res["eqn"] += fld_eq(cu[key], F[key], U)
    return res

def rand_poly(rng):
    p = {}
    for k in ((0, 0), (1, 0), (0, 1), (1, 1)):
        v = Fr(rng.randint(-3, 3), rng.randint(1, 4))
        if v: p[k] = v
    return p

def main():
    rng = random.Random(5555)
    zchoices = [Fr(5, 4), Fr(3, 7), Fr(7, 5), Fr(1)]
    tot = {"rem": 0, "phi": 0, "tu2i": 0, "dmu": 0, "eqn": 0, "closed": 0}
    c1_fired = False
    c4 = {"rem": 0, "eqn": 0}
    saved = {}
    print("d l  ztail            rem phi tu2i dmu eqn closed | noB1-rem | conc-rem conc-eqn")
    for d in (3, 4):
        for l in (2, 3):
            for inst in range(6):
                ztail = [rng.choice(zchoices) for _ in range(d - 2)]
                C = Cell(d, l, ztail)
                a = [{u: rand_poly(rng) for u in C.U} for _ in range(d)]
                F = C.curl(a)
                r = tu3(C, F, "spread")
                r0 = tu3(C, F, "none")
                rc = tu3(C, F, "concentrated")
                for k in tot: tot[k] += r[k]
                if r0["rem"] > 0: c1_fired = True
                c4["rem"] += rc["rem"]; c4["eqn"] += rc["eqn"]
                if inst == 0: saved[(d, l)] = (C, F)
                print(f"{d} {l}  {str([str(z) for z in ztail]):16s} {r['rem']:3d} {r['phi']:3d} {r['tu2i']:4d} {r['dmu']:3d} {r['eqn']:3d} {r['closed']:6d} | {r0['rem']:8d} | {rc['rem']:8d} {rc['eqn']:8d}")
    print("TOTALS (spread):", tot)
    # C2: d = 2 counterexample to the d >= 3 clause
    c2_fired = True
    for l in (2, 3):
        C = Cell(2, l, [])
        F = {(0, 1): {u: (P(1) if u[0] == l - 1 else {}) for u in C.U}}
        Om1 = {u: peval1(v, 0) for u, v in C.sigma(F[(0, 1)], 0).items()}
        phi = {u: peval1(v, 1) for u, v in C.sigma(Om1, 1).items()}
        vals = sorted({str(phi[u].get((0, 0), 0)) for u in C.U})
        print(f"C2 d=2 l={l}: Phi values {vals}")
        if all(not phi[u] for u in C.U): c2_fired = False
    # C3: non-closed perturbation
    c3_fired = True
    for d in (3, 4):
        C, F = saved[(d, 2)]
        Fp = {k: dict(v) for k, v in F.items()}
        o = tuple([0] * d)
        Fp[(0, 1)][o] = padd(Fp[(0, 1)][o], P(1))
        r = tu3(C, Fp, "spread")
        print(f"C3 d={d} l=2 perturbed: {r}")
        if not (r["phi"] or r["rem"] or r["eqn"]): c3_fired = False
    okR = tot["rem"] == 0
    okB = tot["phi"] == 0 and tot["tu2i"] == 0 and tot["dmu"] == 0
    okA = tot["eqn"] == 0 and tot["closed"] == 0
    print(f"r55u_2-R (all divisions exact): {'PASS' if okR else 'FAIL'}")
    print(f"r55u_2-B (Phi == 0, TU-2(i), D mu = Omega): {'PASS' if okB else 'FAIL'}")
    print(f"r55u_2-A (D∧b == F): {'PASS' if okA else 'FAIL'}")
    print(f"r55u_2-C1 (b_1 omitted -> nonzero remainder somewhere): {'FIRED as designed' if c1_fired else 'DID NOT FIRE'}")
    print(f"r55u_2-C2 (d = 2 -> Phi != 0): {'FIRED as designed' if c2_fired else 'DID NOT FIRE'}")
    print(f"r55u_2-C3 (non-closed -> detected): {'FIRED as designed' if c3_fired else 'DID NOT FIRE'}")
    print(f"r55u_2-C4 (concentrated b_1, reporting): remainders {c4['rem']}, equation discrepancies {c4['eqn']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
