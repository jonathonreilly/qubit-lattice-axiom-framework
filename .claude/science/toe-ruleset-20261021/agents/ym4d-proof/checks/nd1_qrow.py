#!/usr/bin/env python3
# checks/nd1_qrow.py  -- check nd1 for target T55-P (NQ_DEF.md).
# Criteria: checks/nd1_criteria.md, written BEFORE this file existed.
#
# Builds, from the primary definitions only, the level-0 rows of
#   Q_root   (PROOF.md "S4' [S3] Order-averaged averaging"; LINEAR_PACKAGE.md "the root map")
#   Q_str^LP (LINEAR_PACKAGE.md  (Q_strA)(X,mu) := L^-d sum_{y in B(X)} sum_{j<L} A_mu(y + j e_mu))
#   Q_str^NO (NORMS.md sec.N1 conventions: L^-(d-1) over the L^(d-1) straight paths of L links)
#   h        (PROOF.md L3g(a)-slice: h(A)(X) := avg_sigma avg_{y in B(X)} int_{P^sigma(c_X -> y)} A)
# and runs gates A,B,C,D,E with their designed-FAIL controls A',B',C',D',E'.
#
# Exact Fraction / integer arithmetic. Plain python, one process, no numpy, no BLAS, no numeric lock.
# Independent of nq1_qnorm.py and of the reviewer's revnq1/ code: nothing is imported from either.

from fractions import Fraction
from itertools import permutations, product
import sys

L = 3
D = 4
HALF = (L - 1) // 2                      # block radius; L odd  =>  root is a lattice site
BLOCK = [tuple(v) for v in product(range(-HALF, HALF + 1), repeat=D)]   # B(X) relative to c_X
ORDERS = list(permutations(range(D)))    # the d! coordinate orders sigma
NSIG = len(ORDERS)

def e(mu):
    v = [0] * D
    v[mu] = 1
    return tuple(v)

def add(p, q, s=1):
    return tuple(a + s * b for a, b in zip(p, q))

# ---------- row algebra.  A row is {(position, direction): Fraction} on level-0 links ----------

def racc(row, key, val):
    if val == 0:
        return
    n = row.get(key, 0) + val
    if n == 0:
        row.pop(key, None)
    else:
        row[key] = n

def rscale(row, c):
    return {k: v * c for k, v in row.items() if v * c != 0}

def rsub(a, b):
    out = dict(a)
    for k, v in b.items():
        racc(out, k, -v)
    return out

def radd(a, b):
    out = dict(a)
    for k, v in b.items():
        racc(out, k, v)
    return out

def rtrans(row, v):
    return {(add(p, v), nu): c for (p, nu), c in row.items()}

def rl1(row):
    return sum(abs(c) for c in row.values())

def rdiff_count(a, b):
    keys = set(a) | set(b)
    return sum(1 for k in keys if a.get(k, 0) != b.get(k, 0))

def reval_dlambda(row, lam):
    """Apply the row (a linear functional on 1-forms) to the exact 1-form d_0 lambda."""
    tot = Fraction(0)
    for (p, nu), c in row.items():
        tot += c * (lam(add(p, e(nu))) - lam(p))
    return tot

# ---------- the geometric primitives, built directly from the definitions ----------

def axial_path(start, end, sigma):
    """P^sigma(start -> end): move the coordinates in the order sigma.  Returns [(link, sign)]."""
    cur = list(start)
    out = []
    for c in sigma:
        while cur[c] < end[c]:
            out.append(((tuple(cur), c), 1))
            cur[c] += 1
        while cur[c] > end[c]:
            cur[c] -= 1
            out.append(((tuple(cur), c), -1))
    assert tuple(cur) == tuple(end)
    return out

def straight_leg(y, mu):
    """S_y: the straight leg of L steps from y to y + L e_mu."""
    return [((add(y, tuple(j * x for x in e(mu))), mu), 1) for j in range(L)]

