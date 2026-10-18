#!/usr/bin/env python3
"""Fresh-context reviewer check (own code) of X5/X6 (exact mod Gauss), X9/X10, X12b, X13, Y7 of
scripts/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18.py.

Own engines, not imported from the runner or the upstream runner:
 * a sparse exact (Fraction) quadratic Poisson engine with named variables, {q, p} = +1;
 * mod Gauss = restriction of the E-covector of each bilinear E.A coefficient to ker(div), with ker(div)
   from a sympy nullspace (the runner instead parametrises E = curl^T b + h);
 * Maxwell bracket from the closed formula derived by hand here:
   coefficient of N_s M_t in {H(N), H(M)} is  B_st = diag(u_.t) D^T diag(w_.s) D - diag(u_.s) D^T diag(w_.t) D
   (as an E_l A_b bilinear), computed with dense integer numpy for the translation-invariant classification;
 * gravity clauses (kin, R1, G_g) re-typed from the 09-24 / upstream definitions (they are supplied premises),
   evaluated by the own engine.
"""
import random
import sys
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

PAIRS = ((0, 1), (0, 2), (1, 2))
out = {}


def rep(name, ok, detail=""):
    out[name] = bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)


# =============================================================== lattice geometry (own)
class Geo:
    def __init__(s, L):
        s.L = L
        s.sites = list(itertools.product(range(L), repeat=3))
        s.si = {x: i for i, x in enumerate(s.sites)}
        s.links = [(x, j) for x in s.sites for j in range(3)]
        s.li = {l: i for i, l in enumerate(s.links)}
        s.plaqs = [(y, ij) for y in s.sites for ij in PAIRS]
        s.pi = {p: i for i, p in enumerate(s.plaqs)}
        nL, nP, nS = len(s.links), len(s.plaqs), len(s.sites)
        s.D = np.zeros((nP, nL), dtype=np.int64)
        for p, (y, (i, j)) in enumerate(s.plaqs):
            s.D[p, s.li[(s.sh(y, i), j)]] += 1
            s.D[p, s.li[(y, j)]] -= 1
            s.D[p, s.li[(s.sh(y, j), i)]] -= 1
            s.D[p, s.li[(y, i)]] += 1
        s.div = np.zeros((nS, nL), dtype=np.int64)
        for x in s.sites:
            for j in range(3):
                s.div[s.si[x], s.li[(x, j)]] += 1
                s.div[s.si[x], s.li[(s.sh(x, j, -1), j)]] -= 1

    def sh(s, x, j, d=1):
        return tuple((x[k] + (d if k == j else 0)) % s.L for k in range(3))

    def corners(s, p):
        y, (i, j) = s.plaqs[p]
        return {"00": y, "10": s.sh(y, i), "01": s.sh(y, j), "11": s.sh(s.sh(y, i), j)}

    def bond(s, a, b):
        d = [(a[k] - b[k]) % s.L for k in range(3)]
        nz = [k for k in range(3) if d[k]]
        return len(nz) == 1 and d[nz[0]] in (1, s.L - 1)


def kernel_div(g):
    M = sp.Matrix(g.div.tolist())
    ns = M.nullspace()
    cols = []
    for v in ns:
        den = sp.ilcm(*[sp.fraction(e)[1] for e in v])
        cols.append([int(e * den) for e in v])
    return np.array(cols, dtype=np.int64).T  # nL x dim


