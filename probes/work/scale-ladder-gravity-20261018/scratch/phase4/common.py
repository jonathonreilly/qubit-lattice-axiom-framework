import os, sys, time, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/hopeful-benz-ed56f8/scripts')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r14
from r14 import Complex, d4cone, strain_metric, HC, segment_readings
t0 = time.time()
OFFd, Sd = d4cone(); Dc = Complex(OFFd, Sd)
print(f"[build {time.time()-t0:.1f}s, E={Dc.E}]", file=sys.stderr)
ITT = HC.index((3, 3))
def cvec(T):
    """coupling vector: sum_{mu nu} h_{mu nu} T^{mu nu} = c . h  in the HC basis"""
    return np.array([T[a, b] * (1 if a == b else 2) for a, b in HC])
def hmat(h):
    H = np.zeros((4, 4), complex)
    for i, (a, b) in enumerate(HC): H[a, b] = H[b, a] = h[i]
    return H
def partners(k, Q=None):
    Q = Dc.Q(k) if Q is None else Q
    w, V = np.linalg.eigh(0.5 * (Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    A = np.hstack([Dc.line_map(k), Dc.gauge(k)]); P = np.eye(Dc.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    return np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
def Qinv(k, Q=None):
    """inverse of the edge form on the orthogonal complement of the exact vertex-displacement range"""
    Q = Dc.Q(k) if Q is None else Q; G = Dc.gauge(k)
    U = np.linalg.svd(G)[0]; r = np.linalg.matrix_rank(G, tol=1e-9); B = U[:, r:]
    return B @ np.linalg.inv(B.conj().T @ Q @ B) @ B.conj().T
def T_of_c(c):
    T = np.zeros((4, 4), complex)
    for i, (a, b) in enumerate(HC): T[a, b] = T[b, a] = c[i] / (1 if a == b else 2)
    return T
def lattice_conserved(k, L):
    W = L @ Dc.gauge(k)[:, :4]
    Cb = np.linalg.svd(W.T)[2][4:]
    if np.abs(Cb @ W).max() > 1e-10: Cb = Cb.conj()
    assert np.abs(Cb @ W).max() < 1e-10
    return Cb
