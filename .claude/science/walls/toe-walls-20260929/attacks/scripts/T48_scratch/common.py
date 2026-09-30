import numpy as np
from scipy.optimize import least_squares

# comparators (repo's CKM values, NP-CKM note lines 83-84,213)
OBS = dict(Vus=0.22500, Vcb=0.04210, Vub=0.00370, J=3.08e-5)
THETA_E_DEG = 12.16   # THETA13 note: sin th13 = sin th_e/sqrt2, sin^2 th13 = 0.0222

# rounded running masses (MeV). Comparators only.  Set MZ ~ running at M_Z; set LOW ~ PDG-style low scale.
MASSES = {
 "MZ":  dict(u=[1.24, 626.0, 172700.0], d=[2.69, 53.5, 2860.0], e=[0.48657, 102.718, 1746.24]),
 "LOW": dict(u=[2.16, 1270.0, 172600.0], d=[4.70, 93.5, 4180.0], e=[0.51100, 105.658, 1776.86]),
}

def seed(r12, r23, r13, th):
    R = np.eye(3, dtype=complex)
    R[0,1] = r12; R[1,0] = r12
    R[1,2] = r23; R[2,1] = r23
    R[0,2] = r13*np.exp(-1j*th); R[2,0] = np.conj(R[0,2])
    return R

def circ_seed(rho, phi):
    R = np.eye(3, dtype=complex)
    b = rho*np.exp(1j*phi)
    R[0,1] = b; R[1,0] = np.conj(b)
    R[1,2] = b; R[2,1] = np.conj(b)
    R[2,0] = b; R[0,2] = np.conj(b)
    return R

def eig_sorted(H):
    w, U = np.linalg.eigh(H)
    idx = np.argsort(np.abs(w))
    return w[idx], U[:, idx]

def dress_solve(R, t, d0=None, iters=60):
    """find positive diagonal d s.t. |eig(D R D)| sorted = t (Newton in log d, analytic Jacobian 2|U_ik|^2). returns d, resid"""
    t = np.asarray(t, float); lt = np.log(t)
    x = np.log(np.sqrt(t)) if d0 is None else np.log(d0)
    for it in range(iters):
        d = np.exp(x)
        w, U = eig_sorted(d[:,None]*R*d[None,:])
        f = np.log(np.abs(w)+1e-300) - lt
        if np.max(np.abs(f)) < 1e-12: break
        Jm = 2*np.abs(U)**2          # Jm[i,k] = d log|lam_k| / d log d_i
        try:
            step = np.linalg.solve(Jm.T, -f)
        except np.linalg.LinAlgError:
            step = -f*0.5
        m = np.max(np.abs(step))
        if m > 1.5: step *= 1.5/m
        x = x + step
    d = np.exp(x)
    w, U = eig_sorted(d[:,None]*R*d[None,:])
    return d, np.max(np.abs(np.log(np.abs(w)+1e-300)-lt))

def dress_solve_h(R, t, nh=12):
    """homotopy R(s)=I+s(R-I) from the trivial seed; robust."""
    t = np.asarray(t, float)
    d = np.sqrt(t)
    I = np.eye(3, dtype=complex)
    for s in np.linspace(0, 1, nh+1)[1:]:
        d, res = dress_solve(I + s*(R-I), t, d0=d)
    return d, res

def dressed_U(R, t, d0=None):
    d, res = dress_solve(R, t, d0)
    if res > 1e-9:
        d, res = dress_solve_h(R, t)
    w, U = eig_sorted(d[:,None]*R*d[None,:])
    return U, d, res

def ckm_from(Uu, Ud):
    V = Uu.conj().T @ Ud
    a = np.abs(V)
    J = np.imag(V[0,0]*V[1,1]*np.conj(V[0,1])*np.conj(V[1,0]))
    return a, abs(J)

def relerr(pred, obs): return abs(pred-obs)/obs
