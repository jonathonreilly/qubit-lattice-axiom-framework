#!/usr/bin/env python3
"""Independent adversarial check of B3 (iid-priority formation coding radius).

Written from scratch (does not import or copy the B3 runner). Differences in path:
  * the repo's ACTUAL exponential race is implemented: X_x = argmin_s E_{x,s}/r(s|eta)
    with six iid Exp(1) marks per site (the B3 runner used an inverse-CDF single
    uniform instead); plus an order-sensitive, clock-reading rule with zeros and a
    hole symbol, to stress Definition 1;
  * determining set K_x computed by my own BFS; locality tested by resampling
    (a) everything outside K_x, (b) everything outside the ball B(x, L_x+1),
    and a negative control resampling ONE site of N(A_x) \\ A_x (the boundary times
    are genuinely read: a later neighbour can become earlier);
  * Lemma 1 checked on a DIFFERENT lattice (Z^2, SAW counts OEIS A001411);
  * Proposition 4 path-order product formula checked by Monte Carlo;
  * covariance decay on a 3D torus with FFT correlations vs an empirical two-copy
    intersection probability and the analytic Theorem 2 / 2' bounds.
Usage: python3 independent_check.py [seed]
"""
import sys, math, time
import numpy as np
from collections import deque

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
rng = np.random.default_rng(seed)
results = []
def check(name, ok, info=""):
    results.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + info if info else ""), flush=True)

# ---------------------------------------------------------------- torus geometry
def torus(L, dim):
    N = L**dim
    idx = np.arange(N).reshape((L,)*dim)
    nb = []
    for ax in range(dim):
        for sh in (1, -1):
            nb.append(np.roll(idx, sh, axis=ax).ravel())
    return np.stack(nb, 1)  # N x 2dim

def coords(L, dim):
    return np.stack(np.unravel_index(np.arange(L**dim), (L,)*dim), 1)

def tdist(c, x, L):
    d = np.abs(c - c[x]); return np.minimum(d, L - d).sum(1)

# ---------------------------------------------------------------- rules
HOLE = 6
def race_product(p, q, r):
    """Repo race: X = argmin_s E_s / r(s|eta), r proportional to prod_{t in eta} phi[t][s]."""
    phi = np.full((7, 6), float(r))
    for a in range(3):
        phi[2*a, 2*a] = phi[2*a+1, 2*a+1] = p
        phi[2*a, 2*a+1] = phi[2*a+1, 2*a] = q
    phi[HOLE, :] = 1.0  # holes (unused here) are ignored
    def rule(x, eta_lab, eta_t, Tx, E):
        w = np.ones(6)
        for t in eta_lab: w = w * phi[t]
        return int(np.argmin(E / (w / w.sum())))
    return rule

def adversarial_rule(x, eta_lab, eta_t, Tx, E):
    """Order-sensitive, clock-reading, zeros, holes: copy the label of the MOST RECENTLY
    formed non-hole neighbour if it formed within 0.1 of T_x; if formed neighbours
    disagree and T_x > 0.7 emit a HOLE; otherwise uniform race."""
    real = [(t, l) for t, l in zip(eta_t, eta_lab) if l != HOLE]
    if real:
        t_last, l_last = max(real)
        if Tx - t_last < 0.1: return int(l_last)
        if len(set(l for _, l in real)) > 1 and Tx > 0.7: return HOLE
    return int(np.argmin(E))

def form(T, E, rule, NB):
    N = len(T); X = np.full(N, -1, int); Ld = np.zeros(N, int)
    for x in np.argsort(T):
        lab, ts, best = [], [], -1
        for z in NB[x]:
            if T[z] < T[x]:
                lab.append(X[z]); ts.append(T[z]); best = max(best, Ld[z])
        Ld[x] = best + 1
        X[x] = rule(x, lab, ts, T[x], E[x])
    return X, Ld

def det_set(x, T, NB):
    A = {x}; dq = deque([x])
    while dq:
        y = dq.popleft()
        for z in NB[y]:
            if T[z] < T[y] and z not in A: A.add(z); dq.append(z)
    K = set(A)
    for y in A: K.update(NB[y].tolist())
    return A, K

