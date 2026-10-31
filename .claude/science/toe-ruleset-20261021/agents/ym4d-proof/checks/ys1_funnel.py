"""ys1_funnel.py -- YSUP session 25.  Exact, plain python, Fractions/ints only, no numpy, no BLAS.

Decides: is the block-averaged axial line integral Phi_k small enough at the core of a |z|^-3 field
to deliver (Y-sup^loc) (needs <~ 1/n) or (TENT-osc) (needs <~ 1/n^2)?

Verdicts are those pre-registered in checks/ys1_criteria.md (written before this file).

Conventions REBUILT from the definitions quoted in YSUP 1.0, not imported:
  h_i(w)(Y)      = avg over the 24 coordinate orders and the L^D block offsets o of the signed
                   sum of w along the axial path c_Y -> c_Y + o           [BFT_B 29.2 Lemma FT (i)]
  (Q_str v)(Y,m) = L^-D sum_{r in [0,L)^D} sum_{j<L} v_m(L Y + r + j e_m)  [BFT_B 27.1]
  Phi_k(v)(X)    = sum_{i<k} ev^{(i+1->k)} h_i (Q_str^{(0->i)} v) (X)      [BFT_A 38.3 / BL-2 (b)]
  roots: off(l) = (L^l - 1)/2 + L^l Z^D; the level-i avatar of the level-k root is
         Y_i = (off(k) - off(i)) / L^i, and L*Y_{i+1} + OFF = Y_i.
"""
from fractions import Fraction as F
from itertools import permutations, product
import math

L, D = 3, 4
OFF = (L - 1) // 2          # per-level offset of a block centre in the parent's coordinates


def off(l):
    return (L ** l - 1) // 2


def avatar(k, i):
    return (off(k) - off(i)) // L ** i


# ---------------------------------------------------------------- axial funnel weights
def build_HT(half=OFF):
    """HT[(z,c)] = weight of the level-i link (c_Y + z, c) in h_i(.)(Y)."""
    W1 = F(1, 24 * L ** D)
    HT = {}
    for sig in permutations(range(D)):
        for o in product(range(-half, half + 1), repeat=D):
            z = [0] * D
            for c in sig:
                while z[c] != o[c]:
                    if o[c] > z[c]:
                        key = (tuple(z), c)
                        HT[key] = HT.get(key, F(0)) + W1
                        z[c] += 1
                    else:
                        z[c] -= 1
                        key = (tuple(z), c)
                        HT[key] = HT.get(key, F(0)) - W1
    return {k: v for k, v in HT.items() if v != 0}


HT = build_HT()


def hfun(w, Y, parent_off=OFF):
    tot = F(0)
    for (z, c), wt in HT.items():
        v = w.get((tuple(L * Y[n] + parent_off + z[n] for n in range(D)), c))
        if v:
            tot += wt * v
    return tot


