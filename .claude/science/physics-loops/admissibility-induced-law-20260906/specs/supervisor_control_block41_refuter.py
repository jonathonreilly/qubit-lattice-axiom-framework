#!/usr/bin/env python3
"""Block 41 refuting pass: machinery disjoint from the runner's (site-level enumeration on general graphs, no transfer vectors).

W1  two clusters on a 2 x 5 window separated by an empty column: weight = product, contents independent (T2)
W2  the 2 x 4 periodic ladder by enumeration of all 7^8 site states against the runner's transfer-matrix g(r) (T3)
W3  the symmetry lemma on the occupied 2 x 3 window at (12,1,2), every pair of sites (T4)
W4  a rule whose weights depend on the direction of the bond: a record of unread content is surrounded by a radial content field (the limit of T4)
W5  closure of the mean on the 3 x 3 torus for symmetric transit with an arbitrary initial law; failure with glue; equality on arrangements of isolated records (T5)
W6  the production mean at (5,2,3) next to four records, by the row sums (T5)
W7  block 01's reading (ii): an empty neighbour's direction-dependent factor carries no action across a gap (T2 survives)
Exact arithmetic only.
"""
import importlib.util
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
RUNNER = ROOT / "scripts" / "admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_screened_density_signed_tilt_2026_09_20.py"
AX = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]


def om(p, q, r):
    return [[p if a == b else q if tuple(-t for t in AX[a]) == AX[b] else r for b in range(6)] for a in range(6)]


def graph_weight(bonds, cfg, w):
    """cfg: tuple with None for empty; w: 6x6 weights"""
    t = Fraction(1)
    for (i, j) in bonds:
        if cfg[i] is not None and cfg[j] is not None:
            t *= w[cfg[i]][cfg[j]]
    return t


fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ---------------------------------------------------------------- W1
def w1():
    cols, rows = 5, 2
    idx = {(i, j): i * cols + j for i in range(rows) for j in range(cols)}
    bonds = [(idx[i, j], idx[i, j + 1]) for i in range(rows) for j in range(cols - 1)] + [(idx[0, j], idx[1, j]) for j in range(cols)]
    ok = True
    for c in (Fraction(2, 7), Fraction(1), Fraction(3)):
        w = [[c * v for v in row] for row in om(12, 1, 2)]
        left = [idx[0, 0], idx[1, 0], idx[0, 1], idx[1, 1]]          # a 2 x 2 block (one cycle)
        right = [idx[0, 3], idx[1, 3], idx[0, 4]]                      # three records, column 2 empty
        def total(sites):
            s = Fraction(0)
            for vals in product(range(6), repeat=len(sites)):
                cfg = [None] * (rows * cols)
                for k, site in enumerate(sites):
                    cfg[site] = vals[k]
                s += graph_weight(bonds, cfg, w)
            return s
        ok = ok and total(left + right) == total(left) * total(right)
    report("W1", ok, "a 2 x 2 block and three records on a 2 x 5 window with an empty column between them: the weight is the product of the two weights at three scales")