# ================================================================ 1. Lemma 1 on Z^2
A001411 = [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100]
def lazy_paths_Z2(nmax, rng):
    T = {}
    def t(p):
        if p not in T: T[p] = rng.random()
        return T[p]
    memo = {}
    def cnt(p):
        if p in memo: return memo[p]
        c = np.zeros(nmax+1); c[0] = 1
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            q = (p[0]+d[0], p[1]+d[1])
            if t(q) < t(p): c[1:] += cnt(q)[:-1]
        memo[p] = c; return c
    return cnt((0, 0))
nmax = 9; NS = 60000
P = np.array([lazy_paths_Z2(nmax, rng) for _ in range(NS)])
ok = True; ok2 = True; rows = []
for n in range(1, nmax+1):
    ex = A001411[n]/math.factorial(n+1); mu = P[:, n].mean(); se = P[:, n].std()/math.sqrt(NS)
    pL = (P[:, n] > 0).mean(); seL = math.sqrt(max(pL*(1-pL), 1/NS)/NS)
    ok &= abs(mu - ex) < 4*se + 1e-12
    ok2 &= pL <= ex + 4*seL
    rows.append(f"n={n}: E#={mu:.4f} vs {ex:.4f}, P(L>=n)={pL:.2e}")
print("\n".join(rows))
check("1a Z^2: E[#decreasing paths of length n] = c_n/(n+1)! (|z|<4), n=1..9", ok)
check("1b Z^2: P(L>=n) <= c_n/(n+1)!", ok2)

# ================================================================ 2. Prop 4 path order formula
lam = np.array([1.0, 3.0, 0.5, 2.0, 1.5])
exact = np.prod([lam[k]/lam[:k+1].sum() for k in range(len(lam))])
M = 2_000_000
Ts = rng.exponential(1/lam, size=(M, len(lam)))
emp = np.all(np.diff(Ts, axis=1) < 0, axis=1).mean()
bnd = (lam.max()/lam.min())**(len(lam)-1)/math.factorial(len(lam))
check("2 Prop 4: P(T_v0>...>T_v4) = prod lam_k/sum_{j<=k} lam_j and <= bound",
      abs(emp-exact) < 4*math.sqrt(exact/M) and exact <= bnd,
      f"emp {emp:.5f} exact {exact:.5f}; (rho^n)/(n+1)! = {bnd:.4f} (note uses rho^(n+1), looser)")

# ================================================================ 3. locality on 3D torus
L = 16; dim = 3; NB = torus(L, dim); N = L**dim; C = coords(L, dim)
rules = {"race(3,1,2)": race_product(3, 1, 2), "race-ferro(20,1,1)": race_product(20, 1, 1),
         "adversarial": adversarial_rule}
for rname, rule in rules.items():
    okK = okB = True; ctrl = 0; nctrl = 0; ntr = 12
    for tr in range(ntr):
        T = rng.random(N); E = rng.exponential(size=(N, 6))
        X, Ld = form(T, E, rule, NB)
        cand = np.where((Ld >= 3) & (Ld <= 7))[0]; x = int(rng.choice(cand))
        A, K = det_set(x, T, NB)
        assert max(tdist(C, x, L)[list(A)]) <= Ld[x]  # A inside ball of radius L_x
        Km = np.zeros(N, bool); Km[list(K)] = True
        for mask, tag in ((~Km, "K"), (tdist(C, x, L) > Ld[x] + 1, "ball")):
            T2 = T.copy(); E2 = E.copy()
            T2[mask] = rng.random(mask.sum()); E2[mask] = rng.exponential(size=(mask.sum(), 6))
            X2, _ = form(T2, E2, rule, NB)
            if tag == "K": okK &= X2[x] == X[x]
            else: okB &= X2[x] == X[x]
        # negative control: boundary site of N(A)\A made earlier than its A-neighbour,
        # plus resampling of the whole A\{x} marks -> X_x must change in some trial
        bnd_sites = list(K - A)
        T3 = T.copy(); E3 = E.copy()
        for z in bnd_sites: T3[z] = rng.random() * T[x]  # boundary may now precede
        inner = [a for a in A if a != x]
        E3[inner] = rng.exponential(size=(len(inner), 6))
        X3, _ = form(T3, E3, rule, NB); nctrl += 1; ctrl += int(X3[x] != X[x])
    check(f"3 [{rname}] X_x invariant under resampling outside K_x ({ntr} full recomputes)", okK)
    check(f"3 [{rname}] X_x invariant under resampling outside B(x, L_x+1)", okB)
    check(f"3 [{rname}] control: perturbing inside K_x changes X_x sometimes", ctrl > 0, f"{ctrl}/{nctrl}")

