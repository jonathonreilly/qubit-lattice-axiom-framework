"""t3: cone shape (isotropy, degeneracy) for plain/signed x (e,o)-block/Strang-block cycles; nu_3."""
import numpy as np, sys
from vcyc import layers_U, plain6, strang9, nu3

pi = np.pi
rng = np.random.default_rng(3)
Ks = np.array([[pi, pi, pi]])

def slopes(layers, signed, th_tot, dirs, d=1e-6):
    ref = layers_U(Ks, layers, signed)[0]
    ph0 = np.angle(np.linalg.eigvals(ref))
    KK = Ks + d * dirs
    U = layers_U(KK, layers, signed)
    out = []
    for u in U:
        ev = np.linalg.eigvals(u) * np.exp(-1j * ph0[0])
        out.append(np.sort(np.angle(ev)) / d)
    return np.array(out), np.abs(ref - np.exp(1j * ph0[0]) * np.eye(8)).max()

dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
dirs = np.vstack([np.eye(3), np.array([[1, 1, 1]]) / np.sqrt(3), np.array([[1, 1, 0]]) / np.sqrt(2), dirs])

for th in [pi / 8, pi / 4, 3 * pi / 8]:
    for name, lay in [("plain-6 ", plain6(th)), ("strang-9", strang9(th))]:
        for signed in (False, True):
            sl, deg = slopes(lay, signed, th, dirs)
            pos = sl[:, 4:]                     # four upper slopes per direction
            spread = np.abs(sl).max() - np.abs(sl).min()
            print(f"th={th:.4f} {name} signed={signed!s:5}: |U(K*)-phase*1|={deg:.1e}; "
                  f"|slope| range [{np.abs(sl).min():.5f}, {np.abs(sl).max():.5f}] (sin th={np.sin(th):.5f}); "
                  f"diag111 slopes {np.round(sl[3], 4)}")
    print()

# calibration of nu3 on an embedded degree-one 2x2 map
def deg1(K):
    m = np.stack([np.sin(K[:, 0]), np.sin(K[:, 1]), np.sin(K[:, 2])], 1)
    m0 = 2.0 - np.cos(K).sum(1)
    n = np.sqrt(m0 ** 2 + (m ** 2).sum(1))
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    U2 = (m0[:, None, None] * np.eye(2) + 1j * (m[:, 0, None, None] * sx + m[:, 1, None, None] * sy
                                                 + m[:, 2, None, None] * sz)) / n[:, None, None]
    U = np.broadcast_to(np.eye(8, dtype=complex), (K.shape[0], 8, 8)).copy()
    U[:, :2, :2] = U2
    return U

import vcyc
orig = vcyc.layers_U
vcyc.layers_U = lambda K, layers, signed: deg1(np.atleast_2d(K))
print("nu3 calibration (embedded degree-one map, N=20):", np.round(vcyc.nu3(None, None, N=20), 4))
vcyc.layers_U = orig
for th in [pi / 4, 3 * pi / 8]:
    for name, lay in [("plain-6", plain6(th)), ("strang-9", strang9(th))]:
        for signed in (False, True):
            v = vcyc.nu3(lay, signed, N=16)
            print(f"nu3 th={th:.4f} {name} signed={signed}: {np.round(v, 6)}")
