"""rl55_1 -- exact enumeration of the soft-density patch geometry in d = 4 (criteria: rl55_1_criteria.md, written first).

Integer / Fraction arithmetic only. No floats. Prints results to stdout.
Words: BFT_A §3.4 / PROOF "Decision 4": axial path c_X -> y (axis order), L straight +mu steps, then the axial path
c_Y -> y + L e_mu (same order) traversed in reverse.
"""
from fractions import Fraction
from itertools import permutations, product
import sys

D = 4


def add(z, w):
    return tuple(a + b for a, b in zip(z, w))


def unit(nu, t=1):
    return tuple(t if i == nu else 0 for i in range(D))


def axial_path(a, b, order):
    """vertex list from a to b, moving coordinates in the given order, one unit step at a time."""
    verts = [a]
    z = list(a)
    for nu in order:
        while z[nu] != b[nu]:
            z[nu] += 1 if b[nu] > z[nu] else -1
            verts.append(tuple(z))
    return verts


def word_vertices(L, mu, order, y):
    o = (L - 1) // 2
    cX = (o,) * D
    cY = add(cX, unit(mu, L))
    leg1 = axial_path(cX, y, order)
    leg2 = [add(y, unit(mu, t)) for t in range(L + 1)]
    leg3 = list(reversed(axial_path(cY, add(y, unit(mu, L)), order)))
    verts = leg1 + leg2[1:] + leg3[1:]
    return verts


def steps_of(verts):
    out = []
    for a, b in zip(verts, verts[1:]):
        diff = tuple(bb - aa for aa, bb in zip(a, b))
        nz = [i for i in range(D) if diff[i] != 0]
        assert len(nz) == 1 and abs(diff[nz[0]]) == 1, (a, b)
        nu = nz[0]
        if diff[nu] == 1:
            out.append((a, nu, +1))
        else:
            out.append((b, nu, -1))
    return out


def all_words(L, mu, yrange):
    o = (L - 1) // 2
    cX = (o,) * D
    words = []
    for order in permutations(range(D)):
        for off in product(yrange, repeat=D):
            y = add(cX, off)
            words.append(word_vertices(L, mu, order, y))
    return words


def in_box(z, L, mu, top_mu):
    for nu in range(D):
        hi = top_mu if nu == mu else L - 1
        if not (0 <= z[nu] <= hi):
            return False
    return True


def max_l1_diam(points):
    best = 0
    pts = list(points)
    for signs in product((1, -1), repeat=D):
        vals = [sum(s * c for s, c in zip(signs, p)) for p in pts]
        best = max(best, max(vals) - min(vals))
    return best


