"""checks/tq1_charge.py -- check tq1 for TENTQ.md (session 25).

Criteria: checks/tq1_criteria.md, written BEFORE this script.
Exact Fractions, plain python, single thread, no numpy/BLAS, no numeric lock.

A1  Sum_X Q_X(S) = 0                                   (global neutrality of the box charges)
A2  Q_X(S) = Sum_l <d(ev^{(0->l)} chi5_X), S_l>        (summation-by-parts form of the box charge)
A3  ||d(ev^{(0->l)} chi5_X)||_1 = 2d (n/L^l)^{d-1}     (exact total variation, BFT_B 25.1 (f))
A4  Sum_X chi5_X = 1 and <chi5_X> = n^d                (BFT_B 16.1 (b), 25.1 (f))
A5  Sum_X Q_X Phi(X) = Sum_l <d(ev^{(0->l)} Psi), S_l>, Psi = Sum_X Phi(X) chi5_X   (tent interpolation)
A6  Phi_k(x_0 + d mu)(X) - Phi_k(x_0)(X) = A^{(0->k)}mu(X) - mu(c_X)                (tent-gauge identity)
A7  rebuild of REVIEW_BFT_A_S8 S8-7's exact tent values
A8  informational: max|Phi_k(u)| and its one-coarse-step difference
"""
from fractions import Fraction as F
from itertools import permutations, product

L = 3


# ----------------------------------------------------------------- tents
def sigma5(num, den):
    """sigma_5(t) at t = num/den >= 0, exact."""
    t = F(num, den)
    if t >= 1:
        return F(0)
    return 1 - (10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5)


def per(a, side):
    """periodic distance |a| on Z/side."""
    a %= side
    return min(a, side - a)


def chi5(w, cX, n, side, d):
    v = F(1)
    for nu in range(d):
        v *= sigma5(per(w[nu] - cX[nu], side), n)
        if v == 0:
            return F(0)
    return v


# ----------------------------------------------------------------- lattice ops on a torus
def sites(side, d):
    return list(product(range(side), repeat=d))


def shift(z, mu, s, side, d):
    w = list(z)
    w[mu] = (w[mu] + s) % side
    return tuple(w)


def dstar(v, side, d):
    """(d*v)(z) = sum_mu [v(z-e_mu,mu) - v(z,mu)];  d^T = d* for <d*v,f> = <v,df>."""
    out = {}
    for z in sites(side, d):
        tot = F(0)
        for mu in range(d):
            tot += v.get((shift(z, mu, -1, side, d), mu), F(0)) - v.get((z, mu), F(0))
        if tot:
            out[z] = tot
    return out


def avatar(Y, l, d):
    """level-0 site of the level-l site Y (roots at off(l) = (L^l-1)/2 mod L^l)."""
    off = (L ** l - 1) // 2
    return tuple(off + (L ** l) * Y[nu] for nu in range(d))


