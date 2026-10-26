#!/usr/bin/env python3
"""Disjoint check for J:derive:review-20261004-ice-angular-seed-errors:a1.

Object: uniform cubic ice on the even L^3 torus (a supplied model, as in the landed ice notes),
the multiset {0,1,1} of folded wavevector components, i.e. k = (2 pi/L)(0,1,1) and its images.
At such k the divergence constraint leaves two polarizations: E_x (the free one, k_x = 0) and
E_t = (E_y - E_z)/sqrt2.  With P_ii = 1 (k_i = 0) and P_ii = 1/2 (|k_i| = 1), the source's
"assignment difference" for this multiset is
        D = K_cont * ( S_zz(k_z != 0)/(1/2) - S_zz(k_z = 0)/1 )  =  K_cont * (S_tt - S_xx).
Machinery here is disjoint from the source runner: no numba, no per-loop FFT, no binned errors.
  * exact L=2: backtracking enumeration + an independent Z_7 character-sum count (not 2^24 bits);
  * sampler: vectorised many-chain worm in numpy, every chain its own seed, incremental Fourier
    amplitudes at the 6 needed wavevectors, errors from independent chains (seed level),
    integrated autocorrelation time, group heterogeneity, TOST equivalence.
Predeclared (set before the production run; pilot runs at L=4,6,8 had been seen, see ATTEMPT.md):
    EPS = 0.005 (equivalence margin on D), TOST level 90 %, burn-in 100-150 loops, Sokal window 6.
Prints one line per check then TOTAL and SUMMARY.  No HIT line is printed by this script.
"""
import sys
import time
from fractions import Fraction
import numpy as np
from scipy import stats
import sympy as sp

T0 = time.time()
DEADLINE = T0 + 520.0           # global wall-clock guard (seconds)
PASS = FAIL = 0
EPS = 0.005
Z90 = 1.6448536269514722


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"{'PASS' if cond else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)


# ====================================================================== A. exact L = 2
sites = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
sid = {s: n for n, s in enumerate(sites)}
links = [(i, s) for i in range(3) for s in sites]


def head(i, s):
    t = list(s)
    t[i] = (t[i] + 1) % 2
    return tuple(t)


tail_idx = [sid[s] for i, s in links]
head_idx = [sid[head(i, s)] for i, s in links]
inc = [[] for _ in sites]
for a, (i, s) in enumerate(links):
    inc[tail_idx[a]].append((a, +1))
    inc[head_idx[a]].append((a, -1))
last = [max(a for a, _ in inc[v]) for v in range(8)]
check_at = [[v for v in range(8) if last[v] == a] for a in range(24)]
cfgs = []
val = [0] * 24


def rec(a):
    if a == 24:
        cfgs.append(tuple(val))
        return
    for v in (1, -1):
        val[a] = v
        if all(sum(sg * val[b] for b, sg in inc[s]) == 0 for s in check_at[a]):
            rec(a + 1)


rec(0)
planes = [[a for a in range(24) if links[a][0] == i and links[a][1][i] == 0] for i in range(3)]
Wsq = Fraction(0)
zero = 0
secs = set()
for c in cfgs:
    W = tuple(sum(c[a] for a in planes[i]) for i in range(3))
    secs.add(W)
    zero += all(w == 0 for w in W)
    Wsq += sum(w * w for w in W)
Wsq /= 3 * len(cfgs)
check("A1 exact L=2 backtracking enumeration: 9600 ice configs, 880 zero-winding, 125 sectors, <W^2>=76/25",
      len(cfgs) == 9600 and zero == 880 and len(secs) == 125 and Wsq == Fraction(76, 25),
      f"{len(cfgs)}, {zero}, {len(secs)}, {Wsq}")

KS = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]


def sgn(k, s):
    return -1 if sum(k[j] * s[j] for j in range(3)) % 2 else 1


