"""R3-3 (a): split the frame-to-frame variation of the per-realization link sum into an in-band part (average over nearby
lattice translates x = g l, |l| small vs W) and an out-of-band part (variation over x at fixed frame).
Reuses r33_D's link-vector enumeration. Poisson comparator: Var ~ 3 * mean (E1'-b bound, leading)."""
import numpy as np, time, sys
src = open('r33_D_perrealization_links.py').read().split('rng = np.random.default_rng(1)')[0]
exec(src)
rng = np.random.default_rng(7)
ls = [np.array(l, float) for l in [(0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,-1,0,0),(0,1,1,0),(0,1,-1,1),(0,2,0,0),
                                     (0,0,2,-1),(0,-1,-1,-1),(0,2,1,0),(0,0,-2,1)]]
Lp = np.array([[np.sqrt(7)*l[0], l[1], l[2], l[3]] for l in ls])
for D in (20.0, 40.0, 80.0):
    W = D/5; mv = mean_val(D, W)
    yc = np.array([D, D, 0, 0])
    tot_pt, tot_avg, within = [], [], []
    for s in range(30):
        eta = rng.uniform(0, 1.0)
        Gm = randrot(rng) @ boost(eta, rng.normal(size=3)) @ randrot(rng)
        Y = X @ Gm.T
        vals = []
        for lp in Lp:
            sh = Gm @ lp
            d2 = ((Y - sh - yc)**2).sum(1)    # J(g(v - l)) shifted: y = x - g v with x = g l  ->  g v - g l vs yc
            vals.append(np.exp(-d2/(2*W*W)).sum())
        vals = np.array(vals)
        # remove the smooth gradient of J across the l's (in-band, deterministic): fit linear in (g l)
        A = np.c_[np.ones(len(Lp)), (Lp @ Gm.T)]
        coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
        resid = vals - A @ coef
        tot_pt.append(vals[0]); tot_avg.append(coef[0]); within.append(resid.std())
    tot_pt = np.array(tot_pt); tot_avg = np.array(tot_avg); within = np.array(within)
    print(f"D={D:4.0f} W={W:4.1f} mean={mv:8.2f}: frame sd/mean at one point {tot_pt.std()/mv:.4f}; "
          f"frame sd/mean of the smooth (in-band) part {tot_avg.std()/mv:.4f}; within-frame (lattice-scale) sd/mean {within.mean()/mv:.4f}; "
          f"Poisson sqrt(3/mean) = {np.sqrt(3/mv):.4f}")
print(f"time {time.time()-t0:.1f}s")
