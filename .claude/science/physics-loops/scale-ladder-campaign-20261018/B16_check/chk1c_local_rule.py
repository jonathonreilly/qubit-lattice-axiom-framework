"""B16 check, item 1c: exact LOCAL characterisation of closing timings (position-dependent, corner-supported).

Hand-derived rule (proof sketch in REPORT): with corner-supported smearings, the coefficient of a DIAGONAL
lapse pair (s,t) of plaquette p is  sum_{l in dp} sigma E_l F_p (w_ps u_lt - u_ls w_pt); different l give
independent monomials and a diagonal pair lies in only one plaquette, so closure (bond support) holds iff for
every l in dp:  u_ls w_pt = 0 whenever t is opposite to s.  Equivalently: with U_p = union of the supports
of p's four links, the plaquette weight must sit on corners whose OPPOSITE corner is not in U_p
(so U_p must miss at least one corner).  Gauss cannot help (an E-combination on one plaquette's links is
never a gradient-combination ... checked here numerically mod Gauss too).

C1e  random position-dependent timings obeying the rule: bond-supported exactly (L=4, 40 samples).
C1f  random timings violating the rule at >= 1 plaquette: NOT bond-supported, also mod Gauss (40 samples).
C1g  consequence: translation-invariant timings must be one-sided on every axis (a two-sided axis i covers all
     4 corners of every (i,j) plaquette) -> the 8 B16 classes; the rule admits reflection-symmetric
     NON-translation-invariant timings (e.g. the staggered one of C1d).
C2i  diagnosis of the staggered generator: block-average (2x2x2, removes the (-1)^x doubler modes) of
     delta_xi F - L_xi F converges, while the unaveraged error stays O(1): the staggered G' = L_xi + O(1) staggered
     (doubler) component -> it is not a consistent lattice relabelling at the lattice scale.
"""
from fractions import Fraction as Fr
import random

import numpy as np

from chk_lat import Lat, em_pair_coeffs
from chk1_timing import bondsupport, staggered
from chk1b_induced_generator import induced_generator

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


OPP = {"00": "11", "11": "00", "10": "01", "01": "10"}


def plaq_ok(lat, u, p):
    cs = lat.corners(p)
    inv = {v: k for k, v in cs.items()}
    U = {inv[s] for a in lat.Fp[p] for s in u[a]}
    return [n for n in cs if OPP[n] not in U]


def random_timing(lat, rng, obey=True, sweeps=6):
    """MCMC over link supports starting from a valid one-sided class, keeping every plaquette admissible;
    then random admissible plaquette weights."""
    o = [rng.choice("th") for _ in range(3)]
    u = [{x: Fr(1)} if o[j] == "t" else {lat.sh(x, j): Fr(1)} for (x, j) in lat.links]
    for _ in range(sweeps * len(lat.links)):
        k = rng.randrange(len(lat.links))
        x, j = lat.links[k]
        y = lat.sh(x, j)
        ch = rng.choice(["t", "h", "b"])
        a = Fr(rng.randint(1, 3), 4)
        new = {x: Fr(1)} if ch == "t" else ({y: Fr(1)} if ch == "h" else {x: a, y: 1 - a})
        old = u[k]
        u[k] = new
        if not all(plaq_ok(lat, u, p) for (p, s) in lat.inc[k]):
            u[k] = old
    w = []
    for p in range(len(lat.plaqs)):
        cs = lat.corners(p)
        allowed = plaq_ok(lat, u, p)
        pick = rng.sample(allowed, rng.randint(1, len(allowed)))
        wt = [Fr(rng.randint(1, 4)) for _ in pick]
        tot = sum(wt)
        w.append({cs[n]: v / tot for n, v in zip(pick, wt)})
    nboth = sum(len(d) == 2 for d in u)
    return u, w, nboth


def c1ef():
    lat = Lat(4)
    P = lat.transverse_projector()
    rng = random.Random(11)
    ok_n = 0
    both_tot = 0
    tried = 0
    while ok_n < 40 and tried < 5000:
        tried += 1
        u_, w_, nboth = random_timing(lat, rng, True)
        nb, _ = bondsupport(lat, u_, w_)
        ok_n += 1
        both_tot = both_tot + nboth if ok_n > 1 else nboth
        if nb:
            check("C1e", False, "rule-obeying timing not bond-supported")
            return
    check("C1e", ok_n == 40, f"40 random position-dependent timings obeying the local rule (MCMC; mean {both_tot / 40:.1f} two-sided links per sample): all exactly bond-supported")
    bad_n, fails = 0, 0
    tried = 0
    while bad_n < 40 and tried < 5000:
        tried += 1
        # violate at one random plaquette only: start from obeying, then add a forbidden corner at one plaquette
        u, w, _ = random_timing(lat, rng, True, sweeps=2)
        p = rng.randrange(len(lat.plaqs))
        cs = lat.corners(p)
        inv = {v: k for k, v in cs.items()}
        U = {inv[s] for a in lat.Fp[p] for s in u[a]}
        bad = [n for n in cs if OPP[n] in U]
        if not bad:
            continue
        n = rng.choice(bad)
        w[p] = dict(w[p])
        w[p] = {k: v / 2 for k, v in w[p].items()}
        w[p][cs[n]] = w[p].get(cs[n], 0) + Fr(1, 2)
        nbg, _ = bondsupport(lat, u, w, True, P)
        bad_n += 1
        fails += nbg > 0
    check("C1f", bad_n == 40 and fails == 40, f"40 timings violating the rule at a single plaquette: all fail bond support even mod Gauss ({fails}/40)")


