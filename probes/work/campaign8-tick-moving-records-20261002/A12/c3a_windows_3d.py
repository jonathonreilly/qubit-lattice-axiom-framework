"""C3a: T-tick windowed formation weight at one site, 3D seas (supplied toys).
(S) half-filled staggered sea (A9's vacuum), change sampled once per tick: U = e^{-iH}, E(k) = sqrt(sum sin^2 k).
    Single-site seed has weight 1/2 on each band at every k (chiral structure; diagonal of H g(|H|) vanishes).
    Infinite-volume measure from the triple convolution of the distribution of sin^2 k (k uniform).
(C) strict-cone 3D two-band conveyor step U = e^{-i kx sx} e^{-i ky sy} e^{-i kz sz} (A5 T6.4, one ordering),
    seed e_x (x) |up>; k-grid L^3 (antiperiodic offsets), closed-form quaternion product.
Vacuum rate of F = n_{w_hat}, w_hat = sum_t f(t) U^{-t} seed: eps = int rho_- |W|^2 / int (rho_+ + rho_-)|W|^2.
Measures are binned onto the FFT grid theta_j = 2 pi j / M, so W(theta_j) is exact (zero-padded FFT)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

PI = np.pi
M = 2 ** 18
TH = 2 * PI * np.arange(M) / M
TH = np.where(TH > PI, TH - 2 * PI, TH)               # in (-pi, pi]


def to_grid(theta, weight):
    j = np.round(np.mod(theta, 2 * PI) * M / (2 * PI)).astype(np.int64) % M
    return np.bincount(j, weights=weight, minlength=M)


def staggered_measure(B=2 ** 16, N1=2 ** 22):
    k = 2 * PI * (np.arange(N1) + 0.5) / N1
    h = np.bincount(np.minimum((np.sin(k) ** 2 * B).astype(np.int64), B - 1), minlength=B) / N1
    n = 4 * B
    hs = np.fft.irfft(np.fft.rfft(h, n) ** 3, n)[: 3 * B - 2]   # histogram of S = sum of 3, bins (j+1.5)/B
    hs = np.clip(hs, 0, None); hs /= hs.sum()
    E = np.sqrt((np.arange(3 * B - 2) + 1.5) / B)
    up = to_grid(E, 0.5 * hs); lo = to_grid(-E, 0.5 * hs)
    return up, lo, E.max()


def conveyor_measure(L=128):
    k = PI * (2 * np.arange(L) + 1) / L
    c, s = np.cos(k), np.sin(k)
    cx, cy, cz = c[:, None, None], c[None, :, None], c[None, None, :]
    sx, sy, sz = s[:, None, None], s[None, :, None], s[None, None, :]
    a0 = (cx * cy * cz - sx * sy * sz).ravel()
    az = (cx * cy * sz + cz * sx * sy).ravel()
    om = np.arccos(np.clip(a0, -1, 1))
    nz = az / np.maximum(np.sin(om), 1e-300)
    wu = 0.5 * (1 + nz) / a0.size; wl = 0.5 * (1 - nz) / a0.size
    return to_grid(om, wu), to_grid(-om, wl)


def lnTn2(n, y):
    """ln T_n(y)^2."""
    out = np.empty_like(y)
    big = np.abs(y) > 1
    a = np.arccosh(np.abs(y[big]))
    out[big] = 2 * (n * a + np.log1p(np.exp(-2 * n * a)) - np.log(2))
    out[~big] = 2 * np.log(np.abs(np.cos(n * np.arccos(y[~big]))) + 1e-300)
    return out


def eps_from_logW2(lw2, up, lo, band=None):
    msk_u, msk_l = up > 0, lo > 0
    lu = np.log(up[msk_u]) + lw2[msk_u]; ll = np.log(lo[msk_l]) + lw2[msk_l]
    num = np.logaddexp.reduce(ll); den = np.logaddexp(num, np.logaddexp.reduce(lu))
    eta = None
    if band is not None:
        inb = msk_u & (TH >= band[0]) & (TH <= band[1])
        eta = np.exp(np.logaddexp.reduce(np.log(up[inb]) + lw2[inb]) - den)
    return num - den, eta


def taps(name, T, Om):
    t = np.arange(T)
    v = 2 * (t + 1) / (T + 1) - 1
    w = {"rect": np.ones(T), "hann": np.sin(PI * (t + 1) / (T + 1)) ** 2,
         "bump": np.exp(-1.0 / (1.0 - v ** 2))}[name]
    return w * np.exp(-1j * Om * t)


def run(model, up, lo, Om, th_e, arc=None):
    print(f"--- {model}: carrier Omega={Om:.4f}, Chebyshev main-lobe half-width {th_e:.4f}; "
          f"total weight {up.sum()+lo.sum():.6f} (upper {up.sum():.4f}) ---")
    print(f"{'T':>5} {'rect':>10} {'hann':>10} {'bump':>10} {'ln cheb':>9}" + (f" {'ln arcCheb':>10}" if arc else "")
          + f" {'ln soft(E=.2)':>13} {'eta[.1,.3]':>10}")
    x0 = 1 / np.cos(th_e / 2)
    rows = []
    for T in (8, 16, 32, 64, 128, 256, 512):
        e = {}
        for name in ("rect", "hann", "bump"):
            W = M * np.fft.ifft(taps(name, T, Om), M)
            e[name] = np.exp(eps_from_logW2(np.log(np.abs(W) ** 2 + 1e-320), up, lo)[0])
        lc, _ = eps_from_logW2(lnTn2(T - 1, x0 * np.cos((TH - Om) / 2)), up, lo)
        extra = ""
        if arc:
            ctr, alpha = arc                     # Chebyshev polynomial of the occupied arc only
            anti = ctr + PI
            la, _ = eps_from_logW2(lnTn2(T - 1, np.cos((TH - anti) / 2) / np.sin(alpha / 2)), up, lo)
            extra = f" {la:10.2f}"
        E0 = 0.2                                  # soft detector centred at E0, main lobe [0, 2 E0]
        ls, eta = eps_from_logW2(lnTn2(T - 1, np.cos((TH - E0) / 2) / np.cos(E0 / 2)), up, lo, band=(0.1, 0.3))
        rows.append((T, e, lc, ls))
        print(f"{T:5d} {e['rect']:10.3e} {e['hann']:10.3e} {e['bump']:10.3e} {lc:9.2f}{extra} {ls:13.2f} {eta:10.3f}")
    Ts = np.array([r[0] for r in rows], float)
    for name in ("rect", "hann"):
        y = np.log([r[1][name] for r in rows]); print(f"  {name}: d ln eps/d ln T (T=64..512) = {np.polyfit(np.log(Ts[-4:]), y[-4:], 1)[0]:+.3f}")
    yb = np.log([r[1]['bump'] for r in rows])
    print(f"  bump: d ln eps/d sqrt T (T=64..512) = {np.polyfit(np.sqrt(Ts[-4:]), yb[-4:], 1)[0]:+.3f}")
    yc = np.array([r[2] for r in rows]); ys = np.array([r[3] for r in rows])
    print(f"  cheb: d ln eps/dT (T=64..512) = {np.polyfit(Ts[-4:], yc[-4:], 1)[0]:+.4f} vs -2 arccosh(1/cos(th_e/2)) = {-2*np.arccosh(x0):+.4f}")
    print(f"  soft(E=0.2): d ln eps/dT (T=64..512) = {np.polyfit(Ts[-4:], ys[-4:], 1)[0]:+.4f} vs -2 arccosh(1/cos(0.1)) = {-2*np.arccosh(1/np.cos(0.1)):+.4f}")


up, lo, Emax = staggered_measure()
run("staggered sea, U = e^{-iH} per tick", up, lo, Om=Emax / 2, th_e=Emax / 2, arc=(-Emax / 2, Emax / 2))
up, lo = conveyor_measure()
run("3D conveyor step (strict cone)", up, lo, Om=PI / 2, th_e=PI / 2)
