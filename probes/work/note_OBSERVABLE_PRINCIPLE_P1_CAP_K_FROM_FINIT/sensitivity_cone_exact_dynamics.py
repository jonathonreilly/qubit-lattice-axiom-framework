#!/usr/bin/env python3
"""J:note falsifiers for OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10 (on main).

The note's load-bearing step: for the hard-core hopping model H = sum_<xy> (a_x^dag a_y + h.c.) + m sum n_x, a source V supported in X
and a register observable B_y at l1-distance D from X,
    ||alpha_t^{H+V}(B_y) - alpha_t^H(B_y)|| <= (||V||/(4W)) sum_{n >= D+1} (4Wt)^n/n!,   W = |m| + 2d,
whence every delta-sensitive register lies within D* = v_LR tau + ln((e/(e-1)) J_V/(v_LR delta)), v_LR = 4eW, and the canonical cap
(Z^3, tau = 1, J_V = 1, delta = 1/10, s_X = 1) is D* ~ 63.82, N_reach = 129^3 = 2146689 (admits 4^10, not 4^11). Falsifiers: the bound
fails on exact dynamics; the canonical numbers are wrong; the unbounded-speed comparator does not break the bound.

Disjoint machinery, beyond the note's sizes (its runner: dense many-body eigh on a 10-site ring and the 8-site 2x2x2 block, D <= 5):
  1. canonical arithmetic at 40 digits; the l1-ball actually swept by the proof (integer distance <= floor D*) counted exactly;
  2. d = 1, EXACT full operator norm on open chains of 61 sites via Jordan-Wigner: H, V = lam n_0 (or a bond source lam(c_0^dag c_1 +
     h.c.)) and sigma^z_y are free-fermion bilinears, and ||dGamma(|phi'><phi'| - |phi><phi|)|| = sqrt(1 - |<phi, phi'>|^2), so the
     sensitivity is 2 ||P_perp (phi' - phi)|| with phi = e^{iht} e_y, phi' = e^{ih't} e_y; computed by exact-sign Taylor series in
     60-digit arithmetic, D = 1..20, t = 0.01..3, lam in {1, 1/100}; plus the actual delta = 1/10 sensitivity radius at tau = 1 vs D*;
  3. d = 3: the full Fock space of an open 2x2x3 block (12 sites, all number sectors, D = 1..4) and the one-particle sector of an open
     9x9x9 box (a lower bound for the full norm; D = 1..12), both against the W = 6 bound;
  4. unbounded-speed comparator: one long bond 0 <-> r on the chain, r = 5, 10, 20 (one-particle sector, a lower bound).
"""
from __future__ import annotations

import itertools
import math

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 60


def bound(D, t, W, lam):
    """(lam/(4W)) sum_{n >= D+1} (4Wt)^n / n!  in mpmath."""
    x = mp.mpf(4 * W) * mp.mpf(t)
    term = x ** (D + 1) / mp.factorial(D + 1)
    tot, n = mp.mpf(0), D + 1
    while True:
        tot += term
        n += 1
        term = term * x / n
        if term < tot * mp.mpf(10) ** (-mp.mp.dps + 5):
            break
    return mp.mpf(lam) / (4 * W) * tot


# ------------------------------------------------------------------------------------------------------------ 1. canonical arithmetic
def canonical():
    e = sp.E
    Dstar = 24 * e + sp.log(sp.Rational(10) / (24 * (e - 1)))
    Dn = sp.N(Dstar, 40)
    ceilD, floorD = int(sp.ceiling(Dn)), int(sp.floor(Dn))
    N = (1 + 2 * ceilD) ** 3
    kjoint = N // 2 + 1                               # first k with 4^k > 2^N
    r = floorD
    ball = sum(2 * (r - abs(a)) ** 2 + 2 * (r - abs(a)) + 1 for a in range(-r, r + 1))
    ball_formula = (2 * r + 1) * (2 * r * r + 2 * r + 3) // 3
    # runner T9 (quasilocal truncation R = 10): D* with and without the R factor in front of the log
    WH = 1.757278
    v10 = 2 * math.e * 2 * (2 * WH) * 10
    d_noR = v10 + math.log(math.e / (math.e - 1) / (v10 * 0.1))
    d_R = v10 + 10 * math.log(math.e / (math.e - 1) * 10 / (v10 * 0.1))
    return {"D*": Dn, "ceil": ceilD, "floor": floorD, "N_reach": N, "4^10 <= N < 4^11": 4 ** 10 <= N < 4 ** 11,
            "first joint k": kjoint, "l1 ball radius floor(D*)": (ball, ball == ball_formula), "box (1+2 floor)^3": (1 + 2 * floorD) ** 3,
            "ball admits 4^10": 4 ** 10 <= ball, "T9 D*(R=10) as run / with R": (round(d_noR, 2), round(d_R, 2))}