# =============================================================== X5 own: translation-invariant classification at L=4
def x5(L=4):
    g = Geo(L)
    K = kernel_div(g)
    rep("own X0 dim ker div = 2L^3+1", K.shape[1] == 2 * L ** 3 + 1, f"{K.shape}")
    nS, nL, nP = len(g.sites), len(g.links), len(g.plaqs)
    # monomials: u_(axis, end) x w_(plane, corner)
    uk = [(j, e) for j in range(3) for e in (0, 1)]
    wk = [(ij, c) for ij in PAIRS for c in ("00", "10", "01", "11")]
    Umat = {}
    for (j, e) in uk:
        U = np.zeros((nL, nS), dtype=np.int64)
        for l, (x, jj) in enumerate(g.links):
            if jj == j:
                U[l, g.si[x if e == 0 else g.sh(x, j)]] = 1
        Umat[(j, e)] = U
    Wmat = {}
    for (ij, c) in wk:
        W = np.zeros((nP, nS), dtype=np.int64)
        for p, (y, pl) in enumerate(g.plaqs):
            if pl == ij:
                W[p, g.si[g.corners(p)[c]]] = 1
        Wmat[(ij, c)] = W
    s0 = (0, 0, 0)
    targets = [t for t in g.sites if t != s0 and not g.bond(s0, t)]
    rows_ex, rows_g = [], []
    DT = g.D.T
    nonzero_pairs = set()
    for t in targets:
        si, ti = g.si[s0], g.si[t]
        blocks_ex, blocks_g = [], []
        for a in uk:
            for b in wk:
                U, W = Umat[a], Wmat[b]
                B = (U[:, ti][:, None] * (DT @ (W[:, si][:, None] * g.D))) - (U[:, si][:, None] * (DT @ (W[:, ti][:, None] * g.D)))
                blocks_ex.append(B.reshape(-1))
                blocks_g.append((K.T @ B).reshape(-1))
                if B.any():
                    nonzero_pairs.add(t)
        rows_ex.append(np.stack(blocks_ex, axis=1))
        rows_g.append(np.stack(blocks_g, axis=1))
    diag = {t for t in targets if sum(1 for k in range(3) if t[k] % L) == 2 and all(t[k] % L in (0, 1, L - 1) for k in range(3))}
    rep("own: only plaquette-diagonal lapse pairs can appear (L=4)", nonzero_pairs <= diag and len(diag) == 12, f"{len(nonzero_pairs)} non-bond pairs from origin carry monomials")
    usym = {k: sp.Symbol(f"u{k[0]}{'th'[k[1]]}") for k in uk}
    wsym = {k: sp.Symbol(f"w{k[0][0]}{k[0][1]}_{k[1]}") for k in wk}
    mon = [usym[a] * wsym[b] for a in uk for b in wk]
    norm = [usym[(j, 0)] + usym[(j, 1)] - 1 for j in range(3)] + [sum(wsym[(ij, c)] for c in ("00", "10", "01", "11")) - 1 for ij in PAIRS]
    sols = {}
    for label, rows in (("exact", rows_ex), ("mod Gauss", rows_g)):
        R = np.concatenate(rows, axis=0)
        R = R[np.any(R != 0, axis=1)]
        R = np.unique(R, axis=0)
        Ms = sp.Matrix(R.tolist())
        rref, piv = Ms.T.rref()  # pivot columns of R^T = independent rows of R
        basis = [Ms.row(i) for i in piv]
        eqs = [sum(int(r[c]) * mon[c] for c in range(len(mon))) for r in basis]
        sol = sp.solve(eqs + norm, list(usym.values()) + list(wsym.values()), dict=True)
        sols[label] = (len(basis), sol)
    def describe(sol):
        outl = []
        for s in sol:
            if len(s) != 18:
                return None
            ax = tuple("t" if s[usym[(j, 0)]] == 1 and s[usym[(j, 1)]] == 0 else ("h" if s[usym[(j, 1)]] == 1 and s[usym[(j, 0)]] == 0 else "?") for j in range(3))
            pc = tuple([c for c in ("00", "10", "01", "11") if s[wsym[(ij, c)]] == 1][0] if sum(s[wsym[(ij, c)]] for c in ("00", "10", "01", "11")) == 1 and all(s[wsym[(ij, c)]] in (0, 1) for c in ("00", "10", "01", "11")) else "?" for ij in PAIRS)
            outl.append((ax, pc))
        return sorted(outl)
    exp = []
    for ax in itertools.product("th", repeat=3):
        pc = tuple(("0" if ax[i] == "t" else "1") + ("0" if ax[j] == "t" else "1") for (i, j) in PAIRS)
        exp.append((ax, pc))
    exp = sorted(exp)
    de, dg = describe(sols["exact"][1]), describe(sols["mod Gauss"][1])
    rep("own X5 exact: 8 one-sided classes, matching corners", de == exp, f"{sols['exact'][0]} independent conditions; {len(sols['exact'][1])} solutions")
    rep("own X5 mod Gauss: same 8 classes", dg == exp, f"{sols['mod Gauss'][0]} independent conditions; {len(sols['mod Gauss'][1])} solutions")
    return g, K


