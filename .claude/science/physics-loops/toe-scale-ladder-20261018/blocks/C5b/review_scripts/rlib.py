"""Reviewer helpers for C5b (independent of lib5b.py / walks5b.py)."""
import numpy as np

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = (SX, SY, SZ)


class Tally:
    def __init__(self):
        self.p = 0; self.f = 0

    def check(self, msg, ok):
        ok = bool(ok)
        print(('PASS ' if ok else 'FAIL ') + msg, flush=True)
        if ok: self.p += 1
        else: self.f += 1

    def total(self):
        print(f'TOTAL: PASS={self.p} FAIL={self.f}', flush=True)


def su2(a0, a):
    """a0*1 + i a.sigma for arrays a0 (...), a (...,3)."""
    return (a0[..., None, None] * np.eye(2)
            + 1j * (a[..., 0, None, None] * SX + a[..., 1, None, None] * SY + a[..., 2, None, None] * SZ))


def w3_from_derivs(U, dU, cell_volume):
    """W3 = (1/8 pi^2) sum tr(A1 [A2, A3]) dV, A_a = U^dag dU_a (U unitary)."""
    Ud = np.conj(np.swapaxes(U, -1, -2))
    A = [Ud @ d for d in dU]
    dens = np.trace(A[0] @ (A[1] @ A[2] - A[2] @ A[1]), axis1=-2, axis2=-1)
    return dens.sum() * cell_volume / (8 * np.pi ** 2)


def w3_grid_fd(func, N, lo=-np.pi, hi=np.pi, h=1e-4, chunk=None):
    """W3 of a smooth map given as func(K[...,3]) -> U[...,n,n]; derivatives by central differences
    (step h), midpoint rule on an N^3 grid of [lo,hi)^3 (periodic, so spectrally accurate for smooth maps)."""
    g = lo + (np.arange(N) + 0.5) * (hi - lo) / N
    tot = 0.0 + 0j
    dV = ((hi - lo) / N) ** 3
    for i in range(N):
        K = np.stack(np.meshgrid([g[i]], g, g, indexing='ij'), -1).reshape(-1, 3)
        U = func(K)
        dU = []
        for a in range(3):
            e = np.zeros(3); e[a] = h
            dU.append((func(K + e) - func(K - e)) / (2 * h))
        tot += w3_from_derivs(U, dU, dV)
    return tot


def frames(U, eps, phi):
    """Eigenvectors of U whose quasienergy E (U psi = e^{-iE} psi) lies in the window (phi-2pi, eps).
    Returns list of (n x m) arrays (m may vary by point)."""
    lam, V = np.linalg.eig(U)
    E = -np.angle(lam)                    # in (-pi, pi]
    # map E into (phi-2pi, phi]
    E = phi - np.mod(phi - E, 2 * np.pi)
    out = []
    for j in range(U.shape[0]):
        sel = E[j] < eps
        Q, _ = np.linalg.qr(V[j][:, sel]) if sel.any() else (V[j][:, :0], None)
        out.append(Q)
    return out, E


def chern_surface_faces(func, faces, eps, phi, M):
    """FHS Chern number of P_< (window (phi-2pi, eps)) on a closed surface made of parallelogram faces.
    faces: list of (origin, e_u, e_v) with e_u x e_v pointing OUTWARD. M plaquettes per side."""
    total = 0.0
    ranks = set()
    for (o, eu, ev) in faces:
        s = np.linspace(0, 1, M + 1)
        K = o + s[:, None, None] * eu + s[None, :, None] * ev
        U = func(K.reshape(-1, 3))
        F, _ = frames(U, eps, phi)
        F = [F[i * (M + 1) + j] for i in range(M + 1) for j in range(M + 1)]
        ranks.update(f.shape[1] for f in F)

        def link(a, b):
            if F[a].shape[1] != F[b].shape[1]:
                return np.nan
            return np.linalg.det(F[a].conj().T @ F[b]) if F[a].shape[1] else 1.0
        idx = lambda i, j: i * (M + 1) + j
        for i in range(M):
            for j in range(M):
                a, b, c, d = idx(i, j), idx(i + 1, j), idx(i + 1, j + 1), idx(i, j + 1)
                total += np.angle(link(a, b) * link(b, c) * link(c, d) * link(d, a))
    # sign calibrated in r1 against direct quadrature of (i/2pi) int tr(P dP^dP):
    # the counter-clockwise plaquette phase sum equals -2pi Ch.
    return -total / (2 * np.pi), ranks


def cube_faces(c, d):
    """6 faces of the cube [c-d, c+d]^3 with outward orientation."""
    c = np.asarray(c, float)
    faces = []
    for a in range(3):
        b, e = (a + 1) % 3, (a + 2) % 3
        ub = np.zeros(3); ub[b] = 2 * d
        ue = np.zeros(3); ue[e] = 2 * d
        # +a face: outward +e_a ; (ub, ue) has ub x ue = +e_a (cyclic)
        o = c.copy(); o[a] += d; o[b] -= d; o[e] -= d
        faces.append((o, ub, ue))
        o = c.copy(); o[a] -= d; o[b] -= d; o[e] -= d
        faces.append((o, ue, ub))
    return faces


def weyl_data(func, p, eps, h=1e-6):
    """Linearisation at a two-fold touching at quasienergy eps: U(p+dk) ~ e^{-i eps} exp(-i(t.dk + dk^T v sigma))
    on the 2-dim eigenspace D. Returns chi = sign det v, v, t, |v^{-1} t| (basis-invariant type-I parameter),
    and the basis-dependent quantity |v^{-T} t| used in the author's s3."""
    U0 = func(p[None])[0]
    lam, V = np.linalg.eig(U0)
    idx = np.argsort(np.abs(lam - np.exp(-1j * eps)))[:2]
    D, _ = np.linalg.qr(V[:, idx])
    v = np.zeros((3, 3)); t = np.zeros(3)
    for a in range(3):
        e = np.zeros(3); e[a] = h
        dU = (func((p + e)[None])[0] - func((p - e)[None])[0]) / (2 * h)
        Ha = 1j * np.exp(1j * eps) * (D.conj().T @ dU @ D)
        Ha = (Ha + Ha.conj().T) / 2
        t[a] = np.trace(Ha).real / 2
        for j in range(3):
            v[a, j] = np.trace(Ha @ PAULI[j]).real / 2
    return (int(np.sign(np.linalg.det(v))), v, t,
            np.linalg.norm(np.linalg.solve(v, t)), np.linalg.norm(np.linalg.solve(v.T, t)), D)


def smoothstep(x):
    """C-infinity step: 0 for x<=0, 1 for x>=1."""
    x = np.clip(x, 0, 1)
    f = lambda y: np.where(y > 0, np.exp(-1 / np.maximum(y, 1e-300)), 0.0)
    return f(x) / (f(x) + f(1 - x))
