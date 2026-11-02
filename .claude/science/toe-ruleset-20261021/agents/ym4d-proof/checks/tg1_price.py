"""checks/tg1_price.py -- check tg1 for TGAUGE_PRICE.md (session 25).

Criteria: checks/tg1_criteria.md, written BEFORE this script. Criteria NOT amended.
Exact Fractions / Python ints, plain python -I, single thread, no numpy/BLAS, no numeric lock.

Z   non-vacuity gate: T_res != 0 and mu not identically 0
A   TGAUGE rebuild:  Phi_k(x0+dmu)(X) - Phi_k(x0)(X) = A^{(0->k)}mu(X) - mu(c_X)
B   the construction: mu_flat, mu_pt in Lambda_* with A^{(0->k)}mu = -Phi_k(x0), Phi_k(x0+dmu)(c_X) = 0
C   THE PRICE:  C1  n^2 <Chat_def, x0> = T_res      (Proposition COF-res, outside formula)
                C2  n^2 <Chat_def, dmu> = -T_res    (for BOTH mu)
D   the invariance: D1 d*C(j) = D(S);  D2 D(S) root-supported and neutral;  D3 <C(j), dmu> = 0
E   estimator ratio rho_est(l) = ||d(A^{(0->l)}mu)||_1 / [(n/L^l)^{d-1} osc_1(nu)]
F   DESIGNED-FAIL CONTROL 1: mu_root outside Lambda_*  -> D3 must FAIL
G   DESIGNED-FAIL CONTROL 2: corrupted root offset off(k):=0 -> A must FAIL
H   reference rebuild of REVIEW_BFT_A_S8 S8-7's four rationals (d=4, k=2)
"""
from fractions import Fraction as F
from itertools import permutations, product

L = 3
OFFH = (L - 1) // 2


# ----------------------------------------------------------------- geometry
def off(l):
    return (L ** l - 1) // 2


def avatar(Y, l, d):
    """level-l site -> its level-0 site."""
    return tuple(off(l) + L ** l * Y[i] for i in range(d))


def relevel(Y, l, m, d):
    """level-l site -> the level-m site (m <= l) with the same level-0 avatar."""
    s = (off(l) - off(m)) // L ** m
    return tuple(s + L ** (l - m) * Y[i] for i in range(d))


def sites(side, d):
    return list(product(range(side), repeat=d))


def shift(z, mu, s, side, d):
    w = list(z)
    w[mu] = (w[mu] + s) % side
    return tuple(w)


def d_of(f, side, d):
    out = {}
    for Y in set(list(f.keys()) + [shift(Y, mu, -1, side, d) for Y in f for mu in range(d)]):
        for mu in range(d):
            val = f.get(shift(Y, mu, 1, side, d), F(0)) - f.get(Y, F(0))
            if val:
                out[(Y, mu)] = val
    return out


def dstar(v, side, d):
    """(d*v)(z) = sum_mu [v(z-e_mu,mu) - v(z,mu)];  <d*v,f> = <v,df>."""
    out = {}
    cand = set()
    for (z, mu) in v:
        cand.add(z)
        cand.add(shift(z, mu, 1, side, d))
    for z in cand:
        tot = F(0)
        for mu in range(d):
            tot += v.get((shift(z, mu, -1, side, d), mu), F(0)) - v.get((z, mu), F(0))
        if tot:
            out[z] = tot
    return out


def pair(v, w):
    return sum(val * w.get(key, F(0)) for key, val in v.items())


def add(a, b, c=F(1)):
    for key, val in b.items():
        a[key] = a.get(key, F(0)) + c * val
    return a


# ----------------------------------------------------------------- Q_str, forward and transpose
def tmult(d):
    """t -> #{(r_m,j) in [0,L)^2 : r_m + j = t}."""
    return {t: L - abs(t - (L - 1)) for t in range(2 * L - 1)}


TM = tmult(0)


