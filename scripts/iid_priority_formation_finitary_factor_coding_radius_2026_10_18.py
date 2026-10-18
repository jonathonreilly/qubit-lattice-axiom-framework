#!/usr/bin/env python3
"""B3 runner: coding radius of iid-priority formation fields (numerical checks).

Checks the load-bearing lemmas of docs/IID_PRIORITY_FORMATION_IS_A_FINITARY_FACTOR_OF_IID_NOISE_WITH_FACTORIAL_CODING_RADIUS_TAIL_BOUNDED_THEOREM_NOTE_2026-10-18.md numerically. Finite Monte Carlo
evidence only; the theorems are proved analytically in the note.

  A. Self-avoiding-walk counts c_n on Z^3 (exhaustive enumeration) against the
     literature sequence (OEIS A001412, an expected constant independent of this
     code) and against the crude bound 6*5^(n-1).
  B. Infinite-volume (lazily sampled) decreasing paths from the origin on Z^3:
     the exact identity E[# decreasing paths of length n] = c_n/(n+1)! and the
     tail P(L >= n) <= c_n/(n+1)! <= 6*5^(n-1)/(n+1)!.
  C. Two-copy determining-set intersection probability
     P(K_0(w) meets K_{d e}(w')) against the analytic Gamma(d) of Lemma 4.
  D. Concrete rules on an L^3 torus (native product (3,1,2), ferro product
     (20,1,1), copy-when-unanimous with zeros): (i) locality lemma by resampling
     the noise outside K_x and outside the ball B(x, L(x)+1) and recomputing the
     WHOLE field; (ii) pooled tail of L(x); (iii) |C(d)| <= 2*P_bad(d).
  E. Start-slice forgetting: a fixed slab of +x Records, ferro rule; the
     one-point function at distance h from the slab against 2*c_{h-1}/h!.

Usage: python3 scripts/iid_priority_formation_finitary_factor_coding_radius_2026_10_18.py [--quick] [--seed N]
"""
import argparse, math, random, sys, time
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    sys.stdout.flush()

OFFS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
# OEIS A001412: number of n-step self-avoiding walks on the cubic lattice.
A001412 = [1, 6, 30, 150, 726, 3534, 16926, 81390, 387966, 1853886, 8809878]

# ---------------------------------------------------------------- A. SAW counts
def saw_counts(nmax):
    counts = [0]*(nmax+1)
    visited = {(0,0,0)}
    def rec(p, n):
        counts[n] += 1
        if n == nmax: return
        x,y,z = p
        for dx,dy,dz in OFFS:
            q = (x+dx, y+dy, z+dz)
            if q not in visited:
                visited.add(q); rec(q, n+1); visited.discard(q)
    rec((0,0,0), 0)
    return counts

def saw_upper(c_exact, nmax):
    """c_n exact where enumerated, else c_m*5^(n-m) (non-reversal continuation)."""
    m = len(c_exact)-1
    return [c_exact[n] if n <= m else c_exact[m]*5**(n-m) for n in range(nmax+1)]

def gamma_bound(cup, d, jmax=80):
    """Gamma(d) = sum_{j+j' >= d-2} a_j a_j', a_j = c_j/(j+1)!  (Lemma 4)."""
    a = [cup[j]/math.factorial(j+1) for j in range(jmax+1)]
    tot = 0.0
    for j in range(jmax+1):
        for jp in range(jmax+1):
            if j+jp >= d-2: tot += a[j]*a[jp]
    return tot

def gamma_crude(d):
    """(144/25) * sum_{N >= max(d-2,0)} 10^N/(N+2)!  (closed-form version)."""
    M = max(d-2, 0)
    return 144/25*sum(math.exp(N*math.log(10) - math.lgamma(N+3)) for N in range(M, M+400))

def ball_bound(cup, d):
    """Ball-coupling version (Thm 3a) for single sites with osc f = osc g = 1:
    P(R > m) <= c_m/(m+1)!, m = floor((d-1)/2)."""
    m = (d-1)//2
    return min(1.0, cup[m]/math.factorial(m+1)) if m >= 1 else 1.0

