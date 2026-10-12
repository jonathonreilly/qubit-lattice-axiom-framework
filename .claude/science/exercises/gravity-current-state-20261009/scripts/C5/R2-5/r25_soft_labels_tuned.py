"""R2-5 check 8b: route P3 with a theta-even on-site record weight w_rec (RP-neutral: on-site
weights factor as F * theta F).  The record sector's growth per step is w_rec * lam_UD with
lam_UD = top eigenvalue of [[1, e],[x, 1]] = 1 + sqrt(x e) >= 2 under RP (x e >= 1).
Balance: w_rec = (1 + kappa) / lam_UD.  kappa = 0 is the balance point; the arrow length
(formation spread) and the formation probability depend on kappa at the scale of 1/T.
Reported for kappa in {+1e-2, +1e-3, 0, -1e-3}: m(t) profile, formation per blank site-step,
un-formation per record-step, RP eigenvalues unchanged.
"""
import numpy as np
from r25_soft_labels import law, th, B, U, D
def halfline_onsite(w, wrec, T):
    onsite = np.array([1.0, wrec, wrec])
    alpha = [np.array([1.0, 0, 0])]
    for t in range(1, T + 1):
        a = (alpha[-1] @ w) * onsite; alpha.append(a / a.sum())
    beta = [None] * (T + 1); beta[T] = np.ones(3)
    for t in range(T - 1, -1, -1):
        b = w @ (onsite * beta[t + 1]); beta[t] = b / b.sum()
    m, fr, ur = [], [], []
    for t in range(T):
        P = alpha[t][:, None] * w * (onsite * beta[t + 1])[None, :]; P /= P.sum()
        pB = P[B].sum(); pR = 1 - pB
        fr.append((P[B, U] + P[B, D]) / max(pB, 1e-300)); ur.append((P[U, B] + P[D, B]) / max(pR, 1e-300)); m.append(pR)
    return np.array(m), np.array(fr), np.array(ur)
if __name__ == "__main__":
    r, u, eta = 1e-3, 1e-9, 0.1
    w, M = law(r, u, eta)
    e, x = u / r, (1 + eta) * r / u
    lam = 1 + np.sqrt(x * e)
    print(f"r={r} u={u} eta={eta}: lam_UD = {lam:.6f}; eig(M) = {np.linalg.eigvalsh(M)}")
    T = 4000
    for kappa in (1e-2, 1e-3, 0.0, -1e-3):
        wrec = (1 + kappa) / lam
        m, fr, ur = halfline_onsite(w, wrec, T)
        print(f"  kappa={kappa:+.0e}: m(t=1,10,100,1000,T/2)={m[1]:.3e},{m[10]:.3e},{m[100]:.3e},{m[1000]:.3e},{m[T//2]:.3e}; "
              f"formation/blank-step at t=100: {fr[100]:.2e}; un-formation/record-step at t=100: {ur[100]:.2e}")
