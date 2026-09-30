"""Lemma C needs odds = the conditional law given the WHOLE past.  Cat law sqrt(2/3)|0..0> + sqrt(1/3)|1..1> on a ring of n sites
(the wall's own W9 counterexample).  Compare the calibration gap of
  (a) full-past predictive (attacker's cat_product.py object) and
  (b) nearest-neighbour-recorded-only odds (what the Admissibility axiom literally allows), same random orders.
Exact over the two configurations; random orders sampled."""
import numpy as np
rng = np.random.default_rng(5)
a2, b2 = 2/3, 1/3
def run(n, norders=4000):
    out = {"full": [], "nn": []}
    for cfg, w in ((0, a2), (1, b2)):
        for _ in range(norders):
            order = rng.permutation(n)
            rec = {}
            pf, pn = [], []
            for x in order:
                # full past predictive P(x=0 | recorded)
                if rec:
                    v = next(iter(rec.values()))
                    p_full = 1.0 if v == 0 else 0.0
                else:
                    p_full = a2
                nb = [(x-1) % n, (x+1) % n]
                got = [rec[y] for y in nb if y in rec]
                p_nn = (1.0 if got[0] == 0 else 0.0) if got else a2
                pf.append(p_full); pn.append(p_nn)
                rec[x] = cfg
            F = 1.0 if cfg == 0 else 0.0     # frequency of outcome 0
            out["full"].append((w, F - np.mean(pf)))
            out["nn"].append((w, F - np.mean(pn)))
    res = {}
    for k, v in out.items():
        wts = np.array([w for w, _ in v]); d = np.array([x for _, x in v])
        wts = wts / wts.sum()
        res[k] = (float((wts * d).sum()), float((wts * d**2).sum()))
    return res
for n in (8, 16, 32, 64):
    r = run(n)
    print(f"n={n:3d}  bound 1/(4n)={1/(4*n):.4f} | full-past predictive: mean gap {r['full'][0]:+.4f}, E[gap^2] {r['full'][1]:.5f} | NN-recorded-only odds: mean gap {r['nn'][0]:+.4f}, E[gap^2] {r['nn'][1]:.5f}")