def row_h():
    """h(A)(X) := avg_sigma avg_{y in B(X)} int_{P^sigma(c_X -> y)} A, at the coarse site anchored at 0."""
    w = Fraction(1, NSIG * (L ** D))
    row = {}
    origin = tuple([0] * D)
    for sigma in ORDERS:
        for y in BLOCK:
            for link, s in axial_path(origin, y, sigma):
                racc(row, link, w * s)
    return row

def row_q_root(mu):
    """Q_root A(X,mu) := avg_{sigma,y} int_{T^sigma_y} A,
       T^sigma_y = P^sigma(c_X -> y) . S_y . P^sigma(c_Y -> y + L e_mu)^dag.
       The third leg is walked INDEPENDENTLY from c_Y (not translated from the first), so that gate A
       has at least the power to test translation covariance and the L e_mu offset."""
    w = Fraction(1, NSIG * (L ** D))
    row = {}
    cY = tuple(L * x for x in e(mu))
    for sigma in ORDERS:
        for y in BLOCK:
            yfar = add(y, cY)
            for link, s in axial_path(tuple([0] * D), y, sigma):
                racc(row, link, w * s)
            for link, s in straight_leg(y, mu):
                racc(row, link, w * s)
            for link, s in axial_path(cY, yfar, sigma):
                racc(row, link, -w * s)
    return row

def row_q_str_lp(mu):
    """LINEAR_PACKAGE: L^-d sum_{y in B(X)} sum_{j<L} A_mu(y + j e_mu).  L^d block legs."""
    w = Fraction(1, L ** D)
    row = {}
    for y in BLOCK:
        for link, s in straight_leg(y, mu):
            racc(row, link, w * s)
    return row

def row_q_str_norms(mu):
    """NORMS sec.N1: L^-(d-1) over the L^(d-1) straight paths of L links (one per transverse offset,
       starting on the near face of the block)."""
    w = Fraction(1, L ** (D - 1))
    row = {}
    for y in BLOCK:
        if y[mu] != -HALF:
            continue
        for link, s in straight_leg(y, mu):
            racc(row, link, w * s)
    return row

# ---------- composition to level 2 ----------
# A level-1 site X1 sits at level-0 position L*X1 (relative coordinates anchored at the root).

def compose2(rowtop, base):
    """rowtop is a row over LEVEL-1 links; base[nu] is the level-0 row of the level-1 link (0,nu).
       Returns the level-0 row of the composite."""
    out = {}
    for (X1, nu), c in rowtop.items():
        shift = tuple(L * x for x in X1)
        for (p, mu2), c2 in base[nu].items():
            racc(out, (add(p, shift), mu2), c * c2)
    return out

# ---------- lambdas for gates E / E' ----------

def lam1(x):
    return x[0] ** 3 + 2 * x[1] ** 2 - x[2] * x[3] + 5 * x[0]

def lam2(x):                      # POST-HOC only (see the report); not in the pre-registered criteria
    return x[2] ** 3 + x[3] ** 3

# ======================================================================================

