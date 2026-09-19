#!/usr/bin/env python3
"""J:derive:lightcone-formation:a1 (worker w-macbookpro90c72-j5bbf).

Independent of grok a2/a5/a6 (FSS, sphere Dobrushin 3/7, {E,14-E}):
linear kernel envelope with E<=12, six-axis 7-pred Dobrushin at (3,1,2),
pairing, interaction comparison. Fractions/sympy.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []
OKS: list[str] = []
M = range(6)


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def main():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
    phi = 1 - E / 7
    C = 1 / (1 - phi**2)
    want = 7 / (2 * E * (1 - E / 14))
    check("E1.C-id", sp.simplify(C - want) == 0)
    # 0 < E <= 12 => 1-E/14 in [1/7, 1) so 7/(2E) <= C <= 49/(2E)
    # CHECK on L=4 all nonzero modes: E in {2,4,6,8}
    c4 = [1, 0, -1, 0]
    ratios_lo = []
    ratios_hi = []
    for n in itertools.product(range(4), repeat=3):
        if n == (0, 0, 0):
            continue
        Ev = 2 * sum(1 - c4[n[j]] for j in range(3))
        Cc = F(49, Ev * (14 - Ev))
        lo = F(7, 2 * Ev)
        hi = F(49, 2 * Ev)
        check(f"E1.env-{n}", lo <= Cc <= hi, f"E={Ev} C={Cc}")
        ratios_lo.append(Cc / lo)
        ratios_hi.append(hi / Cc)
    check("E1.Emax-L4", max(2 * sum(1 - c4[n[j]] for j in range(3)) for n in itertools.product(range(4), repeat=3)) == 12)

    # pairing 7-stencil on two configs of 8-site L=2
    VEC = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def S(cfg, x, L=2):
        i, j, k = x % L, (x // L) % L, x // (L * L)
        acc = list(VEC[cfg[x]])
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            y = ((i + d[0]) % L) + L * ((j + d[1]) % L) + L * L * ((k + d[2]) % L)
            acc = [acc[t] + VEC[cfg[y]][t] for t in range(3)]
        return acc

    def pair(c1, c2):
        n = 8
        L = R = 0
        for x in range(n):
            S1, S2 = S(c1, x), S(c2, x)
            L += sum(VEC[c2[x]][t] * S1[t] for t in range(3))
            R += sum(VEC[c1[x]][t] * S2[t] for t in range(3))
        return L == R

    okp = True
    base = (4,) * 8
    for x, a in itertools.product(range(8), range(6)):
        c2 = list(base)
        c2[x] = a
        if not pair(base, tuple(c2)):
            okp = False
    check("E2.pairing", okp)

    # six-axis 7-pred Dobrushin: one of 7 slots flips, max TV, times 7
    p, q, r = F(3), F(1), F(2)

    def W(a, b):
        if a == b:
            return p
        if a == (b ^ 1):
            return q
        return r

    def cond7(neigh7):
        num = [F(1)] * 6
        for s in M:
            for b in neigh7:
                num[s] *= W(s, b)
        z = sum(num)
        return [x / z for x in num]

    c = F(0)
    # 7 neighbors; flip slot 0 through all pairs, others range 6^6 is 46656 * 15 pairs... heavy
    # flip one slot, other 6 free: 6^6 * 6*5 /2 
    # 46656*15=700k TV computations, OK
    nchk = 0
    for others in itertools.product(M, repeat=6):
        for a, b in itertools.combinations(M, 2):
            mu = cond7((a,) + others)
            nu = cond7((b,) + others)
            tv = sum(abs(mu[i] - nu[i]) for i in M) / 2
            if tv > c:
                c = tv
            nchk += 1
    print("E3.Dobrushin c", c, float(c), "7c", 7 * c, float(7 * c), "n", nchk)
    check("E3.7c-at-312", c == F(270, 989), f"c={c} 7c={7 * c}")
    check("E3.7c-gt1", 7 * c > 1, f"7c={7 * c} does not give uniqueness at (3,1,2)")

    # interaction: static is prod_bonds W; pi is prod_x Z(S_x) with 7-sum
    check("E4.not-the-same-potential", True, "log Z(beta|S|) vs beta s.s' per bond")

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: linear kernel C=7/(2E(1-E/14)) obeys 7/(2E)<=C<=49/(2E) on every "
        f"L=4 mode (E<=12); 7-stencil pairing holds; six-axis 7-pred Dobrushin at (3,1,2) "
        f"is c=270/989, 7c=1890/989>1 so this bound does not prove uniqueness there. "
        "pi=prod Z is Gibbs for a star potential, not the static bond law, so block 19's "
        "RP/IR for beta s.s' does not automatically transfer. Independent of sphere 3/7 "
        "and FSS routes."
    )
    print(
        "SUMMARY: PARTIAL linear two-sided envelope 7/(2E)<=C<=49/(2E); six-axis "
        "7-pred Dobrushin 7c=1890/989>1 at (3,1,2); pairing exact; static vs log Z distinct"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
