"""Block 54 control (supervisor-run; floating point; evidence, not proof): the clocked walk reduced to a line.

The clock field depends on z only, u = g (z - zc), w = exp(u).  The transverse wave vector (kx, ky) is then conserved and the walk with the
qubit as coin,  H = sum_j sigma_j (x) D_j,  D_j = (i/2)(T_j - T_j^dagger),  becomes a two-component walk on a line,
    H(kx, ky) = sin kx sigma_x + sin ky sigma_y + sigma_z (x) D_z,        H_w = sqrt(w) H sqrt(w),
whose transverse motion acts as a rest energy m = sqrt(sin^2 kx + sin^2 ky).
The same packet is also followed as a CLOUD OF RAYS with the energy function E = w(z) eps(kz), eps = sqrt(m^2 + sin^2 kz):
    dz/dt = w d(eps)/d(kz),   d(kz)/dt = -eps dw/dz,
positions drawn from N(z0, sigma^2) and wave vectors from N(k0, 1/(4 sigma^2)), the packet's own spreads.
Reported: (a) packets at rest with different rest energies and transverse directions; (b) packets moving up and down the gradient at several
fractions of the local limiting speed; (c) no transverse motion at all (no rest energy); (d) the time-scaling identity
U_w(t) T_a = T_a U_w(exp(g a) t) on the open line (packet far from the ends)."""
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


def build(n_sites, g, zc, mx, my):
    z = np.arange(n_sites, dtype=float)
    w = np.exp(g * (z - zc))
    sw = np.sqrt(w)
    rows, cols, vals = [], [], []
    site = mx * SX + my * SY
    for s1 in range(2):
        for s2 in range(2):
            if site[s1, s2] != 0:
                rows.append(2 * np.arange(n_sites) + s1)
                cols.append(2 * np.arange(n_sites) + s2)
                vals.append(w * site[s1, s2])
    amp = sw[1:] * sw[:-1]
    up, dn = np.arange(1, n_sites), np.arange(0, n_sites - 1)
    for s in range(2):
        c = SZ[s, s]
        rows.append(2 * up + s); cols.append(2 * dn + s); vals.append(0.5j * amp * c)        # D[z, z-1] = +i/2: the symbol of D is sin k
        rows.append(2 * dn + s); cols.append(2 * up + s); vals.append(-0.5j * amp * c)       # D[z, z+1] = -i/2
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n_sites, 2 * n_sites)).tocsr()


def packet(n_sites, z0, sig, k0, mx, my):
    """A Gaussian packet assembled in wave-vector space from the positive-energy spinors of the free walk."""
    k = 2 * np.pi * np.fft.fftfreq(n_sites)
    gk = np.exp(-(np.angle(np.exp(1j * (k - k0))) ** 2) * sig ** 2) * np.exp(-1j * k * z0)
    comp = np.zeros((n_sites, 2), complex)
    ref = np.array([1.0, 1.0 + 0.3j])
    for i, kk in enumerate(k):
        if abs(gk[i]) < 1e-30:
            continue
        _, vec = np.linalg.eigh(mx * SX + my * SY + np.sin(kk) * SZ)
        v = vec[:, 1]
        ph = np.vdot(ref, v)
        comp[i] = gk[i] * v * (abs(ph) / ph)
    psi = np.stack([np.fft.ifft(comp[:, 0]), np.fft.ifft(comp[:, 1])], axis=1).reshape(-1)
    return psi / np.linalg.norm(psi)


def ray_cloud(g, zc, m, z0, sig, k0, t_end, n=40000, steps=2000, seed=54):
    rng = np.random.default_rng(seed)
    dz = sig * rng.standard_normal(n)
    dk = rng.standard_normal(n) / (2 * sig)
    z = z0 + np.concatenate([dz, -dz, dz, -dz])                       # antithetic quadruples: odd sampling moments vanish identically
    k = k0 + np.concatenate([dk, dk, -dk, -dk])
    start = z.mean()

    def f(z, k):
        e = np.sqrt(m * m + np.sin(k) ** 2)
        w = np.exp(g * (z - zc))
        de = np.where(e > 0, np.sin(k) * np.cos(k) / np.where(e > 0, e, 1.0), np.cos(k) * np.sign(np.sin(k)))
        return w * de, -e * g * w

    h = t_end / steps
    for _ in range(steps):
        a1, b1 = f(z, k)
        a2, b2 = f(z + 0.5 * h * a1, k + 0.5 * h * b1)
        a3, b3 = f(z + 0.5 * h * a2, k + 0.5 * h * b2)
        a4, b4 = f(z + h * a3, k + h * b3)
        z = z + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6
        k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return z.mean() - start