def _independent_rows(Ms):
    # greedy exact row basis
    basis_idx, red = [], []
    for i in range(Ms.rows):
        cand = Ms[i:i + 1, :]
        test = sp.Matrix.vstack(*(red + [cand])) if red else cand
        if test.rank() > len(red):
            red.append(cand)
            basis_idx.append(i)
    return basis_idx


# =============================================================== X6 own: position-dependent timings, sparse exact
def pair_coeffs(g, U, W):
    """U: list over links of {site: Fr}, W: list over plaquettes of {site: Fr}. returns {(s,t): {(l,b): Fr}} coefficient of N_s M_t."""
    Dp = [{l: int(g.D[p, l]) for l in np.nonzero(g.D[p])[0]} for p in range(len(g.plaqs))]
    inc = {}
    for p, d in enumerate(Dp):
        for l in d:
            inc.setdefault(l, []).append(p)
    co = {}

    def add(s, t, key, v):
        d = co.setdefault((s, t), {})
        d[key] = d.get(key, 0) + v
    for l in range(len(g.links)):
        for p in inc[l]:
            for s, ws in W[p].items():
                for t, ut in U[l].items():
                    for b, db in Dp[p].items():
                        v = Dp[p][l] * db * ws * ut
                        add(s, t, (l, b), v)     # + w_ps u_lt
                        add(t, s, (l, b), -v)    # - u_l(s') w_p(t') with s'=t, t'=s
    return {k: {kk: vv for kk, vv in d.items() if vv != 0} for k, d in co.items()}


def nonbond_count(g, K, co, gauss):
    bad = 0
    for (s, t), d in co.items():
        if s == t or g.bond(s, t) or not d:
            continue
        if gauss:
            # columns b: E-covector c_l ; need K^T c = 0 for each b
            byb = {}
            for (l, b), v in d.items():
                byb.setdefault(b, {})[l] = v
            alive = False
            for b, cv in byb.items():
                ls = list(cv)
                vec = np.array([[float(cv[l])] for l in ls])
                # exact: integer combination check with Fractions
                tot = [sum(Fr(int(K[l, c])) * cv[l] for l in ls) for c in range(K.shape[1])]
                if any(x != 0 for x in tot):
                    alive = True
                    break
            if not alive:
                continue
        bad += 1
    return bad


OPP = {"00": "11", "11": "00", "10": "01", "01": "10"}


def allowed_corners(g, U, p, Dp_links):
    cs = g.corners(p)
    inv = {v: k for k, v in cs.items()}
    covered = {inv[s] for l in Dp_links[p] for s in U[l]}
    return [n for n in cs if OPP[n] not in covered]


