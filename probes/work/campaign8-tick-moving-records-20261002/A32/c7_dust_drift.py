"""
A32 check C7: which lapse paces a record's step? (claim-rule convention across a lapse gradient)

Supplied toy (classical record part only, continuous-time limit of SW+CL with blind weights): one record
wandering on a chain of 101 sites with reflecting ends; lapse N(x) = 1 - 0.3 x/100 (slower clocks at large x).
A step x->y needs a claim; its rate per coordinate time is set by
  claimant-scheduled: k N(y)   (the claim is the empty site's instrument, at the empty site's lapse-paced ticks)
  record-scheduled:   k N(x)   (the record's own clock sets its steps)
  bond-symmetric:     k (N(x)+N(y))/2
Prediction (detailed balance, EXACT): stationary density proportional to N, 1/N and uniform respectively.
"""
import signal
import numpy as np
signal.alarm(55)
Ls = 101
x = np.arange(Ls)
N = 1 - 0.3 * x / (Ls - 1)
for name, r in [("claimant-scheduled", lambda a, b: N[b]),
                ("record-scheduled", lambda a, b: N[a]),
                ("bond-symmetric", lambda a, b: 0.5 * (N[a] + N[b]))]:
    Q = np.zeros((Ls, Ls))
    for a in range(Ls):
        for b in (a - 1, a + 1):
            if 0 <= b < Ls:
                Q[a, b] = r(a, b)
        Q[a, a] = -Q[a].sum()
    w, V = np.linalg.eig(Q.T)
    pi = np.real(V[:, np.argmin(np.abs(w))]); pi /= pi.sum()
    cands = {"prop. N": N / N.sum(), "prop. 1/N": (1 / N) / (1 / N).sum(), "uniform": np.ones(Ls) / Ls}
    best = {k: np.abs(pi - v).max() for k, v in cands.items()}
    print(f"  {name:<20} pi(end)/pi(start) = {pi[-1]/pi[0]:.6f}   max|pi - candidate|: " +
          ", ".join(f"{k} {v:.1e}" for k, v in best.items()))
print("  N(end)/N(start) = 0.7: claimant scheduling piles dust where clocks run FAST, record scheduling where they")
print("  run SLOW (ratio 1/0.7 = 1.428571), the symmetric bond lapse gives no drift.")
