"""(a) exactness check of h(t) = h0 (1-p)^t for spontaneous formation, with crowd-tilted moves (g=2) and without,
       several seeds, 2D 128^2;
   (b) mean-field recursions for each rule vs the toy1 npz outputs at checkpoints."""
import numpy as np
from t1lib import tick

p = 0.05
L = 128
N = L * L
ts = [5, 20, 50, 100]
for moves, g in [(False, 0.0), (True, 0.0), (True, 2.0)]:
    ratios = {t: [] for t in ts}
    expected_counts = {t: [] for t in ts}
    for seed in range(8):
        rng = np.random.default_rng(100 + seed)
        occ = rng.random((L, L)) < 0.2
        h0 = 1 - occ.mean()
        expg = np.exp(g * np.arange(5))
        for t in range(1, max(ts) + 1):
            occ, out, form = tick(occ, g, "spont", rng, dict(p=p), moves=moves, expg=expg)
            if t in ts:
                ratios[t].append((1 - occ.mean()) / (h0 * (1 - p) ** t))
                expected_counts[t].append(N * h0 * (1 - p) ** t)
    line = []
    for t in ts:
        r = np.array(ratios[t])
        # binomial-ish sd of the ratio for one run ~ 1/sqrt(expected holes); mean over 8 runs
        sd = 1 / np.sqrt(np.mean(expected_counts[t])) / np.sqrt(len(r))
        line.append(f"t={t}: ratio {r.mean():.4f} +- {sd:.4f}")
    print(f"spont exactness, moves={moves}, g={g}: " + "; ".join(line))

# (b) mean-field recursions (product closure, z=4), h0 = 0.8
z = 4
def mf(rule, T=2000, h0=0.8, beta=1.0):
    h = np.empty(T + 1); h[0] = h0
    for t in range(T):
        x = h[t]; rho = 1 - x
        if rule == "spont": phi = 1.0
        elif rule == "contact": phi = 1 - x ** z
        elif rule == "kempty": phi = 1 - rho ** z
        elif rule == "crowd_soft": phi = (x + rho * np.exp(-beta)) ** z
        elif rule == "crowd_hard": phi = x
        h[t + 1] = x - p * x * phi
    return h
cps = [10, 100, 500, 1000, 2000]
for rule in ["spont", "contact", "kempty", "crowd_soft", "crowd_hard"]:
    hm = mf(rule)
    out = []
    for mv in (0, 1):
        try:
            d = np.load(f"toy1_{rule}_m{mv}.npz")
            out.append("toy(m=%d): " % mv + " ".join(f"{d['h'][c]:.5f}" for c in cps))
        except FileNotFoundError:
            pass
    print(f"{rule:10s} MF: " + " ".join(f"{hm[c]:.5f}" for c in cps) + " | " + " | ".join(out))
print("checkpoints t =", cps)
# asymptotic MF forms: kempty h ~ 1/(z p t); crowd_hard h ~ 1/(p t); crowd_soft rate p e^{-z beta}
print("MF asymptotes at t=2000: kempty 1/(z p t) =", 1 / (z * p * 2000), " crowd_hard 1/(p t) =", 1 / (p * 2000),
      " crowd_soft rate p e^{-z} =", p * np.exp(-4))