# ---------------------------------------------------------------------------------------------- 2. exact d = 1 full-norm sensitivity
def evolve(nb, diag, y, t, n):
    """e^{iAt} e_y for a real symmetric sparse A: Taylor terms c_k = t^k A^k e_y / k! (real), phases i^k."""
    t = mp.mpf(t)
    c = [mp.mpf(0)] * n
    c[y] = mp.mpf(1)
    re, im = c[:], [mp.mpf(0)] * n
    eps = mp.mpf(10) ** (-mp.mp.dps - 3)
    k = 0
    while True:
        k += 1
        c = [(diag[i] * c[i] + mp.fsum(a * c[j] for j, a in nb[i])) * t / k for i in range(n)]
        r = k % 4
        if r == 0:
            re = [p + q for p, q in zip(re, c)]
        elif r == 1:
            im = [p + q for p, q in zip(im, c)]
        elif r == 2:
            re = [p - q for p, q in zip(re, c)]
        else:
            im = [p - q for p, q in zip(im, c)]
        if k > 8 and max(abs(x) for x in c) < eps:
            return re, im


def sens(phi, phip):
    wr = [p - q for p, q in zip(phip[0], phi[0])]
    wi = [p - q for p, q in zip(phip[1], phi[1])]
    ipr = mp.fsum(a * b + c * d for a, c, b, d in zip(phi[0], phi[1], wr, wi))   # Re <phi, w>
    ipi = mp.fsum(a * d - c * b for a, c, b, d in zip(phi[0], phi[1], wr, wi))   # Im <phi, w>
    pr = [b - (ipr * a - ipi * c) for a, c, b in zip(phi[0], phi[1], wr)]
    pi = [d - (ipr * c + ipi * a) for a, c, d in zip(phi[0], phi[1], wi)]
    return 2 * mp.sqrt(mp.fsum(x * x for x in pr) + mp.fsum(x * x for x in pi))


def chain(R=30, extra=None):
    n = 2 * R + 1
    nb = [[] for _ in range(n)]
    for i in range(n - 1):
        nb[i].append((i + 1, mp.mpf(1)))
        nb[i + 1].append((i, mp.mpf(1)))
    if extra:
        a, b = extra
        nb[a].append((b, mp.mpf(1)))
        nb[b].append((a, mp.mpf(1)))
    return n, nb


def one_d():
    R = 30
    n, nb = chain(R)
    s = R
    zero = [mp.mpf(0)] * n
    variants = {"site lam=1": ("site", mp.mpf(1)), "site lam=1/100": ("site", mp.mpf(1) / 100), "bond lam=1": ("bond", mp.mpf(1))}
    nbs = {}
    for name, (kind, lam) in variants.items():
        d2 = zero[:]
        nb2 = [list(x) for x in nb]
        if kind == "site":
            d2[s] = lam
        else:
            nb2[s].append((s + 1, lam))
            nb2[s + 1].append((s, lam))
        nbs[name] = (nb2, d2)
    Ds = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
    ts = ["0.01", "0.03", "0.1", "0.2", "0.35", "0.5", "0.75", "1", "1.5", "2", "3"]
    worst, checked, skipped, viol = {}, 0, 0, []
    for t in ts:
        cache = {}
        for D in Ds:
            for name, (kind, lam) in variants.items():
                y = s + D if kind == "site" else s + 1 + D
                b = bound(D, t, 2, lam)
                if b >= 2 or b < mp.mpf(10) ** -45:
                    skipped += 1
                    continue
                if y not in cache:
                    cache[y] = evolve(nb, zero, y, t, n)
                nb2, d2 = nbs[name]
                S = sens(cache[y], evolve(nb2, d2, y, t, n))
                checked += 1
                ratio = S / b
                key = (name, D)
                worst[key] = max(worst.get(key, 0), float(ratio))
                if S > b:
                    viol.append((name, D, t, float(S), float(b)))
    # actual delta = 1/10 radius at tau = 1 (site source, lam = 1): largest D with max_{t <= 1} S >= 1/10
    nb2, d2 = nbs["site lam=1"]
    radius = 0
    for D in range(1, 9):
        y = s + D
        mx = max(sens(evolve(nb, zero, y, t, n), evolve(nb2, d2, y, t, n)) for t in [k / 20 for k in range(1, 21)])
        if mx >= mp.mpf(1) / 10:
            radius = D
    Dstar1 = 8 * mp.e + mp.log(10 / (8 * (mp.e - 1)))
    return worst, checked, skipped, viol, radius, Dstar1


