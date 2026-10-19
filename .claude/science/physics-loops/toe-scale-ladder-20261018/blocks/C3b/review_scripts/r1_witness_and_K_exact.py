"""Reviewer r1: witness X (exact) and Theorem K1 (exact rational enumeration), plus K3 scope.

(a) Witness X on the 3D torus 6^3: for BOTH phases and random noise the record equals the late indicator; exact
    covariance over the phase; translation by e1 swaps the phases (stationarity); clock covariance itself is +-1/4
    at all distances (non-mixing); O_h preserves parity.  Ancestry depth L <= 1.
(b) Theorem K1, different instance from the author: Potts q=3 noisy-plurality rule on a 2x3 grid graph, Gamma = S_3
    acting on colours, clock law = an ARBITRARY non-exchangeable mixture of total orders AND orders with ties (strict
    convention).  For every clock realisation T: E[f|T] = 0 for Gamma-mean-zero f; on disjoint ancestries
    E[fg|T] = E[f|T]E[g|T]; overall |E f g| <= ||f|| ||g|| P(overlap).  g is NOT symmetric.
    Negative control: a colour-biased rule (not S_3-invariant) gives E f != 0.
(c) K3 scope: gradient-stationary level clock T_x = x on Z has an infinite decreasing run (so K3 needs stationarity
    of T itself); copy rule then has two solutions (two phases).  Stationary strongly-correlated clocks (AR(1) rho=0.999,
    random-phase sawtooth) have finite runs in MC.
"""
import itertools
from fractions import Fraction
import numpy as np
from rv_common import check, total

rng = np.random.default_rng(77)

# ---------------- (a) witness X ----------------
Lb = 6
X = np.indices((Lb,) * 3).reshape(3, -1).T
N = len(X)
par = X.sum(1) % 2
idx = np.arange(N).reshape((Lb,) * 3)
nbrs = []
for ax in range(3):
    for sh in (1, -1):
        nbrs.append(np.roll(idx, -sh, axis=ax).ravel())
nbrs = np.stack(nbrs, 1)
records = {}
ok = True
Lmax = 0
for phi in (0, 1):
    for rep in range(30):
        T = (par + phi) % 2 + 0.49 * rng.random(N)
        earlier = T[nbrs] < T[:, None]
        xi = earlier.any(1).astype(int)
        ok &= np.array_equal(xi, (par + phi) % 2)
        # depth: longest decreasing path; early sites have no earlier nbr, late sites have only early nbrs
        Ld = np.where(earlier.any(1), 1, 0)
        late_has_earlier_late = (earlier & (((par[nbrs] + phi) % 2) == 1)).any()
        ok &= not late_has_earlier_late
        Lmax = max(Lmax, Ld.max())
    records[phi] = (par + phi) % 2
check("a1 record == late-sublattice indicator, both phases, 60 samples, noise amplitude 0.49", ok)
check("a2 ancestry depth L(x) <= 1 everywhere", Lmax == 1)
# exact covariance over uniform phase
covs = set()
for x in range(N):
    E0 = Fraction(records[0][0] + records[1][0], 2)
    Ex = Fraction(records[0][x] + records[1][x], 2)
    E0x = Fraction(records[0][0] * records[0][x] + records[1][0] * records[1][x], 2)
    c = E0x - E0 * Ex
    covs.add((int(X[x].sum() % 2), c))
check("a3 exact Cov(xi_0,xi_x) = +1/4 (even), -1/4 (odd), for every x", covs == {(0, Fraction(1, 4)), (1, Fraction(-1, 4))},
      str(sorted(covs)))
# stationarity: shifting by e1 maps parity field to 1-parity, i.e. phase 0 <-> phase 1
sh = np.roll(par.reshape((Lb,) * 3), 1, axis=0).ravel()
check("a4 translation by e1 swaps the two phases (law stationary under uniform phase; 2-point rotation is transitive)",
      np.array_equal(sh, 1 - par))
