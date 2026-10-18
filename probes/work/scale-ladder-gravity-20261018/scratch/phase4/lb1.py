# light bending + generic-direction exchange through the strain metric
from common import *
def response(k, T1, L=None, Q=None):
    L = strain_metric(Dc, k) if L is None else L; Q = Dc.Q(k) if Q is None else Q
    J = L.conj().T @ cvec(T1)
    x = np.linalg.pinv(Q, rcond=1e-11) @ J
    return L, Q, J, x
for kk in [np.array([0, 0.04, 0, 0.]), np.array([0, 0.02, 0, 0.]), np.array([0, 0.012, 0.009, 0.]), np.array([0, 0.008, 0.006, 0.0])]:
    T1 = np.zeros((4, 4)); T1[3, 3] = 1
    L, Q, J, x = response(kk, T1); h = L @ x; k2 = kk @ kk
    G = Dc.gauge(kk)
    # transverse spatial direction x perp k
    kh = kk[:3] / np.linalg.norm(kk[:3]); e = np.cross(kh, [0, 0, 1.]) if abs(kh[2]) < .9 else np.cross(kh, [1., 0, 0]); e /= np.linalg.norm(e)
    nE = np.array([*e, 1j]); Tnull = np.outer(nE, nE); Tdust = np.zeros((4, 4), complex); Tdust[3, 3] = -1  # (0,0,0,i)^2
    Al = cvec(Tnull) @ h; An = cvec(Tdust) @ h
    ward = np.abs(cvec(Tnull) @ L @ G).max() / np.abs(cvec(Tnull) @ L).max()
    print(f"|k|={np.sqrt(k2):.4f}: J.gauge {np.linalg.norm(G.conj().T@J)/np.linalg.norm(J):.0e}; Newton A k^2 {An.real*k2:+.6f}; light A k^2 {Al.real*k2:+.6f} (im {abs(Al.imag)*k2:.0e}); 1+gamma = {(Al/An).real:.6f}; |c_null L G|/|c_null L| {ward:.1e}")
