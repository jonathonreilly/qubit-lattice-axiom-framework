#!/usr/bin/env python3
"""f4: discrete flow (F-3) and bare-coupling tuning (F-4) on synthetic admissible data. Criteria: f4_criteria.md."""
import sys, time
import numpy as np

t0 = time.time(); OUT = []; fails = []
def say(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def crit(name, ok, detail):
    say(f"[{name}] {'PASS' if ok else 'FAIL'} :: {detail}")
    if not ok: fails.append(name)

N, L = 3, 3
lg = np.log(L)
b0p = 11 * N ** 2 / (12 * np.pi ** 2)
A, Ap, Crho = 2.0, 0.5, 3.0
KMAX = 1000
k = np.arange(KMAX + 1)
dk = A * L ** (-2.0 * k) * np.cos(1.3 * k) + Ap * (np.cos(0.7 * (k + 1)) - np.cos(0.7 * k))
# R = sup_{j<=n<=KMAX} |sum_{k=j}^{n-1} d_k| (exact on the range)
cs = np.concatenate([[0.0], np.cumsum(dk[:KMAX])])
R = cs.max() - cs.min()
Ceff = Crho + 1.0                      # delta-beta absorbed: g^6 <= g^2
gam = np.sqrt(0.5 * b0p * lg / Ceff)
bm, bp = b0p - Ceff * gam ** 2 / lg, b0p + Ceff * gam ** 2 / lg
g1 = (gam ** -2 + R) ** -0.5
say(f"beta0'={b0p:.6f} R={R:.6f} gamma={gam:.6f} beta-={bm:.6f} beta+={bp:.6f} g1={g1:.6f}")

def flow(g0, K):
    """returns u[0..n] where n is the admissible length (stops after the first g_k > gamma)."""
    u = [g0 ** -2]
    for kk in range(K):
        gk2 = 1.0 / u[-1]
        if gk2 > gam ** 2 * (1 + 1e-15):
            break
        rho = Crho * gk2 * np.sin(5 * kk + 17 * g0)
        db = gk2 ** 3 * np.cos(kk)
        u.append(u[-1] - (b0p * lg + dk[kk]) - rho - db)
        if u[-1] <= 0: break
    return np.array(u)

# (A) two-sided flow bounds on admissible prefixes
viol = 0; checked = 0
for g0 in np.linspace(0.02, gam, 50):
    u = flow(g0, 200)
    g2 = 1 / u
    # admissible prefix: g_0..g_{n-1} <= gamma  (u_n may exceed the window)
    nadm = len(u) - 1
    while nadm > 0 and np.any(g2[:nadm] > gam ** 2 * (1 + 1e-15)):
        nadm -= 1
    for n in range(nadm + 1):
        for j in range(n + 1):
            diff = u[j] - u[n]; m = n - j
            checked += 1
            if not (bm * m * lg - R - 1e-9 <= diff <= bp * m * lg + R + 1e-9):
                viol += 1
crit("A", viol == 0, f"(F-3) bounds: {checked} (j,n) pairs over 50 runs, violations {viol}")

# (B), (C) shooting
def admissible(g0, K):
    u = flow(g0, K)
    return len(u) == K + 1 and np.all(1 / u[:K + 1] <= gam ** 2 * (1 + 1e-15)), u

def shoot(K, g):
    target = g ** -2
    # scan from small g0 upward: (0, g0_sharp] = first admissible component
    grid = np.linspace(1e-4, gam, 4000)
    prev = None
    for g0 in grid:
        ok, u = admissible(g0, K)
        F = u[K] - target if ok else -np.inf      # inadmissible counts as "below target" (FLOW §9 proof)
        if prev is not None and np.sign(F) != np.sign(prev[1]):
            lo, hi = prev[0], g0          # F(lo) > 0 >= F(hi) (or the reverse)
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                okm, um = admissible(mid, K)
                Fm = um[K] - target if okm else -np.inf
                if np.sign(Fm) == np.sign(prev[1]): lo = mid
                else: hi = mid
                if hi - lo < 1e-16: break
            for cand in (lo, hi):
                okc, uc = admissible(cand, K)
                if okc and abs(uc[K] - target) <= 1e-9 * target:
                    return cand, uc
            return None, None
        if not ok:
            break
        prev = (g0, F)
    return None, None

found = 0; violC = 0; infoD = []
for K in (10, 100, 1000):
    for g in (g1, g1 / 2, g1 / 10):
        g0, u = shoot(K, g)
        if g0 is None:
            say(f"   K={K} g={g:.5f}: no tuned g0 found"); continue
        found += 1
        kk = np.arange(K + 1)
        lo = g ** -2 + bm * (K - kk) * lg - R; hi = g ** -2 + bp * (K - kk) * lg + R
        violC += int(np.sum((u < lo - 1e-9) | (u > hi + 1e-9)))
        say(f"   K={K} g={g:.5f}: g0={g0:.6e}, |u_K-g^-2|/g^-2={abs(u[K]-g**-2)*g**2:.1e}, max g_k={np.sqrt((1/u).max()):.5f}")
        if K == 1000: infoD.append(g0 ** -2 / (b0p * K * lg))
crit("B", found == 9, f"tuned g0 found in {found}/9 cases, all g_k <= gamma")
crit("C", violC == 0, f"two-sided tuned bounds: violations {violC}")
say(f"   [info D] K=1000: g0^-2/(beta0' K log L) = " + ", ".join(f"{x:.4f}" for x in infoD))
say(f"f4 done: {'ALL PASS' if not fails else 'FAIL: ' + ','.join(fails)}; wall {time.time()-t0:.1f}s")
with open(sys.argv[1] if len(sys.argv) > 1 else "f4_out.txt", "w") as fh:
    fh.write("\n".join(OUT) + "\n")
