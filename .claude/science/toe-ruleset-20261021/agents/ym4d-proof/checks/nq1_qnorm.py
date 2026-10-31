#!/usr/bin/env python3
"""checks/nq1_qnorm.py -- exact row norms ||Q^j||_{inf->inf} for Setting SC's Q.

Criteria pre-registered in checks/nq1_criteria.md (written before this script).
Exact integer arithmetic (common denominator (d!*L^d)^j = 1944^j), reported as
Fractions.  Plain python, one process, no numpy, no BLAS, no numeric lock.

Q = Q_root, the linearised S4' root map of PROOF.md L3g(a)-slice / LINEAR_PACKAGE
section 1.2:
    Q A(X,mu) = avg_{sigma,y in B(X)} [ int_{P^sigma(c_X->y)} A
                                      + sum_{m<L} A_mu(y+m e_mu)
                                      - int_{P^sigma(c_Y->y+L e_mu)} A ]
with B(X) the centred L^d block at c_X = L*X, P^sigma the complete-axial path
taking the coordinates in the order sigma, and c_Y = c_X + L e_mu.

Q^j := Q_{j-1} o ... o Q_0 : level-0 1-forms -> level-j 1-forms, built ONE LEVEL
AT A TIME by translating the one-level row pattern (nothing of size L^{dj} is
ever formed).

Control: the same code path with Q := Q_str (the straight average), weight d!
per (y,m) so that the denominator is the same 1944.
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import permutations, product

L = 3
D = 4
HALF = (L - 1) // 2
ORDERS = list(permutations(range(D)))
NORD = len(ORDERS)                 # d! = 24
NBLK = L ** D                      # L^d = 81
DEN1 = NORD * NBLK                 # 1944

# ---- key packing: linear in the coordinates, so a translation is an integer add
S = 1024
COFF = 256                         # decode offset; needs |x_i| < COFF


def pack(x, nu):
    return ((((x[0] * S + x[1]) * S + x[2]) * S + x[3]) << 2) + nu


def pdelta(t):
    return (((t[0] * S + t[1]) * S + t[2]) * S + t[3]) << 2


BASEK = pack((COFF, COFF, COFF, COFF), 0)


def unpack(key):
    k = key + BASEK
    nu = k & 3
    k >>= 2
    x3 = (k % S) - COFF
    k //= S
    x2 = (k % S) - COFF
    k //= S
    x1 = (k % S) - COFF
    k //= S
    x0 = (k % S) - COFF
    return (x0, x1, x2, x3), nu


OUT = []


def say(s):
    OUT.append(s)
    print(s)
    sys.stdout.flush()


# ---------------------------------------------------------------- building rows
def add_path(acc, base, o, sigma, sign):
    """Axial path from base to base+o, coordinates taken in the order sigma.

    A step in the + direction traverses the link at the current site with
    coefficient +sign; a step in the - direction traverses the link one site
    back with coefficient -sign.
    """
    cur = list(base)
    for nu in sigma:
        step = o[nu]
        if step > 0:
            for t in range(step):
                p = list(cur)
                p[nu] = cur[nu] + t
                k = pack(p, nu)
                acc[k] = acc.get(k, 0) + sign
            cur[nu] += step
        elif step < 0:
            for t in range(1, -step + 1):
                p = list(cur)
                p[nu] = cur[nu] - t
                k = pack(p, nu)
                acc[k] = acc.get(k, 0) - sign
            cur[nu] += step


def q_root_pattern(mu):
    """One-level row of Q_root for the link (X=0, mu), numerators over DEN1."""
    acc = {}
    far = [0] * D
    far[mu] = L
    for sigma in ORDERS:
        for o in product(range(-HALF, HALF + 1), repeat=D):
            add_path(acc, (0, 0, 0, 0), o, sigma, +1)
            site = list(o)
            for m in range(L):
                site[mu] = o[mu] + m
                k = pack(site, mu)
                acc[k] = acc.get(k, 0) + 1
            add_path(acc, far, o, sigma, -1)
    return {k: v for k, v in acc.items() if v != 0}


def q_str_pattern(mu):
    """One-level row of Q_str for (X=0, mu), numerators over the same DEN1."""
    acc = {}
    for o in product(range(-HALF, HALF + 1), repeat=D):
        site = list(o)
        for m in range(L):
            site[mu] = o[mu] + m
            k = pack(site, mu)
            acc[k] = acc.get(k, 0) + NORD
    return {k: v for k, v in acc.items() if v != 0}


def h_pattern():
    """Row of h for the level-(i+1) site X=0, numerators over DEN1."""
    acc = {}
    for sigma in ORDERS:
        for o in product(range(-HALF, HALF + 1), repeat=D):
            add_path(acc, (0, 0, 0, 0), o, sigma, +1)
    return {k: v for k, v in acc.items() if v != 0}


def translate(row, t):
    dk = pdelta(t)
    return {k + dk: v for k, v in row.items()}


def row_sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}


# ---------------------------------------------------------------- composition
def compose(pats, j, mu, tag):
    """Row of Q^j for the level-j link (0, mu); numerators over DEN1**j."""
    plist = [list(pats[nu].items()) for nu in range(D)]
    cur = {pack((0, 0, 0, 0), mu): 1}
    for step in range(j):
        t0 = time.time()
        new = {}
        nget = new.get
        for key, coef in cur.items():
            x, nu = unpack(key)
            dk = pdelta((L * x[0], L * x[1], L * x[2], L * x[3]))
            for pk, w in plist[nu]:
                k2 = pk + dk
                new[k2] = nget(k2, 0) + coef * w
        cur = {k: v for k, v in new.items() if v != 0}
        say("      %s mu=%d level %d->%d : %d nonzero entries (%.1fs)"
            % (tag, mu, j - step, j - step - 1, len(cur), time.time() - t0))
    return cur


def l1(row, j):
    return Fr(sum(abs(v) for v in row.values()), DEN1 ** j)


def dirsums(row, j):
    s = [0] * D
    for k, v in row.items():
        s[k & 3] += v
    return [Fr(v, DEN1 ** j) for v in s]


def apply_field(row, j, f):
    tot = 0
    for k, v in row.items():
        x, nu = unpack(k)
        tot += v * f(x, nu)
    return Fr(tot, DEN1 ** j)


# ---------------------------------------------------------------- gates
def gate_G1(qpats, spats):
    ok = True
    hp = h_pattern()
    for mu in range(D):
        t = [0] * D
        t[mu] = L
        dh = row_sub(translate(hp, t), hp)
        diff = row_sub(qpats[mu], row_sub(spats[mu], dh))
        say("  G1 mu=%d : entries of Q - (Q_str - d h) = %d" % (mu, len(diff)))
        ok &= (len(diff) == 0)
    say("  G1 %s  (slice identity Q_root = Q_str - d h)" % ("PASS" if ok else "FAIL"))
    return ok


def lam(x):
    return 7 * x[0] - 3 * x[1] + 2 * x[2] + 5 * x[3] + x[0] * x[0] - 2 * x[1] * x[3]


def dlam(x, nu):
    y = list(x)
    y[nu] += 1
    return lam(y) - lam(x)


def main():
    t_start = time.time()
    jmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    JS = tuple(range(1, jmax + 1))
    say("nq1  L=%d d=%d  orders=%d block=%d  denominator per level = %d  jmax=%d"
        % (L, D, NORD, NBLK, DEN1, jmax))
    qpats = {mu: q_root_pattern(mu) for mu in range(D)}
    spats = {mu: q_str_pattern(mu) for mu in range(D)}
    for mu in range(D):
        say("  pattern sizes mu=%d : Q_root %d links, Q_str %d links"
            % (mu, len(qpats[mu]), len(spats[mu])))
    ok = gate_G1(qpats, spats)

    g2 = g3 = g4 = g5 = True
    res = {}
    for j in JS:
        vals = []
        for mu in range(D):
            row = compose(qpats, j, mu, "Q_root")
            n = l1(row, j)
            ds = dirsums(row, j)
            # G2: constant reproduction
            for nu0 in range(D):
                want = Fr(L ** j) if nu0 == mu else Fr(0)
                if ds[nu0] != want:
                    g2 = False
                    say("  G2 FAIL j=%d mu=%d nu0=%d : got %s want %s"
                        % (j, mu, nu0, ds[nu0], want))
            # G3: pure-gauge covariance
            got = apply_field(row, j, dlam)
            far = [0] * D
            far[mu] = L ** j
            want = Fr(lam(far) - lam((0, 0, 0, 0)))
            if got != want:
                g3 = False
                say("  G3 FAIL j=%d mu=%d : got %s want %s" % (j, mu, got, want))
            vals.append(n)
            say("  Q_root j=%d mu=%d : max_b-sum = %s = %.6f   support %d links"
                % (j, mu, n, float(n), len(row)))
            del row
        if len(set(vals)) != 1:
            g5 = False
            say("  G5 FAIL j=%d : direction-dependent values %s" % (j, vals))
        res[j] = vals[0]
        # G4: straight-average control (one direction suffices; all four checked at j=1)
        mus = range(D) if j == 1 else (0,)
        for mu in mus:
            rs = compose(spats, j, mu, "Q_str")
            ns = l1(rs, j)
            neg = sum(1 for v in rs.values() if v < 0)
            if ns != Fr(L ** j) or neg != 0:
                g4 = False
                say("  G4 FAIL j=%d mu=%d : %s (want %d), %d negative entries"
                    % (j, mu, ns, L ** j, neg))
            else:
                say("  G4 ok  Q_str j=%d mu=%d : %s = L^j, all entries >= 0"
                    % (j, mu, ns))
            del rs
    say("  G2 %s  (constant reproduction Q^j const = L^j const)" % ("PASS" if g2 else "FAIL"))
    say("  G3 %s  (pure-gauge covariance Q^j d = d ev^j)" % ("PASS" if g3 else "FAIL"))
    say("  G4 %s  (straight-average control = L^j exactly)" % ("PASS" if g4 else "FAIL"))
    say("  G5 %s  (direction invariance)" % ("PASS" if g5 else "FAIL"))

    say("")
    say("RESULT  n_j := max_c sum_b |Q^j(c,b)|   (exact; Q = Q_root of Setting SC)")
    prev = None
    incs = []
    Rs = {}
    for j in JS:
        n = res[j]
        R = n / Fr(L ** j)
        Rs[j] = R
        say("  j=%d : n_j = %s = %.6f ;  L^j = %d ;  p_L^j = %d ;  R_j = n_j/L^j = %s = %.6f"
            % (j, n, float(n), L ** j, 11 ** j, R, float(R)))
        if prev is not None:
            incs.append(R - prev)
        prev = R
    for i, v in enumerate(incs):
        say("  increment R_%d-R_%d = %s = %.6f" % (i + 2, i + 1, v, float(v)))

    pL_over_L = Fr(11, 3)
    if 3 not in Rs:
        say("STAGED RUN jmax=%d : no verdict (the pre-registered verdicts need j=1,2,3)" % jmax)
        say("SUMMARY staged wall %.1fs" % (time.time() - t_start))
        return
    bounded = all(Rs[j] <= pL_over_L for j in (1, 2, 3)) and incs[1] <= incs[0]
    polynomial = (any(Rs[j] > pL_over_L for j in (1, 2, 3))
                  and incs[0] != 0
                  and Fr(1, 2) <= incs[1] / incs[0] <= Fr(2))
    crude = Rs[3] >= Fr(1, 2) * pL_over_L ** 3
    say("")
    say("VERDICTS (pre-registered in checks/nq1_criteria.md)")
    say("  nq1-1 BOUNDED    : %s" % ("FIRES" if bounded else "does not fire"))
    say("  nq1-2 POLYNOMIAL : %s" % ("FIRES" if polynomial else "does not fire"))
    say("  nq1-3 CRUDE      : %s" % ("FIRES" if crude else "does not fire"))
    say("  nq1-4 OTHER      : %s"
        % ("FIRES" if not (bounded or polynomial or crude) else "does not fire"))
    gates = ok and g2 and g3 and g4 and g5
    say("  GATES G1-G5      : %s" % ("ALL PASS" if gates else "FAIL -- verdicts VOID"))
    say("SUMMARY gates=%s bounded=%s polynomial=%s crude=%s  wall %.1fs"
        % (gates, bounded, polynomial, crude, time.time() - t_start))


if __name__ == "__main__":
    main()