# ---------------------------------------------------------------- W2
def w2():
    spec = importlib.util.spec_from_file_location("runner41", RUNNER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rho_t, g_t = mod.ladder_pair_correlation(12, 1, 2, Fraction(2, 7), Fraction(1, 12), length=4)
    n = 8                                                           # site k = 2 j + i
    bonds = [(2 * j, 2 * j + 1) for j in range(4)] + [(2 * j + i, 2 * ((j + 1) % 4) + i) for j in range(4) for i in (0, 1)]
    adj = {k: [] for k in range(n)}
    for (a, b) in bonds:
        adj[max(a, b)].append(min(a, b))
    o = om(12, 1, 2)
    # integer sums of omega-products by (records, record-record bonds), for the total and for the pairs (0, 2 d)
    tot, pair = {}, {1: {}, 2: {}}
    cfg = [None] * n

    def rec(k, nrec, nb, wprod):
        if k == n:
            key = (nrec, nb)
            tot[key] = tot.get(key, 0) + wprod
            if cfg[0] is not None:
                for d in (1, 2):
                    if cfg[2 * d] is not None:
                        pair[d][key] = pair[d].get(key, 0) + wprod
            return
        cfg[k] = None
        rec(k + 1, nrec, nb, wprod)
        for v in range(6):
            cfg[k] = v
            t, m = wprod, nb
            for j in adj[k]:
                if cfg[j] is not None:
                    t *= o[v][cfg[j]]
                    m += 1
            rec(k + 1, nrec + 1, m, t)
        cfg[k] = None

    rec(0, 0, 0, 1)
    z, c = Fraction(1, 12), Fraction(2, 7)
    val = lambda d: sum(z ** k[0] * c ** k[1] * v for k, v in d.items())
    Z = val(tot)
    one = {}
    # density by symmetry: every site equivalent; count of records / 8
    rho = sum(k[0] * z ** k[0] * c ** k[1] * v for k, v in tot.items()) / Z / n
    ok = rho == rho_t and all(val(pair[d]) / Z / rho ** 2 - 1 == g_t[d] for d in (1, 2))
    report("W2", ok, f"the periodic 2 x 4 ladder by enumeration of all 7^8 site states: density and g(1), g(2) equal the runner's transfer-matrix values exactly (g(1) - 1 = {(g_t[1]).numerator * 10 ** 6 // (g_t[1]).denominator}/10^6)")


# ---------------------------------------------------------------- W3, W4
def content_field(bonds, nsites, w, x, y, given, site_factor=None):
    num = [Fraction(0)] * 3
    den = Fraction(0)
    for vals in product(range(6), repeat=nsites):
        if given is not None and vals[x] != given:
            continue
        t = graph_weight(bonds, vals, w)
        if site_factor:
            t *= site_factor(vals)
        den += t
        for k in range(3):
            num[k] += t * AX[vals[y]][k]
    return [v / den for v in num]


def w3():
    cols, rows = 3, 2
    idx = {(i, j): i * cols + j for i in range(rows) for j in range(cols)}
    bonds = [(idx[i, j], idx[i, j + 1]) for i in range(rows) for j in range(cols - 1)] + [(idx[0, j], idx[1, j]) for j in range(cols)]
    w = om(12, 1, 2)
    ok = True
    for x in range(6):
        for y in range(6):
            if x == y:
                continue
            coefs = set()
            for a in range(6):
                f = content_field(bonds, 6, w, x, y, a)
                nz = [k for k in range(3) if AX[a][k]][0]
                ok = ok and all(f[k] == 0 for k in range(3) if k != nz)
                coefs.add(f[nz] * AX[a][nz])
            ok = ok and len(coefs) == 1
            ok = ok and all(v == 0 for v in content_field(bonds, 6, w, x, y, None))
    report("W3", ok, "the occupied 2 x 3 window at (12,1,2): for all 30 ordered pairs of sites the content field at y given the content a at x is one coefficient times the vector of a, and zero when the content at x is not read")


def w4():
    # three sites on a line along +x; a bond from site i to site i+1 has direction +x = AX[2]; the weight carries a factor h for a
    # content pointing along the bond away from its own site (covariant under rotations acting on sites and contents together)
    w = om(3, 1, 2)
    def factor(vals):
        t = Fraction(1)
        for i in (0, 1):
            if AX[vals[i]] == (1, 0, 0):
                t *= 2                                  # site i points at site i + 1
            if AX[vals[i + 1]] == (-1, 0, 0):
                t *= 2                                  # site i + 1 points at site i
        return t
    f = content_field([(0, 1), (1, 2)], 3, w, 1, 2, None, site_factor=factor)
    report("W4", f[0] != 0 and f[1] == 0 and f[2] == 0, f"a rule whose weights depend on the direction of the bond (outside the declared class): the content field at a neighbour of a record of unread content is ({f[0]}, 0, 0), along the bond: the lemma of T4 needs the declared isotropic pair weight")


# ---------------------------------------------------------------- W5
def w5():
    L = 3
    sites = [(i, j) for i in range(L) for j in range(L)]
    idx = {s: k for k, s in enumerate(sites)}
    nb = {idx[i, j]: [idx[(i + 1) % L, j], idx[(i - 1) % L, j], idx[i, (j + 1) % L], idx[i, (j - 1) % L]] for (i, j) in sites}
    n = len(sites)

    def drift(glue):
        """d/dt E[n_x] under an arbitrary law mu, minus the Laplacian of E[n]; glue: rate 1 + glue * (occupied neighbours of the target)"""
        worst = Fraction(0)
        iso_ok = True
        dmean = [Fraction(0)] * n
        mean = [Fraction(0)] * n
        tot = Fraction(0)
        for eta in range(2 ** n):
            occ = [(eta >> v) & 1 for v in range(n)]
            mu = Fraction(1 + (eta * 7919) % 13, 1 + (eta * 104729) % 11)      # an arbitrary positive law
            tot += mu
            gen = [Fraction(0)] * n
            for u in range(n):
                if occ[u]:
                    for t in nb[u]:
                        if not occ[t]:
                            rate = 1 + glue * sum(occ[s] for s in nb[t] if s != u)
                            gen[u] -= rate
                            gen[t] += rate
            isolated = all(not (occ[u] and any(occ[t] for t in nb[u])) for u in range(n))
            lap = [sum(occ[y] - occ[x] for y in nb[x]) for x in range(n)]
            if glue and isolated and sum(occ) == 1:
                iso_ok = iso_ok and gen == lap
            for x in range(n):
                dmean[x] += mu * gen[x]
                mean[x] += mu * occ[x]
        res = [dmean[x] / tot - sum(mean[y] - mean[x] for y in nb[x]) / tot for x in range(n)]
        return res, iso_ok

    res0, _ = drift(0)
    res1, iso = drift(1)
    report("W5", all(v == 0 for v in res0) and any(v != 0 for v in res1) and iso, "the 3 x 3 torus, an arbitrary law on its 512 arrangements: under symmetric transit d/dt E[n_x] equals the Laplacian of E[n] at every site; with a preference for occupied neighbourhoods it does not; for a single record the two generators agree")


def w6():
    p, q, r = 5, 2, 3
    c0 = Fraction(6, p + q + 4 * r)
    w = [[c0 * v for v in row] for row in om(p, q, r)]
    rows_ok = all(sum(row) == 6 for row in w)
    k = 4
    mean = sum(Fraction(sum(w[v][b] for b in range(6)), 6) ** k for v in range(6)) / 6
    agree = sum(w[v][0] ** k for v in range(6)) / 6
    report("W6", rows_ok and mean == 1 and agree > 1, f"(5,2,3): every row of the neutral pair weight sums to 6, so the mean formation rate next to four records of independent uniform contents is the rate in the void; next to four agreeing records it is {agree} times that")


def w7():
    # block 01's reading (ii): an empty neighbour in direction d gives the record beside it a factor by the orbit of (content, d)
    w = om(3, 1, 2)
    def absent(s, d):
        dot = sum(AX[s][k] * d[k] for k in range(3))
        return Fraction(2) if dot == 1 else Fraction(3) if dot == -1 else Fraction(5)
    sites = 5
    occupied = (0, 1, 3)                                  # a pair, an empty site, a single record, an empty end
    def weight(vals, occ):
        t = Fraction(1)
        for k, i in enumerate(occ):
            for d, j in (((1, 0, 0), i + 1), ((-1, 0, 0), i - 1)):
                if 0 <= j < sites:
                    if j in occ:
                        if j > i:
                            t *= w[vals[k]][vals[occ.index(j)]]
                    else:
                        t *= absent(vals[k], d)
        return t
    total = sum(weight(v, occupied) for v in product(range(6), repeat=3))
    left = sum(weight(v, (0, 1)) for v in product(range(6), repeat=2))
    # the single record at site 3 has empty neighbours on both sides in either window
    right = sum(weight(v, (3,)) for v in product(range(6), repeat=1))
    report("W7", total == left * right, "block 01's reading (ii) with absence factors (2, 3, 5): a pair and a single record separated by one empty site weigh the product of their separate weights; the empty neighbour's factor is a one-record factor and carries no action across the gap")


if __name__ == "__main__":
    for fn in (w1, w3, w4, w5, w6, w7, w2):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
