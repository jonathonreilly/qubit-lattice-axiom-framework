# Check of row 1081 L144: Proposition DIL (Wilson form) on frozen Q_8, n = 2,
# one transverse link (Example KIN-7 of row 1076). Independent small script.
import numpy as np
from math import cosh, sinh, exp, log, sqrt
sizes = np.array([1,1,2,2,2.])          # classes {1},{-1},{+-i},{+-j},{+-k}
xval  = np.array([1,-1,0,0,0.])          # x = (1/2) tr on each class
chars = np.array([[1,1,1,1,1],[1,1,1,-1,-1],[1,1,-1,1,-1],[1,1,-1,-1,1],[2,-2,0,0,0.]])
dims  = np.array([1,1,1,1,2.])
U = chars*np.sqrt(sizes/8.)              # rows: orthonormal characters in class coords
assert np.allclose(U@U.T, np.eye(5))
def lam(b):
    w = np.exp(b*xval)*sizes
    return (chars@w)/(dims*w.sum())
def ops(bM, bL):
    KPhi = U.T@np.diag(lam(bM)**2)@U
    D    = U.T@np.diag(lam(bL)**2)@U
    E2   = np.diag(np.exp(bM*xval))
    w,V = np.linalg.eigh(KPhi); Kh = V@np.diag(np.sqrt(w))@V.T
    SSt = Kh@E2@Kh                      # S S*, S = KPhi^(1/2) E
    return KPhi, D, E2, Kh, SSt
def gap(M):
    ev = np.sort(np.linalg.eigvalsh(M))[::-1]
    return log(ev[0])-log(ev[1])
def run(bM, bL):
    KPhi, D, E2, Kh, SSt = ops(bM, bL)
    Dh = U.T@np.diag(lam(bL))@U
    m_inf = gap(SSt)
    m_L   = gap(Dh@SSt@Dh)              # same nonzero spectrum as S* D S
    w,V = np.linalg.eigh(SSt); psi = V[:,-1]
    dv = np.sort(lam(bL)**2)[::-1]
    bound = 2*log(psi@D@psi) - log(dv[0]*dv[1])
    return m_inf, m_L, m_L-m_inf, bound
print("bM bL m_inf m_L diff DILbound bound<=diff")
for bM in [2.4, 6.0, 12.0]:
    for bL in [1.0, 2.0, 3.5, 5.0, 8.0]:
        mi, mL, d, b = run(bM, bL)
        print(f"{bM:5.1f} {bL:5.1f} {mi:.6f} {mL:.6f} {d:+.6e} {b:+.6e} {b<=d+1e-12}")
# KIN-7 limit at bM=12, bL=8: row 1076 says diff ~ -2.680e-3 vs -8e^-8 = -2.684e-3;
# row 1081 says the DIL bound is ~ -12 eta = -12 e^-8 = %.4e
print("-8 eta, -12 eta at bL=8:", -8*exp(-8), -12*exp(-8))
