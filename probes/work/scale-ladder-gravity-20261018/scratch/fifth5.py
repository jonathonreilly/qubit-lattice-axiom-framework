import numpy as np, sys
sys.path.insert(0, '.')
from fifth import null5, R, gauge
Qe, Mh = R.regge(np.eye(4))
np.set_printoptions(precision=3, suppress=True)
for q in [np.array([0.02, 0, 0, 0]), np.array([0.02, 0.01, 0, 0.0]), np.array([0.01, 0.012, -0.007, 0.004]), np.array([0.5, 0.2, -0.3, 0.1])]:
    f, _, _ = null5(q); M = Mh(q)
    a, *_ = np.linalg.lstsq(M, f, rcond=None); share = np.linalg.norm(M@a)/np.linalg.norm(f)
    H = R.hfull(np.real(a*np.exp(-1j*np.angle(a[np.argmax(abs(a))]))))
    qh = q/np.linalg.norm(q)
    tr = np.trace(H); qq = qh@H@qh
    print(f"q={q}: metric share {share:.3f}; h (phase-fixed real part) diag {np.diag(H)} offdiag {H[0,1]:.3f},{H[0,2]:.3f},{H[0,3]:.3f},{H[1,2]:.3f},{H[1,3]:.3f},{H[2,3]:.3f}; tr {tr:.3f} qhq {qq:.3f}")