# ----------------------------------------------------------------- model builder
def rng(seed):
    x = seed

    def nxt():
        nonlocal x
        x = (1103515245 * x + 12345) % (1 << 31)
        return F((x % 199) - 99, 1 + (x // 199) % 17)
    return nxt


def model(d, k, T, sparse, seed):
    n = L ** k
    side = T * n
    sl = {l: side // L ** l for l in range(k + 1)}          # side of the level-l torus
    nxt = rng(seed)
    S = {}
    for l in range(k):                                       # slots l = 0..k-1
        v = {}
        if sparse:
            pts = [tuple((3 * l + 5 * i + 2 * nu) % sl[l] for nu in range(d)) for i in range(3)]
            for z in pts:
                for mu in range(d):
                    v[(z, mu)] = nxt()
        else:
            for z in sites(sl[l], d):
                for mu in range(d):
                    v[(z, mu)] = nxt()
        S[l] = v
    return n, side, sl, S


def composite_divergence(S, k, sl, side, d):
    """D(S) = d*S_0 + sum_{1<=l<=k-1} ev^{(0->l)T} d*S_l, a level-0 function."""
    D = dict(dstar(S[0], sl[0], d))
    for l in range(1, k):
        for Y, val in dstar(S[l], sl[l], d).items():
            z = avatar(Y, l, d)
            D[z] = D.get(z, F(0)) + val
    return {z: v for z, v in D.items() if v != 0}


def ev_pull(phi0, l, sidel, side, d):
    """ev^{(0->l)} of a level-0 function: the level-l function Y -> phi0(avatar(Y))."""
    return {Y: phi0.get(avatar(Y, l, d), F(0)) for Y in sites(sidel, d)}


def d_of(f, sidel, d):
    out = {}
    for Y in sites(sidel, d):
        for mu in range(d):
            val = f.get(shift(Y, mu, 1, sidel, d), F(0)) - f.get(Y, F(0))
            if val:
                out[(Y, mu)] = val
    return out


def pair(v, w):
    return sum(val * w.get(key, F(0)) for key, val in v.items())


# ----------------------------------------------------------------- Phi_k machinery (d = 4, k = 2)
OFFH = (L - 1) // 2
W1 = F(1, 24 * L ** 4)


def axial(a, b, order):
    out, z = [], list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


HT = {}
for sig in permutations(range(4)):
    for o in product(range(-OFFH, OFFH + 1), repeat=4):
        for (z, c, s) in axial([0] * 4, list(o), sig):
            HT[(z, c)] = HT.get((z, c), F(0)) + s * W1
HT = {kk: vv for kk, vv in HT.items() if vv != 0}


def hfun(w, Y):
    tot = F(0)
    for (z, c), wt in HT.items():
        tot += wt * w.get((tuple(L * Y[i] + OFFH + z[i] for i in range(4)), c), F(0))
    return tot


def qstr(v, targets):
    """one straight-average step, computed only at the given level-(up) sites."""
    out = {}
    for Y in targets:
        for m in range(4):
            tot = F(0)
            for r in product(range(L), repeat=4):
                for j in range(L):
                    z = [L * Y[i] + r[i] for i in range(4)]
                    z[m] += j
                    tot += v.get((tuple(z), m), F(0))
            if tot:
                out[(Y, m)] = tot / L ** 4
    return out


def Phi2(v, X):
    """Phi_2(v)(X) for a level-2 site X, absolute (non-periodic) coordinates."""
    Y1 = tuple(L * X[i] + OFFH for i in range(4))            # level-1 avatar of X
    nb = [tuple(L * X[i] + r[i] for i in range(4)) for r in product(range(L), repeat=4)]
    return hfun(v, Y1) + hfun(qstr(v, nb), X)


def plaq(s, m, nn):
    s = tuple(s)
    sm = list(s); sm[m] += 1
    sn = list(s); sn[nn] += 1
    return {(tuple(sm), nn): F(1), (s, nn): F(-1), (tuple(sn), m): F(-1), (s, m): F(1)}


# ================================================================= run
print("tq1: TENTQ session 25.  criteria: checks/tq1_criteria.md (written first).")
verd = {}

for tag, d, k, T, sparse, seed in [("M1 (d=2,k=2,T=3)", 2, 2, 3, False, 7),
                                   ("M2 (d=4,k=2,T=3)", 4, 2, 3, True, 11)]:
    n, side, sl, S = model(d, k, T, sparse, seed)
    D = composite_divergence(S, k, sl, side, d)
    roots = [avatar(X, k, d) for X in sites(sl[k], d)]
    print(f"\n=== {tag}: n={n}, side={side}, {len(roots)} level-{k} boxes, "
          f"|supp D| = {len(D)} ===")

    # A4
    tot_chi = {}
    chiX = {}
    for cX in roots:
        c = {w: chi5(w, cX, n, side, d) for w in sites(side, d)}
        c = {w: v for w, v in c.items() if v != 0}
        chiX[cX] = c
        for w, v in c.items():
            tot_chi[w] = tot_chi.get(w, F(0)) + v
    a4a = all(tot_chi.get(w, F(0)) == 1 for w in sites(side, d))
    a4b = all(sum(chiX[cX].values()) == n ** d for cX in roots)
    print(f"A4  sum_X chi5_X == 1 everywhere: {a4a};  <chi5_X> == n^d = {n**d}: {a4b}")
    verd[f"A4/{tag}"] = a4a and a4b

    # A1
    QX = {cX: pair(chiX[cX], D) for cX in roots}
    s1 = sum(QX.values())
    print(f"A1  sum_X Q_X = {s1}   (exactly 0: {s1 == 0});  "
          f"max|Q_X| = {float(max(abs(q) for q in QX.values())):.6g}, "
          f"#(Q_X != 0) = {sum(1 for q in QX.values() if q != 0)}")
    verd[f"A1/{tag}"] = (s1 == 0)

    # A2
    bad2 = []
    for cX in roots:
        rhs = F(0)
        for l in range(k):
            evc = ev_pull(chiX[cX], l, sl[l], side, d)
            rhs += pair(d_of(evc, sl[l], d), S[l])
        if rhs != QX[cX]:
            bad2.append((cX, QX[cX], rhs))
    print(f"A2  Q_X == sum_l <d(ev chi5_X), S_l> for all {len(roots)} X: {not bad2}"
          + (f"   FAILURES: {bad2[:3]}" if bad2 else ""))
    verd[f"A2/{tag}"] = not bad2

    # A3
    cX0 = roots[0]
    a3 = True
    for l in range(k + 1):
        evc = ev_pull(chiX[cX0], l, sl[l], side, d)
        tv = sum(abs(v) for v in d_of(evc, sl[l], d).values())
        want = 2 * d * F(n, L ** l) ** (d - 1)
        print(f"A3  l={l}: ||d(ev chi5_X)||_1 = {tv}  vs  2d(n/L^l)^(d-1) = {want}   "
              f"{'OK' if tv == want else 'MISMATCH'}")
        a3 = a3 and (tv == want)
    verd[f"A3/{tag}"] = a3

    # A5
    nxt = rng(seed + 101)
    Phi = {cX: nxt() for cX in roots}
    lhs = sum(QX[cX] * Phi[cX] for cX in roots)
    Psi = {}
    for cX in roots:
        for w, v in chiX[cX].items():
            Psi[w] = Psi.get(w, F(0)) + Phi[cX] * v
    rhs = F(0)
    for l in range(k):
        rhs += pair(d_of(ev_pull(Psi, l, sl[l], side, d), sl[l], d), S[l])
    print(f"A5  sum_X Q_X Phi(X) = {lhs}\n    sum_l <d(ev Psi), S_l>  = {rhs}   "
          f"equal: {lhs == rhs}")
    verd[f"A5/{tag}"] = (lhs == rhs)

# ----------------------------------------------------------------- A6
print("\n=== M3 (d=4, k=2): tent-gauge identity ===")
nxt = rng(29)
mu = {}
for z in product(range(12), repeat=4):
    mu[z] = nxt()
dmu = {}
for z in product(range(-1, 12), repeat=4):
    for c in range(4):
        w = list(z); w[c] += 1
        val = mu.get(tuple(w), F(0)) - mu.get(z, F(0))
        if val:
            dmu[(z, c)] = val
nxt2 = rng(31)
x0 = {}
for z in product(range(12), repeat=4):
    for c in range(4):
        x0[(z, c)] = nxt2()
x0pd = dict(x0)
for key, v in dmu.items():
    x0pd[key] = x0pd.get(key, F(0)) + v

X = (0, 0, 0, 0)
lhs = Phi2(x0pd, X) - Phi2(x0, X)
blk = F(0)
for s in product(range(L ** 2), repeat=4):
    blk += mu.get(s, F(0))
rhs = blk / (L ** 2) ** 4 - mu[(4, 4, 4, 4)]
print(f"A6  Phi_2(x0+dmu)(X) - Phi_2(x0)(X) = {lhs}")
print(f"    A^(0->2)mu(X) - mu(c_X)          = {rhs}")
print(f"    equal: {lhs == rhs};   Phi_2(dmu)(X) alone = {Phi2(dmu, X)} "
      f"(linearity: {Phi2(dmu, X) == lhs})")
verd["A6"] = (lhs == rhs) and (Phi2(dmu, X) == lhs)

# ----------------------------------------------------------------- A7, A8
print("\n=== A7: rebuild of REVIEW_BFT_A_S8 S8-7's exact tent values (d=4, k=2) ===")
cX = (4, 4, 4, 4)
u_raw = plaq([cX[i] + (1, 0, 0, 0)[i] for i in range(4)], 0, 1)
u = {kk: vv / 8 for kk, vv in u_raw.items()}
Y1 = (1, 1, 1, 1)
phi1 = hfun(u, Y1)
nb0 = [tuple(r) for r in product(range(L), repeat=4)]
phi2 = hfun(qstr(u, nb0), (0, 0, 0, 0))
psi = phi1 + phi2
want = {"phi1": F(-1, 432), "phi2": F(-17, 104976), "ratio": F(17, 243), "psi": F(-65, 26244)}
got = {"phi1": phi1, "phi2": phi2, "ratio": phi2 / phi1, "psi": psi}
for key in ("phi1", "phi2", "ratio", "psi"):
    print(f"A7  {key:5s}: got {got[key]}  want {want[key]}   {'OK' if got[key] == want[key] else 'MISMATCH'}")
verd["A7"] = all(got[key] == want[key] for key in want)

print("\n=== A8 (informational): Phi_2(u) across neighbouring level-2 boxes ===")
vals = {X: Phi2(u, X)}
for mu_ in range(4):
    for s in (+1, -1):
        Xn = list(X); Xn[mu_] += s; Xn = tuple(Xn)
        vals[Xn] = Phi2(u, Xn)
mx = max(abs(v) for v in vals.values())
grad = max(abs(vals[X] - v) for Xn, v in vals.items() if Xn != X)
print(f"A8  Phi_2(u)(0) = {vals[X]};  max over the 8 one-step neighbours = "
      f"{max(abs(v) for Xn, v in vals.items() if Xn != X)}")
print(f"A8  max|Phi_2(u)| = {mx};  max one-coarse-step difference = {grad};  "
      f"ratio grad/max = {grad / mx if mx else 'n/a'}")

print("\n=== VERDICTS ===")
for key in sorted(verd):
    print(f"  {key:22s}: {'PASS' if verd[key] else 'FAIL'}")
print(f"  OVERALL: {'ALL PASS' if all(verd.values()) else 'NOT ALL PASS'}")
