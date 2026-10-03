"""A37 t5: classical analog (supplied; decohered possibilities) of one record moving through a gas of excitations
on a ring, under swap versus push bookkeeping.  NOT the framework's quantum dynamics: the possibilities are
replaced by a classical exclusion gas (density rho, symmetric hops with probability h per bond per half-tick,
never across the record).  The record steps with content-weighted odds (c/2)(w_exc n_y + w_vac (1 - n_y)).
Rules for a step x -> y (identical particles, so only occupations matter):
  SW  : y's occupation moves to x
  PL1 : y -> y+1, y+1 -> x (capped push, return jump 2)
  PA  : the train at y is pushed to the first vacancy ahead (equivalently y's excitation jumps there); x vacant
  PF  : y's excitation is erased; x vacant  (the gas is eaten along the path)
Usage: python3 t5_snowplough.py {blind|attract|repel}
"""
import sys, signal
import numpy as np
signal.alarm(55)
L, R, T = 200, 300, 1500
rho, h, c = 0.3, 0.3, 0.5
WEIGHTS = {"blind": (1.0, 1.0), "attract": (1.0, 0.2), "repel": (0.2, 1.0)}
wsel = sys.argv[1] if len(sys.argv) > 1 else "attract"
w_exc, w_vac = WEIGHTS[wsel]

def run(rule, seed):
    rng = np.random.default_rng(seed)
    ar = np.arange(R)
    n = (rng.random((R, L)) < rho).astype(np.int8)
    X = np.zeros(R, int); n[:, 0] = 0          # record at site 0 (placeholder 0)
    Xu = np.zeros(R, int); last = np.zeros(R, int); psum = 0.0; pcount = 0
    nexc0 = n.sum(1).astype(float)
    for t in range(T):
        for p in (0, 1):
            ii = np.arange(p, L, 2); jj = (ii + 1) % L
            sw = rng.random((R, ii.size)) < h
            sw &= ~((ii[None, :] == X[:, None]) | (jj[None, :] == X[:, None]))
            a = n[:, ii].copy(); b = n[:, jj].copy()
            n[:, ii] = np.where(sw, b, a); n[:, jj] = np.where(sw, a, b)
        yR = (X + 1) % L; yL = (X - 1) % L
        nR = n[ar, yR]; nL = n[ar, yL]
        pR = (c / 2) * (w_exc * nR + w_vac * (1 - nR)); pL = (c / 2) * (w_exc * nL + w_vac * (1 - nL))
        u = rng.random(R)
        go = np.where(u < pR, 1, np.where(u < pR + pL, -1, 0))
        for d in (1, -1):
            g = np.nonzero(go == d)[0]
            if g.size == 0:
                continue
            x = X[g]; y = (x + d) % L; y2 = (x + 2 * d) % L
            if rule == "SW":
                n[g, x] = n[g, y]
            elif rule == "PL1":
                ny, ny2 = n[g, y].copy(), n[g, y2].copy()
                n[g, x] = ny2; n[g, y2] = ny
            elif rule == "PA":
                occ = n[g, y] == 1
                gg, xx = g[occ], x[occ]
                if gg.size:
                    idx = (xx[:, None] + d * (2 + np.arange(L - 1))[None, :]) % L
                    vals = n[gg[:, None], idx]
                    first = np.argmax(vals == 0, axis=1)
                    n[gg, idx[np.arange(gg.size), first]] = 1
                n[g, x] = np.where(n[g, x] == 1, 1, 0)   # x stays vacant unless the train wrapped into it
            elif rule == "PF":
                n[g, x] = 0
            n[g, y] = 0                                 # record placeholder at the new site
            X[g] = y; Xu[g] += d
            has = last[g] != 0
            psum += np.sum(last[g][has] * d); pcount += has.sum()
            last[g] = d
    prof = np.array([n[ar, (X + d_ * s) % L].mean() for s in range(-15, 16) for d_ in [1]])
    # orient the profile along each run's net displacement so 'ahead' means the direction it travelled
    sgn = np.where(Xu >= 0, 1, -1)
    prof_or = np.array([np.mean(n[ar, (X + sgn * s) % L]) for s in range(-15, 16)])
    left_exc = n.sum(1).mean() / nexc0.mean()
    # length of the contiguous train of excitations directly ahead (along the net travel direction)
    idx = (X[:, None] + sgn[:, None] * (1 + np.arange(L - 1))[None, :]) % L
    vals = n[ar[:, None], idx]
    train = np.argmax(vals == 0, axis=1)
    return dict(msd=np.mean(Xu.astype(float) ** 2), speed=np.mean(np.abs(Xu)) / T, C1=psum / max(pcount, 1),
                prof=prof_or, left=left_exc, train=train.mean(), trainmax=train.max())

print(f"ring L={L}, runs {R}, ticks {T}, gas density {rho}, hop prob {h}, c={c}, weights {wsel} (w_exc={w_exc}, w_vac={w_vac})")
for rule in ["SW", "PL1", "PA", "PF"]:
    r = run(rule, seed=37)
    pr = r["prof"]
    print(f"  {rule:3s} MSD {r['msd']:9.1f}  mean |X|/T {r['speed']:.4f}  lag-1 step corr {r['C1']:+.4f}  excitations left {r['left']:.3f}"
          f"  train ahead: mean {r['train']:.1f}, max {r['trainmax']}")
    print(f"      density behind (s=-15..-1, oriented along net travel): {' '.join(f'{v:.2f}' for v in pr[:15])}")
    print(f"      density ahead  (s=+1..+15):                           {' '.join(f'{v:.2f}' for v in pr[16:])}")