def main():
    out = []
    def say(s):
        out.append(s)
        print(s)

    say("check nd1 -- T55-P.  L=%d, d=%d, block radius %d, %d coordinate orders." % (L, D, HALF, NSIG))
    say("")

    qroot = {mu: row_q_root(mu) for mu in range(D)}
    qstr_lp = {mu: row_q_str_lp(mu) for mu in range(D)}
    qstr_no = {mu: row_q_str_norms(mu) for mu in range(D)}
    h = row_h()

    say("supports: Q_root %s | Q_str^LP %s | Q_str^NORMS %s | h %d" % (
        [len(qroot[m]) for m in range(D)], [len(qstr_lp[m]) for m in range(D)],
        [len(qstr_no[m]) for m in range(D)], len(h)))
    say("row l1 of h = %s (= %s)" % (rl1(h), float(rl1(h))))
    say("")

    # ---------------- gate A and control A' ----------------
    say("### gate A  (slice identity  Q_root = Q_str^LP - d.h)")
    okA = True
    for mu in range(D):
        rhs = radd(rsub(qstr_lp[mu], rtrans(h, tuple(L * x for x in e(mu)))), h)
        n = rdiff_count(qroot[mu], rhs)
        say("   mu=%d: differing entries = %d" % (mu, n))
        okA &= (n == 0)
    say("   gate A: %s" % ("PASS" if okA else "FAIL"))

    say("### control A' (designed to FAIL: the same identity with NORMS sec.N1's Q_str)")
    firedA = True
    for mu in range(D):
        rhs = radd(rsub(qstr_no[mu], rtrans(h, tuple(L * x for x in e(mu)))), h)
        n = rdiff_count(qroot[mu], rhs)
        say("   mu=%d: differing entries = %d" % (mu, n))
        firedA &= (n != 0)
    say("   control A': %s" % ("FAILED AS DESIGNED" if firedA else "DID NOT FIRE -> gate A is VOID"))
    say("")

    # ---------------- gate B and control B' ----------------
    say("### gate B  (||Q_root||_{inf->inf} > L ?)")
    okB = True
    for mu in range(D):
        v = rl1(qroot[mu])
        say("   mu=%d: ||Q_root|| = %s = %.6f   (L = %d)" % (mu, v, float(v), L))
        okB &= (v > L)
    say("   gate B: %s" % ("PASS" if okB else "FAIL"))

    say("### control B' (designed to FAIL the '> L' test: the same code path on Q_str^LP)")
    firedB = True
    for mu in range(D):
        v = rl1(qstr_lp[mu])
        say("   mu=%d: ||Q_str^LP|| = %s" % (mu, v))
        firedB &= not (v > L)
    say("   control B': %s" % ("FAILED AS DESIGNED" if firedB else "DID NOT FIRE -> gate B is VOID"))
    say("")

    # ---------------- level 2 ----------------
    q2 = {mu: compose2(qroot[mu], qroot) for mu in range(D)}
    s2 = {mu: compose2(qstr_lp[mu], qstr_lp) for mu in range(D)}
    say("level-2 supports: Q^(2) %s | Q_str^(2) %s" % (
        [len(q2[m]) for m in range(D)], [len(s2[m]) for m in range(D)]))
    say("")

    # ---------------- gate C and control C' ----------------
    say("### gate C  (exact values, and the session-24 bounds)")
    tgt = {1: Fraction(205, 27), 2: Fraction(2021, 81)}
    sharp = {1: Fraction(25, 3), 2: Fraction(91, 3)}
    q0 = Fraction(11, 3)
    okC = True
    firedC = True
    for j, rows in ((1, qroot), (2, q2)):
        vals = [rl1(rows[m]) for m in range(D)]
        same = all(v == vals[0] for v in vals)
        v = vals[0]
        say("   j=%d: ||Q^j|| = %s = %.6f  (all four directions equal: %s)" % (j, v, float(v), same))
        say("        target %s  | sharp bound %s  | q0*L^j = %s  | L^j = %d | p_L^j = %d"
            % (tgt[j], sharp[j], q0 * L ** j, L ** j, 11 ** j))
        okC &= same and (v == tgt[j]) and (v <= sharp[j]) and (v <= q0 * L ** j)
        firedC &= (L ** j < v < 11 ** j)
    say("   gate C: %s" % ("PASS" if okC else "FAIL"))
    say("   control C' (value strictly between L^j and p_L^j at both j): %s"
        % ("holds -- neither frame is right, as designed" if firedC else "DOES NOT HOLD"))
    say("")

    # ---------------- gate D and control D' ----------------
    say("### gate D  (telescoping at j=2:  Q^(2) = Q_str^(2) - D_2[ev_1 h_0 + h_1 S_0])")
    h1s0 = compose2(h, qstr_lp)          # h at level 1, composed with the level-0 straight average
    G = radd(h, h1s0)                    # ev_1 h_0 collapses to h on origin-anchored rows
    okD = True
    for mu in range(D):
        shift = tuple(L * L * x for x in e(mu))
        rhs = rsub(s2[mu], rsub(rtrans(G, shift), G))
        n = rdiff_count(q2[mu], rhs)
        say("   mu=%d: differing entries = %d   (|Q^(2)| = %d, |rhs| = %d)" % (mu, n, len(q2[mu]), len(rhs)))
        okD &= (n == 0)
    say("   gate D: %s" % ("PASS" if okD else "FAIL"))

    say("### control D' (designed to FAIL: far-end shift L e_mu instead of L^2 e_mu)")
    firedD = True
    for mu in range(D):
        shift = tuple(L * x for x in e(mu))
        rhs = rsub(s2[mu], rsub(rtrans(G, shift), G))
        n = rdiff_count(q2[mu], rhs)
        say("   mu=%d: differing entries = %d" % (mu, n))
        firedD &= (n != 0)
    say("   control D': %s" % ("FAILED AS DESIGNED" if firedD else "DID NOT FIRE -> gate D is VOID"))
    say("")

    # ---------------- gate E and control E' ----------------
    say("### gate E  (root covariance through the composite: Q^(j)(d_0 lam) = lam(L^j e_mu) - lam(0))")
    okE = True
    for j, rows in ((1, qroot), (2, q2)):
        for mu in range(D):
            got = reval_dlambda(rows[mu], lam1)
            want = Fraction(lam1(tuple(L ** j * x for x in e(mu))) - lam1(tuple([0] * D)))
            ok = (got == want)
            okE &= ok
            say("   j=%d mu=%d: got %s, want %s  -> %s" % (j, mu, got, want, "ok" if ok else "MISMATCH"))
    say("   gate E: %s" % ("PASS" if okE else "FAIL"))

    say("### control E' (designed to FAIL: Q_str^LP in place of Q_root; Q_str.d = d.blockmean, not d.ev)")
    firedE = False
    perdir = []
    for j, rows in ((1, qstr_lp), (2, s2)):
        for mu in range(D):
            got = reval_dlambda(rows[mu], lam1)
            want = Fraction(lam1(tuple(L ** j * x for x in e(mu))) - lam1(tuple([0] * D)))
            differs = (got != want)
            firedE |= differs
            perdir.append((j, mu, differs))
            say("   j=%d mu=%d: got %s, want %s  -> %s" % (j, mu, got, want, "DIFFERS (fires)" if differs else "agrees"))
    say("   control E': %s  (fired in %d of %d cases)"
        % ("FAILED AS DESIGNED" if firedE else "DID NOT FIRE -> gate E is VOID",
           sum(1 for _, _, x in perdir if x), len(perdir)))
    say("")

    # ---------------- POST-HOC (labelled; no pre-registered verdict) ----------------
    say("### POST-HOC probe P1 (run after seeing E'; labelled post-hoc, no pre-registered verdict)")
    say("    E' with lam2(x) = x2^3 + x3^3, to see whether the directions in which E' did not fire")
    say("    are a property of lam1 or of the operator.")
    for j, rows in ((1, qstr_lp), (2, s2)):
        for mu in range(D):
            got = reval_dlambda(rows[mu], lam2)
            want = Fraction(lam2(tuple(L ** j * x for x in e(mu))) - lam2(tuple([0] * D)))
            say("   j=%d mu=%d: Q_str gives %s, root value %s -> %s"
                % (j, mu, got, want, "differs" if got != want else "agrees"))
    say("")
    say("### POST-HOC probe P2: ||h . Q_str^(i)|| for i = 0, 1 (the only lossy step of the assembly)")
    for i, r in ((0, h), (1, compose2(h, qstr_lp))):
        say("   i=%d: ||h Q_str^(i)|| = %s = %.6f   (/L^i = %.6f)"
            % (i, rl1(r), float(rl1(r)), float(rl1(r)) / L ** i))

    say("")
    say("SUMMARY  gateA=%s A'=%s | gateB=%s B'=%s | gateC=%s C'=%s | gateD=%s D'=%s | gateE=%s E'=%s"
        % (okA, firedA, okB, firedB, okC, firedC, okD, firedD, okE, firedE))

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