def x6(g, K, nsamp=12, seed=7):
    rng = random.Random(seed)
    Dp_links = [list(np.nonzero(g.D[p])[0]) for p in range(len(g.plaqs))]
    inc = {}
    for p, ls in enumerate(Dp_links):
        for l in ls:
            inc.setdefault(l, []).append(p)
    good, viol, nb2 = 0, 0, 0
    tries = 0
    while good < nsamp:
        tries += 1
        # plaquette-first generator (different from the runner's link-first sweep):
        # start from a random one-sided orientation per axis, then make random links two-sided whenever all
        # their plaquettes keep a nonempty allowed set; then pick random weights on allowed corners.
        ori = [rng.choice((0, 1)) for _ in range(3)]
        U = [{(x if ori[j] == 0 else g.sh(x, j)): Fr(1)} for (x, j) in g.links]
        order = list(range(len(g.links)))
        rng.shuffle(order)
        for l in order[: len(order) // 3]:
            x, j = g.links[l]
            choice = rng.random()
            new = {x: Fr(1, 3), g.sh(x, j): Fr(2, 3)} if choice < 0.5 else ({g.sh(x, j): Fr(1)} if ori[j] == 0 else {x: Fr(1)})
            old = U[l]
            U[l] = new
            if not all(allowed_corners(g, U, p, Dp_links) for p in inc[l]):
                U[l] = old
        W = []
        for p in range(len(g.plaqs)):
            al = allowed_corners(g, U, p, Dp_links)
            k = rng.randint(1, len(al))
            pick = rng.sample(al, k)
            wts = [Fr(rng.randint(1, 5)) for _ in pick]
            W.append({g.corners(p)[n]: w_ / sum(wts) for n, w_ in zip(pick, wts)})
        nb2 += sum(len(u) == 2 for u in U)
        co = pair_coeffs(g, U, W)
        if nonbond_count(g, K, co, gauss=False) == 0:
            good += 1
        else:
            print("rule-obeying sample failed!", flush=True)
            good += 1
            viol -= 100
        # violation: move half the weight of a random plaquette onto a forbidden corner (if any)
        cand = [p for p in range(len(g.plaqs)) if len(allowed_corners(g, U, p, Dp_links)) < 4]
        p = rng.choice(cand)
        cs = g.corners(p)
        forb = [n for n in cs if n not in allowed_corners(g, U, p, Dp_links)]
        n = rng.choice(forb)
        W2 = list(W)
        W2[p] = {k_: v / 2 for k_, v in W[p].items()}
        W2[p][cs[n]] = W2[p].get(cs[n], 0) + Fr(1, 2)
        co2 = pair_coeffs(g, U, W2)
        viol += nonbond_count(g, K, co2, gauss=True) > 0
    rep("own X6 local rule: rule-obeying random position-dependent timings are bond-supported; single violations fail mod Gauss",
        viol == nsamp, f"{nsamp} obeying samples (mean {nb2 / nsamp:.1f} two-sided links), {viol}/{nsamp} violations fail mod Gauss")


# =============================================================== X9/X10, X13 own: induced generators
def induced(g, co, c=Fr(1)):
    """X_(s,i) = B_{s, s+i} / c  (from bracket = sum_b xi~_b (-c) X_b, xi~_b = N_(s+i) M_s - N_s M_(s+i))."""
    X = {}
    for s in g.sites:
        for i in range(3):
            X[(s, i)] = {k: v / c for k, v in co.get((s, g.sh(s, i)), {}).items()}
    return X


def x9_x13(g, K):
    # forward timing
    U = [{x: Fr(1)} for (x, j) in g.links]
    W = [{g.plaqs[p][0]: Fr(1)} for p in range(len(g.plaqs))]
    co = pair_coeffs(g, U, W)
    Xf = induced(g, co)
    ok = nonbond_count(g, K, co, False) == 0
    # stated G_A[xi] = sum xi_(y,i) sum_{j != i} E_(y+i,j) F_ij(y),  F_ij = -F_ji
    for y in g.sites:
        for i in range(3):
            exp = {}
            for j in range(3):
                if j == i:
                    continue
                ij = (min(i, j), max(i, j))
                sg = 1 if i < j else -1
                p = g.pi[(y, ij)]
                l = g.li[(g.sh(y, i), j)]
                for b in np.nonzero(g.D[p])[0]:
                    exp[(l, b)] = exp.get((l, b), 0) + sg * int(g.D[p, b])
            exp = {k: Fr(v) for k, v in exp.items() if v}
            ok &= exp == Xf[(y, i)]
    # antisymmetry consistency: B_{s+i,s} = -B_{s,s+i}
    ok &= all({k: -v for k, v in co.get((g.sh(s, i), s), {}).items()} == co.get((s, g.sh(s, i)), {}) for s in g.sites for i in range(3))
    rep("own X9/X10 forward timing: bracket = G_A[-c xi~] bond by bond with the stated G_A (L=4)", ok)
    # staggered
    par = 0
    Us = [{x: Fr(1)} if sum(x) % 2 == par else {g.sh(x, j): Fr(1)} for (x, j) in g.links]
    Ws = [{s: Fr(1, 2) for s in g.corners(p).values() if sum(s) % 2 != par} for p in range(len(g.plaqs))]
    cos = pair_coeffs(g, Us, Ws)
    nb = nonbond_count(g, K, cos, False)
    rep("own X8 staggered timing bond-supported exactly (L=4)", nb == 0, f"non-bond pairs: {nb}")
    Xs = induced(g, cos)
    # X13 content: with any bond-supported bracket, closure relative to the induced generator is automatic. Here we test
    # what is NOT automatic: does the induced generator at uniform xi = e_0 act on A as a translation + gauge?
    nL = len(g.links)
    T = np.zeros((nL, nL))
    for s in g.sites:
        for (l, b), v in Xs[(s, 0)].items():
            T[l, b] += float(v)  # {A_l, G'} = dG'/dE_l = sum_b T_lb A_b
    Tf = np.zeros((nL, nL))
    for s in g.sites:
        for (l, b), v in Xf[(s, 0)].items():
            Tf[l, b] += float(v)
    return T, Tf, Us, Ws


def stag_generator_smooth(L=16):
    """floating point: action of the induced staggered generator at uniform xi = e_0 on the field strength of a smooth A."""
    g = Geo(L)
    par = 0
    Us = [{x: Fr(1)} if sum(x) % 2 == par else {g.sh(x, j): Fr(1)} for (x, j) in g.links]
    Ws = [{s: Fr(1, 2) for s in g.corners(p).values() if sum(s) % 2 != par} for p in range(len(g.plaqs))]
    cos = pair_coeffs(g, Us, Ws)
    Xs = induced(g, cos)
    nL = len(g.links)
    T = np.zeros((nL, nL))
    for s in g.sites:
        for (l, b), v in Xs[(s, 0)].items():
            T[l, b] += float(v)
    U = [{x: Fr(1)} for (x, j) in g.links]
    W = [{g.plaqs[p][0]: Fr(1)} for p in range(len(g.plaqs))]
    Xf = induced(g, pair_coeffs(g, U, W))
    Tf = np.zeros((nL, nL))
    for s in g.sites:
        for (l, b), v in Xf[(s, 0)].items():
            Tf[l, b] += float(v)
    A = np.zeros(nL)
    k = 2 * np.pi / L
    for l, (x, j) in enumerate(g.links):
        A[l] = [np.sin(k * x[0] + 2 * k * x[1]), np.cos(k * x[2] - k * x[0]), np.sin(k * (x[0] + x[1] + x[2]))][j]
    Fs, Ff = g.D @ (T @ A), g.D @ (Tf @ A)
    # continuum-like reference: exact translation of F by -1 along e0 (backward difference); compare smooth & staggered parts
    return {"|D T_stag A|/|D T_fwd A|": np.linalg.norm(Fs) / np.linalg.norm(Ff),
            "|stag - fwd|/|fwd|": np.linalg.norm(Fs - Ff) / np.linalg.norm(Ff)}


# =============================================================== own quadratic Poisson engine (X12b, Y7)
CONJ = {"hd": "Pd", "hf": "Pf", "phi": "pi", "A": "E"}
PCONJ = {v: k for k, v in CONJ.items()}


def padd(a, b, s=1):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, 0) + s * v
        if o[k] == 0:
            del o[k]
    return o


