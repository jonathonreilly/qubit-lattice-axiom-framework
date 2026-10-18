#!/usr/bin/env python3
"""Independent check of B8 (frequency consistency), written from scratch.

Not derived from the B8 or B3 runners. Differences of path:
  * label drawn by the actual exponential race argmin_s E_s / w_s (not inverse CDF);
  * neighbours from flat-index arithmetic, not np.roll tables;
  * conditional frequencies computed per torus and their across-torus spread
    tested for 1/n scaling; three different deterministic site sequences.

Part 1 (exact arithmetic): own chi bound from Lemma 0 with own Gamma(d);
  SAW counts c_0..c_8 enumerated here, c_9..c_15 from OEIS A001412, then c_{n+1}<=5c_n.
  Theorem B m(eps), k_m recomputed.
Part 2 (MC, ferro (20,1,1) rule of the repo six-label product family):
  Var F_n scaling along (a) row-major contiguous, (b) separated sublattice, (c) fixed
  random permutation; conditional frequency F_n(0 | X_{+x}=0) and the formation-time
  context version, both their limits and their 1/sqrt(n) concentration.
"""
import math, sys, time
import numpy as np
from multiprocessing import Pool

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  :: {detail}" if detail else "")); sys.stdout.flush()

# ---------------------------------------------------------------- Part 1
def saw_counts(nmax):
    dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    cnt = [0]*(nmax+1)
    def rec(p, vis, n):
        cnt[n] += 1
        if n == nmax: return
        for d in dirs:
            q = (p[0]+d[0], p[1]+d[1], p[2]+d[2])
            if q not in vis:
                vis.add(q); rec(q, vis, n+1); vis.remove(q)
    rec((0,0,0), {(0,0,0)}, 0)
    return cnt

