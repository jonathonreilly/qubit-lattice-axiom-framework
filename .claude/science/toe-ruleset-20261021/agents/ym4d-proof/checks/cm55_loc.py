# cm55_loc.py -- exact locality radii for the weighted (m > 0) constants used in COFM55.md.
# Criteria: checks/cm55_criteria.md (Part A, items L0-L4 and controls C1-C4; Amendment A1 for L3).
# Exact integers / Fractions only. d = 4, L = 3, coarse torus side T = 6. Roots = block centres
# (corner roots only in control C4). No third-party modules.
from fractions import Fraction as F
from itertools import permutations, product

D = 4
L = 3
T = 6
ONE = (1, 1, 1, 1)


def tdist(a, b):
    """l1 torus distance on (R/TZ)^4 between two coarse positions (tuples of Fractions)."""
    s = F(0)
    for x, y in zip(a, b):
        dlt = (x - y) % T
        s += min(dlt, T - dlt)
    return s


def pos(site, level, k):
    """coarse position of a level-`level` site (integer 4-tuple)."""
    rho = F(1, L ** (k - level))
    return tuple(F(c) * rho for c in site)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scal(c, a):
    return tuple(c * x for x in a)


def unit(nu):
    return tuple(1 if i == nu else 0 for i in range(D))


def h_support(root_rel):
    """Support of the order-averaged slice functional h(.)(X) for the block {0..L-1}^4 of a
    level-(l+1) site (level-l units), root at root_rel (relative coordinates).
    Returns (support dict link->set(signs), sign_consistent flag). A link is (base, mu) with base the
    lower endpoint; traversal sign +1 if the path moves +e_mu across it."""
    sup = {}
    for y in product(range(L), repeat=D):
        for order in permutations(range(D)):
            cur = list(root_rel)
            for mu in order:
                while cur[mu] != y[mu]:
                    if y[mu] > cur[mu]:
                        base = tuple(cur)
                        cur[mu] += 1
                        sgn = +1
                    else:
                        cur[mu] -= 1
                        base = tuple(cur)
                        sgn = -1
                    link = (base, mu)
                    sup.setdefault(link, set()).add(sgn)
    consistent = all(len(s) == 1 for s in sup.values())
    for (base, mu) in sup:
        # every traversed link must be block-interior
        assert all(0 <= c < L for c in base) and base[mu] + 1 < L, ("non-interior link", base, mu)
    return sup, consistent


results = []
controls = []


def report(name, ok, detail):
    results.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")


def control(name, claim_holds, detail):
    fires = not claim_holds
    controls.append((name, fires))
    print(f"{name}: {'FIRES' if fires else 'DOES NOT FIRE'}  {detail}")


