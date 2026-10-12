"""R6-2 check 2b: repeat part (A) of r62_hww_dispersion.py with a larger box (R=5, doubled coords)."""
import sys, numpy as np
sys.argv = ["x"]
import importlib.util
spec = importlib.util.spec_from_file_location("m", "r62_hww_dispersion.py")
src = open("r62_hww_dispersion.py").read().split("R = 3")[0]
ns = {}
exec(src, ns)
from scipy.linalg import null_space
for R in (4, 5):
    hv, A = ns["build"](R)
    W = null_space(A)
    eps_list = [0.1, 0.05, 0.025, 0.0125]
    d = np.array([1.0, 2.0, 3.0]) / np.sqrt(14)
    sm = []
    for e in eps_list:
        S = np.array([ns["symbol"](hv, W[:, a], e * d) for a in range(W.shape[1])])
        sm.append(np.linalg.svd(S, compute_uv=False)[0])
    p = np.polyfit(np.log(eps_list), np.log(sm), 1)[0]
    print(f"R={R}: {len(hv)} h-vars, invariant functionals dim={W.shape[1]}, largest symbol ~ eps^{p:.3f}")
