import sys, pickle, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG
from r2 import R2
from r2c import comp_inv
from d4v import Lrel
from d4q import Lsym, HC
from rp3 import lumped
D = pickle.load(open('d4.pkl', 'rb')); ML = lumped(); itt = HC.index((3, 3))
def S_eff(k):  # lowest generalized eigenvalue of the P1 stiffness against the lumped mass: the D4 scalar's static symbol
    w = sl.eigvals(RG.p1_scalar(D, k), ML); return np.min(np.abs(w))
def hodge_nn(k): return np.sum(4*np.sin(np.asarray(k)/2)**2)
print(" dir         |k|   strain(l=0) h_tt*S_eff  h_tt*k^2   h_tt*NN | face+R2 h_tt*S_eff   h_tt*NN")
for n in [(1,0,0), (1,1,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.05, 0.4, 1.0):
        k = np.array([*(km*n), 0.0]); T = np.zeros(10); T[itt] = 1.0
        L = Lrel(k); x = comp_inv(D.Q(k), D.gauge(k), L.conj().T @ T); h1 = (L @ x)[itt].real
        L2 = Lsym(k); x2 = comp_inv(D.Q(k) - 0.1*R2(D, k), D.gauge(k), L2.conj().T @ T); h2 = (L2 @ x2)[itt].real
        Se = S_eff(k)
        print(f" {str(np.round(n,2)):22s} {km:.2f}   {h1*Se:+.5f}  {h1*km**2:+.5f}  {h1*hodge_nn(k):+.5f} | {h2*Se:+.5f}  {h2*hodge_nn(k):+.5f}")
