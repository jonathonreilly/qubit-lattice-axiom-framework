"""2D control: direct simulation vs EXACT variance law, including the exponentially growing regime (gamma = m^3 ell^2/4)."""
import numpy as np, time
from scipy.special import j0
from e1p_core import sprinkle2d_diamond, chain_sums_2d
from E1p_4_massive2d import exact_W
rng = np.random.default_rng(7)
for U, ms, nreal in [(60.0, [0.1, 0.3, 0.5, 0.7], 400), (120.0, [0.1, 0.2, 0.3, 0.4], 200)]:
    tau = np.sqrt(2) * U
    m = np.array(ms)
    Ks = np.array([chain_sums_2d(*sprinkle2d_diamond(U, rng), U, np.zeros(1), np.full(len(m), 0.5), -m**2)[0]
                   if False else None for _ in range(0)])
    out = []
    t0 = time.time()
    for r in range(nreal):
        u, v = sprinkle2d_diamond(U, rng)
        K, _ = chain_sums_2d(u, v, U, np.zeros(len(u)), np.full(len(m), 0.5), -m**2)
        out.append(K)
    out = np.array(out)
    print(f"U={U} tau={tau:.1f} N~{U*U:.0f} nreal={nreal} ({time.time()-t0:.0f}s)")
    for k, mm in enumerate(m):
        taus, S, W, it = exact_W(mm, 1.0, tau * 1.0005, ntau=500, nq=int(min(400, 40 + 6 * mm * tau)))
        Vex = np.interp(tau, taus, W - S); Kex = 0.5 * j0(mm * tau)
        sd = out[:, k].std(ddof=1); mu = out[:, k].mean()
        print(f"   m*ell={mm:.2f} m*tau={mm*tau:6.1f} m^3ell^2tau/4={mm**3*tau/4:5.2f}: sim sd={sd:.4e} exact sd={np.sqrt(Vex):.4e} "
              f"ratio={sd/np.sqrt(Vex):.3f} | sim mean={mu:+.4e} exact mean={Kex:+.4e} (se {sd/np.sqrt(nreal):.1e})")