def c1g():
    # translation invariant with a two-sided axis i: every (i,j) plaquette has U_p = all corners -> no allowed corner
    lat = Lat(4)
    ok = True
    for i in range(3):
        for other in ("t", "h"):
            # axis i both, others `other`
            u = []
            for (x, j) in lat.links:
                y = lat.sh(x, j)
                if j == i:
                    u.append({x: Fr(1, 2), y: Fr(1, 2)})
                else:
                    u.append({x: Fr(1)} if other == "t" else {y: Fr(1)})
            for p, (y0, (a, b)) in enumerate(lat.plaqs):
                if i in (a, b):
                    cs = lat.corners(p)
                    inv = {v: k for k, v in cs.items()}
                    U = {inv[s] for aa in lat.Fp[p] for s in u[aa]}
                    ok &= len(U) == 4
    check("C1g", ok, "translation-invariant timing with any two-sided axis i: every (i,j) plaquette has U_p = all 4 corners, so no admissible plaquette weight -> only the 8 one-sided classes (agrees with C1b)")


def c2i():
    from chk2_cone import lie_test  # noqa: F401  (re-implemented below with block averaging)
    import chk2_cone as c2
    errs = []
    for L in (8, 12, 16, 20):
        lat = Lat(L)
        u, w = staggered(lat, 0)
        X = induced_generator(lat, u, w, Fr(1))
        raw, blk = lie_test_blocks(lat, X)
        errs.append((L, raw, blk))
        print(f"    STAG L={L}: raw rel. error {raw:.4e}, 2^3-block-averaged rel. error {blk:.4e}")
    sl = np.polyfit(np.log([e[0] for e in errs]), np.log([e[2] for e in errs]), 1)[0]
    print(f"    block-averaged slope {sl:.2f}")
    check("C2i", errs[-1][1] > 0.5 and errs[-1][2] < 0.2 * errs[-1][1] and sl < -0.5,
          "staggered generator: smooth (block-averaged) part converges to L_xi F, but an O(1) staggered (doubler) component remains pointwise")


def lie_test_blocks(lat, X):
    import chk2_cone as c2
    L = lat.L
    tp = 2 * np.pi / L
    def Acont(j, r):
        x, y, z = r
        return [np.sin(tp * y) + 0.5 * np.cos(tp * z + 0.3), np.cos(tp * (x + 0.2)) * np.sin(tp * z), 0.7 * np.sin(tp * (x - y))][j]
    def xic(i, r):
        x, y, z = r
        return [1.0 + 0.5 * np.sin(tp * z), 0.3 * np.cos(tp * x), 0.4 * np.sin(tp * y + 0.1)][i]
    A = np.zeros(len(lat.links))
    for k, (x, j) in enumerate(lat.links):
        r = np.array(x, float); r[j] += 0.5
        A[k] = Acont(j, r)
    xi = {}
    for x in lat.sites:
        for i in range(3):
            r = np.array(x, float); r[i] += 0.5
            xi[(x, i)] = xic(i, r)
    dA = np.zeros(len(lat.links))
    for b, d in X.items():
        for (k, a), v in d.items():
            dA[k] += xi[b] * float(v) * A[a]
    dF = np.array([sum(s * dA[a] for a, s in fp.items()) for fp in lat.Fp])
    h = 1e-4
    def Fc(i, j, r):
        def dA_(jj, kk):
            e = np.zeros(3); e[kk] = h
            return (Acont(jj, r + e) - Acont(jj, r - e)) / (2 * h)
        return dA_(j, i) - dA_(i, j)
    exact = np.zeros(len(lat.plaqs))
    for p, (y, (i, j)) in enumerate(lat.plaqs):
        r = np.array(y, float); r[i] += 0.5; r[j] += 0.5
        def dF_(ii, jj, kk):
            e = np.zeros(3); e[kk] = h
            return (Fc(ii, jj, r + e) - Fc(ii, jj, r - e)) / (2 * h)
        def dxi(m, kk):
            e = np.zeros(3); e[kk] = h
            return (xic(m, r + e) - xic(m, r - e)) / (2 * h)
        exact[p] = sum(xic(k, r) * dF_(i, j, k) for k in range(3)) + sum(Fc(k, j, r) * dxi(k, i) + Fc(i, k, r) * dxi(k, j) for k in range(3))
    raw = np.linalg.norm(dF - exact) / np.linalg.norm(exact)
    # block average over 2x2x2 blocks per orientation
    def blockavg(v):
        out = {}
        cnt = {}
        for p, (y, ij) in enumerate(lat.plaqs):
            key = (tuple(c // 2 for c in y), ij)
            out[key] = out.get(key, 0) + v[p]
            cnt[key] = cnt.get(key, 0) + 1
        return np.array([out[k] / cnt[k] for k in sorted(out)])
    bd, be = blockavg(dF), blockavg(exact)
    return raw, np.linalg.norm(bd - be) / np.linalg.norm(be)


if __name__ == "__main__":
    c1ef()
    c1g()
    c2i()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