def run_L(L, report):
    o = (L - 1) // 2
    centred = range(-o, o + 1)
    ok = {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True}
    ctrl = {"K1": False, "K2": False, "K3": False}
    used = {}       # mu -> set of (base, nu)
    occ = {}        # mu -> dict (base, nu) -> occurrence count summed over words
    nwords = {}
    Dnu_all = []
    for mu in range(D):
        words = all_words(L, mu, centred)
        nwords[mu] = len(words)
        verts_all = [v for w in words for v in w]
        # P1
        if not all(in_box(v, L, mu, 2 * L - 1) for v in verts_all):
            ok["P1"] = False
        # K2: lowered +mu face must be violated by some vertex
        if not all(in_box(v, L, mu, 2 * L - 2) for v in verts_all):
            ctrl["K2"] = True
        # P2 tightness
        mins = [min(v[i] for v in verts_all) for i in range(D)]
        maxs = [max(v[i] for v in verts_all) for i in range(D)]
        exp_max = [2 * L - 1 if i == mu else L - 1 for i in range(D)]
        if mins != [0] * D or maxs != exp_max:
            ok["P2"] = False
        # steps
        u = set()
        oc = {}
        signed = [Fraction(0)] * D
        for w in words:
            for (base, nu, sg) in steps_of(w):
                u.add((base, nu))
                oc[(base, nu)] = oc.get((base, nu), 0) + 1
                signed[nu] += sg
        used[mu] = u
        occ[mu] = oc
        # P4
        for nu in range(D):
            if signed[nu] / len(words) != (L if nu == mu else 0):
                ok["P4"] = False
        # P3: per-direction diameters and rectangle hulls
        for nu in range(D):
            bases = [b for (b, n) in u if n == nu]
            Dn = max_l1_diam(bases)
            Dnu_all.append((mu, nu, Dn))
            lo = [min(b[i] for b in bases) for i in range(D)]
            hi = [max(b[i] for b in bases) for i in range(D)]
            corner_lo = tuple(lo)
            corner_hi = tuple(hi)
            # rectangle and its e_nu shift inside Box(c)
            if not (in_box(corner_lo, L, mu, 2 * L - 1) and in_box(corner_hi, L, mu, 2 * L - 1)
                    and in_box(add(corner_hi, unit(nu)), L, mu, 2 * L - 1)):
                ok["P3"] = False
        # K1: uncentred y-range must leave the box
        words_k1 = all_words(L, mu, range(0, L))
        if not all(in_box(v, L, mu, 2 * L - 1) for w in words_k1 for v in w):
            ctrl["K1"] = True
    maxD = max(d for (_, _, d) in Dnu_all)
    if maxD > 5 * L - 4:
        ok["P3"] = False
    if maxD > 5 * L - 6:
        ctrl["K3"] = True
    # P5 incidence over a fundamental cell
    max_nc = 0
    max_nbox = 0
    max_cfreq = Fraction(0)
    for z in product(range(L), repeat=D):
        for nu in range(D):
            nc = 0
            nbox = 0
            cf = Fraction(0)
            for mu in range(D):
                rng = [range(-2, 2)] * D
                for Xp in product(*rng):
                    zz = tuple(z[i] - L * Xp[i] for i in range(D))
                    key = (zz, nu)
                    if key in used[mu]:
                        nc += 1
                        cf += Fraction(occ[mu][key], nwords[mu])
                    if in_box(zz, L, mu, 2 * L - 1) and in_box(add(zz, unit(nu)), L, mu, 2 * L - 1):
                        nbox += 1
            if nc > nbox:
                ok["P5"] = False
            max_nc = max(max_nc, nc)
            max_nbox = max(max_nbox, nbox)
            max_cfreq = max(max_cfreq, cf)
    report.append("L = %d: words per mu = %d, p_L = 5L-4 = %d" % (L, nwords[0], 5 * L - 4))
    maxlen = 0
    for mu in range(D):
        pass
    report.append("  max l1 diameter of used nu-link base points, per (mu, nu): %s" %
                  ", ".join("(%d,%d):%d" % t for t in Dnu_all))
    report.append("  max over (mu, nu) = %d  (bound 5L-4 = %d; Box l1 diameter = 5L-4)" % (maxD, 5 * L - 4))
    report.append("  incidence: max n_c = %d, max n_box = %d, max cfreq = %s" % (max_nc, max_nbox, max_cfreq))
    for g in ("P1", "P2", "P3", "P4", "P5"):
        report.append("  %s: %s" % (g, "PASS" if ok[g] else "FAIL"))
    for k in ("K1", "K2", "K3"):
        report.append("  %s: %s" % (k, "FIRES" if ctrl[k] else "DOES NOT FIRE"))
    return all(ok.values()), ctrl


def main():
    report = []
    allok = True
    fired = {"K1": True, "K2": True, "K3": True}
    for L in (3, 5):
        okL, ctrl = run_L(L, report)
        allok = allok and okL
        for k in fired:
            fired[k] = fired[k] and ctrl[k]
    for line in report:
        print(line)
    overall = allok and all(fired.values())
    print("OVERALL rl55_1: %s" % ("PASS" if overall else "FAIL"))
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
