"""t8: upper-cone group velocities |d phase/dq| along n at finite q (mean and spread over the 4 upper bands),
Strang-9 signed vs palindrome-18 signed; relative to the linear-order speed."""
import numpy as np
from vcyc import layers_U, strang9
pi = np.pi
Ks = np.array([pi, pi, pi])
def blk(a, phi): return [(a, 0, phi / 2), (a, 1, phi), (a, 0, phi / 2)]
def pal18(phi): return blk(0, phi) + blk(1, phi) + blk(2, phi) + blk(2, phi) + blk(1, phi) + blk(0, phi)
def upper(lay, K, ref):
    ph = np.sort(np.angle(np.linalg.eigvals(layers_U(K[None], lay, True)[0]) * np.conj(ref)))
    return ph[4:]
dirs = {"axis": np.array([1., 0, 0]), "face": np.array([1., 1, 0]) / np.sqrt(2),
        "body": np.ones(3) / np.sqrt(3), "generic": np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])}
for name, lay, v0 in [("strang-9, th=0.6", strang9(0.6), np.sin(0.6)), ("palindrome-18, phi=0.3", pal18(0.3), 2 * np.sin(0.3))]:
    ref = np.exp(1j * np.angle(np.linalg.eigvals(layers_U(Ks[None], lay, True)[0])[0]))
    for q in (0.05, 0.15, 0.45):
        row = []
        for dn, n in dirs.items():
            h = 1e-5
            vp = (upper(lay, Ks + (q + h) * n, ref) - upper(lay, Ks + (q - h) * n, ref)) / (2 * h)
            row.append(f"{dn}: mean {vp.mean()/v0:.4f} spread {(vp.max()-vp.min())/v0:.4f}")
        print(f"{name} q={q}: v/v_lin  " + " | ".join(row))
