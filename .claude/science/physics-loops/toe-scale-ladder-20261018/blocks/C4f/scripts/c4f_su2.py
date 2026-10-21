"""SU(2) lift of Q in SO(3) and the n-basis (index 0 = magnon |+n>, 1 = vacuum spin |-n>)."""
import numpy as np
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex); SIG = [SX, SY, SZ]; I2 = np.eye(2, dtype=complex)
def su2_lift(Qm):
    Qm = np.array(Qm, float); tr = np.trace(Qm)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    if abs(ang) < 1e-9: return I2
    if abs(ang - np.pi) < 1e-9:
        Mx = (Qm + np.eye(3)) / 2; k = int(np.argmax(np.diag(Mx))); n = Mx[:, k] / np.sqrt(Mx[k, k])
    else:
        n = np.array([Qm[2, 1] - Qm[1, 2], Qm[0, 2] - Qm[2, 0], Qm[1, 0] - Qm[0, 1]]) / (2 * np.sin(ang))
    return np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))
_n = np.ones(3) / np.sqrt(3)
_w, _V = np.linalg.eigh(sum(_n[i] * SIG[i] for i in range(3)))
Bn = np.column_stack([_V[:, 1], _V[:, 0]])
