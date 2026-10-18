#!/usr/bin/env python3
"""B8 runner: spatial frequency consistency for iid-priority formation fields.

Numerical checks for docs/IID_PRIORITY_FORMATION_SPATIAL_FREQUENCY_CONSISTENCY_BOUNDED_THEOREM_NOTE_2026-10-18.md. This is finite Monte Carlo evidence. The
theorems are proved analytically in the note; the runner does not prove them.

Simulation code (torus neighbours, the six-label product rules and the
copy-when-unanimous rule) is adapted from the sibling B3 runner
(scripts/iid_priority_formation_finitary_factor_coding_radius_2026_10_18.py), which is used
read-only. The formation loop is rewritten here so that rules can read the
direction of each formed neighbour and so that the formation-time neighbour
set of every site is recorded.

Groups
  X. Exact arithmetic: the repo's stationary counterexample (2026-09-02 note,
     section 8) and the explicit rigorous constants of Theorems A and B.
  O. Order-blind soldered chiral-pair rule (12 classes, kappa=1/2; 2026-10-16
     note). Expected constants come from that note's product form
     prod r0 prod phi, which is computed here from the formula, not from the
     simulation:
       O1 class frequencies -> 1/12;
       O2 conditional frequencies given one or two neighbour Records -> the
          rule weight r(a|eta) (exact, by the product form);
       O3 n Var(box mean of h) equals 1/3 + (1/36)(l-1)/l exactly, where
          h(a) = X_{+x}(a) + X_{-x}(a), for l = 1,2,4,8,11;
       O4 along a fixed deterministic sequence of distinct torus sites
          (a scrambled enumeration chosen before and independently of the
          fields), n Var(F_n) equals 1/3 + (2/n)(#x-bonds among the first n
          sites)(1/72), the exact prediction for that site set.
  F. Order-sensitive ferro product rule (20,1,1) (B3 class, no exact law):
       F1 label-0 frequency -> 1/6 (label symmetry of rule and marks);
       F2 n Var(F_l) stays below the covariance sum chi estimated from the
          measured correlation function (Theorem A's inequality), and equals
          sum_z C(z) times the box-overlap weight (the variance identity);
       F3 frequency given the formation-time context "only formed neighbour
          was +x, holding label 0" -> rule weight 20/25 (exact, by the race);
       F4 frequency given the final-Record context "+x neighbour holds 0"
          differs from 20/25 (witness that the formation-law conditional is
          not the rule weight for an order-sensitive rule).
  C. Copy-when-unanimous rule (zeros, order-sensitive): label frequency 1/6
     and the same two variance checks.
  R. A stationary formation law outside the class (rule drawn once, ferro or
     native with probability 1/2): the per-torus frequency of x-bond label
     agreement does not concentrate (non-ergodic), unlike either pure rule.

Usage: python3 runner_frequency_consistency.py [--quick] [--seed N]
"""
import argparse, math, sys, time
from fractions import Fraction as Fr
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    sys.stdout.flush()

# Direction index j: 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z; opposite is j^1.
OFFS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
A001412 = [1, 6, 30, 150, 726, 3534, 16926, 81390, 387966, 1853886, 8809878]

def torus_nbrs(L):
    """Adapted from B3: column j is the neighbour at OFFS[j]."""
    idx = np.arange(L**3).reshape(L,L,L)
    cols = []
    for ax in range(3):
        for sh in (-1, 1):
            cols.append(np.roll(idx, sh, axis=ax).ravel())
    return [tuple(int(v) for v in row) for row in np.stack(cols,1)]

def form(T, U, rule, NB):
    """Formation in increasing T. rule(eta, u) with eta a list of
    (direction index, label) of already-formed neighbours. Returns labels and
    the bitmask of neighbour directions formed before each site."""
    N = len(T)
    lab = [-1]*N; mask = [0]*N
    for x in np.argsort(T, kind="stable").tolist():
        eta = []; m = 0; nb = NB[x]
        for j in range(6):
            lz = lab[nb[j]]
            if lz >= 0:
                eta.append((j, lz)); m |= 1 << j
        mask[x] = m
        lab[x] = rule(eta, U[x])
    return np.array(lab), np.array(mask)

def sample_cat(w, u):
    tot = sum(w); acc = 0.0; thr = u*tot
    for s, ws in enumerate(w):
        acc += ws
        if thr < acc: return s
    return len(w)-1