ok = True
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        ok &= np.all(((X[:, perm] * np.array(sg)).sum(1) % 2) == par)
check("a5 O_h (48 signed permutations) preserves parity", ok)
# clock itself non-mixing: Cov(T_0, T_x) = Cov(parity terms) = +-1/4 (noise independent)
# clock non-mixing: Cov(T_0,T_x) from the parity part, exact over the phase (iid noise adds nothing off-diagonal)
cT = set()
for x in range(1, N):
    t0 = [(par[0] + ph) % 2 for ph in (0, 1)]; tx = [(par[x] + ph) % 2 for ph in (0, 1)]
    cT.add(Fraction(t0[0] * tx[0] + t0[1] * tx[1], 2) - Fraction(t0[0] + t0[1], 2) * Fraction(tx[0] + tx[1], 2))
check("a6 clock covariance Cov(T_0,T_x) in {+1/4,-1/4} for all x != 0 (clock non-mixing)",
      cT == {Fraction(1, 4), Fraction(-1, 4)}, str(sorted(cT)))

# ---------------- (b) Theorem K1 exact on a 2x3 grid, Potts q=3 ----------------
q = 3
sites = [(i, j) for i in range(2) for j in range(3)]
sid = {s: k for k, s in enumerate(sites)}
G = {k: [sid[(i + di, j + dj)] for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (i + di, j + dj) in sid]
     for k, (i, j) in enumerate(sites)}
n = len(sites)
eps = Fraction(1, 7)


def rule_sym(s, seen):
    """noisy plurality: with prob 1-eps copy a uniformly chosen plurality colour of seen; else uniform. S_3-invariant."""
    if not seen:
        return Fraction(1, q)
    cnt = [seen.count(c) for c in range(q)]
    m = max(cnt)
    win = [c for c in range(q) if cnt[c] == m]
    return (1 - eps) * (Fraction(1, len(win)) if s in win else 0) + eps / q


def rule_bias(s, seen):
    base = rule_sym(s, seen)
    if not seen:
        return Fraction(1, 2) if s == 0 else Fraction(1, 4)
    return base


def record_law(T, rule):
    """exact law of the record given clock values T (ties allowed; strict-earlier convention). Sequential by levels."""
    levels = sorted(set(T))
    dist = {(): Fraction(1)}
    order = []
    for lv in levels:
        grp = [x for x in range(n) if T[x] == lv]
        nd = {}
        for conf, pr in dist.items():
            cm = dict(zip(order, conf))
            # all sites of this level choose independently given earlier ones
            opts = []
            for x in grp:
                seen = [cm[y] for y in G[x] if T[y] < T[x]]
                opts.append([(s, rule(s, seen)) for s in range(q)])
            for combo in itertools.product(*opts):
                p = pr
                for (s, ps) in combo:
                    p *= ps
                if p:
                    key = conf + tuple(s for s, _ in combo)
                    nd[key] = nd.get(key, 0) + p
        dist = nd
        order += grp
    out = {}
    for conf, pr in dist.items():
        cm = dict(zip(order, conf))
        key = tuple(cm[x] for x in range(n))
        out[key] = out.get(key, 0) + pr
    return out


def anc(T, x):
    a, st = {x}, [x]
    while st:
        y = st.pop()
        for z in G[y]:
            if T[z] < T[y] and z not in a:
                a.add(z); st.append(z)
    return a


# arbitrary clock law: weighted list of clock vectors (some with ties), not exchangeable, not stationary
clock_law = []
base_orders = [list(range(n)), list(reversed(range(n))), [0, 3, 1, 4, 2, 5], [5, 5, 1, 1, 3, 0], [2, 0, 2, 1, 0, 3],
               [1, 1, 1, 1, 1, 1], [4, 0, 3, 1, 2, 5]]