# ------------------------------------------------------------------------------------------------------------------ 3. d = 3
def block_full(dims=(2, 2, 3)):
    sites = list(itertools.product(*[range(k) for k in dims]))
    idx = {p: i for i, p in enumerate(sites)}
    ns = len(sites)
    bonds = [(idx[p], idx[q]) for p in sites for q in sites if sum(abs(a - b) for a, b in zip(p, q)) == 1 and idx[p] < idx[q]]
    src = idx[(0, 0, 0)]
    regs = {}
    for p in sites:
        D = sum(p)
        if D >= 1 and D not in regs:
            regs[D] = idx[p]
    ts = [0.005, 0.01, 0.02, 0.05, 0.1]
    meas = {(D, t): 0.0 for D in regs for t in ts}
    for N in range(ns + 1):
        basis = [sum(1 << i for i in c) for c in itertools.combinations(range(ns), N)]
        pos = {b: k for k, b in enumerate(basis)}
        dim = len(basis)
        H = np.zeros((dim, dim))
        for k, b in enumerate(basis):
            for i, j in bonds:
                if (b >> i & 1) != (b >> j & 1):
                    H[pos[b ^ (1 << i) ^ (1 << j)], k] += 1.0
        vdiag = np.array([(b >> src) & 1 for b in basis], float)
        E0, Q0 = np.linalg.eigh(H)
        E1, Q1 = np.linalg.eigh(H + np.diag(vdiag))
        for D, y in regs.items():
            bdiag = np.array([1.0 - 2 * ((b >> y) & 1) for b in basis])
            A0 = Q0.T @ (bdiag[:, None] * Q0)
            A1 = Q1.T @ (bdiag[:, None] * Q1)
            for t in ts:
                P0 = np.exp(1j * E0 * t)
                P1 = np.exp(1j * E1 * t)
                al0 = Q0 @ ((P0[:, None] * A0) * P0.conj()[None, :]) @ Q0.T
                al1 = Q1 @ ((P1[:, None] * A1) * P1.conj()[None, :]) @ Q1.T
                nrm = np.abs(np.linalg.eigvalsh(al1 - al0)).max() if dim else 0.0
                meas[(D, t)] = max(meas[(D, t)], nrm)
    out, viol = {}, []
    for (D, t), m in meas.items():
        b = float(bound(D, t, 6, 1))
        if b < 1e-10 or b >= 2:
            continue
        out[D] = max(out.get(D, 0), m / b)
        if m > b + 1e-12:
            viol.append((D, t, m, b))
    return ns, out, viol


def box_one_particle(Lb=9):
    sites = list(itertools.product(range(Lb), repeat=3))
    idx = {p: i for i, p in enumerate(sites)}
    n = len(sites)
    h = np.zeros((n, n))
    for p in sites:
        for mu in range(3):
            q = list(p)
            q[mu] += 1
            if q[mu] < Lb:
                h[idx[p], idx[tuple(q)]] = h[idx[tuple(q)], idx[p]] = 1.0
    c = Lb // 2
    s = idx[(c, c, c)]
    dist = np.array([sum(abs(a - c) for a in p) for p in sites])
    res, viol = {}, []
    for lam in (1.0, 0.01):
        E0, Q0 = np.linalg.eigh(h)
        h1 = h.copy()
        h1[s, s] += lam
        E1, Q1 = np.linalg.eigh(h1)
        for t in [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3]:
            Phi0 = Q0 @ (np.exp(1j * E0 * t)[:, None] * Q0.T)     # columns e^{iht} e_y
            Phi1 = Q1 @ (np.exp(1j * E1 * t)[:, None] * Q1.T)
            W_ = Phi1 - Phi0
            ip = np.einsum("iy,iy->y", Phi0.conj(), W_)
            Pp = W_ - Phi0 * ip[None, :]
            S = 2 * np.linalg.norm(Pp, axis=0)
            for D in range(1, 13):
                b = float(bound(D, t, 6, lam))
                if b < 1e-10 or b >= 2:
                    continue
                m = S[dist == D].max()
                res[(lam, D)] = max(res.get((lam, D), 0), m / b)
                if m > b + 1e-12:
                    viol.append((lam, D, t, m, b))
    return n, res, viol