def product_rule(p, q, r):
    """B3's six-label product rule (labels 2a, 2a+1 antipodal on axis a)."""
    phi = [[float(r)]*6 for _ in range(6)]
    for a in range(3):
        phi[2*a][2*a] = phi[2*a+1][2*a+1] = float(p)
        phi[2*a][2*a+1] = phi[2*a+1][2*a] = float(q)
    def rule(eta, u):
        w = [1.0]*6
        for _, t in eta:
            row = phi[t]
            for s in range(6): w[s] *= row[s]
        return sample_cat(w, u)
    return rule, phi

def copy_unanimous_rule(eta, u):
    """B3's copy-when-unanimous rule (zeros, order-sensitive)."""
    if eta and all(t == eta[0][1] for _, t in eta): return eta[0][1]
    return min(int(6*u), 5)

# --- order-blind soldered chiral-pair rule, compressed to 12 classes --------
# class label = 2*j + c: points along direction j, chirality chi = +1 (c=0) or -1 (c=1).
KAPPA = 0.5
def Xc(d, a):
    return (1 if a % 2 == 0 else -1) if a // 2 == d else 0
def phi_cp(d, a, b):
    """Bond factor for site value a with a neighbour in direction d holding b."""
    return 1.0 + KAPPA*Xc(d, a)*Xc(d ^ 1, b)
def chiral_rule(eta, u):
    w = [1.0]*12
    for d, b in eta:
        xb = Xc(d ^ 1, b)
        if xb:
            w[2*d] *= 1.0 + KAPPA*xb
            w[2*d+1] *= 1.0 - KAPPA*xb
    return sample_cat(w, u)
def r_chiral(a, eta):
    """Exact rule weight r(a|eta) = (1/12) prod phi (normalised, 2026-10-16 note)."""
    p = Fr(1, 12)
    for d, b in eta:
        p *= Fr(phi_cp(d, a, b)).limit_denominator(4)
    return p

