"""na55_geo — exact set checks for NODEA55.md (criteria: checks/na55_geo_criteria.md, written first).
Plain python, integers only, seeded RNG. No floats in any verdict."""
import itertools, random, sys, time

t0 = time.time()
L = 3
random.seed(55055)
OFF1 = list(itertools.product((-1, 0, 1), repeat=4))


def pi(X):
    return {tuple(c // L for c in x) for x in X}


def N(X, t):
    offs = list(itertools.product(range(-t, t + 1), repeat=4))
    return {tuple(x[i] + o[i] for i in range(4)) for x in X for o in offs}


def N1(X):
    return {tuple(x[i] + o[i] for i in range(4)) for x in X for o in OFF1}


def Sig(X):
    return N1(pi(X))


def children(x):
    return [tuple(L * x[i] + o[i] for i in range(4)) for o in itertools.product(range(L), repeat=4)]


def col(X):
    return {c for x in X for c in children(x)}


def box_pi(lo, hi):
    return tuple(l // L for l in lo), tuple(h // L for h in hi)


def box_points(lo, hi):
    return set(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(4)]))


def pi_N_box(X, t):
    """pi(N_t(X)) computed as a union over x of pi(box [x-t, x+t]); exact because pi and N_t distribute over unions
    and pi maps an axis box onto the axis box of its corner projections (floor is monotone)."""
    out = set()
    for x in X:
        lo = tuple(c - t for c in x)
        hi = tuple(c + t for c in x)
        plo, phi = box_pi(lo, hi)
        out |= box_points(plo, phi)
    return out


def adv_coord(rng):
    D = rng.randint(3, 12)
    return (3 ** D - 1) // 2 + rng.randint(-2, 2)


def rand_point(rng, adversarial):
    if adversarial:
        return tuple(adv_coord(rng) for _ in range(4))
    return tuple(rng.randint(-200, 200) for _ in range(4))


def star_walk(rng, base, n):
    S = [base]
    while len(S) < n:
        y = rng.choice(S)
        o = rng.choice([o for o in OFF1 if o != (0, 0, 0, 0)])
        z = tuple(y[i] + o[i] for i in range(4))
        if z not in S:
            S.append(z)
    return set(S)


res = {}
# ---------------- G1 ----------------
viol = 0
neg_fired = False
cnt = 0
for u in range(-60, 61):
    for t in range(1, 10):
        for v in range(u - t, u + t + 1):
            cnt += 1
            d = abs(u // 3 - v // 3)
            if d > (t + 2) // 3:
                viol += 1
            if d > (t + 1) // 3:
                neg_fired = True
res['G1'] = (viol == 0)
print("G1: %d (u,v,t) triples, violations of |floor(u/3)-floor(v/3)| <= floor((t+2)/3): %d -> %s"
      % (cnt, viol, "PASS" if viol == 0 else "FAIL"))
print("G1n (control, floor((t+1)/3)): fired = %s" % neg_fired)

# ---------------- G2 ----------------
v_a = v_b = 0
neg2 = 0
ns = 0
direct = 0
for s in range(320):
    rng = random.Random(1000 + s)
    adversarial = (s % 2 == 1)
    k = rng.randint(1, 6)
    X = {rand_point(rng, adversarial) for _ in range(k)}
    piX = pi(X)
    if len(X) <= 2 and s % 4 == 0:
        A = pi(N(X, 8))          # direct materialisation
        direct += 1
    else:
        A = pi_N_box(X, 8)
    if not A <= N(piX, 3):
        v_a += 1
    if not A <= N(piX, 2):
        neg2 += 1
    B = pi_N_box(X, 3) if len(X) > 2 else pi(N(X, 3))
    if not B <= N1(piX):
        v_b += 1
    ns += 1
res['G2'] = (v_a == 0 and v_b == 0)
print("G2: %d samples (%d by direct materialisation); violations (a) pi(N_8 X) <= N_3(pi X): %d, (b) pi(N_3 X) <= N_1(pi X): %d -> %s"
      % (ns, direct, v_a, v_b, "PASS" if res['G2'] else "FAIL"))
print("G2n (control, pi(N_8 X) <= N_2(pi X)): failed on %d samples (control fires iff > 0)" % neg2)

# ---------------- G3 + G4 ----------------
def sig_iter(D, M):
    """[|Sigma^s(D)| for s = 1..M] and the sets."""
    out = []
    cur = set(D)
    sets = []
    for s in range(1, M + 1):
        cur = Sig(cur)
        out.append(len(cur))
        sets.append(cur)
    return out, sets


v3a = v3b = v3c = 0
neg3 = 0
v4 = 0
n3 = 0
maxratio = (0, 1)
for s in range(240):
    rng = random.Random(5000 + s)
    adversarial = (s % 3 == 1)
    n = rng.randint(1, 5)
    M = rng.randint(1, 8)
    base = rand_point(rng, adversarial)
    D = star_walk(rng, base, n)
    X = col(D)
    levels = []
    # level m: pi(N_8(col D)). col(D) is the union over x in D of the boxes [3x, 3x+2]^4, so N_8(col D) is the union of
    # the boxes [3x-8, 3x+10]^4 and pi of a box is the box of the projected corners (floor is monotone): exact.
    lev = set()
    for xx in D:
        lo = tuple(3 * c - 8 for c in xx)
        hi = tuple(3 * c + 2 + 8 for c in xx)
        plo, phi = box_pi(lo, hi)
        lev |= box_points(plo, phi)
    levels.append(lev)
    for r in range(1, M + 1):    # levels m+1 .. m+M
        lev = pi(lev)
        levels.append(lev)
    Csize = sum(len(z) for z in levels)
    sz, sigsets = sig_iter(D, M)
    bound_a = 2401 * n + sum(sz)
    if Csize > bound_a:
        v3a += 1
    if Csize > 81 * n + sum(sz):
        neg3 += 1
    # (b) closed column [D] inside C
    ok_b = D <= levels[0]
    cur = set(D)
    for r in range(1, M + 1):
        cur = pi(cur)
        ok_b = ok_b and (cur <= levels[r])
    if not ok_b:
        v3b += 1
    if Csize > 12401 * n + 10000 * M:
        v3c += 1
    if Csize * maxratio[1] > maxratio[0] * bound_a:
        maxratio = (Csize, bound_a)
    # G4 on the same D
    if pi(N1(col(D))) != N1(D):
        v4 += 1
    n3 += 1
# G4 on arbitrary sets
n4 = 0
for s in range(120):
    rng = random.Random(9000 + s)
    k = rng.randint(1, 5)
    Xs = {rand_point(rng, s % 2 == 1) for _ in range(k)}
    if pi(N1(col(Xs))) != N1(Xs):
        v4 += 1
    n4 += 1
res['G3'] = (v3a == 0 and v3b == 0 and v3c == 0)
res['G4'] = (v4 == 0)
print("G3: %d samples; violations (a) |C| <= 2401n + sum|Sigma^s D|: %d, (b) [D] <= C: %d, (c) |C| <= 12401n + 10000M: %d -> %s"
      % (n3, v3a, v3b, v3c, "PASS" if res['G3'] else "FAIL"))
print("    largest observed |C| / bound_a = %d/%d = %.6f" % (maxratio[0], maxratio[1], maxratio[0] / maxratio[1]))
print("G3n (control, 81 in place of 2401): failed on %d samples (fires iff > 0)" % neg3)
print("G4: %d + %d samples; pi(N_1(col X)) != N_1(X) on %d -> %s" % (n3, n4, v4, "PASS" if res['G4'] else "FAIL"))

# ---------------- G5 ----------------
def sh_norm(X, Mtop):
    """sum_{r=0..Mtop} |Sigma^r(X)|"""
    tot = len(X)
    cur = set(X)
    for r in range(1, Mtop + 1):
        cur = Sig(cur)
        tot += len(cur)
    return tot


v5 = 0
n5 = 0
worst = None
for s in range(240):
    rng = random.Random(13000 + s)
    k = rng.randint(1, 4)
    M = rng.randint(1, 10)
    adversarial = (s % 2 == 1)
    S = list({rand_point(rng, adversarial) for _ in range(k)})
    xS = {rng.choice(children(Q)) for Q in S}
    nS = sh_norm(S, M)            # levels k .. k+M
    nx = sh_norm(xS, M + 1)       # levels k-1 .. k+M
    if nx > 16 * nS + 66 * len(S):
        v5 += 1
    r = (nx - nS) / len(S)
    if worst is None or r > worst:
        worst = r
    n5 += 1


def interval_sig(lo, hi):
    return lo // 3 - 1, hi // 3 + 1


def one_d_sizes(start, M):
    """sizes of the 1D Sigma^r({start}) for r = 0..M (intervals)."""
    lo = hi = start
    out = [1]
    for r in range(1, M + 1):
        lo, hi = interval_sig(lo, hi)
        out.append(hi - lo + 1)
    return out


fam_v = 0
fam_rows = []
conv_ok = {'A': True, 'B': True}
for Dd in range(2, 61):
    w = (3 ** Dd - 1) // 2
    q = 3 * w
    x = 3 * q
    # convention A: ||S|| over r = 0..Dd (levels k..k+Dd), ||x(S)|| over r = 0..Dd+1 (levels k-1..k+Dd)
    sQ = one_d_sizes(q, Dd + 1)
    sx = one_d_sizes(x, Dd + 2)
    nS_A = sum(z ** 4 for z in sQ[:Dd + 1])
    nx_A = sum(z ** 4 for z in sx[:Dd + 2])
    # convention B: one level fewer on both sides
    nS_B = sum(z ** 4 for z in sQ[:Dd])
    nx_B = sum(z ** 4 for z in sx[:Dd + 1])
    if nx_A > 16 * nS_A + 66 or nx_B > 16 * nS_B + 66:
        fam_v += 1
    if nx_A - nS_A != 81 + 175 * Dd:
        conv_ok['A'] = False
    if nx_B - nS_B != 81 + 175 * Dd:
        conv_ok['B'] = False
    if Dd in (2, 3, 10, 30, 60):
        fam_rows.append((Dd, nS_A, nx_A, nx_A - nS_A, nx_B - nS_B))
res['G5'] = (v5 == 0 and fam_v == 0)
print("G5: %d random samples, violations of ||x(S)|| <= 16||S|| + 66|S|: %d; single-cube family D=2..60 violations: %d -> %s"
      % (n5, v5, fam_v, "PASS" if res['G5'] else "FAIL"))
print("    largest random excess per cube (||x(S)||-||S||)/|S| = %.3f" % worst)
for row in fam_rows:
    print("    D=%d: ||S||=%d ||x(S)||=%d excess(A)=%d excess(B)=%d  (81+175D=%d)" % (row + (81 + 175 * row[0],)))
print("G5c (CONFIRMATORY, excess = 81 + 175 D for all D = 2..60): convention A %s, convention B %s"
      % ("REPRODUCES" if conv_ok['A'] else "does not", "REPRODUCES" if conv_ok['B'] else "does not"))
# negative control at D = 20000 (1D intervals; big integers)
Dd = 20000
w = (3 ** Dd - 1) // 2
q = 3 * w
x = 3 * q
lo, hi = q, q
nS = 1
for r in range(1, Dd + 1):
    lo, hi = interval_sig(lo, hi)
    nS += (hi - lo + 1) ** 4
lo, hi = x, x
nx = 1
for r in range(1, Dd + 2):
    lo, hi = interval_sig(lo, hi)
    nx += (hi - lo + 1) ** 4
excess = nx - nS
print("G5n (control): D=20000 single cube: excess ||x(S)|| - ||S|| = %d ; fires (excess > 3073362) = %s ; "
      "16||S||+66 - ||x(S)|| = %d (>= 0 required by G5)" % (excess, excess > 3073362, 16 * nS + 66 - nx))
if 16 * nS + 66 - nx < 0:
    res['G5'] = False
print("SUMMARY:", " ".join("%s=%s" % (k, "PASS" if v else "FAIL") for k, v in res.items()),
      " elapsed %.1fs" % (time.time() - t0))
