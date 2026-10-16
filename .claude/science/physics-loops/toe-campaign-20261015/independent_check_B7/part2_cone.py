"""Part 2b: spinorial two-layer walks W(k) = G(k) qB G(k)^dag qA, qA,qB unit quaternions in the
(real) commutant span{I, K, S1/sqrt3, S2/sqrt3} of the spinorial class-3 action.
First-order degenerate perturbation theory at k=0: W(k) ~ W0 (1 - i k.h + ...), restricted to each
4-fold eigenspace of W0, gives 4x4 Hermitian h_j.  Eigenvalues of khat.h = group velocities (block
units: d omega / d k_block).  Isotropy test over many directions; decomposition of h into the two
T1 operators J and J^(3) (cubic) via fitting the direction dependence."""
import numpy as np
from walks import *
from quat import x56 as K, x62 as S1, x60 as S2
np.set_printoptions(linewidth=200, suppress=True, precision=5)
Q = [K, S1 / np.sqrt(3), S2 / np.sqrt(3)]
def quat(a):
    a = np.asarray(a, float); a = a / np.linalg.norm(a)
    return a[0] * np.eye(8) + sum(a[i + 1] * Q[i] for i in range(3))
X = [np.diag([v[j] - 0.5 for v in corners]) for j in range(3)]  # centred corner positions

def Wk(qA, qB, k):
    G = np.diag([np.exp(1j * np.dot(k, v)) for v in corners])
    return G @ qB @ G.conj().T @ qA

def eff_h(qA, qB):
    W0 = qB @ qA
    w, V = np.linalg.eig(W0)
    out = []
    for lam in np.unique(np.round(w, 8)):
        P = V[:, np.abs(w - lam) < 1e-6]
        P, _ = np.linalg.qr(P)
        # dW/dk_j = i [X_j, qB] qA  (the 1/2 part of V_j commutes);  W ~ lam(1 - i k.h)
        hs = []
        for j in range(3):
            dW = 1j * (X[j] @ qB - qB @ X[j]) @ qA
            h = (1j / lam) * P.conj().T @ dW @ P
            hs.append(h)
        out.append((lam, P, hs))
    return out

def dirs(n=400, seed=0):
    r = np.random.default_rng(seed).normal(size=(n, 3))
    return r / np.linalg.norm(r, axis=1)[:, None]

if __name__ == "__main__":
    rng = np.random.default_rng(5)
    for trial in range(4):
        qA = quat(rng.normal(size=4)); qB = quat(rng.normal(size=4))
        A = two_layer(qA.astype(complex), qB.astype(complex))
        D = class_D(3)
        print(f"\ntrial {trial}: covariance {covariance_defect(A, D):.1e}, unitarity {unitarity_defect(A):.1e}")
        for lam, P, hs in eff_h(qA, qB):
            herm = max(np.abs(h - h.conj().T).max() for h in hs)
            sp = np.array([np.sort(np.linalg.eigvalsh(sum(n[j] * hs[j] for j in range(3)))) for n in dirs()])
            print(f"  level omega0 = {-np.angle(lam):+.5f} (mult {P.shape[1]}), herm defect {herm:.1e}")
            print("   velocity eigenvalues along 100:", np.linalg.eigvalsh(hs[2]),
                  " 111:", np.linalg.eigvalsh(sum(hs) / np.sqrt(3)))
            print("   spread over 400 directions per sorted branch:", sp.max(0) - sp.min(0))
            # check exact cone: compare with W(k) eigenphases at small k
            kk = 1e-5 * np.array([0.3, -0.5, 0.8]); kk_n = kk / np.linalg.norm(kk)
            ev = np.linalg.eigvals(Wk(qA, qB, kk))
            near = ev[np.abs(ev - lam) < 1e-3]
            print("   numeric slopes at |k|=1e-5:", np.sort(-np.angle(near / lam) / np.linalg.norm(kk)),
                  " vs pert:", np.linalg.eigvalsh(sum(kk_n[j] * hs[j] for j in range(3))))
