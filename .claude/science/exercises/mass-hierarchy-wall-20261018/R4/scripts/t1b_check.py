"""check: at the CKM-best sigma=2.5, do the leptons also pass (one sigma for all nine + CKM)?"""
import itertools
import numpy as np
from common import MZ, LOW, obs_logs
E = np.eye(3, dtype=int)
L = [E[0], E[1], E[2]]
ORB = [[E[0], E[1], E[2]], [E[1] + E[2], E[2] + E[0], E[0] + E[1]]]
def area(p, q, r):
    return 0.5 * np.abs(np.cross(q - p, r - p)).sum()
AM = []
for orb in ORB:
    for t in itertools.product((-1, 0, 1), repeat=3):
        for h in itertools.product((-1, 0, 1, 2), repeat=3):
            R = [o + np.array(t) for o in orb]
            AM.append([[area(L[i], np.array(h), R[j]) for j in range(3)] for i in range(3)])
AM = np.array(AM, float)
for sg in (2.5, 2.75):
    s = np.linalg.svd(np.exp(-sg * AM), compute_uv=False)
    LS = np.log(np.maximum(s[:, ::-1], 1e-300))
    for label, data in (("MZ", MZ), ("LOW", LOW)):
        Yo = obs_logs(data)
        h = [(0.5 * np.ptp(Yo[k] - LS, -1)).min() for k in range(3)]
        print(label, "sigma", sg, "per-sector best factors u,d,e:", np.round(np.exp(h), 2))