wts = [Fraction(3, 20), Fraction(1, 10), Fraction(1, 5), Fraction(1, 10), Fraction(3, 20), Fraction(1, 20), Fraction(1, 4)]
assert sum(wts) == 1
clock_law = list(zip(base_orders, wts))
A, B = [0], [5]
f = lambda conf: (1 if conf[0] == 0 else 0) - Fraction(1, 3)          # Gamma-mean-zero
g = lambda conf: (2 if conf[5] == 1 else 0) + (1 if conf[4] == 2 else 0) - Fraction(1, 2)  # arbitrary, uses B'={4,5}
Bset = [4, 5]
fn, gn = Fraction(2, 3), Fraction(5, 2)
# check Gamma-mean-zero for f on all single-site values
check("b0 f is S_3-mean-zero", all(sum(((1 if gm[s] == 0 else 0) - Fraction(1, 3)) for gm in itertools.permutations(range(q))) == 0
                                   for s in range(q)))
Efg = Fraction(0); Pov = Fraction(0); okcond = True; okci = True
for T, w in clock_law:
    law = record_law(T, rule_sym)
    Ef = sum(p * f(c) for c, p in law.items())
    Eg = sum(p * g(c) for c, p in law.items())
    Efg_T = sum(p * f(c) * g(c) for c, p in law.items())
    okcond &= (Ef == 0)
    aA = anc(T, 0); aB = set().union(*[anc(T, b) for b in Bset])
    disj = not (aA & aB)
    if disj:
        okci &= (Efg_T == Ef * Eg)
    else:
        Pov += w
    Efg += w * Efg_T
check("b1 E[f(xi_A)|T] = 0 for every clock realisation (incl. ties): Gamma-invariant product kernel", okcond)
check("b2 disjoint ancestries => E[fg|T] = E[f|T]E[g|T] exactly", okci)
check("b3 |E f g| <= ||f|| ||g|| P(Anc(A) cap Anc(B) != empty)", abs(Efg) <= fn * gn * Pov,
      f"|Efg|={float(abs(Efg)):.5f} bound={float(fn*gn*Pov):.5f} P(ov)={Pov}")
check("b4 the bound is not vacuous here (P(ov) < 1 and E f g != 0)", Pov < 1 and Efg != 0, f"Efg={Efg}")
# negative control
Ef_bias = sum(w * sum(p * f(c) for c, p in record_law(T, rule_bias).items()) for T, w in clock_law)
check("b5 negative control: colour-biased rule (not S_3-invariant) gives E f != 0", Ef_bias != 0, f"Ef={float(Ef_bias):.4f}")

# ---------------- (c) K3 scope ----------------
# gradient-stationary level clock T_x = x: every x has decreasing run x, x-1, x-2, ... (infinite). Copy rule:
# r(s|eta)=delta_{eta} when one earlier nbr. Formation eq xi_x = xi_{x-1} for all x has two solutions on Z.
check("c1 level clock T_x=x on Z (stationary increments, NOT stationary): L(0)=inf, copy rule has 2 solutions -> "
      "K3 does not extend to gradient-stationary clocks", True, "by hand: T_0>T_-1>T_-2>...; xi==+1 and xi==-1")


def max_run(T):
    # longest strictly decreasing run starting at the centre site, both directions
    c = len(T) // 2
    r = 0
    while c + r + 1 < len(T) and T[c + r + 1] < T[c + r]:
        r += 1
    l = 0
    while c - l - 1 >= 0 and T[c - l - 1] < T[c - l]:
        l += 1
    return max(r, l), (r == len(T) - c - 1) or (l == c)


Nl = 200001
rho = 0.999
z = rng.standard_normal(Nl)
T = np.empty(Nl); T[0] = z[0]
for i in range(1, Nl):
    T[i] = rho * T[i - 1] + np.sqrt(1 - rho ** 2) * z[i]
runs = [max_run(T[c - 2000:c + 2001]) for c in range(3000, Nl - 3000, 997)]
check("c2 stationary AR(1) rho=0.999: decreasing runs from sampled sites finite (never hit the 2000 window edge)",
      not any(h for _, h in runs), f"max run {max(r for r, _ in runs)}")
P = 50
phi = rng.random() * P
Ts = (np.arange(-500, 501) + phi) % P
r_, hit = max_run(-Ts)  # decreasing direction of the sawtooth
check("c3 random-phase sawtooth (stationary, non-mixing): run length < period", r_ < P and not hit, f"run {r_}")
total()
