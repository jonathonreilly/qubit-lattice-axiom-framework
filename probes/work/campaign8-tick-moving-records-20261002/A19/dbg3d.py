import numpy as np
from track3d import layers_U, strang9, PI
lay = strang9(0.6)
nhat = np.array([1.0, 0.55, 0.25]); nhat /= np.linalg.norm(nhat)
U0 = layers_U(np.array([[PI, PI, PI]]), lay)[0]
ref0 = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
for q0 in (0.2, 0.4, 0.8):
    Kp = np.array([PI, PI, PI]) + q0 * nhat
    def phs(K):
        return np.sort(np.angle(np.linalg.eigvals(layers_U(K[None], lay)[0]) * np.conj(ref0)))
    h = 1e-5
    p0 = phs(Kp)
    grads = np.array([(phs(Kp + h * e) - phs(Kp - h * e)) / (2 * h) for e in np.eye(3)]).T   # (8 bands, 3): d(phase)/dK
    print(f"q0={q0}: eigenphases {np.round(p0,4)}")
    for b in range(8):
        v = -grads[b] * 2      # velocity = dE/dK (E = -phase), K in cells -> x2 for sites
        print(f"   band {b}: phase {p0[b]:+.4f}  v(sites/cycle) {np.round(v,3)} |v|={np.linalg.norm(v):.3f} cos(v,n)={v@nhat/np.linalg.norm(v):+.3f}")