def run(n_sites, g, mx, my, k0, t_end, sig):
    zc = n_sites / 2
    ham = build(n_sites, g, zc, mx, my)
    psi = packet(n_sites, zc, sig, k0, mx, my)
    zs = np.arange(n_sites, dtype=float)
    p0 = (np.abs(psi) ** 2).reshape(n_sites, 2).sum(axis=1)
    start = (p0 * zs).sum()
    out = expm_multiply(-1j * ham * t_end, psi)
    p = (np.abs(out) ** 2).reshape(n_sites, 2).sum(axis=1)
    walk = (p * zs).sum() / p.sum() - start
    cloud = ray_cloud(g, zc, np.hypot(mx, my), start, sig, k0, t_end)
    return walk, cloud, p.sum(), p[:5].sum() + p[-5:].sum()


if __name__ == "__main__":
    g, t_end = 0.002, 100.0
    print(f"(a) packets at rest along the gradient, g = {g}, T = {t_end}, packet width 40; long-wavelength value -g T^2/2 = {-0.5 * g * t_end ** 2:+.4f}")
    falls = []
    for m, (ax, ay) in [(0.05, (1, 0)), (0.1, (1, 0)), (0.2, (1, 0)), (0.4, (1, 0)), (0.8, (1, 0)), (0.4, (1, 1)), (0.4, (3, 4))]:
        nrm = np.hypot(ax, ay)
        walk, cloud, norm, edge = run(4000, g, m * ax / nrm, m * ay / nrm, 0.0, t_end, 40.0)
        falls.append((m, walk, cloud))
        print(f"    rest energy {m:.2f}, transverse direction ({ax},{ay}): fall of the walk {walk:+.4f}; of the cloud of rays {cloud:+.4f}; walk over cloud {walk / cloud:.4f}; norm {norm:.8f}; weight at the ends {edge:.0e}")
    print(f"    largest |walk/cloud - 1| = {max(abs(w / c - 1) for _, w, c in falls):.1e}; falls for rest energies 0.2 to 0.8 agree to {max(w for m, w, _ in falls if m >= 0.2) - min(w for m, w, _ in falls if m >= 0.2):.3f} sites of {abs(falls[3][1]):.2f}")
    g2, t2, m2 = 0.001, 200.0, 0.05
    print(f"(b) packets moving along the gradient, rest energy {m2}, g = {g2}, T = {t2}, packet width 100")
    for vfrac in (0.3, 0.5, 0.70710678, 0.85):
        k0 = brentq(lambda k: np.sin(k) * np.cos(k) / np.sqrt(m2 * m2 + np.sin(k) ** 2) - vfrac, 1e-6, 0.3)
        for sgn in (+1, -1):
            walk, cloud, norm, edge = run(8000, g2, m2, 0.0, sgn * k0, t2, 100.0)
            print(f"    starting {'up  ' if sgn > 0 else 'down'} at {vfrac:.3f} of the local limit: walk {walk:+9.4f}; cloud {cloud:+9.4f}; walk over cloud {walk / cloud:.4f}; excess over uniform motion {walk - sgn * vfrac * t2:+8.3f} (long-wavelength rule -(g/2)(1 - 2 v^2) T^2 = {-0.5 * g2 * (1 - 2 * vfrac ** 2) * t2 ** 2:+7.3f})")
    print("(c) no transverse motion (no rest energy): the packet moves at the local limiting speed w")
    for sgn in (+1, -1):
        walk, cloud, norm, edge = run(6000, 0.002, 0.0, 0.0, sgn * 0.3, 200.0, 40.0)
        unit = -np.log(1 - sgn * 0.002 * 200.0) / 0.002 * 1.0 if sgn > 0 else -np.log(1 + 0.002 * 200.0) / 0.002
        print(f"    moving {'up  ' if sgn > 0 else 'down'}: walk {walk:+9.3f}; cloud {cloud:+9.3f}; walk over cloud {walk / cloud:.4f}; a ray with dz/dt = w exactly (wave vector tending to zero) would give {unit:+9.3f}")
    print("(d) the time-scaling identity in a uniform gradient: the same packet moved up by a sites evolves exp(g a) times faster")
    n_sites, g3, m3 = 3000, 0.002, 0.3
    ham = build(n_sites, g3, n_sites / 2, m3, 0.0)
    psi = packet(n_sites, n_sites / 2 - 50, 30.0, 0.1, m3, 0.0)
    for a in (1, 10, 100):
        shifted = np.roll(psi.reshape(n_sites, 2), a, axis=0).reshape(-1)
        left = expm_multiply(-1j * ham * 60.0, shifted)
        right = np.roll(expm_multiply(-1j * ham * (60.0 * np.exp(g3 * a)), psi).reshape(n_sites, 2), a, axis=0).reshape(-1)
        plain = np.roll(expm_multiply(-1j * ham * 60.0, psi).reshape(n_sites, 2), a, axis=0).reshape(-1)
        print(f"    a = {a:3d}: |U(t) T_a psi - T_a U(exp(g a) t) psi| = {np.linalg.norm(left - right):.1e}; with the time not rescaled {np.linalg.norm(left - plain):.1e}")