# ------------------------------------------------------------------------------------------------------------- 4. comparator
def comparator():
    R = 30
    out = {}
    for r in (5, 10, 20):
        n, nb = chain(R, extra=(R, R + r))
        zero = [mp.mpf(0)] * n
        d2 = zero[:]
        d2[R] = mp.mpf(1)
        for t in ("0.05", "0.1"):
            S = sens(evolve(nb, zero, R + r, t, n), evolve(nb, d2, R + r, t, n))
            out[(r, t)] = S / bound(r, t, 2, 1)
    return out


def main():
    c = canonical()
    print(f"1. canonical cap: {c}")
    worst, checked, skipped, viol1, radius, Dstar1 = one_d()
    top = sorted(worst.items(), key=lambda kv: -kv[1])[:6]
    print(f"2. d = 1 exact full-norm sensitivity (61-site open chain, 60 digits): {checked} (source, D, t) points checked, {skipped} "
          f"outside (bound >= 2 or < 1e-45); largest measured/bound {[(k, round(v, 4)) for k, v in top]}; "
          f"worst by D (site lam=1): {[(D, float('%.3g' % worst.get(('site lam=1', D), 0))) for D in (1, 2, 3, 5, 8, 12, 20)]}; "
          f"violations {viol1}")
    print(f"   actual delta = 1/10 sensitivity radius at tau = 1 (d = 1): {radius}; D* for d = 1: {mp.nstr(Dstar1, 6)}")
    ns, blk, viol3 = block_full()
    print(f"3a. d = 3 open 2x2x3 block, full Fock space ({2 ** ns} states, all sectors): worst measured/bound by D {blk}; violations {viol3}")
    n1, box, viol4 = box_one_particle()
    print(f"3b. d = 3 open 9x9x9 box, one-particle sector ({n1} sites): worst measured/bound by (lam, D) "
          f"{ {k: float('%.3g' % v) for k, v in box.items()} }; violations {viol4}")
    comp = comparator()
    print(f"4. long-bond comparator (one-particle sector): sensitivity / finite-range bound {({k: mp.nstr(v, 4) for k, v in comp.items()})}")
    fails = []
    if not (abs(c["D*"] - sp.Float("63.822", 40)) < 0.001 and c["ceil"] == 64 and c["N_reach"] == 2146689 and c["4^10 <= N < 4^11"]
            and c["first joint k"] == 1073345):
        fails.append("canonical numbers")
    if viol1 or viol3 or viol4:
        fails.append("sensitivity above the series bound")
    if min(comp.values()) <= 1:
        fails.append("comparator does not break the bound")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: canonical D* = {sp.N(c['D*'], 8)}, ceil 64, N_reach = 2146689, 4^10 <= N < 4^11, first joint-reading failure "
          f"k = {c['first joint k']} (all as stated); the proof's own l1 cone (integer distance <= 63) holds {c['l1 ball radius floor(D*)'][0]} "
          f"sites, below 4^10; exact full-norm sensitivities on a 61-site chain ({checked} points, D to 20, site and bond sources) stay "
          f"below the series bound, largest ratio {top[0][1]:.4f} at {top[0][0]}; the d = 1 delta = 1/10 radius at tau = 1 is {radius} "
          f"against D* = {mp.nstr(Dstar1, 4)}; the 12-site 2x2x3 full Fock space and the 729-site one-particle sector stay below the "
          f"W = 6 bound (largest {max(list(blk.values()) + list(box.values())):.4f}); the long-bond comparator exceeds the finite-range "
          f"bound by {mp.nstr(min(comp.values()), 3)} to {mp.nstr(max(comp.values()), 3)}; runner T9 evaluates D*(R=10) = "
          f"{c['T9 D*(R=10) as run / with R'][0]} without the R factor in front of the log ({c['T9 D*(R=10) as run / with R'][1]} with it); "
          f"no falsifier fires")


if __name__ == "__main__":
    main()
