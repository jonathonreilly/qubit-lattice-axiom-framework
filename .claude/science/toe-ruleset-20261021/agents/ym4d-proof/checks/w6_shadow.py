"""w6 Part G: exact shadow geometry on Z^4 (L = 3).  Criteria: checks/w6_criteria.md (written before this script).
Pure Python, exact integer arithmetic, single thread, no numpy / no BLAS -> no numeric lock (brief rule 6).
Informational, never a proof."""
import itertools
import random
import time

L = 3
RHO = 8
OFF1 = list(itertools.product((-1, 0, 1), repeat=4))
t0 = time.time()


def Nt(X, t):
    off = list(itertools.product(range(-t, t + 1), repeat=4))
    return {tuple(x[i] + o[i] for i in range(4)) for x in X for o in off}


def N1(X):
    return {tuple(x[i] + o[i] for i in range(4)) for x in X for o in OFF1}


def pi(X):
    return {tuple(c // L for c in x) for x in X}


def Sig(X):
    return N1(pi(X))


def shadows(X, M):
    """[Sigma^0(X), ..., Sigma^M(X)]"""
    out = [set(X)]
    for _ in range(M):
        out.append(Sig(out[-1]))
    return out


def norm_sh(X, M):
    return sum(len(s) for s in shadows(X, M))


def star_cluster(rng, base, n):
    P = [base]
    while len(P) < n:
        b = rng.choice(P)
        y = tuple(b[i] + rng.choice((-1, 0, 1)) for i in range(4))
        if y not in P:
            P.append(y)
    return P


def sample(rng, base):
    P = star_cluster(rng, base, rng.randint(1, 6))
    Y = []
    for _ in range(rng.randint(1, 8)):
        for _try in range(200):
            b = rng.choice(P + Y)
            dist = rng.randint(1, RHO)
            o = [rng.randint(-dist, dist) for _ in range(4)]
            o[rng.randrange(4)] = rng.choice((-dist, dist))
            y = tuple(b[i] + o[i] for i in range(4))
            if y not in P and y not in Y:
                Y.append(y)
                break
    return P, Y


res = {}
rng = random.Random(20261028)
DEPTHS = (5, 10, 20, 30)

# ---- build the sample list: S-rand (origin-ish base) and S-adv (all-ones base-3 base point) ----
samples = []          # (tag, M, P, Y)
for M in DEPTHS:
    for _ in range(60):
        base = tuple(rng.randint(-40, 40) for _ in range(4))
        P, Y = sample(rng, base)
        samples.append(("S-rand", M, P, Y))
    zeta = (3 ** (M + 1) - 1) // 2
    for _ in range(20):
        base = (zeta, zeta, zeta, zeta)
        P, Y = sample(rng, base)
        samples.append(("S-adv", M, P, Y))

# ---------------- G1: the shadow radius ----------------
viol = {1: 0, 2: 0, 3: 0}
wit1 = None
for tag, M, P, Y in samples:
    for X in (set(P), set(P) | set(Y)):
        sh = shadows(X, M)
        pr = set(X)
        for r in range(1, M + 1):
            pr = pi(pr)
            for t in (1, 2, 3):
                if not sh[r] <= Nt(pr, t):
                    viol[t] += 1
                    if t == 1 and wit1 is None:
                        wit1 = (tag, M, r, len(sh[r]), len(Nt(pr, 1)))
res['G1'] = (viol[3] == 0 and viol[2] == 0 and viol[1] >= 1)
print("G1 shadow radius: violations t=1: %d, t=2: %d, t=3: %d ; first t=1 witness %s"
      % (viol[1], viol[2], viol[3], wit1))

# ---------------- G2: translate coverings ----------------
g2a = g2b = g2c = g2min = 0
T2 = list(itertools.product((-1, 1), repeat=4))
T3 = list(itertools.product((-2, 0, 2), repeat=4))
T4 = list(itertools.product((-3, 0, 3), repeat=4))
T3bad = list(itertools.product((-2, 2), repeat=4))
for tag, M, P, Y in samples[::3]:
    A = set(P) | set(Y)
    n1 = N1(A)

    def tr(T):
        out = set()
        for t in T:
            out |= {tuple(x[i] + t[i] for i in range(4)) for x in n1}
        return out
    if tr(T2) != Nt(A, 2):
        g2a += 1
    if tr(T3) != Nt(A, 3):
        g2b += 1
    if tr(T4) != Nt(A, 4):
        g2c += 1
    if tr(T3bad) == Nt(A, 3):
        g2min += 1
res['G2'] = (g2a == 0 and g2b == 0 and g2c == 0 and g2min == 0)
print("G2 translate coverings: N_2 by {-1,1}^4 failures %d ; N_3 by {-2,0,2}^4 failures %d ; "
      "N_4 by {-3,0,3}^4 failures %d ; N_3 by only {-2,2}^4 successes %d (must be 0)"
      % (g2a, g2b, g2c, g2min))

# ---------------- G3: THE DECISIVE TEST ----------------
E = {}
for M in range(2, 31):
    zeta = (3 ** (M + 1) - 1) // 2
    z = (zeta,) * 4
    y = (zeta + 8, zeta, zeta, zeta)
    nP = norm_sh({z}, M)
    nPY = norm_sh({z, y}, M)
    E[M] = (nPY - nP, nP, nPY)
slopes = [E[M + 1][0] - E[M][0] for M in range(2, 30)]
monotone = all(s >= 1 for s in slopes)
constant_tail = any(all(E[m][0] == E[M][0] for m in range(M, 31)) for M in range(2, 28))
res['G3'] = monotone and E[30][0] > 258 and not constant_tail
print("G3 DECISIVE: excess E(M) for the all-ones base-3 position, P={z}, Y={z+8e_1}, |Y|=1:")
for M in (2, 5, 10, 20, 29, 30):
    print("    M=%2d  ||P||_sh=%7d  ||PuY||_sh=%7d  E=%6d  E/M=%.2f  ratio=%.4f"
          % (M, E[M][1], E[M][2], E[M][0], E[M][0] / M, E[M][2] / E[M][1]))
print("    slopes E(M+1)-E(M) for M=2..29: min %d max %d (all >= 1: %s); constant tail present: %s; E(30)=%d vs 258"
      % (min(slopes), max(slopes), monotone, constant_tail, E[30][0]))
print("    VERDICT: additive form %s"
      % ("REFUTED" if res['G3'] else ("SUPPORTED" if constant_tail else "neither")))

# S-adv with |Y| > 1, for the record
advr = []
for tag, M, P, Y in samples:
    if tag == "S-adv" and M == 30 and len(Y) > 1:
        nP = norm_sh(set(P), M)
        advr.append(((norm_sh(set(P) | set(Y), M) - nP) / len(Y), norm_sh(set(P) | set(Y), M) / nP))
if advr:
    print("    S-adv at M=30, |Y|>1: max excess per Y-cube %.1f ; max ||PuY||/||P|| %.4f"
          % (max(x[0] for x in advr), max(x[1] for x in advr)))

# ---------------- G4 / G5: the attachment inequality ----------------
c_att5 = 1 + 153664 * RHO
v81 = v6561 = 0
worst = 0.0
for tag, M, P, Y in samples:
    nP = norm_sh(set(P), M)
    nPY = norm_sh(set(P) | set(Y), M)
    if nPY > 81 * nP + c_att5 * len(Y):
        v81 += 1
    if nPY > 6561 * nP + c_att5 * len(Y):
        v6561 += 1
    worst = max(worst, (nPY - c_att5 * len(Y)) / nP)
res['G4'] = (v81 == 0 and v6561 == 0)
res['G5'] = True
print("G4 attachment inequality on %d samples: violations with factor 81: %d ; with session-5's 6561: %d (c_att=%d)"
      % (len(samples), v81, v6561, c_att5))
print("G5 informational: smallest multiplicative factor the samples force = max (||PuY||_sh - c_att*|Y|)/||P||_sh = %.4f"
      % worst)

# ---------------- G6: the price of one extra R-free ring ----------------
g6v = 0
maxlev = 0.0
maxtot = 0.0
for tag, M, P, Y in samples:
    X = set(P) | set(Y)
    shX = shadows(X, M)
    shN = shadows(N1(X), M)
    if len(shN[0]) > 81 * len(shX[0]):
        g6v += 1
    for r in range(1, M + 1):
        if len(shN[r]) > 16 * len(shX[r]):
            g6v += 1
        maxlev = max(maxlev, len(shN[r]) / len(shX[r]))
    s1 = sum(len(shX[r]) for r in range(1, M + 1))
    s2 = sum(len(shN[r]) for r in range(1, M + 1))
    maxtot = max(maxtot, s2 / s1)
res['G6'] = (g6v == 0)
print("G6 ring price: violations of |sh_r(N_1 X)| <= 16|sh_r(X)| (r>=1) or |N_1 X| <= 81|X|: %d ; "
      "max per-level ratio %.4f ; max (sum_{r>=1} sh(N_1X))/(sum_{r>=1} sh(X)) %.4f (PLD §18.4 quotes 82 = 81+1)"
      % (g6v, maxlev, maxtot))

print("RESULTS: " + " ".join(f"{k}:{'PASS' if v else 'FAIL'}" for k, v in sorted(res.items())))
print("OVERALL G " + ("PASS" if all(res.values()) else "FAIL"))
print("secs %.1f" % (time.time() - t0))