Ssum = {}
Cross = {}
viol = 0
for k in KS:
    sg = [sgn(k, s) for s in sites]
    for i in range(3):
        Ssum[(i, k)] = 0
    for c in cfgs:
        F = [sum(c[i * 8 + n] * sg[n] for n in range(8)) for i in range(3)]
        for i in range(3):
            Ssum[(i, k)] += F[i] ** 2
        # divergence constraint: sum_i (1 - e^{-i k_i}) F_i = 2 * sum_{k_i = pi} F_i = 0
        if sum(F[i] for i in range(3) if k[i]) != 0:
            viol += 1
        pair = [i for i in range(3) if k[i]]
        Cross[k] = Cross.get(k, 0) + F[0 if k[0] == 0 else (1 if k[1] == 0 else 2)] * (F[pair[0]] - F[pair[1]])
Sx = {key: Fraction(v, 8 * len(cfgs)) for key, v in Ssum.items()}
free = [Sx[(i, k)] for k in KS for i in range(3) if k[i] == 0]        # the E_i with k_i = 0
yz = [Sx[(i, k)] for k in KS for i in range(3) if k[i] == 1]
check("A2 exact L=2: divergence constraint holds on all 9600 configs at the three face-diagonal k; "
      "free-polarization S = 38/25, each transverse-pair component 43/75, free-transverse cross term 0",
      viol == 0 and set(free) == {Fraction(38, 25)} and set(yz) == {Fraction(43, 75)}
      and all(v == 0 for v in Cross.values()), f"viol={viol} free={set(free)} pair={set(yz)} cross={set(Cross.values())}")
Kc2 = Fraction(2 * 8 + 1, 3 * 8)
A_ex, B_ex = free[0], yz[0]
D2 = Kc2 * (2 * B_ex - A_ex)
check("A3 exact L=2 angular difference D_2 = K_cont(S_tt - S_xx) = -119/450 (nonzero: the transverse form is "
      "not exact there); S_tt=86/75, S_xx=114/75 as in the landed polarization note",
      D2 == Fraction(-119, 450) and 2 * B_ex == Fraction(86, 75) and A_ex == Fraction(114, 75),
      f"D_2={D2}={float(D2):.6f}")

# independent Z_7 character-sum count (divergence in {-6,..,6} even, so mod 7 is faithful)
phi = np.indices((7,) * 7).reshape(7, -1).astype(np.int8)
phi = np.vstack([np.zeros((1, phi.shape[1]), np.int8), phi])
tab_c = 2 * np.cos(2 * np.pi * np.arange(7) / 7)
tab_s = 2 * np.sin(2 * np.pi * np.arange(7) / 7)
Cl, Sl = [], []
for a in range(24):
    d = (phi[tail_idx[a]] - phi[head_idx[a]]) % 7
    Cl.append(tab_c[d])
    Sl.append(tab_s[d])
zl = [a for a in range(24) if links[a][0] == 2]
Pn = np.ones(phi.shape[1])
for a in range(24):
    if a not in zl:
        Pn = Pn * Cl[a]
Z_all = lambda v: v.sum() / 7 ** 7
count = Z_all(Pn * np.prod([Cl[a] for a in zl], axis=0))
tot = {k: 0.0 for k in KS}
Zpair = {}
for ia, a in enumerate(zl):
    for b in zl[ia:]:
        if a == b:
            Zpair[(a, b)] = count
        else:
            prod = -Sl[a] * Sl[b] * Pn
            for c in zl:
                if c != a and c != b:
                    prod = prod * Cl[c]
            Zpair[(a, b)] = Z_all(prod)
for k in (KS[0], KS[1], KS[2]):
    s = 0.0
    for a in zl:
        for b in zl:
            key = (a, b) if a <= b else (b, a)
            s += sgn(k, links[a][1]) * sgn(k, links[b][1]) * Zpair[key]
    tot[k] = s
ok = abs(count - 9600) < 1e-4 and all(abs(tot[k] - Ssum[(2, k)]) < 1e-3 for k in KS)
check("A4 independent Z_7 character-sum machinery reproduces the count 9600 and sum_config |F_z(k)|^2 at the "
      "three face-diagonal k (integers from the enumeration)", ok,
      f"count={count:.6f}; F_z sums {[round(tot[k], 4) for k in KS]} vs {[Ssum[(2, k)] for k in KS]}")
del phi, Cl, Sl, Pn