# ------------------------------------------------ B/C. lazy infinite-volume field
def explore(rng, NMAX=40):
    """Sample iid U(0,1) times lazily on Z^3; return (L(0), path counts by length,
    ancestor set A(0), determining set K(0)=A u N(A))."""
    T = {}
    def t(p):
        v = T.get(p)
        if v is None:
            v = rng.random(); T[p] = v
        return v
    memo = {}
    def go(p):
        r = memo.get(p)
        if r is not None: return r
        tp = t(p); x,y,z = p
        cnt = [0]*(NMAX+1); cnt[0] = 1; L = 0
        for dx,dy,dz in OFFS:
            q = (x+dx,y+dy,z+dz)
            if t(q) < tp:
                Lq, cq = go(q)
                if Lq+1 > L: L = Lq+1
                for n in range(NMAX):
                    if cq[n] == 0 and n > Lq: break
                    cnt[n+1] += cq[n]
        memo[p] = (L, cnt)
        return memo[p]
    L, cnt = go((0,0,0))
    A = set(memo)
    K = set(A)
    for (x,y,z) in A:
        for dx,dy,dz in OFFS: K.add((x+dx,y+dy,z+dz))
    return L, cnt, A, K

# ---------------------------------------------------------------- D/E. torus
def torus_nbrs(L):
    idx = np.arange(L**3).reshape(L,L,L)
    cols = []
    for ax in range(3):
        for sh in (-1, 1):
            cols.append(np.roll(idx, sh, axis=ax).ravel())
    return [tuple(int(v) for v in row) for row in np.stack(cols,1)]

def torus_dist(L):
    c = np.indices((L,L,L)).reshape(3,-1).T
    def dist_from(x):
        d = np.abs(c - c[x]); d = np.minimum(d, L-d)
        return d.sum(1)
    return dist_from

VEC = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)

def product_rule(p, q, r):
    phi = [[float(r)]*6 for _ in range(6)]
    for a in range(3):
        phi[2*a][2*a] = phi[2*a+1][2*a+1] = float(p)
        phi[2*a][2*a+1] = phi[2*a+1][2*a] = float(q)
    def rule(eta, u):
        w = [1.0]*6
        for t in eta:
            row = phi[t]
            for s in range(6): w[s] *= row[s]
        tot = sum(w); acc = 0.0; thr = u*tot
        for s in range(6):
            acc += w[s]
            if thr < acc: return s
        return 5
    return rule

def copy_unanimous_rule(eta, u):
    """Repo's adverse rule: point mass at the common label if the formed
    neighbours are nonempty and identical, else uniform (has zeros; order-sensitive)."""
    if eta and all(t == eta[0] for t in eta): return eta[0]
    return min(int(6*u), 5)

def form(T, U, rule, NB, fixed=None):
    """Formation on a finite graph. fixed: dict site->label (start slice B).
    Returns labels and L(x) = longest decreasing path from x among non-B sites."""
    N = len(T)
    lab = [-1]*N; Ld = [0]*N
    isB = [False]*N
    if fixed:
        for s, v in fixed.items(): lab[s] = v; isB[s] = True
    order = np.argsort(T, kind="stable")
    for x in order.tolist():
        if isB[x]: continue
        eta = []; best = -1
        for z in NB[x]:
            lz = lab[z]
            if lz >= 0:
                eta.append(lz)
                if not isB[z] and Ld[z] > best: best = Ld[z]
        Ld[x] = best+1  # 0 if no formed non-B neighbour
        lab[x] = rule(eta, U[x])
    return np.array(lab), np.array(Ld)

def ancestors(x, T, NB, isB=None):
    A = {x}; st = [x]
    while st:
        y = st.pop()
        for z in NB[y]:
            if (isB is None or not isB[z]) and T[z] < T[y] and z not in A:
                A.add(z); st.append(z)
    K = set(A)
    for y in A: K.update(NB[y])
    return A, K

def corr_axes(lab, L, dmax):
    v = VEC[lab].reshape(L,L,L,3)
    return np.array([np.mean([(v*np.roll(v, -d, axis=ax)).sum(-1).mean() for ax in range(3)])/3
                     for d in range(dmax+1)])