# ---------------- L0: h support, centre roots ----------------
centre = tuple((L - 1) // 2 for _ in range(D))
corner = (0, 0, 0, 0)
supC, consC = h_support(centre)
supK, consK = h_support(corner)
report("L0 (sign consistency, centre roots)", consC,
       f"links in support = {len(supC)}; corner-root support = {len(supK)} (consistent={consK})")

# ---------------- L1: FLUX ----------------
k = 2
L1_ok = True
DF = {}
for l in (0, 1):
    s = L ** (k - l)
    best = F(0)
    for X in ((0, 0, 0, 0), (T - 1, T - 1, T - 1, T - 1)):
        Xpos = tuple(F(c) for c in X)
        for mu in range(D):
            for r in product(range(s), repeat=D):
                if r[mu] != s - 1:
                    continue  # upper mu-face of B_l(X): Z + e_mu leaves the block
                Z = tuple(s * X[i] + r[i] for i in range(D))
                dd = tdist(Xpos, pos(Z, l, k))
                if dd > best:
                    best = dd
    DF[l] = best
    pred = 4 * (1 - F(1, s))
    ok = (best == pred) and best < 4
    L1_ok = L1_ok and ok
    print(f"   L1 l={l}: D_F = {best} (prediction 4(1-L^(l-k)) = {pred})")
report("L1 (FLUX read radius = 4(1-L^(l-k)) < 4)", L1_ok, f"D_F = {DF}")
control("C1 (claim D_F(1) <= 4(1-1/L) - 1/L)", DF[1] <= 4 * (1 - F(1, L)) - F(1, L), f"D_F(1) = {DF[1]}")

# ---------------- L2: DEC subtraction Q_{k-1}^T b ----------------
k = 2
DQ = F(0)
DQ_str = F(0)
DQ_h = F(0)
for X in ((0, 0, 0, 0), (T - 1, T - 1, T - 1, T - 1)):
    for r in product(range(L), repeat=D):
        y = tuple(L * X[i] + r[i] for i in range(D))
        ypos = pos(y, 1, k)
        for mu in range(D):
            reads = []
            # Q_str^T: reads coarse links (X(y - i e_mu), mu), i < L
            for i in range(L):
                z = tuple(y[j] - (i if j == mu else 0) for j in range(D))
                Xb = tuple(z[j] // L for j in range(D))
                reads.append(("str", Xb))
            # h^T d*: only if the link is in the support of h(.)(X') (block-interior, centre roots)
            if (r, mu) in supC:
                Xp = tuple(y[j] // L for j in range(D))
                for nu in range(D):
                    reads.append(("h", sub(Xp, unit(nu))))
                    reads.append(("h", Xp))
            for tag, Xb in reads:
                dd = tdist(ypos, tuple(F(c) for c in Xb))
                if dd > DQ:
                    DQ = dd
                if tag == "str" and dd > DQ_str:
                    DQ_str = dd
                if tag == "h" and dd > DQ_h:
                    DQ_h = dd
report("L2 (DEC Q^T read radius <= 11/3)", DQ <= F(11, 3),
       f"D_Q = {DQ} (Q_str^T part {DQ_str}, h^T d* part {DQ_h})")
control("C2 (claim D_Q <= 4(L-1)/L)", DQ <= F(4 * (L - 1), L), f"D_Q = {DQ}")

# ---------------- L3: composite straight push-down transposes ----------------
k = 2
L3_ok = True
DP = {}
for (a, b) in ((0, 1), (1, 2), (0, 2)):
    s = L ** (b - a)
    rho_a = F(1, L ** (k - a))
    rho_b = F(1, L ** (k - b))
    best = F(0)
    for Y0 in ((0, 0, 0, 0), (T * L ** (k - b) - 1,) * D):
        for r in product(range(s), repeat=D):
            y = tuple(s * Y0[i] + r[i] for i in range(D))
            ypos = pos(y, a, k)
            for nu in range(D):
                for t in range(s):
                    z = tuple(y[j] - (t if j == nu else 0) for j in range(D))
                    Y = tuple(z[j] // s for j in range(D))
                    dd = tdist(ypos, pos(Y, b, k))
                    if dd > best:
                        best = dd
    DP[(a, b)] = best
    ok = best < 5 * rho_b
    L3_ok = L3_ok and ok
    print(f"   L3 (a,b)=({a},{b}): D_P = {best}; bound 5 rho_b = {5 * rho_b}; prediction 5(rho_b - rho_a) = {5 * (rho_b - rho_a)}"
          f" -> {'matches' if best == 5 * (rho_b - rho_a) else 'DIFFERS'}")
report("L3 (push-down transpose read radius < 5 rho_b)", L3_ok, f"D_P = {DP}")
control("C3 (claim D_P(0,2) <= 4(rho_2 - rho_0))", DP[(0, 2)] <= 4 * (1 - F(1, 9)), f"D_P(0,2) = {DP[(0, 2)]}")


# ---------------- L4: Lemma FT (iv) funnel read radius ----------------
def ft_radius(k, levels, roots="centre"):
    best = F(0)
    sup = supC if roots == "centre" else supK
    for l in levels:
        for X in ((0, 0, 0, 0), (T * L ** (k - l - 1) - 1,) * D):
            # level-(l+1) site X; its level-0 avatar (root)
            if roots == "centre":
                av = tuple(L ** (l + 1) * X[i] + (L ** (l + 1) - 1) // 2 for i in range(D))
            else:
                av = tuple(L ** (l + 1) * X[i] for i in range(D))
            for (rel, mu) in sup:
                y = tuple(L * X[i] + rel[i] for i in range(D))  # level-l base of the output link
                ypos = pos(y, l, k)
                for lp in range(0, l + 1):
                    if roots == "centre":
                        off = (L ** lp - 1) // 2
                    else:
                        off = 0
                    num = tuple(av[i] - off for i in range(D))
                    assert all(c % (L ** lp) == 0 for c in num), "root is not a level-l' site"
                    Zp = tuple(c // (L ** lp) for c in num)
                    for nu in range(D):
                        for Zl in (sub(Zp, unit(nu)), Zp):
                            dd = tdist(ypos, pos(Zl, lp, k))
                            if dd > best:
                                best = dd
    return best


DFT2 = ft_radius(2, (0, 1), "centre")
DFT3 = ft_radius(3, (2,), "centre")
report("L4 (FT (iv) funnel read radius <= 2, centre roots)", DFT2 <= 2 and DFT3 <= 2,
       f"D_FT(k=2, l=0,1) = {DFT2}; D_FT(k=3, l=2) = {DFT3}; prediction 5/3")
DFT2K = ft_radius(2, (0, 1), "corner")
control("C4 (claim D_FT <= 2 with CORNER roots)", DFT2K <= 2, f"D_FT(corner, k=2) = {DFT2K}")

allpass = all(ok for _, ok in results)
allfire = all(f for _, f in controls)
print()
if allpass and allfire:
    print(f"VERDICT cm55_loc: ALL PASS (all controls fired) [{len(results)} criteria, {len(controls)} controls]")
else:
    print("VERDICT cm55_loc: FAILURES:",
          [n for n, ok in results if not ok], "controls not firing:", [n for n, f in controls if not f])
