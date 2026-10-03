"""t7: real-space one-excitation runs on an L^3 torus.
(a) a single record's possibility started on one site: ballistic spread <r^2> ~ t^2, shape anisotropy;
(b) low-energy packets near K* in the upper band: centroid velocity vs direction (isotropy test)."""
import numpy as np
from vcyc import layers_U, plain6, strang9

pi = np.pi

def apply_layer(psi, axis, par, th, signed):
    L = psi.shape[0]
    c, s = np.cos(th), np.sin(th)
    x = np.arange(L)
    if not signed or axis == 0:
        eta = 1.0
    elif axis == 1:
        eta = ((-1.0) ** x)[:, None, None]
    else:
        eta = ((-1.0) ** (x[:, None] + x[None, :]))[:, :, None]
    ps = np.roll(psi, -par, axis=axis)
    et = np.roll(np.broadcast_to(eta, psi.shape), -par, axis=axis) if np.ndim(eta) else eta
    sl0 = [slice(None)] * 3; sl1 = [slice(None)] * 3
    sl0[axis] = slice(0, L, 2); sl1[axis] = slice(1, L, 2)
    a, b = ps[tuple(sl0)].copy(), ps[tuple(sl1)].copy()
    e = et[tuple(sl0)] if np.ndim(et) else et
    ps[tuple(sl0)] = np.exp(1j * th) * (c * a - 1j * e * s * b)
    ps[tuple(sl1)] = np.exp(1j * th) * (-1j * e * s * a + c * b)
    return np.roll(ps, par, axis=axis)

def run(psi, lay, signed):
    for (a, p, th) in lay:
        psi = apply_layer(psi, a, p, th, signed)
    return psi

# consistency of the real-space code with the Bloch matrices: plane wave check
L = 16
rng = np.random.default_rng(8)
K = rng.uniform(-pi, pi, 3)
K = np.round(K / (2 * pi / (L // 2))) * (2 * pi / (L // 2))   # allowed cell momenta
for name, lay, signed in [("plain-6", plain6(0.5), False), ("strang-9", strang9(0.5), True)]:
    phi = rng.normal(size=8) + 1j * rng.normal(size=8)
    psi = np.zeros((L, L, L), complex)
    for X in range(L):
        for Y in range(L):
            for Zc in range(L):
                n = np.array([X // 2, Y // 2, Zc // 2]); p = (X % 2) + 2 * (Y % 2) + 4 * (Zc % 2)
                psi[X, Y, Zc] = np.exp(1j * K @ n) * phi[p]
    out = run(psi, lay, signed)
    phi2 = layers_U(K[None], lay, signed)[0] @ phi
    ref = np.zeros_like(psi)
    for X in range(L):
        for Y in range(L):
            for Zc in range(L):
                n = np.array([X // 2, Y // 2, Zc // 2]); p = (X % 2) + 2 * (Y % 2) + 4 * (Zc % 2)
                ref[X, Y, Zc] = np.exp(1j * K @ n) * phi2[p]
    print(f"real-space vs Bloch ({name}): {np.abs(out - ref).max():.1e}")

# (a) single site start
L = 48
X, Y, Zc = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
def moments(psi, s0):
    P = np.abs(psi) ** 2
    d = [((C - c0 + L // 2) % L) - L // 2 for C, c0 in zip((X, Y, Zc), s0)]
    r2 = d[0] ** 2 + d[1] ** 2 + d[2] ** 2
    return (P * r2).sum(), (P * (d[0] ** 4 + d[1] ** 4 + d[2] ** 4)).sum() / max((P * r2 ** 2).sum(), 1e-30)
for name, th, signed, mk in [("plain-6", pi / 4, False, plain6), ("strang-9 signed", pi / 4, True, strang9),
                             ("strang-9 signed", 0.3, True, strang9)]:
    psi = np.zeros((L, L, L), complex); s0 = (24, 24, 24); psi[s0] = 1
    rows = []
    for t in range(1, 9):
        psi = run(psi, mk(th), signed)
        r2, A = moments(psi, s0)
        rows.append((t, r2, A))
    print(f"(a) {name} th={th:.3f}: <r^2>/t^2 = " + " ".join(f"{r2/t**2:.3f}" for t, r2, A in rows) +
          f"; anisotropy <x^4+y^4+z^4>/<r^4> at t=8: {rows[-1][2]:.3f} (isotropic 0.600, diagonal 0.333)")

# (b) packets near K* (upper band), velocity vs direction
L = 64
Xc, Yc, Zcc = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
ncell = np.stack([Xc // 2, Yc // 2, Zcc // 2], -1)
pidx = (Xc % 2) + 2 * (Yc % 2) + 4 * (Zcc % 2)
def packet(lay, signed, nhat, q0=0.25, w=4.0, T=10, band="upper"):
    Kp = np.array([pi, pi, pi]) + q0 * nhat
    U = layers_U(Kp[None], lay, signed)[0]
    U0 = layers_U(np.array([[pi, pi, pi]]), lay, signed)[0]
    ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    w_, v_ = np.linalg.eig(U)
    ph = np.angle(w_ * np.conj(ref))
    j = np.argmax(ph)                       # top band at this momentum (upper cone)
    phi = v_[:, j]
    c0 = np.array([L // 4, L // 4, L // 4])
    env = np.exp(-(((ncell - c0) ** 2).sum(-1)) / (2 * w ** 2))
    psi = env * np.exp(1j * (ncell @ Kp)) * phi[pidx]
    psi /= np.linalg.norm(psi)
    def cent(psi):
        P = np.abs(psi) ** 2
        return np.array([(P * C).sum() for C in (Xc, Yc, Zcc)])
    r0 = cent(psi)
    for t in range(T):
        psi = run(psi, lay, signed)
    return (cent(psi) - r0) / T
for name, th, signed, mk in [("plain-6", 0.6, False, plain6), ("strang-9 signed", 0.6, True, strang9)]:
    for nhat in [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3)]:
        v = packet(mk(th), signed, nhat)
        print(f"(b) {name} th={th}: n={np.round(nhat, 3)}  centroid velocity (sites/cycle) {np.round(v, 3)}  "
              f"|v|={np.linalg.norm(v):.3f}  (2 sin th = {2*np.sin(th):.3f})")