def qstr(v):
    """one straight-average step: dict (site,dir)->F at level l  ->  dict at level l+1."""
    out = {}
    cand = set()
    for (s, _) in v:
        for Y in product(*[range(s[n] // L - 1, s[n] // L + 1) for n in range(D)]):
            cand.add(Y)
    for Y in cand:
        for m in range(D):
            tot = F(0)
            for r in product(range(L), repeat=D):
                base = [L * Y[n] + r[n] for n in range(D)]
                for j in range(L):
                    z = list(base)
                    z[m] += j
                    tot += v.get((tuple(z), m), F(0))
            if tot:
                out[(Y, m)] = tot / L ** D
    return out


def plaq(s, m, n):
    """d* delta_p for the (m,n)-plaquette based at s, as a 1-form (unnormalised)."""
    s = tuple(s)
    sm = list(s); sm[m] += 1
    sn = list(s); sn[n] += 1
    return {(tuple(sm), n): F(1), (s, n): F(-1), (tuple(sn), m): F(-1), (s, m): F(1)}


def phi_terms(v, k):
    """[phi_1, ..., phi_k]: phi_{i+1} = h_i(Q_str^{(0->i)} v)(Y_{i+1})."""
    out, cur = [], dict(v)
    for i in range(k):
        out.append(hfun(cur, (avatar(k, i + 1),) * D))
        if i + 1 < k:
            cur = qstr(cur)
    return out


# ---------------------------------------------------------------- transpose (disjoint code path)
def hT(k, i):
    """h_i^T delta_{Y_{i+1}} as a dict on level-i links (absolute level-i coords)."""
    Y = (avatar(k, i + 1),) * D
    return {(tuple(L * Y[n] + OFF + z[n] for n in range(D)), c): wt for (z, c), wt in HT.items()}


def qstrT(psi):
    """(Q_str^T psi)(z,m) = L^-D sum_{j<L} psi(Y(z,m,j), m); returns the finer-level dict."""
    out = {}
    for (Y, m), val in psi.items():
        w = val / L ** D
        for r in product(range(L), repeat=D):
            base = [L * Y[n] + r[n] for n in range(D)]
            for j in range(L):
                z = list(base)
                z[m] += j
                key = (tuple(z), m)
                out[key] = out.get(key, F(0)) + w
    return {k: v for k, v in out.items() if v != 0}


def kernel(k, i):
    psi = hT(k, i)
    for _ in range(i):
        psi = qstrT(psi)
    return psi


def pair(ker, v):
    return sum((wt * v[b] for b, wt in ker.items() if b in v), F(0))


# ------------------------------------- composite Q_str^{(0->i)} stencil, longitudinal multiplicity
def mult_long(i):
    """offsets w >= 0 of the composite longitudinal stencil of Q_str^{(0->i)}, with multiplicity."""
    cur = {0: 1}
    for _ in range(i):
        nxt = {}
        for w, c in cur.items():
            for r in range(L):
                for j in range(L):
                    nxt[L * w + r + j] = nxt.get(L * w + r + j, 0) + c
        cur = nxt
    return cur


def kernel_closed(k, i):
    """K_i as classes {(m, Y_perp, z_m): value}; each class holds exactly L^{i(D-1)} fine links.
    K_i(z,m) = L^{-Di} sum_a mult_long_i(z_m - L^i a) * (h_i^T delta)((Y_perp, a), m)."""
    g = hT(k, i)
    ml = mult_long(i)
    out = {}
    for (Y, m), wt in g.items():
        Yp = tuple(Y[n] for n in range(D) if n != m)
        for w, mu in ml.items():
            key = (m, Yp, L ** i * Y[m] + w)
            out[key] = out.get(key, F(0)) + F(mu, L ** (D * i)) * wt
    return {kk: vv for kk, vv in out.items() if vv != 0}


# ---------------------------------------------------------------- the test profile v+
_JTAB = []


def jtab(smax):
    global _JTAB
    _JTAB = []
    j = 0
    for s in range(smax + 2):
        while L ** j < 1 + s:
            j += 1
        _JTAB.append(j)
    return _JTAB


def jstep(s):
    j = 0
    while L ** j < 1 + s:
        j += 1
    return j


# ================================================================ CHECKS
print("=" * 104)
print("ys1 -- YSUP session 25.  d = %d, L = %d.  exact Fractions/ints, single thread, no BLAS, no lock." % (D, L))
print("=" * 104)
tv = sum(abs(v) for v in HT.values())
closed_tv = F(sum(sum(abs(o[n]) for n in range(D)) for o in product(range(-OFF, OFF + 1), repeat=D)), L ** D)
print("|HT| = %d nonzero axial weights;  sum|weights| = %s" % (len(HT), tv))
print("Lemma FT (i) closed form L^-D sum_{y in B}|y - c_X|_1 = %s   -> %s"
      % (closed_tv, "MATCH" if closed_tv == tv else "MISMATCH"))

# ---- A1
print("\n--- A1  rebuild of REVIEW_BFT_A_S8 S8-7's exact rationals (outside numbers) ---")
k2 = 2
cX2 = (off(k2),) * D
p2 = tuple(cX2[n] + (1, 0, 0, 0)[n] for n in range(D))
u2 = plaq(p2, 0, 1)
t2 = phi_terms(u2, k2)
phi1, phi2 = t2[0], t2[1]
psi_u = (phi1 + phi2) / 8
c1 = phi1 == F(-1, 54); c2 = phi2 == F(-17, 13122)
c3 = (phi2 / phi1 == F(17, 243)); c4 = (psi_u == F(-65, 26244))
A1 = c1 and c2 and c3 and c4
print("  c_X = %s, p = %s (unnormalised u = d* delta_p)" % (cX2, p2))
print("  phi_1 = %-14s target -1/54      %s" % (phi1, "ok" if c1 else "MISMATCH"))
print("  phi_2 = %-14s target -17/13122  %s" % (phi2, "ok" if c2 else "MISMATCH"))
print("  ratio = %-14s target 17/243     %s" % (phi2 / phi1, "ok" if c3 else "MISMATCH"))
print("  psi_u = %-14s target -65/26244  %s" % (psi_u, "ok" if c4 else "MISMATCH"))
print("  A1 VERDICT: %s" % ("PASS" if A1 else "FAIL"))

# ---- A2  (brute transpose kernel, i = 0, 1)
print("\n--- A2  kernel K_i = (Q_str^{(0->i)})^T h_i^T delta_X : support / sup / l1  [i = 0,1 brute] ---")
A2 = True
brute = {}
for i in (0, 1):
    kk = i + 1
    K = kernel(kk, i)
    brute[i] = K
    ctr = off(kk)
    half = (L ** (i + 1) - 1) // 2
    ins = True
    for (site, c) in K:
        for e in (0, 1):
            for n in range(D):
                if abs(site[n] + (e if n == c else 0) - ctr) > half:
                    ins = False
    sup = max(abs(v) for v in K.values())
    l1 = sum(abs(v) for v in K.values())
    bnd = F(1, L ** (i * (D - 1)))
    l1c = F(L ** i) * closed_tv
    ca, cb, cc = ins, sup <= bnd, l1 == l1c
    A2 = A2 and ca and cb and cc
    print("  i = %d: |supp| = %-6d (a) both endpoints in level-%d block: %-5s" % (i, len(K), i + 1, ca))
    print("          (b) sup = %-14s <= L^{i(1-D)} = %-10s %s" % (sup, bnd, "ok" if cb else "VIOLATED"))
    print("          (c) l1  = %-14s == L^i * %s = %-10s %s" % (l1, closed_tv, l1c, "ok" if cc else "MISMATCH"))
print("  A2 VERDICT: %s" % ("PASS" if A2 else "FAIL"))

# ---- A2' closed-form kernel, cross-checked at i = 0,1, extended to i = 2,3,4
print("\n--- A2' closed-form kernel classes (cross-checked at i = 0,1; extended to i = 2,3,4) ---")
A2p = True
for i in (0, 1, 2, 3, 4):
    kk = i + 1
    cl = kernel_closed(kk, i)
    sup = max(abs(v) for v in cl.values())
    l1 = sum(abs(v) for v in cl.values()) * L ** (i * (D - 1))
    bnd = F(1, L ** (i * (D - 1)))
    l1c = F(L ** i) * closed_tv
    ok = (sup <= bnd) and (l1 == l1c)
    note = ""
    if i in brute:
        K = brute[i]
        xok = (max(abs(v) for v in K.values()) == sup) and (sum(abs(v) for v in K.values()) == l1)
        ok = ok and xok
        note = "  [brute agrees: %s]" % xok
    A2p = A2p and ok
    print("  i = %d: sup = %-16s (<= %-12s %s)   l1 = %-12s (== %-10s %s)%s"
          % (i, sup, bnd, sup <= bnd, l1, l1c, l1 == l1c, note))
print("  A2' VERDICT: %s" % ("PASS" if A2p else "FAIL"))

# ---- A3
print("\n--- A3  forward pipeline vs transpose kernel (disjoint code paths) ---")
q0 = pair(kernel(k2, 0), u2)
q1 = pair(kernel(k2, 1), u2)
A3 = (q0 == phi1 and q1 == phi2)
print("  <K_0,u> = %-14s  phi_1 = %-14s  %s" % (q0, phi1, "ok" if q0 == phi1 else "MISMATCH"))
print("  <K_1,u> = %-14s  phi_2 = %-14s  %s" % (q1, phi2, "ok" if q1 == phi2 else "MISMATCH"))
print("  A3 VERDICT: %s" % ("PASS" if A3 else "FAIL"))

# ---- A0
print("\n--- A0  the test profile v+ ---")
a0a = all(F(1, L ** (3 * jstep(s))) <= F(1, (1 + s) ** 3) <= F(L ** 3, L ** (3 * jstep(s))) for s in range(0, 300))
a0b = all(jstep(L * s + L - 1) == jstep(s) + 1 for s in range(1, 80))
print("  (A0a) v+(s) <= (1+s)^-3 <= L^3 v+(s), s = 0..299 : %s" % a0a)
print("  (A0b) exact L-scale covariance of the staircase  : %s" % a0b)
print("  A0 VERDICT: %s" % ("PASS" if (a0a and a0b) else "FAIL"))

# ---- A4  THE DISCRIMINATING CHECK
print("\n--- A4  the power of n_i: LI_i (axial line-integral block average) vs BA_i (full block average) ---")
KB = 4
cXb = [off(KB)] * D
pb = [cXb[0] + 1, cXb[1], cXb[2], cXb[3]]
IMAX = 3
jt = jtab(8 * L ** IMAX)
LI, BA = {}, {}
for i in range(IMAX + 1):
    Yc = avatar(KB, i)
    ni = L ** i
    ml = mult_long(i)
    m = 0
    # ---- LI_i at the level-i link (Y_i, m=0), exact integer accumulation
    lo = [ni * Yc] * D
    J = 0
    acc = 0
    cells = []
    for r in product(*[range(ni) for _ in range(D - 1)]):
        site = [0] * D
        idx = 0
        for n in range(D):
            if n != m:
                site[n] = lo[n] + r[idx]; idx += 1
        for w, mu in ml.items():
            site[m] = lo[m] + w
            s = max(abs(site[n] - pb[n]) for n in range(D))
            cells.append((mu, jt[s]))
            if jt[s] > J:
                J = jt[s]
    for mu, j in cells:
        acc += mu * L ** (3 * (J - j))
    LI[i] = F(acc, L ** (3 * J) * L ** (D * i))
    # ---- BA_i : full normalised block average over the level-i block centred at p
    h = (ni - 1) // 2
    J2 = jt[h] if h >= 0 else 0
    acc2 = 0
    for o in product(range(-h, h + 1), repeat=D):
        s = max(abs(o[n]) for n in range(D))
        acc2 += L ** (3 * (J2 - jt[s]))
    BA[i] = F(acc2, L ** (3 * J2) * L ** (D * i))
    print("  i = %d (n_i = %-3d): LI_i = %-30s = %.6e    BA_i = %-30s = %.6e"
          % (i, ni, LI[i], float(LI[i]), BA[i], float(BA[i])))


def bands(fam, name):
    rs = []
    for i in range(len(fam) - 1):
        r = fam[i + 1] / fam[i]
        rho = -math.log(float(r)) / math.log(L)
        rs.append((i, r, rho))
    v2 = all(1.5 <= rho < 2.5 for _, _, rho in rs)
    v3 = all(2.5 <= rho < 3.5 for _, _, rho in rs)
    verdict = "(V-2)" if v2 else ("(V-3)" if v3 else "(V-other)")
    print("  %s ratios:" % name)
    for i, r, rho in rs:
        print("     r_%d = %-26s = %.6f   rho = -log_L r = %.4f" % (i, r, float(r), rho))
    print("  %s VERDICT: %s" % (name, verdict))
    return verdict


vLI = bands([LI[i] for i in range(IMAX + 1)], "LI")
vBA = bands([BA[i] for i in range(IMAX + 1)], "BA")
A4 = vLI in ("(V-2)", "(V-3)") and vBA in ("(V-2)", "(V-3)")
A8 = A4 and (vLI != vBA)
print("  A4 VERDICT: LI = %s, BA = %s  -> %s" % (vLI, vBA, "usable" if A4 else "criteria INADEQUATE"))
print("  A8 VERDICT (the band test reads both objects differently): %s" % ("PASS" if A8 else "FAIL"))

# ---- A5
print("\n--- A5  Phi_k(d delta_{c_X})(X) = L^{-Dk} - 1   (Proposition TGAUGE, TENTQ 2.7; outside formula) ---")
A5 = True
for kk in (1, 2):
    cXk = (off(kk),) * D
    dmu = {}
    for m in range(D):
        z = list(cXk); z[m] -= 1
        dmu[(tuple(z), m)] = dmu.get((tuple(z), m), F(0)) + F(1)
        dmu[(tuple(cXk), m)] = dmu.get((tuple(cXk), m), F(0)) - F(1)
    got = sum(phi_terms(dmu, kk), F(0))
    tgt = F(1, L ** (D * kk)) - 1
    ok = got == tgt
    A5 = A5 and ok
    print("  k = %d: Phi_k = %-24s target %-24s %s" % (kk, got, tgt, "ok" if ok else "MISMATCH"))
print("  A5 VERDICT: %s" % ("PASS" if A5 else "FAIL"))

# ---- A6
print("\n--- A6  k-uniform lower bound on |Phi_k(u)| at k = 3  (u = (1/8) d* delta_p, admissible) ---")
k3 = 3
cX3 = (off(k3),) * D
p3 = tuple(cX3[n] + (1, 0, 0, 0)[n] for n in range(D))
u3 = {b: v / 8 for b, v in plaq(p3, 0, 1).items()}
t3 = phi_terms(u3, k3)
l1u = sum(abs(v) for v in u3.values())
tail = l1u * F(1, L ** (3 * (D - 1))) / (1 - F(1, L ** (D - 1)))
head = sum(t3, F(0))
cov = (t3[0] == phi1 / 8 and t3[1] == phi2 / 8)
A6 = cov and abs(head) > 10 * tail
for i, t in enumerate(t3):
    print("  phi_%d = %-24s = %+.8e" % (i + 1, t, float(t)))
print("  (a) phi_1,phi_2 at k=3 equal (1/8)x their k=2 values (level/translation covariance): %s" % cov)
print("  Phi_3 = %s = %+.8e ;  ||u||_1 = %s ;  tail bound sum_{i>=3} |phi_{i+1}| <= %s = %.4e"
      % (head, float(head), l1u, tail, float(tail)))
print("  (b) |Phi_3| > 10 * tail : %s  (ratio %.1f)" % (abs(head) > 10 * tail, float(abs(head) / tail)))
print("  A6 VERDICT: %s" % ("PASS" if A6 else "FAIL"))

# ---- A7  DESIGNED-FAIL CONTROL
print("\n--- A7  DESIGNED-FAIL CONTROL: off(l) := 0 (block corner instead of block centre) ---")
ctrl = hfun(u2, (avatar(k2, 1),) * D, parent_off=0)
A7 = (ctrl != F(-1, 54))
print("  control phi_1 = %-18s   A1 target -1/54" % ctrl)
print("  A7 VERDICT (control MUST fail A1's target): %s" % ("PASS" if A7 else "FAIL -- A1 CANNOT FAIL"))

print("\n" + "=" * 104)
print("SUMMARY   A0 %s | A1 %s | A2 %s | A2' %s | A3 %s | A4 %s | A5 %s | A6 %s | A7 %s | A8 %s"
      % tuple("PASS" if x else "FAIL" for x in [a0a and a0b, A1, A2, A2p, A3, A4, A5, A6, A7, A8]))
print("=" * 104)
