"""3D winding nu_3 = (1/24 pi^2) int eps^{ijk} tr(W^-1 d_i W W^-1 d_j W W^-1 d_k W) d^3k
for: (a) normalised content-set shift S~ = S/|S| (exactly covariant, quasi-local),
(b) ordered product W_z W_y W_x (strictly local, D_2 only),
(c) exp(-i lam H_W), H_W = sum sin k_a sigma_a (covariant, continuous-time).
Midpoint grid with analytic-free central differences; vectorised."""
import numpy as np

n = 48
g = (np.arange(n) + 0.5) * 2 * np.pi / n
KX, KY, KZ = np.meshgrid(g, g, g, indexing='ij')
I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)


def su2(n0, nx, ny, nz):
    return (n0[..., None, None] * I2 - 1j * (nx[..., None, None] * sx + ny[..., None, None] * sy + nz[..., None, None] * sz))


def S_norm(kx, ky, kz):
    C = np.cos(kx) + np.cos(ky) + np.cos(kz)
    N = np.sqrt(C ** 2 + np.sin(kx) ** 2 + np.sin(ky) ** 2 + np.sin(kz) ** 2)
    return su2(C / N, np.sin(kx) / N, np.sin(ky) / N, np.sin(kz) / N)


def W_prod(kx, ky, kz):
    ex = su2(np.cos(kx), np.sin(kx), 0 * kx, 0 * kx)
    ey = su2(np.cos(ky), 0 * ky, np.sin(ky), 0 * ky)
    ez = su2(np.cos(kz), 0 * kz, 0 * kz, np.sin(kz))
    return ez @ ey @ ex


def W_expH(kx, ky, kz, lam=1.3):
    s = np.stack([np.sin(kx), np.sin(ky), np.sin(kz)])
    r = np.sqrt((s ** 2).sum(0)) + 1e-300
    return su2(np.cos(lam * r), np.sin(lam * r) * s[0] / r, np.sin(lam * r) * s[1] / r, np.sin(lam * r) * s[2] / r)


def nu3(Wf):
    h = 1e-5
    W = Wf(KX, KY, KZ)
    Wi = np.linalg.inv(W)
    d = [(Wf(KX + h, KY, KZ) - Wf(KX - h, KY, KZ)) / (2 * h),
         (Wf(KX, KY + h, KZ) - Wf(KX, KY - h, KZ)) / (2 * h),
         (Wf(KX, KY, KZ + h) - Wf(KX, KY, KZ - h)) / (2 * h)]
    A = [Wi @ di for di in d]
    tot = 0
    for (i, j, k), sgn in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
        tot = tot + sgn * np.trace(A[i] @ A[j] @ A[k], axis1=-2, axis2=-1)
    val = tot.sum() * (2 * np.pi / n) ** 3 / (24 * np.pi ** 2)
    return val


for name, f in [("S/|S| (covariant, quasi-local)", S_norm), ("W_z W_y W_x (strictly local)", W_prod),
                ("exp(-i 1.3 H_W) (continuous-time)", W_expH)]:
    v = nu3(f)
    print(f"{name:36s}: nu_3 = {v.real:+.4f} (imag {v.imag:+.1e})")