def part1():
    c = saw_counts(8)
    oeis = [1, 6, 30, 150, 726, 3534, 16926, 81390, 387966, 1853886, 8809878,
            41934150, 198842742, 943974510, 4468911678, 21175146054]
    check("P1a own SAW enumeration c_0..c_8 equals OEIS A001412", c == oeis[:9], str(c))
    cu = list(oeis)
    while len(cu) < 260: cu.append(cu[-1]*5)
    a = [cu[j]/math.factorial(j+1) for j in range(240)]
    # Gamma(d) = sum_{j+j' >= d-2} a_j a_j' : compute via convolution S_N = sum_{j+j'=N} a_j a_j'
    S = np.convolve(a, a)
    tail = np.cumsum(S[::-1])[::-1]  # tail[N] = sum_{N'>=N} S_N'
    def Gam(d): return float(tail[max(d-2, 0)])
    def ball(d):
        m = (d-1)//2
        return a[m] if m >= 1 else 1.0   # |S|=1: |S| c_m/(m+1)!
    chi = 0.25
    contrib = []
    for d in range(1, 200):
        t = (4*d*d+2)*min(0.25, 0.5*Gam(d), ball(d)); chi += t; contrib.append(t)
    print(f"   own rigorous chi bound (exact c to 15): {chi:.1f}; last-term {contrib[-1]:.2e}")
    check("P1b Lemma 0 single-site chi bound finite and <= 4069 (draft value 4068.7)", chi <= 4069.0, f"{chi:.1f}")
    # crude-only variant (c_n <= 6*5^(n-1))
    acr = [1.0] + [6*5**(j-1)/math.factorial(j+1) for j in range(1, 240)]
    Scr = np.convolve(acr, acr); tcr = np.cumsum(Scr[::-1])[::-1]
    chi_cr = 0.25 + sum((4*d*d+2)*min(0.25, 0.5*float(tcr[max(d-2,0)]), acr[(d-1)//2] if (d-1)//2 >= 1 else 1.0)
                        for d in range(1, 200))
    print(f"   chi bound with crude c_n<=6*5^(n-1): {chi_cr:.1f}")
    # Theorem B: smallest m with c_m/(m+1)! <= eps/4, exact c vs crude
    for eps in (0.1, 0.05, 0.01):
        m_ex = next(m for m in range(1, 200) if a[m] <= eps/4)
        m_cr = next(m for m in range(1, 200) if acr[m] <= eps/4)
        km = 1 + sum(4*d*d+2 for d in range(1, 2*m_cr+1))
        print(f"   eps={eps}: m(exact c)={m_ex}, m(crude)={m_cr}, k_m(crude m)={km}, rate n/{8*km/eps**2:.3g}")
    km14 = 1 + sum(4*d*d+2 for d in range(1, 29))
    check("P1c Theorem B example: m=14 valid at eps=0.05 and k_14=30913", a[14] <= 0.0125 and km14 == 30913,
          f"c_14/15! = {a[14]:.4g}; note exact c gives m=13 ({a[13]:.4g})")
    # Janson/Hoeffding chain: P <= 2exp(-2n(e/2)^2/k)+exp(-2n(e/4)^2/k) <= 3exp(-n e^2/(8k))
    ok = all(2*math.exp(-2*n*(e/2)**2/k) + math.exp(-2*n*(e/4)**2/k) <= 3*math.exp(-n*e*e/(8*k)) + 1e-300
             for n in (1, 10, 10**4, 10**8) for e in (0.01, 0.3, 1.0) for k in (1, 7, 30913))
    check("P1d Theorem B final constant combination 2e^{-ne^2/2k}+e^{-ne^2/8k} <= 3e^{-ne^2/8k}", ok)
    # Theorem C algebra: worst case over a grid of (a,b,r,q) with |a-r|<eta,|b-q|<eta, eta=q eps/4, a<=b, r<=q
    rng = np.random.default_rng(7); worst = 0.0
    for _ in range(200000):
        q = rng.uniform(1e-3, 1); r = rng.uniform(0, q); eps = rng.uniform(1e-3, 2); eta = q*eps/4
        aa = r + rng.uniform(-eta, eta); bb = q + rng.uniform(-eta, eta)
        if aa < 0 or bb <= 0: continue
        worst = max(worst, abs(aa/bb - r/q)/eps)
    check("P1e Theorem C ratio lemma: |a/b - r/q| < eps on the good event (random search)", worst < 1.0, f"max ratio {worst:.3f}")

# ---------------------------------------------------------------- Part 2
L = 24; N = L**3
def nbr_table(L):
    i = np.arange(L**3); x, y, z = i // (L*L), (i // L) % L, i % L
    f = lambda a, b, c: (a % L)*L*L + (b % L)*L + (c % L)
    return np.stack([f(x+1,y,z), f(x-1,y,z), f(x,y+1,z), f(x,y-1,z), f(x,y,z+1), f(x,y,z-1)], 1)
NB = nbr_table(L); NBl = NB.tolist()
# ferro (20,1,1): phi[t][s] = 20 if s==t, 1 if s antipode of t, 1 otherwise
PHI = [[(20.0 if s == t else 1.0) for s in range(6)] for t in range(6)]

def one_torus(seed):
    rg = np.random.default_rng(seed)
    T = rg.random(N); E = rg.exponential(size=(N, 6)).tolist()
    lab = [-1]*N; onlyplusx0 = bytearray(N)  # formation-time context: only +x formed, holding 0
    for x in np.argsort(T).tolist():
        w = [1.0]*6; nform = 0; plusx = -1
        for j, yy in enumerate(NBl[x]):
            t = lab[yy]
            if t >= 0:
                nform += 1; row = PHI[t]
                for s in range(6): w[s] *= row[s]
                if j == 0: plusx = t
        if nform == 1 and plusx == 0: onlyplusx0[x] = 1
        e = E[x]; best = 0; bv = e[0]/w[0]
        for s in range(1, 6):
            v = e[s]/w[s]
            if v < bv: bv = v; best = s
        lab[x] = best
    lab = np.array(lab); I = (lab == 0).astype(float)
    out = {}
    # sequences of distinct sites
    seqA = np.arange(N)                                   # row-major contiguous
    xs = np.arange(0, L, 3); g = np.stack(np.meshgrid(xs, xs, xs, indexing="ij"), -1).reshape(-1, 3)
    seqB = g[:, 0]*L*L + g[:, 1]*L + g[:, 2]               # spacing 3 sublattice (512 sites), |x-x'|_1>=3
    seqC = np.random.default_rng(999).permutation(N)       # fixed before any field
    for name, sq, ns in (("A", seqA, (24, 216, 1728, N)), ("B", seqB, (8, 64, 512)), ("C", seqC, (24, 216, 1728, N))):
        cs = np.cumsum(I[sq]); out[name] = [cs[n-1]/n for n in ns]
    # conditional frequencies along row-major sequence, prefixes n
    ctx = (lab[NB[:, 0]] == 0); tgt = ctx & (lab == 0)
    ctxT = np.frombuffer(bytes(onlyplusx0), dtype=np.uint8).astype(bool); tgtT = ctxT & (lab == 0)
    cond = []
    for n in (N//8, N//2, N):
        cond.append((tgt[:n].sum()/max(ctx[:n].sum(), 1), tgtT[:n].sum()/max(ctxT[:n].sum(), 1)))
    out["cond"] = cond; out["cnt"] = (int(ctx.sum()), int(tgt.sum()), int(ctxT.sum()), int(tgtT.sum()))
    # covariance function via FFT for chi_hat
    gI = I.reshape(L, L, L); fk = np.fft.fftn(gI - gI.mean())
    out["Cov"] = np.real(np.fft.ifftn(fk*np.conj(fk)))/N
    return out

def part2(R):
    with Pool(4) as pool: res = pool.map(one_torus, [1000 + s for s in range(R)])
    p = 1/6; pq = p*(1-p)
    Cz = sum(r["Cov"] for r in res)/R
    dd = np.indices((L,)*3); dd = np.minimum(dd, L-dd).sum(0)
    chi_hat = float(np.abs(Cz[dd <= 6]).sum())
    tau3 = float(np.abs(Cz[(dd >= 3) & (dd <= 6)]).sum())
    print(f"   ferro: chi_hat=sum_(|z|<=6)|C| = {chi_hat:.3f}; tau_hat(3) = {tau3:.4f}; p(1-p)={pq:.4f}")
    allok = True
    for name, ns in (("A", (24, 216, 1728, N)), ("B", (8, 64, 512)), ("C", (24, 216, 1728, N))):
        F = np.array([r[name] for r in res])
        for k, n in enumerate(ns):
            v = F[:, k]; nv = n*v.var(ddof=1)
            se = nv*math.sqrt(2/(R-1))  # approx SE of variance estimate
            mz = (v.mean()-p)/(v.std(ddof=1)/math.sqrt(R))
            print(f"   seq {name} n={n:6d}: mean {v.mean():.5f} (z {mz:+.2f})  n Var F_n = {nv:.4f} +- {se:.4f}")
            allok &= abs(mz) < 4
            if name == "B":
                allok &= abs(nv - pq) <= 4*se + tau3   # Theorem A separated form
            allok &= nv <= chi_hat + 4*se                 # Theorem A general form (empirical chi)
    check("M1 E F_n = p and n Var F_n <= chi_hat (+4SE) on 3 sequences; separated seq gives p(1-p)+tau(3)", allok)
    # geometry prediction: n Var F_n = (1/n) sum_z C(z) A_n(z), A_n = #ordered pairs of prefix sites at offset z
    # (finite-size growth of n Var toward chi is expected; Theorem A only bounds it by chi)
    xs = np.arange(0, L, 3); g = np.stack(np.meshgrid(xs, xs, xs, indexing="ij"), -1).reshape(-1, 3)
    seqs = {"A": np.arange(N), "B": g[:, 0]*L*L + g[:, 1]*L + g[:, 2], "C": np.random.default_rng(999).permutation(N)}
    nss = {"A": (24, 216, 1728, N), "B": (8, 64, 512), "C": (24, 216, 1728, N)}
    mask6 = (dd <= 6); ok2 = True; rows = []
    for name in ("A", "B", "C"):
        F = np.array([r[name] for r in res])
        for k, n in enumerate(nss[name]):
            ind = np.zeros(N); ind[seqs[name][:n]] = 1; gi = ind.reshape(L, L, L); fk = np.fft.fftn(gi)
            An = np.rint(np.real(np.fft.ifftn(fk*np.conj(fk))))
            pred = float((Cz*An)[mask6].sum())/n
            nv = n*F[:, k].var(ddof=1); se = nv*math.sqrt(2/(R-1))
            rows.append(f"{name}{n}: {nv:.3f} vs {pred:.3f}")
            ok2 &= abs(nv - pred) <= 4*se + 0.03
    print("   n Var F_n vs geometry prediction: " + "; ".join(rows))
    check("M2 n Var F_n equals the variance identity sum_z C(z)A_n(z)/n for all 3 sequences (4SE+0.03)", ok2)
    cond = np.array([r["cond"] for r in res])  # R x 3 x 2
    cnt = np.array([r["cnt"] for r in res]).sum(0)
    poolR = cnt[1]/cnt[0]; poolT = cnt[3]/cnt[2]
    print(f"   pooled: P(X0=0|X_+x=0) = {poolR:.4f} (rule weight 0.8);  formation-time context: {poolT:.4f}")
    sdR = cond[:, :, 0].std(0, ddof=1); sdT = cond[:, :, 1].std(0, ddof=1)
    print(f"   across-torus SD of conditional freq at n=N/8,N/2,N: Record ctx {np.round(sdR,4)}, formation ctx {np.round(sdT,4)}")
    seR = cond[:, 2, 0].std(ddof=1)/math.sqrt(R); seT = cond[:, 2, 1].std(ddof=1)/math.sqrt(R)
    check("M3 Record-context conditional freq converges to a non-0.8 value (|z vs 0.8| > 20)",
          abs(cond[:, 2, 0].mean()-0.8)/seR > 20, f"{cond[:,2,0].mean():.4f} +- {seR:.4f}")
    check("M4 formation-time-context conditional freq -> rule weight 0.8 (|z|<4)",
          abs(cond[:, 2, 1].mean()-0.8)/seT < 4, f"{cond[:,2,1].mean():.4f} +- {seT:.4f}")
    rR = sdR[0]/sdR[2]; rT = sdT[0]/sdT[2]
    check("M5 conditional-frequency SD shrinks ~ n^{-1/2} (N/8 -> N: ratio near sqrt 8=2.83, within [2,3.8])",
          2 < rR < 3.8 and 2 < rT < 3.8, f"Record ctx ratio {rR:.2f}, formation ctx ratio {rT:.2f}")

if __name__ == "__main__":
    t0 = time.time()
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 240
    part1(); part2(R)
    print(f"TOTAL PASS={PASS} FAIL={FAIL} ({time.time()-t0:.0f}s, R={R}, L={L})")
