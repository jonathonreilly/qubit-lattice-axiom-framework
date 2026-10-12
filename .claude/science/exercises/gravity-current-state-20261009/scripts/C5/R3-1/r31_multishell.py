"""R3-1 check 5: does summing many timelike shells (a kernel spread over proper times, as a
mesoscale/BD-type kernel would be) average the per-realization LV down?
For shells N = -1..-24 (non-empty), compute S_N(u,kappa) for 48 directions u (rapidity <= 0.7) and
kappa in {0.2, 0.1, 0.05}; compare rel. LV of each shell with rel. LV of the equal-weight sum of LI-normalised
shells  Sigma_N S_N/S_N,LI  (each shell normalised so its LI part is 1)."""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location("s", "r31_lv_scaling_lib.py")
lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
rng = np.random.default_rng(5)
us = [lib.boost(0.7 * rng.uniform() ** (1/3), rng.normal(size=3)) for _ in range(48)]
kaps = [0.2, 0.1, 0.05]
n0max = 520
tot = {k: np.zeros(len(us)) for k in kaps}; single = {k: [] for k in kaps}; nsh = 0
pats = {k: [] for k in kaps}
for N in range(-1, -25, -1):
    try:
        X = lib.shell(N, n0max)
    except ValueError:
        continue
    if len(X[0]) == 0: continue
    nsh += 1
    for k in kaps:
        Sv = np.array([np.exp(-k * (u[0] * X[0] - u[1] * X[1] - u[2] * X[2] - u[3] * X[3])).sum() for u in us])
        r = Sv / Sv.mean()
        tot[k] += r; single[k].append(r.std()); pats[k].append(r - 1)
    print(f"shell N={N}: {len(X[0])} pts; rel LV std at kappa=0.05: {single[0.05][-1]:.3e}", flush=True)
print(f"\n{nsh} non-empty shells")
for k in kaps:
    agg = tot[k] / nsh
    P = np.array(pats[k]); C = np.corrcoef(P); off = C[~np.eye(len(C), dtype=bool)]
    print(f"kappa={k}: mean single-shell rel LV {np.mean(single[k]):.3e}; equal-weight sum rel LV {agg.std():.3e};"
          f" ratio {agg.std()/np.mean(single[k]):.3f} (1/sqrt(nshell) = {1/np.sqrt(nsh):.3f});"
          f" mean pairwise pattern correlation {off.mean():+.3f}")