def mono(*names):
    return tuple(sorted(names, key=repr))


def deriv(poly, var):
    o = {}
    for m, c in poly.items():
        cnt = m.count(var)
        if not cnt:
            continue
        rest = list(m)
        rest.remove(var)
        k = tuple(rest)
        o[k] = o.get(k, 0) + c * cnt
    return o


def lmul(a, b):
    o = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            k = mono(*(m1 + m2))
            o[k] = o.get(k, 0) + c1 * c2
    return {k: v for k, v in o.items() if v}


def vars_of(*polys):
    vs = set()
    for p in polys:
        for m in p:
            vs.update(m)
    return vs


def pb(F, G):
    o = {}
    qs = {v for v in vars_of(F, G) if v[0] in CONJ} | {(PCONJ[v[0]],) + v[1:] for v in vars_of(F, G) if v[0] in PCONJ}
    for q in qs:
        p = (CONJ[q[0]],) + q[1:]
        o = padd(o, lmul(deriv(F, q), deriv(G, p)))
        o = padd(o, lmul(deriv(F, p), deriv(G, q)), -1)
    return o


class Lat:
    def __init__(s, L, alpha=Fr(3, 7), K=Fr(5, 11), mu=Fr(2, 3)):
        s.L, s.al, s.K, s.mu = L, alpha, K, mu
        s.sites = list(itertools.product(range(L), repeat=3))

    def sh(s, x, j, d=1):
        return tuple((x[k] + (d if k == j else 0)) % s.L for k in range(3))