# ====================================================================== main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--seed", type=int, default=20261018)
    args = ap.parse_args()
    q = args.quick
    t0 = time.time()
    rng = random.Random(args.seed); nrng = np.random.default_rng(args.seed)

    # ---------------- A
    nenum = 8 if q else 9
    c = saw_counts(nenum)
    check(f"A1 SAW counts c_0..c_{nenum} on Z^3 equal OEIS A001412",
          c == A001412[:nenum+1], f"enumerated {c}")
    check("A2 c_n <= 6*5^(n-1) for 1<=n<=%d" % nenum,
          all(c[n] <= 6*5**(n-1) for n in range(1, nenum+1)),
          "ratios " + ", ".join(f"{c[n]/(6*5**(n-1)):.3f}" for n in range(1, nenum+1)))
    cup = saw_upper(c, 100)

    # ---------------- B
    NS = 30000 if q else 120000
    NM = nenum
    Ls = np.zeros(NS, int); cnts = np.zeros((NS, NM+1)); Asz = np.zeros(NS); Krad = np.zeros(NS)
    Kzmin = np.zeros(NS, int); Kzmax = np.zeros(NS, int)
    for i in range(NS):
        L, cnt, A, K = explore(rng)
        Ls[i] = L; cnts[i] = cnt[:NM+1]; Asz[i] = len(A)
        Krad[i] = max(abs(a)+abs(b)+abs(cc) for (a,b,cc) in K)
        Kzmin[i] = min(k[2] for k in K); Kzmax[i] = max(k[2] for k in K)
    print(f"B: {NS} infinite-volume samples; mean |A(0)|={Asz.mean():.2f}, max L={Ls.max()}, "
          f"max radius(K)={int(Krad.max())}, radius(K)<=L+1 always: {bool((Krad <= Ls+1).all())}")
    check("B0 radius of K(0) <= L(0)+1 in every sample", bool((Krad <= Ls+1).all()))
    zs = []
    for n in range(1, NM+1):
        mu = cnts[:,n].mean(); se = cnts[:,n].std(ddof=1)/math.sqrt(NS); ex = c[n]/math.factorial(n+1)
        zs.append((n, mu, ex, (mu-ex)/se if se > 0 else 0.0))
    print("   n  mean#paths   c_n/(n+1)!    z")
    for n, mu, ex, z in zs: print(f"  {n:2d}  {mu:10.5f}  {ex:10.5f}  {z:+.2f}")
    check("B1 E[# decreasing paths of length n] = c_n/(n+1)!, |z|<4 for n=1..%d" % NM,
          all(abs(z) < 4 for *_, z in zs))
    print("   n  P(L>=n) emp     c_n/(n+1)!   6*5^(n-1)/(n+1)!  1/(n+1)! (lower)")
    okB2 = True; okB3 = True
    for n in range(1, 16):
        p = (Ls >= n).mean(); se = math.sqrt(max(p*(1-p), 1/NS)/NS)
        b1 = cup[n]/math.factorial(n+1); b0 = 6*5**(n-1)/math.factorial(n+1)
        lo = 1/math.factorial(n+1)
        print(f"  {n:2d}  {p:.3e}      {b1:.3e}    {b0:.3e}        {lo:.3e}")
        okB2 &= p <= b1 + 4*se
        okB3 &= p >= lo - 4*se
    check("B2 empirical P(L>=n) <= c_n/(n+1)! (+4 SE), n=1..15", okB2)
    check("B3 empirical P(L>=n) >= 1/(n+1)! (straight-path lower bound, -4 SE)", okB3)

    # ---------------- C
    NC = 20000 if q else 60000
    DMAX = 14
    hits = np.zeros((NC, DMAX+1))
    for i in range(NC):
        _,_,_,K1 = explore(rng); _,_,_,K2 = explore(rng)
        for d in range(1, DMAX+1):
            h = 0
            for ax in range(3):
                for k in K2:
                    kk = list(k); kk[ax] += d
                    if tuple(kk) in K1: h += 1; break
            hits[i,d] = h/3
    Pbad = hits.mean(0); Pse = hits.std(0, ddof=1)/math.sqrt(NC)
    print("   d  P_bad emp (two copies)   Gamma(d) exact-c   Gamma(d) crude 144/25*sum   ball c_m/(m+1)!")
    okC = True
    for d in range(1, DMAX+1):
        g = gamma_bound(cup, d); gc = gamma_crude(d)
        print(f"  {d:2d}  {Pbad[d]:.3e} +- {Pse[d]:.1e}     {g:.3e}          {gc:.3e}       {ball_bound(cup, d):.3e}")
        okC &= Pbad[d] <= min(1.0, g) + 4*max(Pse[d], 1/NC)
    check("C1 two-copy intersection probability <= Gamma(d) (+4 SE), d=1..%d" % DMAX, okC)
    dstar = next(d for d in range(1, 200) if gamma_crude(d) < 1)
    dstar2 = next(d for d in range(1, 200) if gamma_bound(cup, d) < 1)
    dball = next(d for d in range(1, 200) if ball_bound(cup, d) < 0.25)
    print(f"   two-copy Gamma(d) < 1 from d = {dstar2} (exact c_n) / {dstar} (crude); "
          f"ball bound c_m/(m+1)! < 1/4 from d = {dball}")
    for d in (20, 30, 40, 60):
        print(f"   d={d}: Gamma_crude={gamma_crude(d):.2e}  ball={ball_bound(cup, d):.2e}")
    check("C2 crude closed form dominates exact-count Gamma for d=1..60",
          all(gamma_crude(d) >= gamma_bound(cup, d)*(1-1e-12) for d in range(1, 61)))

    # ---------------- D
    Lt = 24 if q else 32
    NB = torus_nbrs(Lt); N = Lt**3; dist_from = torus_dist(Lt)
    rules = {"native(3,1,2)": product_rule(3,1,2), "ferro(20,1,1)": product_rule(20,1,1),
             "copy-unanimous": copy_unanimous_rule}
    # D(i) locality by resampling (full recomputation of the whole torus)
    ntrial = 6 if q else 10
    for rname in ("native(3,1,2)", "copy-unanimous"):
        rule = rules[rname]
        okK = okBall = True; changed_ctrl = 0; nctrl = 0
        for tr in range(ntrial):
            T = nrng.random(N); U = nrng.random(N)
            lab, Ld = form(T, U, rule, NB)
            cand = np.where((Ld >= 2) & (Ld <= 8))[0]
            x = int(nrng.choice(cand))
            A, K = ancestors(x, T, NB)
            Kmask = np.zeros(N, bool); Kmask[list(K)] = True
            # (a) resample outside K_x
            T2 = T.copy(); U2 = U.copy()
            out = ~Kmask; T2[out] = nrng.random(out.sum()); U2[out] = nrng.random(out.sum())
            lab2, _ = form(T2, U2, rule, NB); okK &= lab2[x] == lab[x]
            # (b) resample outside ball B(x, L(x)+1)
            ball = dist_from(x) <= Ld[x]+1
            T3 = T.copy(); U3 = U.copy(); o3 = ~ball
            T3[o3] = nrng.random(o3.sum()); U3[o3] = nrng.random(o3.sum())
            lab3, _ = form(T3, U3, rule, NB); okBall &= lab3[x] == lab[x]
            # control: resample all noise on K_x \ {x} (inside the determining set)
            T4 = T.copy(); U4 = U.copy(); inn = [a for a in K if a != x]
            T4[inn] = nrng.random(len(inn)); U4[inn] = nrng.random(len(inn))
            lab4, _ = form(T4, U4, rule, NB); nctrl += 1; changed_ctrl += int(lab4[x] != lab[x])
        check(f"D1 [{rname}] X_x unchanged after resampling all noise outside K_x ({ntrial} trials, full recompute)", okK)
        check(f"D2 [{rname}] X_x unchanged after resampling all noise outside B(x, L(x)+1)", okBall)
        check(f"D3 [{rname}] control: resampling noise on K_x minus x changes X_x in some trial (test not vacuous)",
              changed_ctrl > 0, f"{changed_ctrl}/{nctrl} changed")

    # D(ii)+(iii): covariance and tail
    nsamp = 6 if q else 16
    dmax = Lt//2
    for rname, rule in rules.items():
        Cs = []; tails = []
        for s in range(nsamp):
            T = nrng.random(N); U = nrng.random(N)
            lab, Ld = form(T, U, rule, NB)
            Cs.append(corr_axes(lab, Lt, dmax))
            tails.append([(Ld >= n).mean() for n in range(0, 16)])
        Cs = np.array(Cs); Cm = Cs.mean(0); Cse = Cs.std(0, ddof=1)/math.sqrt(nsamp)
        tails = np.array(tails); tm = tails.mean(0); tse = tails.std(0, ddof=1)/math.sqrt(nsamp)
        line = ", ".join(f"C({d})={Cm[d]:+.4f}" for d in range(0, 7))
        print(f"   [{rname}] {line}; |C(d)| d>=8 max {np.abs(Cm[8:]).max():.1e}")
        okT = all(tm[n] <= cup[n]/math.factorial(n+1) + 4*tse[n] + 1e-12 for n in range(1, 16))
        check(f"D4 [{rname}] torus pooled P(L(x)>=n) <= c_n/(n+1)! (+4 SE), n=1..15", okT,
              "P(L>=6)=%.2e vs %.2e" % (tm[6], cup[6]/math.factorial(7)))
        okCov = True; worst = 0; rows = []
        for d in range(1, min(dmax, DMAX)+1):
            lhs = abs(Cm[d]); rhs = 2*Pbad[d] + 4*Cse[d] + 4*2*Pse[d]
            okCov &= lhs <= rhs
            if lhs > 3*Cse[d] and Pbad[d] > 4*Pse[d]:
                worst = max(worst, lhs/(2*Pbad[d])); rows.append(d)
        check(f"D5 [{rname}] |C(d)| <= 2*P_bad(d) (+ stat. tolerance), d=1..{min(dmax, DMAX)}", okCov,
              f"max |C|/(2 P_bad) over resolved d {rows} = {worst:.3f}")

    # ---------------- E. start-slice forgetting
    Le = 24 if q else 32
    NBe = torus_nbrs(Le); Ne = Le**3
    zc = np.indices((Le,Le,Le))[2].ravel()
    fixed = {int(s): 0 for s in np.where(zc == 0)[0]}
    ne = 8 if q else 16
    prof = []
    for s in range(ne):
        T = nrng.random(Ne); U = nrng.random(Ne)
        lab, _ = form(T, U, rules["ferro(20,1,1)"], NBe, fixed)
        vx = VEC[lab][:,0]
        prof.append([vx[zc == z].mean() for z in range(Le)])
    prof = np.array(prof); pm = prof.mean(0); pse = prof.std(0, ddof=1)/math.sqrt(ne)
    # Few samples give an unreliable per-plane SE; use the pooled per-plane spread
    # (all planes, centred per plane) as a floor. Noise scale only, not a fit.
    pooled = math.sqrt(((prof - pm)**2).sum()/(prof.size - Le))/math.sqrt(ne)
    pse = np.maximum(pse, pooled)
    print(f"E: {ne} tori L={Le}, pooled per-plane SE of the mean = {pooled:.4f}")
    okE = True
    okE2 = True
    print("   h  <v_x>(h)        2*P(K_x meets slab) [MC, part B]   analytic 2*c_(h-1)/h!")
    for h in range(1, Le//2+1):
        m = 0.5*(pm[h] + pm[Le-h]); se = 0.5*math.sqrt(pse[h]**2 + pse[Le-h]**2)
        reach = ((Kzmin <= -h) | (Kzmax >= Le-h)); pr = reach.mean()
        prse = math.sqrt(max(pr*(1-pr), 1/NS)/NS)
        b = 2.0 if h == 1 else min(2.0, 2*cup[h-1]/math.factorial(h))
        print(f"  {h:2d}  {m:+.4f}+-{se:.4f}   {2*pr:.3e}                          {b:.3e}")
        okE &= abs(m) <= 2*pr + 4*se + 8*prse
        okE2 &= abs(m) <= b + 4*se
    check("E1 ferro(20,1,1), fixed +x slab: |<v_x>(h)| <= 2 P(K_x meets slab) (+tol), h=1..%d" % (Le//2), okE)
    check("E2 same, against the analytic 2 c_(h-1)/h! (nontrivial only for h >= 12)", okE2,
          f"<v_x>(1)={0.5*(pm[1]+pm[-1]):+.3f}, <v_x>(4)={0.5*(pm[4]+pm[-4]):+.4f}")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}  ({time.time()-t0:.0f} s, seed {args.seed}, quick={q})")
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
