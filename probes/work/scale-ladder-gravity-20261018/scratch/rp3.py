import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from rp import rp_matrix
from rp_run import min_eig
D = pickle.load(open('d4.pkl', 'rb')); offs_t = [float(o[3]) for o in D.OFF]
# lumped mass: vertex volume shares (row sums of the consistent mass at k = 0), diagonal and k-independent
def lumped():
    tix = {t: i for i, t in enumerate(D.types)}; w = np.zeros(len(D.types))
    for vs in D.simp:
        P = np.array([D.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0]))/24
        for v in vs: w[tix[v[1]]] += vol/5
    return np.diag(w)
ML = lumped(); print("lumped vertex volumes:", np.round(np.diag(ML), 4), "sum", ML.sum())
for m2 in (0.3, 1.0):
    for Nt in (6, 8):
        out = []
        for ks in [np.array([0.0, 0.0, 0.0]), np.array([0.7, -0.3, 0.2]), np.array([1.9, 0.4, -1.1])]:
            for t0 in (0.0, 0.5):
                R, _ = rp_matrix(lambda k: RG.p1_scalar(D, k) + m2*ML, offs_t, ks, Nt, t0)
                out.append(min_eig(R)[0])
        print(f"m2={m2} Nt={Nt}: min/max over 3 momenta x 2 planes = {min(out):+.2e}")