def kin(l, n):
    o = {}
    for x in l.sites:
        for j in range(3):
            o = padd(o, {mono(("Pd", x, j), ("Pd", x, j)): n[x] / (4 * l.al)})
        for j in range(3):
            for k in range(3):
                o = padd(o, {mono(("Pd", x, j), ("Pd", x, k)): -Fr(1, 2) * n[x] / (4 * l.al)})
    for y in l.sites:
        for (i, j) in PAIRS:
            c4 = [y, l.sh(y, i), l.sh(y, j), l.sh(l.sh(y, i), j)]
            o = padd(o, {mono(("Pf", y, (i, j)), ("Pf", y, (i, j))): sum(n[z] for z in c4) / 4 / (8 * l.al)})
    return o


def r1(l, n):
    o = {}
    for x in l.sites:
        sec = [n[l.sh(x, i)] - 2 * n[x] + n[l.sh(x, i, -1)] for i in range(3)]
        for j in range(3):
            o = padd(o, {(("hd", x, j),): -sum(sec) + sec[j]})
    for y in l.sites:
        for (i, j) in PAIRS:
            mx = n[y] - n[l.sh(y, i)] - n[l.sh(y, j)] + n[l.sh(l.sh(y, i), j)]
            o = padd(o, {(("hf", y, (i, j)),): 2 * mx})
    return o


def gg(l, xi):
    o = {}
    for x in l.sites:
        for j in range(3):
            o = padd(o, {(("Pd", x, j),): 2 * (xi[(x, j)] - xi[(l.sh(x, j, -1), j)])})
    for y in l.sites:
        for (i, j) in PAIRS:
            o = padd(o, {(("Pf", y, (i, j)),): xi[(l.sh(y, i), j)] - xi[(y, j)] + xi[(l.sh(y, j), i)] - xi[(y, i)]})
    return o


def hscal(l, n, cs):
    o = {}
    for x in l.sites:
        o = padd(o, {mono(("pi", x), ("pi", x)): n[x] / 2, mono(("phi", x), ("phi", x)): n[x] * l.mu / 2})
        for j in range(3):
            y = l.sh(x, j)
            wt = (n[x] + n[y]) / 2 * cs[j] / 2
            o = padd(o, {mono(("phi", y), ("phi", y)): wt, mono(("phi", x), ("phi", x)): wt, mono(("phi", x), ("phi", y)): -2 * wt})
    return o


def gscal(l, xi):
    o = {}
    for x in l.sites:
        for j in range(3):
            v = xi[(x, j)]
            if not v:
                continue
            y = l.sh(x, j)
            for f, sf in ((("phi", y), 1), (("phi", x), -1)):
                for p in (("pi", x), ("pi", y)):
                    o = padd(o, {mono(f, p): v * sf * Fr(1, 2)})
    return o


def Fp(l, y, i, j):
    return {(("A", l.sh(y, i), j),): 1, (("A", y, j),): -1, (("A", l.sh(y, j), i),): -1, (("A", y, i),): 1}


def hem(l, n, cb, g2):
    o = {}
    for x in l.sites:
        for j in range(3):
            o = padd(o, {mono(("E", x, j), ("E", x, j)): n[x] * g2 / 2})
    for y in l.sites:
        for (i, j) in PAIRS:
            f = Fp(l, y, i, j)
            o = padd(o, {k: v * n[y] * cb / (2 * g2) for k, v in lmul(f, f).items()})
    return o


def gA(l, xi):
    o = {}
    for y in l.sites:
        for i in range(3):
            v = xi[(y, i)]
            if not v:
                continue
            for j in range(3):
                if j == i:
                    continue
                f = Fp(l, y, min(i, j), max(i, j)) if i < j else {k: -c for k, c in Fp(l, y, min(i, j), max(i, j)).items()}
                o = padd(o, {k: c * v for k, c in lmul({(("E", l.sh(y, i), j),): 1}, f).items()})
    return o


def solve_exact(target, cols):
    """is target in span(cols)? own Fraction Gaussian elimination over monomial keys."""
    keys = sorted(set(target) | set().union(*[set(c) for c in cols]), key=repr)
    kid = {k: i for i, k in enumerate(keys)}
    rows = []  # pivot rows: dict col->val, keyed by pivot monomial
    piv = {}
    def reduce(vec):
        vec = dict(vec)
        changed = True
        while True:
            ks = [k for k in piv if k in vec]  # earliest-inserted pivot first (terminates)
            if not ks:
                return vec
            k = ks[0]
            pv = piv[k]
            f = vec[k] / pv[k]
            for kk, vv in pv.items():
                vec[kk] = vec.get(kk, 0) - f * vv
                if vec[kk] == 0:
                    del vec[kk]
    for c in cols:
        r = reduce(c)
        if r:
            k = min(r, key=lambda z: kid[z])
            piv[k] = r
    return not reduce(target)