def qstr_fwd(w, l, side_l, d):
    """one straight-average step: level-l 1-form -> level-(l+1) 1-form (scatter, exact)."""
    out = {}
    side_u = side_l // L
    for (z, m), v in w.items():
        base = [z[i] // L for i in range(d)]
        t0 = z[m] % L
        for t in (t0, t0 + L):
            if t > 2 * L - 2:
                continue
            Y = list(base)
            Y[m] = ((z[m] - t) // L) % side_u
            key = (tuple(Y), m)
            out[key] = out.get(key, F(0)) + v * F(TM[t], L ** d)
    return {k: v for k, v in out.items() if v != 0}


def qstr_T(psi, l_up, side_up, d):
    """transpose of one step: level-l_up 1-form -> level-(l_up - 1) 1-form (scatter, exact)."""
    out = {}
    side_l = side_up * L
    for (Y, m), v in psi.items():
        for r in product(range(L), repeat=d):
            for j in range(L):
                z = [(L * Y[i] + r[i]) % side_l for i in range(d)]
                z[m] = (z[m] + j) % side_l
                key = (tuple(z), m)
                out[key] = out.get(key, F(0)) + v / L ** d
    return {k: v for k, v in out.items() if v != 0}


def qstr_T_chain(psi, i, sl, d):
    """(Q_str^{(0->i)})^T : level-i 1-form -> level-0 1-form."""
    cur = psi
    for lvl in range(i, 0, -1):
        cur = qstr_T(cur, lvl, sl[lvl], d)
    return cur


def qstr_fwd_chain(v, i, sl, d):
    """Q_str^{(0->i)} : level-0 1-form -> level-i 1-form."""
    cur = v
    for lvl in range(i):
        cur = qstr_fwd(cur, lvl, sl[lvl], d)
    return cur


# ----------------------------------------------------------------- h_i, forward and transpose
def axial(a, b, order):
    out, z = [], list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


def build_HT(d):
    perms = list(permutations(range(d)))
    W = F(1, len(perms) * L ** d)
    HT = {}
    for sig in perms:
        for o in product(range(-OFFH, OFFH + 1), repeat=d):
            for (z, c, s) in axial([0] * d, list(o), sig):
                HT[(z, c)] = HT.get((z, c), F(0)) + s * W
    return {k: v for k, v in HT.items() if v != 0}


def h_fwd(w, Y, HT, side_i, d):
    """h_i(w)(Y): level-i 1-form w, level-(i+1) site Y."""
    tot = F(0)
    for (z, c), wt in HT.items():
        key = (tuple((L * Y[i] + OFFH + z[i]) % side_i for i in range(d)), c)
        tot += wt * w.get(key, F(0))
    return tot


def h_T(f, HT, side_i, d):
    """h_i^T(f): level-(i+1) function f -> level-i 1-form."""
    out = {}
    for Y, a in f.items():
        for (z, c), wt in HT.items():
            key = (tuple((L * Y[i] + OFFH + z[i]) % side_i for i in range(d)), c)
            out[key] = out.get(key, F(0)) + a * wt
    return {k: v for k, v in out.items() if v != 0}


def Phi_all(v, Xs, k, HT, sl, d):
    """{X: Phi_k(v)(X)} for a list of level-k sites; the Q_str chain is built ONCE."""
    tot = {X: F(0) for X in Xs}
    cur = v
    for i in range(k):
        if i:
            cur = qstr_fwd(cur, i - 1, sl[i - 1], d)
        for X in Xs:
            tot[X] += h_fwd(cur, relevel(X, k, i + 1, d), HT, sl[i], d)
    return tot


def Phi_k(v, X, k, HT, sl, d):
    return Phi_all(v, [X], k, HT, sl, d)[X]


# ----------------------------------------------------------------- block averages
def A_blk(mu, l, sl, d, off_l=None):
    """A^{(0->l)}mu: level-0 function -> level-l function (block mean over [L^l Y, L^l Y + L^l)^d).
    off_l is unused for the block itself; it is only passed to the corrupted control."""
    out = {}
    s0 = sl[0]
    for Y in sites(sl[l], d):
        tot = F(0)
        for s in product(range(L ** l), repeat=d):
            tot += mu.get(tuple((L ** l * Y[i] + s[i]) % s0 for i in range(d)), F(0))
        if tot:
            out[Y] = tot / L ** (d * l)
    return out


def A_blk_sparse(mu, l, sl, d):
    """same, computed only where mu can contribute (sparse scatter)."""
    out = {}
    side_u = sl[l]
    for z, v in mu.items():
        Y = tuple((z[i] // L ** l) % side_u for i in range(d))
        out[Y] = out.get(Y, F(0)) + v / L ** (d * l)
    return {k: v for k, v in out.items() if v != 0}


# ----------------------------------------------------------------- tents
def sigma5(num, den):
    t = F(num, den)
    if t >= 1:
        return F(0)
    return 1 - (10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5)


def per(a, side):
    a %= side
    return min(a, side - a)


def chi5(w, cX, n, side, d):
    v = F(1)
    for nu in range(d):
        v *= sigma5(per(w[nu] - cX[nu], side), n)
        if v == 0:
            return F(0)
    return v


# ----------------------------------------------------------------- rng
def rng(seed):
    x = seed

    def nxt():
        nonlocal x
        x = (1103515245 * x + 12345) % (1 << 31)
        return F((x % 199) - 99, 1 + (x // 199) % 17)
    return nxt


# ================================================================= run
print("tg1: TGAUGE_PRICE session 25.  criteria: checks/tg1_criteria.md (written first, not amended).")
verd = {}
info = []

MODELS = [("P1 (d=2,k=2,T=3)", 2, 2, 3, 7),
          ("P2 (d=2,k=3,T=2)", 2, 3, 2, 13),
          ("P3 (d=4,k=1,T=2)", 4, 1, 2, 17),
          ("P4 (d=4,k=2,T=2)", 4, 2, 2, 19)]

for tag, d, k, T, seed in MODELS:
    n = L ** k
    sl = {l: T * L ** (k - l) for l in range(k + 1)}
    HT = build_HT(d)
    Xs = sites(sl[k], d)
    print(f"\n{'='*78}\n=== {tag}: n={n}, level-0 side={sl[0]}, {len(Xs)} level-{k} boxes, "
          f"|HT|={len(HT)} ===")

    # ---------------- test fields -------------------------------------------------
    nxt = rng(seed)
    # x0G: generic sparse pseudo-random level-0 1-form (for the identity clauses A, C, D)
    x0G = {}
    for q in range(6):
        z = tuple((2 * q + 3 * nu + seed) % sl[0] for nu in range(d))
        for m in range(d):
            x0G[(z, m)] = nxt()
    # x0B: support inside the single level-k block X0 = origin (for clause E's scaling)
    X0 = tuple(0 for _ in range(d))
    cX0 = avatar(X0, k, d)
    x0B = {}
    for q in range(3):
        z = tuple((cX0[nu] + ((q + nu) % ((n + 1) // 2))) % sl[0] for nu in range(d))
        for m in range(d):
            x0B[(z, m)] = nxt()

    # ---------------- clause A: TGAUGE rebuild (pseudo-random mu) -----------------
    # mu is pseudo-random at every level-k root (so that the -mu(c_X) term is alive) and at
    # a spread of further pseudo-random sites; sparse so that d = 4, k = 2 stays affordable.
    nxtm = rng(seed + 101)
    muR = {}
    for X in Xs:
        muR[avatar(X, k, d)] = nxtm()
    for q in range(60):
        z = tuple((7 * q + 11 * nu + 3) % sl[0] for nu in range(d))
        muR[z] = nxtm()
    dmuR = d_of(muR, sl[0], d)
    x0pd = add(dict(x0G), dmuR)
    Ak_muR = A_blk(muR, k, sl, d)
    PhA, PhB = Phi_all(x0pd, Xs, k, HT, sl, d), Phi_all(x0G, Xs, k, HT, sl, d)
    badA = []
    for X in Xs:
        lhs = PhA[X] - PhB[X]
        rhs = Ak_muR.get(X, F(0)) - muR.get(avatar(X, k, d), F(0))
        if lhs != rhs:
            badA.append((X, lhs, rhs))
    print(f"A   TGAUGE at every X ({len(Xs)} boxes): {'PASS' if not badA else 'FAIL'}"
          + (f"  first failures {badA[:2]}" if badA else ""))
    verd[f"A/{tag}"] = not badA

    # ---------------- clause G: DESIGNED-FAIL control (corrupted root offset) ------
    # recompute A^{(0->k)} with the block taken at the WRONG origin: blocks [L^k Y - off(k), ...)
    def A_blk_bad(mu, l):
        out = {}
        s0 = sl[0]
        for Y in sites(sl[l], d):
            tot = F(0)
            for s in product(range(L ** l), repeat=d):
                tot += mu.get(tuple((L ** l * Y[i] + s[i] - off(l)) % s0 for i in range(d)), F(0))
            if tot:
                out[Y] = tot / L ** (d * l)
        return out
    Ak_bad = A_blk_bad(muR, k)
    badG = []
    for X in Xs:
        lhs = PhA[X] - PhB[X]
        rhs = Ak_bad.get(X, F(0)) - muR.get(avatar(X, k, d), F(0))
        if lhs != rhs:
            badG.append(X)
    fired = bool(badG)
    print(f"G   CONTROL 2 (off(k):=0 in the block average): clause A then FAILS at "
          f"{len(badG)}/{len(Xs)} boxes -> control {'FIRES (PASS of the control)' if fired else 'DOES NOT FIRE -> clause A has no power over the block convention'}")
    verd[f"G/{tag}"] = fired

    # ---------------- the root charges D and the residue ---------------------------
    for fieldtag, x0 in (("generic", x0G), ("one-block", x0B)):
        nu = {X: -v for X, v in Phi_all(x0, Xs, k, HT, sl, d).items()}
        nu = {X: v for X, v in nu.items() if v != 0}
        # neutral root charge: +1 at X0, -1 at X1, X1 chosen with nu(X1) = 0 if possible
        X1 = [X for X in Xs if X != X0 and nu.get(X, F(0)) == 0]
        X1 = X1[0] if X1 else [X for X in Xs if X != X0][0]
        Droot = {avatar(X0, k, d): F(1, 2), avatar(X1, k, d): F(-1, 2)}
        Tres = n ** 2 * sum(Droot[avatar(X, k, d)] * (-nu.get(X, F(0)))
                            for X in (X0, X1))
        print(f"\n--- field = {fieldtag}: #(nu != 0) = {len(nu)}; "
              f"T_res = {Tres} ({'NONZERO' if Tres != 0 else 'ZERO'})")
        if fieldtag == "generic":
            verd[f"Z/{tag}"] = (Tres != 0)

        # ------------- clause B: construct mu_flat, mu_pt, mu_root -----------------
        scale = 1 / (1 - F(1, L ** (d * k)))
        mu_flat, mu_pt, mu_root = {}, {}, {}
        for X, val in nu.items():
            cX = avatar(X, k, d)
            for s in product(range(L ** k), repeat=d):
                z = tuple((L ** k * X[i] + s[i]) % sl[0] for i in range(d))
                if z != cX:
                    mu_flat[z] = mu_flat.get(z, F(0)) + val * scale
            zp = list(cX); zp[0] = (zp[0] + 1) % sl[0]
            mu_pt[tuple(zp)] = mu_pt.get(tuple(zp), F(0)) + val * L ** (d * k)
            mu_root[cX] = mu_root.get(cX, F(0)) - val * scale
        MUS = [("mu_flat", mu_flat), ("mu_pt", mu_pt)]
        if fieldtag == "generic":
            verd[f"Z-mu/{tag}"] = bool(mu_flat) and bool(mu_pt)

        for mtag, mu in MUS + [("mu_root", mu_root)]:
            Akmu = A_blk_sparse(mu, k, sl, d)
            dmu = d_of(mu, sl[0], d)
            x0g = add(dict(x0), dmu)
            b1 = all(mu.get(avatar(X, k, d), F(0)) == 0 for X in Xs)
            b2 = all(Akmu.get(X, F(0)) == nu.get(X, F(0)) for X in Xs)
            b3 = all(v == 0 for v in Phi_all(x0g, list(nu), k, HT, sl, d).values())
            print(f"B   {mtag:8s}: mu(c_X)==0 everywhere: {b1};  A^(0->k)mu == nu: {b2};  "
                  f"Phi_k(x0+dmu)(c_X)==0 on supp nu: {b3}")
            if mtag != "mu_root" and fieldtag == "generic":
                verd[f"B-{mtag}/{tag}"] = b1 and b2 and b3

        # ------------- clause C: THE PRICE -----------------------------------------
        Cdef = {}
        for i in range(k):
            R = {}
            for X in Xs:
                Y = relevel(X, k, i + 1, d)
                val = Droot.get(avatar(X, k, d), F(0))
                if val:
                    R[Y] = R.get(Y, F(0)) + val
            Cdef = add(Cdef, qstr_T_chain(h_T(R, HT, sl[i], d), i, sl, d))
        c1lhs = n ** 2 * pair(Cdef, x0)
        print(f"C1  n^2 <Chat_def, x0> = {c1lhs};   T_res = {Tres};   "
              f"{'PASS' if c1lhs == Tres else 'FAIL'}")
        if fieldtag == "generic":
            verd[f"C1/{tag}"] = (c1lhs == Tres)
        for mtag, mu in MUS:
            dmu = d_of(mu, sl[0], d)
            c2 = n ** 2 * pair(Cdef, dmu)
            ok = (c2 == -Tres)
            print(f"C2  {mtag:8s}: n^2 <Chat_def, dmu> = {c2};  -T_res = {-Tres};  "
                  f"{'PASS' if ok else 'FAIL'};   rho = |dM|/|T_res| = "
                  f"{abs(c2)/abs(Tres) if Tres else 'n/a'}")
            if fieldtag == "generic":
                verd[f"C2-{mtag}/{tag}"] = ok

        # ------------- clause D: the invariance ------------------------------------
        if k >= 2:
            lj = k - 1
            # a level-(k-1) 1-form whose divergence is a two-root dipole
            Y0 = relevel(X0, k, lj, d)
            Y1 = relevel(X1, k, lj, d)
            j = {}
            zz = list(Y0)
            while zz[0] != Y1[0]:
                stp = 1 if Y1[0] > zz[0] else -1
                w = list(zz)
                if stp < 0:
                    w[0] -= 1
                j[(tuple(x % sl[lj] for x in w), 0)] = F(-stp)
                zz[0] += stp
            for nu_ in range(1, d):
                while zz[nu_] != Y1[nu_]:
                    stp = 1 if Y1[nu_] > zz[nu_] else -1
                    w = list(zz)
                    if stp < 0:
                        w[nu_] -= 1
                    j[(tuple(x % sl[lj] for x in w), nu_)] = F(-stp)
                    zz[nu_] += stp
            dsj = dstar(j, sl[lj], d)
            DS = {}
            for Y, val in dsj.items():
                DS[avatar(Y, lj, d)] = DS.get(avatar(Y, lj, d), F(0)) + val
            DS = {z: v for z, v in DS.items() if v != 0}
            rootset = set(avatar(X, k, d) for X in Xs)
            d2 = all(z in rootset for z in DS) and sum(DS.values()) == 0
            Cj = dict(qstr_T_chain(j, lj, sl, d))
            for i in range(lj):
                up = {}
                for Y, val in dsj.items():
                    Yi = relevel(Y, lj, i + 1, d)
                    up[Yi] = up.get(Yi, F(0)) + val
                Cj = add(Cj, qstr_T_chain(h_T(up, HT, sl[i], d), i, sl, d), F(-1))
            dsC = dstar(Cj, sl[0], d)
            keys = set(dsC) | set(DS)
            d1 = all(dsC.get(z, F(0)) == DS.get(z, F(0)) for z in keys)
            print(f"D1  d*C(j) == D(S) at all {len(keys)} sites: {d1};   "
                  f"D2  D(S) root-supported & neutral: {d2}  (|supp D(S)| = {len(DS)}, "
                  f"sum = {sum(DS.values())})")
            d3 = {}
            for mtag, mu in MUS + [("mu_root", mu_root)]:
                dmu = d_of(mu, sl[0], d)
                v1 = pair(Cj, dmu)
                v2 = pair(dsC, mu)
                d3[mtag] = v1
                print(f"D3  {mtag:8s}: <C(j), dmu> = {v1};  <d*C(j), mu> = {v2};  "
                      f"adjoint OK: {v1 == v2};  zero: {v1 == 0}")
            if fieldtag == "generic":
                verd[f"D1/{tag}"] = d1
                verd[f"D2/{tag}"] = d2
                verd[f"D3/{tag}"] = (d3["mu_flat"] == 0 and d3["mu_pt"] == 0)
                fired_F = (d3["mu_root"] != 0)
                print(f"F   CONTROL 1 (mu_root outside Lambda_*): <C(j), dmu_root> = "
                      f"{d3['mu_root']} -> control "
                      f"{'FIRES (PASS of the control)' if fired_F else 'DOES NOT FIRE -> D3 has no power'}")
                verd[f"F/{tag}"] = fired_F
        else:
            print("D   DEGENERATE at k = 1 (the inner sum over i < k-1 is empty) -- not a PASS")

        # ------------- clause E: estimator ratios ----------------------------------
        if fieldtag == "one-block" or len(nu) > 0:
            osc1 = F(0)
            for X in Xs:
                for m in range(d):
                    Xn = shift(X, m, 1, sl[k], d)
                    osc1 = max(osc1, abs(nu.get(X, F(0)) - nu.get(Xn, F(0))))
            # the tent's own total variation, for the like-for-like comparator (informational).
            # Computed only in d = 2: in d = 4 the chi^5 sum over the torus is not affordable here.
            chiTV = {l: None for l in range(k)}
            if d == 2:
                for l in range(k):
                    Psi = {}
                    for X in nu:
                        cX = avatar(X, k, d)
                        for w in sites(sl[0], d):
                            cv = chi5(w, cX, n, sl[0], d)
                            if cv:
                                Psi[w] = Psi.get(w, F(0)) + nu[X] * cv
                    evP = {Y: Psi.get(avatar(Y, l, d), F(0)) for Y in sites(sl[l], d)}
                    chiTV[l] = sum(abs(v) for v in d_of(evP, sl[l], d).values())
            for mtag, mu in MUS:
                row = []
                for l in range(k):
                    Al = A_blk_sparse(mu, l, sl, d)
                    tv = sum(abs(v) for v in d_of(Al, sl[l], d).values())
                    denom = F(n, L ** l) ** (d - 1) * osc1
                    rho = tv / denom if denom else None
                    row.append((l, tv, rho, tv / chiTV[l] if chiTV[l] else None))
                print(f"E   {mtag:8s} (field {fieldtag}): osc_1(nu) = {osc1}")
                for (l, tv, rho, rtv) in row:
                    print(f"E     l={l}: ||d(A^(0->l)mu)||_1 = {tv}   rho_est = "
                          f"{float(rho) if rho is not None else 'n/a'}"
                          f"   [informational: /tent TV = {float(rtv) if rtv is not None else 'n/a'}"
                          f", 2d = {2*d}, L^(k-l) = {L**(k-l)}]")
                if fieldtag == "one-block":
                    ei = all(r[2] is not None and r[2] >= 1 for r in row)
                    if mtag == "mu_flat":
                        eii = all(r[2] <= 2 * d for r in row)
                        verd[f"E-i-flat/{tag}"] = ei
                        verd[f"E-ii-flat/{tag}"] = eii
                        print(f"E   mu_flat: (i) rho_est >= 1 everywhere: {ei};  "
                              f"(ii) rho_est <= 2d = {2*d} everywhere: {eii}")
                    else:
                        eiii = all(r[2] >= L ** (k - r[0]) for r in row)
                        verd[f"E-i-pt/{tag}"] = ei
                        verd[f"E-iii-pt/{tag}"] = eiii
                        print(f"E   mu_pt:   (i) rho_est >= 1 everywhere: {ei};  "
                              f"(iii) rho_est >= L^(k-l) everywhere: {eiii}")

# ----------------------------------------------------------------- clause H
print(f"\n{'='*78}\n=== H: rebuild of REVIEW_BFT_A_S8 S8-7's exact rationals (d=4, k=2) ===")
d, k, T = 4, 2, 2
sl = {l: T * L ** (k - l) for l in range(k + 1)}
HT4 = build_HT(4)
X = (0, 0, 0, 0)
cX = avatar(X, k, d)


def plaq(s, m, nn, side):
    s = tuple(x % side for x in s)
    sm = list(s); sm[m] = (sm[m] + 1) % side
    sn = list(s); sn[nn] = (sn[nn] + 1) % side
    return {(tuple(sm), nn): F(1), (s, nn): F(-1), (tuple(sn), m): F(-1), (s, m): F(1)}


u = {kk: vv / 8 for kk, vv in plaq([cX[i] + (1, 0, 0, 0)[i] for i in range(4)], 0, 1, sl[0]).items()}
phi1 = h_fwd(u, relevel(X, k, 1, d), HT4, sl[0], d)
phi2 = h_fwd(qstr_fwd(u, 0, sl[0], d), relevel(X, k, 2, d), HT4, sl[1], d)
want = {"phi1": F(-1, 432), "phi2": F(-17, 104976), "ratio": F(17, 243), "Phi_2": F(-65, 26244)}
got = {"phi1": phi1, "phi2": phi2, "ratio": phi2 / phi1, "Phi_2": phi1 + phi2}
for key in ("phi1", "phi2", "ratio", "Phi_2"):
    print(f"H   {key:6s}: got {got[key]}   want {want[key]}   "
          f"{'OK' if got[key] == want[key] else 'MISMATCH'}")
verd["H"] = all(got[key] == want[key] for key in want)
print(f"H   Phi_k(u) at the 2d one-coarse-step neighbours of X: "
      f"{[Phi_k(u, shift(X, m, s, sl[k], d), k, HT4, sl, d) for m in range(4) for s in (1, -1)]}")

print(f"\n{'='*78}\n=== VERDICTS ===")
for key in sorted(verd):
    print(f"  {key:26s}: {'PASS' if verd[key] else 'FAIL'}")
print(f"  OVERALL: {'ALL PASS' if all(verd.values()) else 'NOT ALL PASS'}")
print(f"  FAILS: {[k for k, v in verd.items() if not v]}")