# ====================================================================== B. symmetry and projector
signed_perms = []
import itertools
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        g = np.zeros((3, 3), int)
        for r in range(3):
            g[r, perm[r]] = signs[r]
        signed_perms.append(g)
k0 = np.array([0, 1, 1])
stab = [g for g in signed_perms if (g @ k0 == k0).all()]
e1, e2 = np.array([1, 0, 0]), np.array([0, 1, -1])
chars = []
for g in stab:
    a1, a2 = g @ e1, g @ e2
    c1 = int(a1 @ e1); c2 = int((a2 @ e2) // 2)
    assert (a1 == c1 * e1).all() and (a2 == c2 * e2).all()
    chars.append((c1, c2))
check("B1 little group of k=(0,1,1) in the 48-element cubic group has order 4, acts on E_x and E_t by two "
      "DIFFERENT characters, so symmetry cannot equate S_xx and S_tt (and forces S_xt = 0)",
      len(signed_perms) == 48 and len(stab) == 4 and len(set(chars)) == 4 and any(c1 != c2 for c1, c2 in chars),
      f"|stab|={len(stab)}, characters (chi_x,chi_t)={sorted(set(chars))}")

a_ = sp.symbols('a', positive=True)
s2 = 2 - 2 * sp.cos(a_)
P_hi = sp.simplify(1 - 0 / (s2 + s2))
P_lo = sp.simplify(1 - s2 / (s2 + s2))
P_num = []
for L in (2, 4, 6, 8, 12, 16, 24):
    kk = 2 * np.pi * np.arange(L) / L
    q = 2 - 2 * np.cos(kk[1])
    P_num.append(1 - q / (q + q))
check("B2 projector normalisation for the multiset {0,1,1}: P_hi=1 and P_lo=1/2 identically in the lattice "
      "s_i^2=2-2cos k_i (exact, sympy) and for every L tested; same value for continuum k_i^2",
      P_hi == 1 and P_lo == sp.Rational(1, 2) and all(abs(p - 0.5) < 1e-14 for p in P_num), f"P_hi={P_hi} P_lo={P_lo}")

# ====================================================================== C. vectorised many-chain worm
KVEC = np.array([[0, 1, 1], [0, 1, -1], [1, 0, 1], [1, 0, -1], [1, 1, 0], [1, -1, 0]])
AMASK = (KVEC.T == 0)
BMASK = ~AMASK


def tables(L):
    N = L ** 3
    idx = np.arange(N)
    x = idx // (L * L); y = (idx // L) % L; z = idx % L
    site = lambda a, b, c: ((a % L) * L + (b % L)) * L + (c % L)
    NF = np.stack([site(x + 1, y, z), site(x, y + 1, z), site(x, y, z + 1)])
    NB = np.stack([site(x - 1, y, z), site(x, y - 1, z), site(x, y, z - 1)])
    ph = np.exp(-2j * np.pi * (KVEC[:, 0:1] * x + KVEC[:, 1:2] * y + KVEC[:, 2:3] * z) / L)
    return N, (x, y, z), NF, NB, np.ascontiguousarray(ph.T)


def init_E(L, M):
    N, (x, y, z), _, _, _ = tables(L)
    alt = lambda a: (1 - 2 * (a % 2)).astype(np.int8)
    E = np.empty((3, N), np.int8)
    E[0] = alt(y); E[1] = alt(z); E[2] = alt(x)
    return np.broadcast_to(E.reshape(1, 3 * N), (M, 3 * N)).copy()


def run(L, M, burn, keep, entropy, deadline, track_w=False):
    """M independent chains, one SeedSequence for the whole group (group = one seed)."""
    rng = np.random.default_rng(np.random.SeedSequence(entropy))
    N, (xs, ys, zs), NF, NB, PH = tables(L)
    E = init_E(L, M)
    F0 = np.einsum('is,sj->ij', E[0].reshape(3, N).astype(float), PH)
    F = np.tile(F0, (M, 1)).astype(complex)
    cs = rng.integers(0, N, M); s0 = cs.copy(); ll = -np.ones(M, np.int64)
    ar = np.arange(M); base = np.arange(3) * N
    want = np.concatenate([np.ones((M, 3), np.int8), -np.ones((M, 3), np.int8)], 1)
    nl = np.zeros(M, np.int64)
    T = burn + keep
    ser = np.zeros((M, T, 2), np.float32)
    acc = np.zeros((M, 3, 6)); nacc = np.zeros(M)
    W2 = np.zeros(M)
    coords = (xs, ys, zs)
    pl = [np.nonzero(coords[i] == 0)[0] + i * N for i in range(3)]
    stopped = False
    snaps = []
    while nl.min() < T:
        if time.time() > deadline:
            stopped = True
            break
        ids = np.concatenate([base[None, :] + cs[:, None], base[None, :] + NB[:, cs].T], 1)
        bs = NB[:, cs].T
        vals = np.take_along_axis(E, ids, 1)
        valid = (vals == want) & (ids != ll[:, None])
        cnt = valid.sum(1)
        r = (rng.random(M) * cnt).astype(np.int64)
        pos = (np.cumsum(valid, 1) > r[:, None]).argmax(1)
        lid = ids[ar, pos]
        eold = E[ar, lid]
        E[ar, lid] = -eold
        ll = lid
        typ = lid // N; sit = lid - typ * N
        F[ar * 3 + typ] += (-2.0 * eold)[:, None] * PH[sit]
        cs = np.where(pos < 3, NF[np.minimum(pos, 2), cs], bs[ar, np.maximum(pos - 3, 0)])
        done = cs == s0
        if done.any():
            d = np.nonzero(done)[0]
            S = (np.abs(F.reshape(M, 3, 6)[d]) ** 2) / N
            Av = (S * AMASK).sum((1, 2)) / AMASK.sum()
            Bv = (S * BMASK).sum((1, 2)) / BMASK.sum()
            t = nl[d]
            ok = t < T
            if ok.any():
                dd = d[ok]; tt = t[ok]
                ser[dd, tt, 0] = Av[ok]; ser[dd, tt, 1] = Bv[ok]
                post = tt >= burn
                acc[dd[post]] += S[ok][post]; nacc[dd[post]] += 1
                if track_w:
                    Wv = np.stack([E[dd[post]][:, pl[i]].sum(1) for i in range(3)], 1).astype(float)
                    W2[dd[post]] += (Wv ** 2).mean(1)
            if len(snaps) < 4 and nl[d[0]] >= burn and nl[d[0]] % 7 == 3:
                snaps.append((E[d[0]].copy(), F.reshape(M, 3, 6)[d[0]].copy()))   # a closed (divergence-free) config
            nl[d] += 1
            s0[d] = rng.integers(0, N, len(d)); cs[d] = s0[d]; ll[d] = -1
    Tn = int(min(T, nl.min()))
    keep_n = max(Tn - burn, 0)
    return dict(snaps=snaps, E=E, F=F.reshape(M, 3, 6), ser=ser[:, burn:burn + keep_n], acc=acc / np.maximum(nacc, 1)[:, None, None],
                W2=W2 / np.maximum(nacc, 1), L=L, N=N, keep=keep_n, stopped=stopped)


def final_config_checks(r):
    """divergence-free, incremental amplitudes == FFT, transversality convention, Parseval (chain 0..2)."""
    L = r['L']; N = r['N']
    bad = 0; amp = 0.0; trans = 0.0; trans_wrong = 0.0; pars = 0.0
    assert len(r['snaps']) >= 1
    for (E1, F1) in r['snaps']:
        E = E1.reshape(3, L, L, L).astype(float)
        div = E[0] - np.roll(E[0], 1, 0) + E[1] - np.roll(E[1], 1, 1) + E[2] - np.roll(E[2], 1, 2)
        bad += int(np.abs(div).sum())
        Fn = [np.fft.fftn(E[i]) for i in range(3)]
        for i in range(3):
            for j, k in enumerate(KVEC):
                amp = max(amp, abs(Fn[i][tuple(k % L)] - F1[i, j]))
            pars = max(pars, abs((np.abs(Fn[i]) ** 2).sum() / N - N))
        kk = 2 * np.pi * np.arange(L) / L
        KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
        good = sum((1 - np.exp(-1j * K)) * Fi for K, Fi in zip((KX, KY, KZ), Fn))
        wrong = sum((1 - np.exp(+1j * K)) * Fi for K, Fi in zip((KX, KY, KZ), Fn))
        trans = max(trans, np.abs(good).max()); trans_wrong = max(trans_wrong, np.abs(wrong).max())
    return bad, amp, trans, trans_wrong, pars


# ---------------------------------------------------------------------- C1: validate sampler at L=2
r2 = run(2, 300, 50, 4000, [20261004, 2, 0], T0 + 120, track_w=True)
bad, amp, trans, trw, pars = final_config_checks(r2)
check("C1 vectorised worm at L=2: configurations stay divergence-free; incremental Fourier amplitudes equal the "
      "FFT; lattice transversality (1-e^{-ik}) holds; Parseval sum_k S=N",
      bad == 0 and amp < 1e-9 and trans < 1e-9 and pars < 1e-8,
      f"(sign test degenerate at L=2: e^{{+i pi}}=e^{{-i pi}}; done at L>=4) div={bad}, amp err {amp:.1e}, transversality {trans:.1e} vs wrong-sign {trw:.2f}, Parseval {pars:.1e}")
M2 = r2['acc'].shape[0]
zs_ = []
for j, k in enumerate(KVEC):
    kk = tuple(k % 2)
    for i in range(3):
        ex = float(Sx[(i, kk)])
        v = r2['acc'][:, i, j]
        zs_.append((v.mean() - ex) / (v.std(ddof=1) / np.sqrt(M2)))
w2 = r2['W2']
zW = (w2.mean() - 3.04) / (w2.std(ddof=1) / np.sqrt(M2))
check("C2 sampler vs exact L=2: all 18 sampled S_ii(k_j) within 4 seed-level standard errors of the exact "
      "enumeration, and <W^2> within 4 of 76/25", max(abs(np.array(zs_))) < 4 and abs(zW) < 4,
      f"max|z|={max(abs(np.array(zs_))):.2f}, z(W^2)={zW:+.2f}, chains={M2}, loops/chain={r2['keep']}")
KC = lambda N: (2 * N + 1) / (3 * N)
D2s = KC(8) * (2 * r2['ser'][:, :, 1] - r2['ser'][:, :, 0]).astype(float)
cm = D2s.mean(1)
z2 = (cm.mean() - float(D2)) / (cm.std(ddof=1) / np.sqrt(M2))
check("C3 estimator of D at L=2 reproduces the exact D_2=-119/450 within 4 seed-level standard errors",
      abs(z2) < 4, f"D_2 hat={cm.mean():+.4f} +- {cm.std(ddof=1) / np.sqrt(M2):.4f}, exact {float(D2):+.4f}, z={z2:+.2f}")
del r2, D2s


# ---------------------------------------------------------------------- C4: production L = 4, 6, 8
def tau_int(D, c=6.0):
    Dc = D - D.mean(1, keepdims=True)
    n = D.shape[1]
    f = np.fft.rfft(Dc, 2 * n, axis=1)
    ac = np.fft.irfft(np.abs(f) ** 2, axis=1)[:, :n].mean(0)
    rho = ac / ac[0]
    t = 0.5
    for w in range(1, n):
        t = 0.5 + rho[1:w + 1].sum()
        if w >= c * t:
            break
    return float(t), rho[1]


CFG = {4: dict(G=4, M=300, burn=150, keep=3000),
       6: dict(G=4, M=300, burn=100, keep=600),
       8: dict(G=4, M=300, burn=100, keep=450)}
RES = {}
for L in (4, 6, 8):
    c = CFG[L]
    dl = min(DEADLINE, T0 + {4: 190, 6: 360, 8: 510}[L])
    Ds, accs, finals, stopped = [], [], [], False
    nk = None
    for g in range(c['G']):
        r = run(L, c['M'], c['burn'], c['keep'], [20261004, L, g], dl)
        stopped |= r['stopped']
        nk = r['keep'] if nk is None else min(nk, r['keep'])
        Ds.append(r);
    nk = max(nk, 20)
    Kc = KC(Ds[0]['N'])
    Dloop = np.concatenate([Kc * (2 * r['ser'][:, :nk, 1] - r['ser'][:, :nk, 0]).astype(float) for r in Ds])   # (chains, loops)
    Macc = np.concatenate([r['acc'] for r in Ds])
    cm = Dloop.mean(1)
    Mtot = len(cm)
    D_hat = cm.mean(); se = cm.std(ddof=1) / np.sqrt(Mtot)
    naive = Dloop.std() / np.sqrt(Dloop.size)
    tau, rho1 = tau_int(Dloop)
    gm = cm.reshape(c['G'], -1).mean(1); gse = cm.reshape(c['G'], -1).std(1, ddof=1) / np.sqrt(cm.reshape(c['G'], -1).shape[1])
    chi_g = float((((gm - D_hat) / gse) ** 2).sum()); p_g = float(stats.chi2.sf(chi_g, c['G'] - 1))
    blocks = cm.reshape(12, -1) if Mtot % 12 == 0 else cm[:Mtot - Mtot % 12].reshape(12, -1)
    bm = blocks.mean(1); bse = blocks.std(1, ddof=1) / np.sqrt(blocks.shape[1])
    chi_b = float(((bm - bm.mean()) ** 2).sum() / (se ** 2 * 12))      # variance of block means = 12*se^2 for 12 blocks
    p_b = float(stats.chi2.sf(chi_b, 11))
    h = nk // 2
    ca = Dloop[:, :h].mean(1); cb = Dloop[:, h:2 * h].mean(1)
    z_burn = float((ca - cb).mean() / ((ca - cb).std(ddof=1) / np.sqrt(Mtot)))
    # cubic-symmetry consistency of the six free-polarization means and the twelve pair means
    Am = np.stack([Macc[:, i, [j for j in range(6) if AMASK[i, j]]].mean(1) for i in range(3)], 1)
    Bm = np.stack([Macc[:, i, [j for j in range(6) if BMASK[i, j]]].mean(1) for i in range(3)], 1)
    zsym = []
    for X in (Am, Bm):
        for u, v in ((0, 1), (1, 2)):
            dd = X[:, u] - X[:, v]
            zsym.append(dd.mean() / (dd.std(ddof=1) / np.sqrt(Mtot)))
    bad, amp, trans, trw, pars = final_config_checks(Ds[0])
    lo, hi = D_hat - Z90 * se, D_hat + Z90 * se
    outcome = "EQUIVALENT" if (lo > -EPS and hi < EPS) else ("OUTSIDE-MARGIN" if (lo > EPS or hi < -EPS) else "UNDECIDED")
    RES[L] = dict(D=D_hat, se=se, naive=naive, tau=tau, outcome=outcome, nloops=Mtot * nk, nk=nk, M=Mtot,
                  sig_loop=Dloop.std(), vr=(se / naive) ** 2)
    check(f"C4.{L}a L={L}: config integrity (divergence-free, incremental==FFT, convention, Parseval)",
          bad == 0 and amp < 1e-8 and trans < 1e-8 and trw > 0.5 and pars < 1e-6,
          f"div={bad}, amp {amp:.1e}, transversality {trans:.1e}, wrong sign {trw:.2f}, Parseval {pars:.1e}")
    check(f"C4.{L}b L={L}: seed-level variance inflation (se/naive)^2 agrees with 2*tau_int within a factor 1.5; "
          f"burn-in halves agree",
          (not stopped or nk >= 100) and (1 / 1.5 < (se / naive) ** 2 / (2 * tau) < 1.5) and abs(z_burn) < 4,
          f"loops/chain={nk}, chains={Mtot}, tau_int={tau:.2f}, rho1={rho1:.3f}, (se/naive)^2={(se / naive) ** 2:.2f}, 2tau={2 * tau:.2f}, burn z={z_burn:+.2f}")
    check(f"C4.{L}c L={L}: seed groups and 12 chain blocks scatter as their seed-level errors predict (chi2 p in (0.001,0.999))",
          0.001 < p_g < 0.999 and 0.001 < p_b < 0.999,
          f"4 groups chi2={chi_g:.2f} p={p_g:.3f}; 12 blocks chi2={chi_b:.2f} p={p_b:.3f}")
    check(f"C4.{L}d L={L}: cubic-symmetry images of the free and pair means agree (|z|<4) so the 18 (component, k) "
          f"pairs may be pooled",
          max(abs(np.array(zsym))) < 4, "z=" + ", ".join(f"{z:+.2f}" for z in zsym))
    check(f"C4.{L}e L={L}: D_hat = {D_hat:+.5f} +- {se:.5f} (seed level, {Mtot} chains); no violation of margin EPS={EPS} "
          f"(90% TOST interval [{lo:+.4f},{hi:+.4f}]) -> {outcome}",
          outcome != "OUTSIDE-MARGIN", f"|D|/se={abs(D_hat) / se:.2f}; loops used {Mtot * nk}; stopped_by_deadline={stopped}")
    del Ds, Dloop

# ====================================================================== D. source numbers, power, scaling (arithmetic on quoted values)
g1, e1_ = -0.0006, 0.0008        # {0,1,1}, seeds 4001-4004 (note, item 2)
g2, e2_ = +0.0024, 0.0008        # {0,1,1}, seeds 4005-4008 (note, item 3)
zq = (g2 - g1) / np.hypot(e1_, e2_)
pq = 2 * stats.norm.sf(abs(zq))
sidak = 1 - (1 - pq) ** 5
chi_p_min5 = 1 - (1 - 0.02) ** 5
chi_two = 1 - 0.95 ** 5 - 5 * 0.05 * 0.95 ** 4
check("D1 arithmetic on the note's own quoted numbers: its two seed groups for {0,1,1} differ by 2.65 sigma; across the "
      "5 multisets that is a Sidak p ~ 0.04, and chi2 probabilities as small as 0.02 (0.05) among 5 multisets occur with "
      "probability ~0.10 (~0.02) under the null -- the scatter is unusual at the 2-4 % level, not conclusive",
      abs(zq - 2.65) < 0.02 and 0.03 < sidak < 0.05 and 0.09 < chi_p_min5 < 0.10 and 0.02 < chi_two < 0.03,
      f"z={zq:.2f}, p={pq:.4f}, Sidak(5)={sidak:.3f}, P(min p<=0.02 of 5)={chi_p_min5:.3f}, P(>=2 of 5 <=0.05)={chi_two:.4f}")
r4 = RES[4]
need = lambda se_t, R: R['sig_loop'] ** 2 * (2 * R['tau']) / se_t ** 2
n02 = need(0.002 / Z90, r4); n005 = need(0.0002, r4)
check("D2 power: measured per-loop sigma and tau_int at L=4 give the number of completed loops needed for a 90% TOST "
      "at margin 0.2% (se 0.12%) and for se = 0.02% (the size of the source's pooled mean offset)",
      n02 > 0 and n005 > n02, f"sigma_loop={r4['sig_loop']:.3f}, tau={r4['tau']:.2f}: loops for se=0.0012: {n02:.2e}; for se=0.0002: {n005:.2e}")
rows = "; ".join(f"L={L}: {RES[L]['D']:+.5f}+-{RES[L]['se']:.5f} [{RES[L]['outcome']}]" for L in (4, 6, 8))
check("D3 summary table of D_hat(L) with seed-level errors, next to the exact D_2 and the source's L=16 {0,1,1} values",
      all(np.isfinite(RES[L]['D']) for L in RES),
      f"L=2 exact {float(D2):+.4f}; {rows}; source L=16: -0.0006+-0.0008 and +0.0024+-0.0008 (binned)")

print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("SUMMARY: for the multiset {0,1,1} (free vs transverse polarization at k=(0,1,1)2pi/L) the angular difference D is exactly "
      "-119/450 at L=2 (landed prior art), is not symmetry-forced to vanish, and seed-level estimates give "
      + ", ".join(f"L={L}: {RES[L]['D']:+.4f}+-{RES[L]['se']:.4f} ({RES[L]['outcome']} at margin {EPS})" for L in (4, 6, 8))
      + f", with tau_int ~ {np.mean([RES[L]['tau'] for L in RES]):.1f} loops so the error model is sound but the sampling precision does not reach 0.05 %.")
sys.exit(1 if FAIL else 0)
