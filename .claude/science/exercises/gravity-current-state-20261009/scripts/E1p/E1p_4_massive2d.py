"""E1' 2D control (Johnston causal-matrix form, arXiv:0909.0944 eq.16): K = aC(I - abC)^{-1}, a = 1/2, b = -m^2/rho.
(1) Simulation: per-realization K(top, bottom) and (KJ)(top) on Poisson diamonds, rho = 1.
(2) EXACT second moment (Mecke; chains carry no emptiness condition, so pair-of-chains expansion closes):
      W(x,y) = Kbar(x,y)^2 + b^2 rho * int_{I(y,x)} Kbar(x,w)^2 W(w,y) d^2w,   Kbar = (1/2) J0(m tau).
    Solved on a tau grid (Lorentz invariance) by Neumann iteration with Gauss-Legendre quadrature in
    light-cone coordinates w = (p,q) in [0,U]^2, U = tau/sqrt2, tau_wy^2 = 2pq, tau_xw^2 = 2(U-p)(U-q).
Usage: python E1p_4_massive2d.py sim U nreal seed | exact
"""
import sys, os, time
import numpy as np
from scipy.special import j0
from e1p_core import sprinkle2d_diamond, chain_sums_2d

mT_list = np.array([0.0, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64])


def sim(U, nreal, seed):
    rng = np.random.default_rng(seed)
    tau = np.sqrt(2) * U
    m = mT_list / tau
    avec = np.full(len(m), 0.5); bvec = -m**2
    Kt = np.zeros((nreal, len(m))); KJt = np.zeros((nreal, len(m)))
    w = 2.0; tc = 3 * w     # smeared source: Euclidean Gaussian of width w centred at t = tc, x = 0
    t0 = time.time()
    for r in range(nreal):
        u, v = sprinkle2d_diamond(U, rng)
        t = (u + v) / np.sqrt(2); x = (u - v) / np.sqrt(2)
        J = np.exp(-((t - tc)**2 + x**2) / (2 * w * w))
        Kt[r], KJt[r] = chain_sums_2d(u, v, U, J, avec, bvec)
    os.makedirs("../out", exist_ok=True)
    np.savez(f"../out/massive2d_U{int(U)}_s{seed}.npz", U=U, tau=tau, mT=mT_list, Kt=Kt, KJt=KJt, w=w, tc=tc)
    print(f"U={U} tau={tau:.1f} N~{U*U:.0f} nreal={nreal} time={time.time()-t0:.1f}s", flush=True)


def exact_W(m, rho, taumax, ntau=400, nq=64, iters=200, tol=1e-12):
    """Return tau grid, Kbar^2, W (second moment) for the 2D point-to-point K."""
    taus = np.linspace(0, taumax, ntau + 1)
    xg, wg = np.polynomial.legendre.leggauss(nq)
    xg = 0.5 * (xg + 1); wg = 0.5 * wg
    P, Q = np.meshgrid(xg, xg, indexing="ij"); WW = np.outer(wg, wg)
    S = 0.25 * j0(m * taus)**2
    W = S.copy()
    c = (m**4) / rho      # b^2 rho
    # precompute kernel pieces per tau
    ker = []
    for tau in taus:
        U = tau / np.sqrt(2)
        twy = np.sqrt(2 * (P * U) * (Q * U))
        txw = np.sqrt(2 * (U - P * U) * (U - Q * U))
        ker.append((twy, 0.25 * j0(m * txw)**2 * WW * U * U))
    for it in range(iters):
        Wn = np.empty_like(W)
        for i, tau in enumerate(taus):
            twy, kw = ker[i]
            Wn[i] = S[i] + c * np.sum(kw * np.interp(twy, taus, W))
        d = np.max(np.abs(Wn - W) / (np.abs(Wn) + 1e-300))
        W = Wn
        if d < tol:
            break
    return taus, S, W, it


if __name__ == "__main__":
    if sys.argv[1] == "sim":
        sim(float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        # exact variance law: relative variance of K(x,y) vs m tau for several rho (in units where m*tau fixed)
        out = []
        for mt_max, ml in [(64, 0.02), (64, 0.05), (64, 0.1), (32, 0.2), (32, 0.4)]:
            # m*ell = ml, rho = 1 => m = ml; tau up to mt_max/m
            m = ml; taus, S, W, it = exact_W(m, 1.0, mt_max / m, ntau=600, nq=80)
            V = W - S
            env = 0.25 * (2 / (np.pi * np.maximum(m * taus, 1e-9)))  # envelope of Kbar^2 for m tau >> 1
            np.savez(f"../out/exact2d_ml{ml}.npz", taus=taus, S=S, W=W, m=m)
            print(f"m*ell={ml}: iterations={it}")
            for mt in [1, 2, 4, 8, 16, 24, 32, 48, 64]:
                if mt > mt_max: continue
                i = np.argmin(np.abs(m * taus - mt))
                x = m * m * taus[i]   # m^2 ell tau
                print(f"   m tau={m*taus[i]:6.2f}  m^2 ell tau={x:7.3f}  Var={V[i]:.4e}  Var/Kbar^2={V[i]/S[i]:.4e}  "
                      f"Var/env={V[i]/min(env[i],0.25):.4e}  sd/(a)={np.sqrt(max(V[i],0))/0.5:.4e}")