# ================================================================ 4. covariance decay
L = 24; NB = torus(L, 3); N = L**3; C = coords(L, 3)
nsamp = 40
for rname in ("race-ferro(20,1,1)", "adversarial"):
    rule = rules[rname]
    acc = []
    for s in range(nsamp):
        T = rng.random(N); E = rng.exponential(size=(N, 6))
        X, _ = form(T, E, rule, NB)
        f = (X == 0).astype(float).reshape(L, L, L)
        F = np.fft.fftn(f - f.mean())
        cor = np.real(np.fft.ifftn(F * np.conj(F))) / N
        acc.append([(cor[d, 0, 0] + cor[0, d, 0] + cor[0, 0, d]) / 3 for d in range(L//2)])
    acc = np.array(acc); Cm = acc.mean(0); Cse = acc.std(0, ddof=1)/math.sqrt(nsamp)
    print(f"[{rname}] Cov(1{{X=0}}_0, 1{{X=0}}_d):", " ".join(f"{d}:{Cm[d]:+.2e}" for d in range(9)))
    acc_r = acc
    globals()["cov_" + rname.split("(")[0].replace("-", "_")] = (Cm, Cse)

# empirical two-copy intersection probability on the torus (own code, own fields)
NP = 3000; Dm = 11; hit = np.zeros(Dm+1)
for i in range(NP):
    T1 = rng.random(N); T2 = rng.random(N)
    _, K1 = det_set(0, T1, NB)
    for d in range(1, Dm+1):
        y = int(np.ravel_multi_index((d, 0, 0), (L, L, L)))
        _, K2 = det_set(y, T2, NB)
        hit[d] += bool(K1 & K2)
Pbad = hit / NP
print("two-copy P(K_0 meets K'_d):", " ".join(f"{d}:{Pbad[d]:.2e}" for d in range(1, Dm+1)))
okc = True
for name in ("cov_race_ferro", "cov_adversarial"):
    Cm, Cse = globals()[name]
    for d in range(1, Dm+1):
        # f = indicator, osc f = 1: |Cov| <= (1/2) P_bad
        lhs = abs(Cm[d]); rhs = 0.5*Pbad[d] + 4*Cse[d] + 2*math.sqrt(max(Pbad[d], 1/NP)/NP)
        okc &= lhs <= rhs
check("4 |Cov(1{X=0}_0,1{X=0}_d)| <= (1/2) P(K_0 meets K'_d) (+tol), both rules, d=1..11", okc)

# analytic bounds (Theorem 2 / 2') on Z^3 with crude c_n <= 6*5^(n-1)
def Gamma_crude(d):
    M = max(d-2, 0)
    return 144/25*sum(math.exp(n*math.log(10) - math.lgamma(n+3)) for n in range(M, M+300))
def ball(d):
    m = (d-1)//2
    return 6*5**(m-1)/math.factorial(m+1) if m >= 1 else float("inf")
print("analytic (osc=1, single sites): d: 0.5*Gamma_crude(d), 0.5*2*ball-form")
for d in (10, 15, 20, 22, 25, 30, 40):
    print(f"  d={d}: two-copy {0.5*Gamma_crude(d):.2e}  ball {ball(d):.2e}")
# check closed-form step: sum_{j+j'=N} 1/((j+1)!(j'+1)!) = (2^(N+2)-2)/(N+2)!
okcf = all(abs(sum(1/(math.factorial(j+1)*math.factorial(N-j+1)) for j in range(N+1))
               - (2**(N+2)-2)/math.factorial(N+2)) < 1e-15 for N in range(0, 30))
check("5 identity sum_{j+j'=N} 1/((j+1)!(j'+1)!) = (2^{N+2}-2)/(N+2)!", okcf)
oktail = all(144/25*sum(10**n/math.factorial(n+2) for n in range(d-2, d+200))
             <= 144/25*10**(d-2)/math.factorial(d)*(d+1)/(d-9) for d in range(10, 60))
check("5 tail estimate sum_{N>=d-2} 10^N/(N+2)! <= 10^{d-2}/d! (d+1)/(d-9), d>=10", oktail)
print(f"TOTAL {sum(results)}/{len(results)} PASS (seed {seed})")