def ball_size(r):
    return 1 + sum(4*d*d + 2 for d in range(1, r+1))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--seed", type=int, default=20261018)
    args = ap.parse_args(); q = args.quick
    t0 = time.time(); rng = np.random.default_rng(args.seed)

    # ======================================================= X. exact arithmetic
    p = Fr(1, 4); m = 4
    var_iid = p*(1-p)/m; var_corr = p*(1-p)
    check("X1 repo counterexample B~Bern(1/4), X_i=B: Var(F_4)=3/16 vs IID 3/64 (exact)",
          var_iid == Fr(3, 64) and var_corr == Fr(3, 16))
    # Cov(X_0, X_i) = 3/16 for every i: covariance sum diverges, Theorem A's hypothesis fails.
    check("X2 counterexample: Cov(X_i,X_j)=p(1-p)=3/16 for all i!=j, so sum_z|C(z)| diverges "
          "and n Var(F_n) = 3n/16 grows linearly", all(Fr(3,16)*n == n*var_corr for n in (1, 10, 100)))
    # Rigorous constants (Z^3 nearest neighbour), single-site indicator, osc = 1.
    cup = [A001412[n] if n < len(A001412) else A001412[-1]*5**(n-len(A001412)+1) for n in range(200)]
    def gamma_bd(d, jmax=120):
        a = [cup[j]/math.factorial(j+1) for j in range(jmax+1)]
        return sum(a[j]*a[jp] for j in range(jmax+1) for jp in range(jmax+1) if j+jp >= d-2)
    def ball_bd(d):
        mm = (d-1)//2
        return cup[mm]/math.factorial(mm+1) if mm >= 1 else 1.0
    chi_bd = 0.25
    for d in range(1, 120):
        chi_bd += (4*d*d+2)*min(0.25, 0.5*gamma_bd(d), ball_bd(d))
    print(f"X: rigorous chi bound for any single-site indicator on Z^3: chi <= {chi_bd:.1f}")
    for eps in (0.1, 0.05, 0.01):
        mm = next(k for k in range(1, 200) if cup[k]/math.factorial(k+1) <= eps/4)
        km = ball_size(2*mm)
        print(f"   Theorem B, |S|=1, eps={eps}: m={mm}, k_m=|B(2m)|={km}, "
              f"P(|F_n-p|>=eps) <= 3 exp(-n/{8*km/eps**2:.3g})")
    check("X3 rigorous chi bound is finite and the tail sum beyond d=119 is negligible",
          math.isfinite(chi_bd) and (4*119**2+2)*ball_bd(119) < 1e-30, f"chi_bd={chi_bd:.1f}")

    # ============================================== O. order-blind chiral-pair rule
    L = 18 if q else 24; NB = torus_nbrs(L); N = L**3
    R = 60 if q else 300
    coords = np.indices((L,L,L)).reshape(3,-1).T
    hval = np.array([Xc(0, a) + Xc(1, a) for a in range(12)], float)
    # deterministic scrambled sequence, fixed before any field is drawn
    seq = np.random.default_rng(12345).permutation(N)
    checkpoints = [n for n in (50, 500, 5000, N) if n <= N]
    # exact x-bond counts in the prefix sets (torus graph, wrap included)
    pos = np.empty(N, int); pos[seq] = np.arange(N)
    xn = np.array([NB[s][0] for s in range(N)])  # +x neighbour
    bond_rank = np.maximum(pos, pos[xn])  # an x-bond enters the prefix at this rank
    nb_prefix = {n: int((bond_rank < n).sum()) for n in checkpoints}
    ells = [l for l in (1, 2, 4, 8, 11) if (l+1) <= L//2 + 1 or l == 1]
    box_vals = {l: [] for l in ells}
    seq_vals = {n: [] for n in checkpoints}
    cls_freq = []; ctx1 = []; ctx2 = []
    a1, b1 = 0, 2*1 + 0        # a=(+x,+1); +x neighbour holds (-x,+1)
    a1m = 1                    # a=(+x,-1)
    b2 = 0                     # -x neighbour holds (+x,+1)
    for s in range(R):
        T = rng.random(N); U = rng.random(N)
        lab, _ = form(T, U, chiral_rule, NB)
        cls_freq.append(np.bincount(lab, minlength=12)/N)
        g = lab.reshape(L,L,L); h = hval[lab].reshape(L,L,L)
        gp = np.roll(g, -1, axis=0); gm = np.roll(g, 1, axis=0)
        c1 = (gp == b1); c2 = c1 & (gm == b2)
        ctx1.append([c1.sum(), (c1 & (g == a1)).sum(), (c1 & (g == a1m)).sum()])
        ctx2.append([c2.sum(), (c2 & (g == a1)).sum(), (c2 & (g == a1m)).sum(), (c2 & (g == 4)).sum()])
        for l in ells:
            st = l + 1; k = L // st
            for i in range(k):
                for j in range(k):
                    for kk in range(k):
                        box_vals[l].append(h[i*st:i*st+l, j*st:j*st+l, kk*st:kk*st+l].mean())
        hs = hval[lab][seq]; cs = np.cumsum(hs)
        for n in checkpoints: seq_vals[n].append(cs[n-1]/n)
    cf = np.array(cls_freq); cfm = cf.mean(0); cfse = cf.std(0, ddof=1)/math.sqrt(R)
    zc = np.abs(cfm - 1/12)/cfse
    print(f"O: {R} tori L={L}, chiral-pair rule; class freq mean range [{cfm.min():.5f},{cfm.max():.5f}], max |z|={zc.max():.2f}")
    check("O1 all 12 class frequencies -> 1/12 (|z| < 4)", bool((zc < 4).all()))
    dev = np.abs(cf - 1/12).max()
    check("O1b every single torus: max_a |F(a) - 1/12| <= 6 sqrt(chi/n) with exact chi=p(1-p)",
          dev <= 6*math.sqrt((1/12)*(11/12)/N), f"max dev {dev:.4f} vs {6*math.sqrt((11/144)/N):.4f}")
    c1a = np.array(ctx1, float); c2a = np.array(ctx2, float)
    exp1 = [float(r_chiral(a1, [(0, b1)])), float(r_chiral(a1m, [(0, b1)]))]
    exp2 = [float(r_chiral(a1, [(0, b1), (1, b2)])), float(r_chiral(a1m, [(0, b1), (1, b2)])),
            float(r_chiral(4, [(0, b1), (1, b2)]))]
    print(f"   exact rule weights: one-nbr context {exp1}; two-nbr context {exp2}")
    okO2 = True
    for arr, exps, tag in ((c1a, exp1, "1"), (c2a, exp2, "2")):
        for i, e in enumerate(exps):
            ratio = arr[:, i+1].sum()/arr[:, 0].sum()
            per = arr[:, i+1]/arr[:, 0]
            se = per.std(ddof=1)/math.sqrt(R)
            z = (ratio - e)/se
            print(f"   context{tag} target{i}: freq {ratio:.5f} vs r(a|eta) {e:.5f}  z={z:+.2f}  (pooled context count {int(arr[:,0].sum())})")
            okO2 &= abs(z) < 4
    check("O2 conditional frequencies given 1- and 2-neighbour Record contexts -> exact r(a|eta) (|z|<4)", okO2)
    okO3 = True
    print("   l   replicas  n Var(box mean h)  exact 1/3+(1/36)(l-1)/l   z")
    for l in ells:
        v = np.array(box_vals[l]); n = l**3; y = (v - v.mean())**2
        est = n*y.mean()*len(v)/(len(v)-1); se = n*y.std(ddof=1)/math.sqrt(len(v))
        ex = 1/3 + (1/36)*(l-1)/l; z = (est - ex)/se
        print(f"  {l:2d}  {len(v):7d}   {est:.4f} +- {se:.4f}     {ex:.4f}               {z:+.2f}")
        okO3 &= abs(z) < 4
    check("O3 n Var(box mean) equals the exact 1-dependent value for every box size (|z|<4); O(1/n) law", okO3)
    okO4 = True
    print("   n     #x-bonds  n Var(F_n) along fixed sequence   exact          z")
    for n in checkpoints:
        v = np.array(seq_vals[n]); y = (v - v.mean())**2
        est = n*y.mean()*R/(R-1); se = n*y.std(ddof=1)/math.sqrt(R)
        ex = 1/3 + (2/n)*nb_prefix[n]*(1/72); z = (est - ex)/se
        print(f"  {n:5d}  {nb_prefix[n]:6d}   {est:.4f} +- {se:.4f}                {ex:.4f}       {z:+.2f}")
        okO4 &= abs(z) < 4 and abs(v.mean())/max(math.sqrt(ex/n/R), 1e-12) < 4
    check("O4 fixed deterministic site sequence: mean -> 0 and n Var(F_n) = exact prediction (|z|<4)", okO4)

    # ============================================== F. ferro (order-sensitive) rule
    Lf = 20 if q else 32; NBf = torus_nbrs(Lf); Nf = Lf**3
    Rf = 30 if q else 120
    ferro, phif = product_rule(20, 1, 1)
    native, _ = product_rule(3, 1, 2)
    ellsf = [1, 2, 4, 8] + ([] if q else [12])
    def run_rule(rule, Rn, Lr, NBr, ells_r, gap, want_ctx=False):
        Nr = Lr**3; xnb = np.array([NBr[x][0] for x in range(Nr)])
        fr = []; boxes = {l: [] for l in ells_r}; Csum = None; ctxF = []; ctxT = []; agree = []
        for s in range(Rn):
            T = rng.random(Nr); U = rng.random(Nr)
            lab, mask = form(T, U, rule, NBr)
            ind = (lab == 0).astype(float); g = ind.reshape(Lr,Lr,Lr)
            fr.append(ind.mean())
            fk = np.fft.fftn(g - g.mean()); Cz = np.real(np.fft.ifftn(fk*np.conj(fk)))/Nr
            Csum = Cz if Csum is None else Csum + Cz
            for l in ells_r:
                st = l + gap; k = Lr // st
                for i in range(k):
                    for j in range(k):
                        for kk in range(k):
                            boxes[l].append(g[i*st:i*st+l, j*st:j*st+l, kk*st:kk*st+l].mean())
            lg = lab.reshape(Lr,Lr,Lr); gp = np.roll(lg, -1, axis=0)
            agree.append((lg == gp).mean())
            if want_ctx:
                cF = (gp == 0)
                ctxF.append([cF.sum(), (cF & (lg == 0)).sum()])
                cT = (mask == 1) & (lab[xnb] == 0)
                ctxT.append([cT.sum(), (cT & (lab == 0)).sum(), (cT & (lab == 1)).sum()])
        return np.array(fr), boxes, Csum/Rn, np.array(ctxF, float), np.array(ctxT, float), np.array(agree)

    def plateau_checks(tag, fr, boxes, Cz, Rn, Lr, ells_r):
        fm = fr.mean(); se = fr.std(ddof=1)/math.sqrt(Rn); z = (fm - 1/6)/se
        check(f"{tag}1 label-0 frequency -> 1/6 (label symmetry), |z|<4", abs(z) < 4,
              f"mean {fm:.5f} +- {se:.5f}, z={z:+.2f}")
        # chi estimated from the measured correlation function (torus-averaged)
        dist = np.indices((Lr,)*3); dist = np.minimum(dist, Lr - dist).sum(0)
        chi_hat = float(np.abs(Cz[dist <= 6]).sum()); chi_signed = float(Cz[dist <= 6].sum())
        print(f"   [{tag}] chi_hat = sum_(|z|<=6) |C(z)| = {chi_hat:.4f} (signed {chi_signed:.4f}); p(1-p)={5/36:.4f}")
        rows = []
        for l in ells_r:
            v = np.array(boxes[l]); n = l**3; y = (v - v.mean())**2
            est = n*y.mean()*len(v)/(len(v)-1); sev = n*y.std(ddof=1)/math.sqrt(len(v))
            # prediction from the measured C(z): sum_z C(z) prod_a (1-|z_a|/l)_+
            zz = np.indices((Lr,)*3); zz = np.minimum(zz, Lr - zz)
            wgt = np.prod(np.clip(1 - zz/l, 0, None), axis=0)
            pred = float((Cz*wgt)[dist <= 6].sum())
            rows.append((l, len(v), est, sev, pred))
            print(f"   [{tag}] l={l:2d} replicas={len(v):5d}  n Var(F_l)={est:.4f} +- {sev:.4f}   from C(z): {pred:.4f}")
        ok_bound = all(est <= chi_hat + 4*sev for (_, _, est, sev, _) in rows)
        check(f"{tag}2a n Var(F_l) <= chi_hat (+4 SE) for all box sizes (Var = O(1/n))", ok_bound)
        okp = all(abs(est - pred) <= 4*sev + 0.02*abs(pred) for (_, _, est, sev, pred) in rows)
        check(f"{tag}2b direct box variance matches sum_z C(z)(overlap weight) (+4 SE, 2%)", okp)

    gapf = 4
    fr, boxes, Cz, ctxF, ctxT, agree_f = run_rule(ferro, Rf, Lf, NBf, ellsf, gapf, want_ctx=True)
    print(f"F: ferro(20,1,1), {Rf} tori L={Lf}")
    plateau_checks("F", fr, boxes, Cz, Rf, Lf, ellsf)
    pT = ctxT[:, 1].sum()/ctxT[:, 0].sum(); perT = ctxT[:, 1]/ctxT[:, 0]
    seT = perT.std(ddof=1)/math.sqrt(Rf); zT = (pT - 20/25)/seT
    p1T = ctxT[:, 2].sum()/ctxT[:, 0].sum(); se1T = (ctxT[:, 2]/ctxT[:, 0]).std(ddof=1)/math.sqrt(Rf)
    z1T = (p1T - 1/25)/se1T
    check("F3 formation-time context (only +x formed earlier, holding 0): freq(0) -> 20/25, freq(1) -> 1/25 (|z|<4)",
          abs(zT) < 4 and abs(z1T) < 4,
          f"freq(0)={pT:.4f}+-{seT:.4f} (z={zT:+.2f}), freq(1)={p1T:.4f} (z={z1T:+.2f}), pooled context count {int(ctxT[:,0].sum())}")
    pF = ctxF[:, 1].sum()/ctxF[:, 0].sum(); seF = (ctxF[:, 1]/ctxF[:, 0]).std(ddof=1)/math.sqrt(Rf)
    zF = (pF - 0.8)/seF
    check("F4 final-Record context (+x neighbour holds 0): freq(0) differs from rule weight 0.8 by > 6 SE",
          abs(zF) > 6, f"freq(0 | X_+x=0) = {pF:.4f} +- {seF:.4f}, z vs 0.8 = {zF:+.1f}")

    # ============================================== C. copy-when-unanimous rule
    Rc = 20 if q else 60
    frc, boxc, Czc, _, _, _ = run_rule(copy_unanimous_rule, Rc, Lf, NBf, ellsf, gapf)
    print(f"C: copy-unanimous, {Rc} tori L={Lf}")
    plateau_checks("C", frc, boxc, Czc, Rc, Lf, ellsf)

    # ============================================== R. non-ergodic mixture (outside the class)
    Rn = 20 if q else 40
    _, _, _, _, _, agree_n = run_rule(native, Rn, Lf, NBf, [1], gapf)
    af, an = agree_f[:Rn], agree_n
    mix = np.concatenate([af, an])  # rule drawn once per torus with prob 1/2 (equal counts)
    within = 0.5*(af.var(ddof=1) + an.var(ddof=1))
    print(f"R: x-bond agreement freq: ferro {af.mean():.4f}+-{af.std(ddof=1):.4f}, native {an.mean():.4f}+-{an.std(ddof=1):.4f}; "
          f"mixture between-torus SD {mix.std(ddof=1):.4f} vs within-rule SD {math.sqrt(within):.4f}")
    check("R1 rule-mixture (stationary, non-ergodic): frequency stays bimodal; mixture SD > 20x pure-rule SD at n=%d" % Nf,
          mix.std(ddof=1) > 20*math.sqrt(within))

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}  ({time.time()-t0:.0f} s, seed {args.seed}, quick={q})")
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