def unitb(l, x, j):
    return {(z, k): (Fr(1) if (z, k) == (x, j) else Fr(0)) for z in l.sites for k in range(3)}


def xtil(l, n, m):
    return {(x, j): n[l.sh(x, j)] * m[x] - n[x] * m[l.sh(x, j)] for x in l.sites for j in range(3)}


def x12b_y7():
    l = Lat(3)
    rng = random.Random(99)
    n = {x: Fr(rng.randint(-3, 3)) for x in l.sites}
    m = {x: Fr(rng.randint(-3, 3)) for x in l.sites}
    kap = l.K / (4 * l.al)
    xt = xtil(l, n, m)
    # gravity alone (09-24 T1, both signs) with own engine
    okT1 = True
    for s in (-1, 1):
        b = pb(padd(kin(l, n), r1(l, n), s * l.K), padd(kin(l, m), r1(l, m), s * l.K))
        okT1 &= b == gg(l, {k: s * kap * v for k, v in xt.items()})
    rep("own 09-24 T1 reproduced: {C_g(N),C_g(M)} = G_g[(sK/4alpha) xi~] (L=3, both s)", okT1)
    gb = pb(padd(kin(l, n), r1(l, n), -l.K), padd(kin(l, m), r1(l, m), -l.K))
    UB = [unitb(l, x, j) for x in l.sites for j in range(3)]
    # Y7: anisotropic scalar
    cs0 = (Fr(7, 5), Fr(7, 5), Fr(2, 9))
    okb = pb(hscal(l, n, cs0), hscal(l, m, cs0)) == gscal(l, {k: -cs0[k[1]] * v for k, v in xt.items()})
    rep("own Y7 per-axis scalar bracket = G_m[-c_j xi~] exactly", okb)
    cols = [padd(gg(l, u), gscal(l, u)) for u in UB]
    tab = {}
    for cs in ((kap,) * 3, (kap, kap, 2 * kap), (2 * kap, kap, kap), (kap, 2 * kap, kap), (kap / 2,) * 3, (kap, kap, kap / 3)):
        tab[tuple(str(c / kap) for c in cs)] = solve_exact(padd(gb, pb(hscal(l, n, cs), hscal(l, m, cs))), cols)
    rep("own Y7 gravity + per-axis scalar closes iff c_j = kappa for all j", tab == {k: (k == ("1", "1", "1")) for k in tab}, f"{tab}")
    # X12b: scalar + Maxwell + gravity
    colsT = [padd(padd(gg(l, u), gscal(l, u)), gA(l, u)) for u in UB]
    tab2 = {}
    for c in (kap, 2 * kap, kap / 2):
        for cb in (kap, 2 * kap, kap / 2):
            tgt = padd(padd(gb, pb(hscal(l, n, (c,) * 3), hscal(l, m, (c,) * 3))), pb(hem(l, n, cb, Fr(4, 9)), hem(l, m, cb, Fr(4, 9))))
            tab2[(str(c / kap), str(cb / kap))] = solve_exact(tgt, colsT)
    rep("own X12b gravity + scalar + Maxwell closes iff c = cB = kappa (3x3 grid)", tab2 == {k: (k == ("1", "1")) for k in tab2}, f"{tab2}")
    # Maxwell bracket alone, own engine: = G_A[-cB xi~]
    cbv, g2 = Fr(3, 2), Fr(5, 7)
    okm = pb(hem(l, n, cbv, g2), hem(l, m, cbv, g2)) == gA(l, {k: -cbv * v for k, v in xt.items()})
    rep("own X9 (numeric lapses, own engine): {H_EM(N),H_EM(M)} = G_A[-cB xi~]", okm)


if __name__ == "__main__":
    g, K = x5(4)
    x6(g, K)
    T, Tf, Us, Ws = x9_x13(g, K)
    if "--smooth" in sys.argv:
        for L in (8, 12, 16):
            print(L, stag_generator_smooth(L), flush=True)
    x12b_y7()
    print(f"TOTAL {sum(out.values())}/{len(out)}")
