"""Lane RI, probe I3, script 5: do lattice-scale (flat, 'Carroll') modes in LOOPS feed Lorentz violation into the
low band?  Onsite phi^4 (V = lambda/4! sum_x phi_x^4) on the fine Z^3 grid, one real scalar, O(lambda^2) sunset.

Euclidean 1PI: Gamma2(p0,p) = p0^2 + omega(p)^2 + (lambda/2) D(0) - (lambda^2/6) FT[D^3](p0,p).
Expanding FT[D^3] at p = 0:  a_t = (lambda^2/12) int dtau sum_x tau^2 D^3,  a_x = (lambda^2/12) int dtau sum_x x_1^2 D^3.
Low-band speed^2 (ball modes have omega^2 = p^2 + m^2 exactly, c0 = 1):  c^2 = (1 + a_x)/(1 + a_t),
so  delta c^2 / lambda^2 = (I_x - I_t)/12  with  I_x = int sum x_1^2 D^3,  I_t = int sum tau^2 D^3.
A Lorentz-invariant regulator gives I_x = I_t.  D(tau,x) = (1/N^3) sum_k e^{ikx} e^{-omega_k |tau|}/(2 omega_k).
Designs (m = kappa/2 so the family is self-similar, kappa = pi/L):
  'radial-flat'   : omega^2 = m^2 + g(|k|^2), relativistic in the ball |k|<kappa, flat beyond 2 kappa (energy ~ coarse cutoff);
  'radial-gapped' : relativistic in the ball, then raised smoothly to M^2 = 4 (fine scale) and flat beyond 2 kappa;
  'NN' control    : nearest-neighbour fine lattice, m = 0.5 (the fine-scale natural baseline).
Box N = 8L (NN: N = 48), periodic, minimal-image x.
"""
import numpy as np
import time


def S(t):
    t = np.clip(t, 0.0, 1.0)
    def psi(x):
        out = np.zeros_like(x); pos = x > 0; out[pos] = np.exp(-1.0 / x[pos]); return out
    a, b = psi(1 - t), psi(t)
    return a / (a + b)


def omega_grid(design, N, L=None, m=None, M2=4.0):
    n = np.fft.fftfreq(N) * N
    k1 = 2 * np.pi * n / N
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    if design == "NN":
        w2 = m * m + sum(2 - 2 * np.cos(K) for K in (KX, KY, KZ))
        return np.sqrt(w2)
    kap = np.pi / L
    kr = np.sqrt(KX ** 2 + KY ** 2 + KZ ** 2)
    kt = np.linspace(0, 2 * kap, 200001)
    if design == "radial-flat":
        dg = S((kt - kap) / kap) * 2 * kt                 # d g / dk
    elif design == "radial-gapped":
        # g(k) = k^2 in the ball, then rises to M2 - m^2 - ... : g'(k) = 2k S + B(k) with a bump B placing the excess
        base = S((kt - kap) / kap) * 2 * kt
        gb = np.concatenate([[0.0], np.cumsum(0.5 * (base[1:] + base[:-1]) * np.diff(kt))])
        bump = np.where((kt > kap) & (kt < 2 * kap), np.exp(-1.0 / np.clip((kt - kap) / kap * (2 * kap - kt) / kap, 1e-300, None)), 0.0)
        Ib = np.sum(0.5 * (bump[1:] + bump[:-1]) * np.diff(kt))
        dg = base + bump * (M2 - gb[-1]) / Ib
    else:
        raise ValueError(design)
    gt = np.concatenate([[0.0], np.cumsum(0.5 * (dg[1:] + dg[:-1]) * np.diff(kt))])
    g = np.interp(np.minimum(kr, 2 * kap), kt, gt)
    return np.sqrt(m * m + g)


def sunset_moments(om, N, ntau=260):
    n = np.fft.fftfreq(N) * N                            # minimal-image coordinates
    X1 = np.broadcast_to(n[:, None, None] ** 2, (N, N, N))
    wmin, wmax = om.min(), om.max()
    taus = np.concatenate([[0.0], np.geomspace(0.02 / wmax, 40.0 / wmin, ntau)])
    It = np.zeros_like(taus); Ix = np.zeros_like(taus); I0 = np.zeros_like(taus)
    base = 1.0 / (2 * om)
    for j, t in enumerate(taus):
        D = np.real(np.fft.ifftn(base * np.exp(-om * t)))
        D3 = D ** 3
        s = D3.sum()
        I0[j] = s; It[j] = t * t * s; Ix[j] = np.sum(X1 * D3)
    trap = lambda f: 2 * np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(taus))   # tau in (-inf, inf)
    return trap(It), trap(Ix), trap(I0), D[0, 0, 0]


if __name__ == "__main__":
    t0 = time.time()
    print("design          L    N   omega_flat   I_t          I_x          dc2/lambda^2=(I_x-I_t)/12   D(0)=<phi^2>  [s]")
    om = omega_grid("NN", 48, m=0.5)
    It, Ix, I0, _ = sunset_moments(om, 48)
    phi2 = np.mean(1 / (2 * om))
    print(f"NN(m=0.5)       -   48  {'-':>10s}   {It:.5e}  {Ix:.5e}  {(Ix-It)/12:+.5e}               {phi2:.4f}   {time.time()-t0:.0f}")
    for design in ("radial-flat", "radial-gapped"):
        for L in (4, 6, 8, 12, 16):
            N = 8 * L
            kap = np.pi / L
            om = omega_grid(design, N, L=L, m=kap / 2)
            It, Ix, I0, _ = sunset_moments(om, N)
            phi2 = np.mean(1 / (2 * om))
            print(f"{design:14s} {L:3d} {N:4d}  {om.max():.4e}   {It:.5e}  {Ix:.5e}  {(Ix-It)/12:+.5e}               {phi2:.4f}   {time.time()-t0:.0f}", flush=True)
    print("\nReading: I_t - I_x is the Lorentz-violating part (zero for a Lorentz-invariant regulator).")
    print("Carroll (flat) modes are local in x, so they feed I_t (tau^2 moment) but not I_x (x^2 moment).")
