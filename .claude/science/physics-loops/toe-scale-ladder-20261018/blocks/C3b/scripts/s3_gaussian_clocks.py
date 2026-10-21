"""C3b s3 (candidate b): Gaussian clocks with slowly decaying covariance, 2D torus, majority rule (q=2, delta=0).

Families (spectral weight f on the torus; lap(k) = 4 - 2cos kx - 2cos ky):
  P(alpha): stationary, f = s2 + lap^((alpha-2)/2)        -> C(r) ~ r^(-alpha)   (0 < alpha < 2)
  F(H)    : gradient-stationary (fractional), f = lap^-(1+H), zero mode removed -> Var(T_x - T_0) ~ |x|^(2H)
Only the order of clocks matters, so only the increment field enters (C3b NOTE sec. 1).

Measured: longest decreasing path L(x) (C3 sec.1), its tail, its max over the box vs box size; colour C(r);
bond field b_x = sigma_x sigma_{x+e1} correlation Cb(r); chi_L = N<m^2> FSS.
Declared criteria (before running):
  * Theorem K check: |C(r)| <= 2 P(L >= r/2) + 4 SE for r = 4, 8.
  * no-LRO: slope of log chi_L vs log L, |slope| < 0.5 (LRO -> 2).
  * finite ancestry: mean L(x) stable between the two largest boxes (relative change < 10%).
Power-law exponents of Cb are reported as NUMERICAL observations only (no pass/fail).
"""
import numpy as np
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from c3b_common import check, total, nbr_table, depth_and_record, axis_corr, mean_se, fit_loglog

rng = np.random.default_rng(2026_10_19)


def spec(L, fam, par, s2=0.01):
    k = 2 * np.pi * np.fft.fftfreq(L)
    KX, KY = np.meshgrid(k, k, indexing='ij')
    lap = 4 - 2 * np.cos(KX) - 2 * np.cos(KY)
    lap[0, 0] = 1.0
    if fam == 'P':
        f = s2 + lap ** ((par - 2) / 2)
        f[0, 0] = s2  # drop the (non-ergodic) constant mode; irrelevant for order anyway
    else:
        f = lap ** (-(1 + par))
        f[0, 0] = 0.0
    return f


def sample(L, f):
    w = rng.standard_normal((L, L))
    return np.real(np.fft.ifft2(np.sqrt(f) * np.fft.fft2(w))).ravel()


def run(L, fam, par, ns, rmax):
    f = spec(L, fam, par)
    nbr = nbr_table((L, L))
    N = L * L
    Cs, Cbs, chis, Lm, Lmax, Ltail = [], [], [], [], [], []
    for s in range(ns):
        T = sample(L, f)
        sig, Ld = depth_and_record(T, nbr, rng.random(N), np.ones(N), 0.0)
        F = sig.reshape(L, L).astype(float)
        Cs.append(axis_corr(F, rmax))
        b = F * np.roll(F, -1, axis=0)
        Cbs.append(axis_corr(b, rmax))
        chis.append(N * F.mean() ** 2)
        Lm.append(Ld.mean()); Lmax.append(Ld.max())
        Ltail.append(np.bincount(np.minimum(Ld, 200), minlength=201) / N)
    f_nz = f[f > 0]
    v = 1.0 / np.mean(1.0 / f) if np.all(f > 0) else np.nan
    return dict(C=np.array(Cs), Cb=np.array(Cbs), chi=np.array(chis), Lm=np.array(Lm), Lmax=np.array(Lmax),
                Ltail=np.array(Ltail), v=v, var=np.mean(f))


if __name__ == "__main__":
    t0 = time.time()
    configs = [('P', 0.25), ('P', 1.0), ('F', 0.5), ('F', 0.8), ('F', 0.95)]
    Ls = [64, 128, 256]
    for fam, par in configs:
        print(f"=== family {fam} par={par} ===")
        res = {}
        for L in Ls:
            ns = int(min(800, 1.6e7 / (L * L)))
            res[L] = run(L, fam, par, ns, L // 2)
            R = res[L]
            m, se = mean_se(R['chi']); lm, lse = mean_se(R['Lm'])
            print(f" L={L:4d} ns={ns:4d}  chi_L={m:8.3f}+-{se:.3f}  <L(x)>={lm:.3f}+-{lse:.3f}  max_box L={R['Lmax'].mean():.1f}"
                  f"  sigma^2/v={R['var']/R['v'] if np.isfinite(R['v']) else float('nan'):.3g}")
        # FSS chi
        ch = np.array([mean_se(res[L]['chi'])[0] for L in Ls]); che = np.array([mean_se(res[L]['chi'])[1] for L in Ls])
        sl, sse, _ = fit_loglog(np.array(Ls, float), ch, che)
        check(f"s3 {fam}{par}: chi_L slope |.|<0.5 (no LRO)", abs(sl) < 0.5, f"slope={sl:.3f}+-{sse:.3f}")
        a, b_ = mean_se(res[Ls[-2]]['Lm'])[0], mean_se(res[Ls[-1]]['Lm'])[0]
        check(f"s3 {fam}{par}: <L(x)> stable in box size (finite ancestry)", abs(b_ / a - 1) < 0.1, f"{a:.3f} -> {b_:.3f}")
        R = res[Ls[-1]]
        tail = R['Ltail'].mean(0)
        PLge = np.cumsum(tail[::-1])[::-1]  # P(L >= n)
        C = R['C'].mean(0); Cse = R['C'].std(0, ddof=1) / np.sqrt(len(R['C']))
        for r in (4, 8):
            bound = 2 * PLge[(r + 1) // 2]
            check(f"s3 {fam}{par}: Theorem K |C({r})| <= 2P(L>=r/2)", abs(C[r]) <= bound + 4 * Cse[r],
                  f"C={C[r]:.2e}+-{Cse[r]:.1e} bound={bound:.2e}")
        print("  P(L>=n) n=1..12:", " ".join(f"{PLge[n]:.2e}" for n in range(1, 13)))
        Cb = R['Cb'].mean(0); Cbse = R['Cb'].std(0, ddof=1) / np.sqrt(len(R['Cb']))
        print("  r     C(r)              Cb(r)")
        for r in (1, 2, 4, 8, 16, 32, 64):
            print(f"  {r:3d}  {C[r]: .3e}+-{Cse[r]:.1e}  {Cb[r]: .3e}+-{Cbse[r]:.1e}")
        rr = np.array([4, 6, 8, 12, 16, 24, 32])
        good = (np.abs(Cb[rr]) > 3 * Cbse[rr])
        if good.sum() >= 3:
            sl, sse, c2 = fit_loglog(rr[good].astype(float), np.abs(Cb[rr][good]), Cbse[rr][good])
            print(f"  NUMERICAL: bond correlation |Cb(r)| ~ r^{sl:.2f}+-{sse:.2f} over r in {list(rr[good])} (chi2/dof {c2:.2f})")
        else:
            print("  NUMERICAL: bond correlation not resolved above 3 SE beyond r=4")
        print(f"  elapsed {time.time()-t0:.0f}s", flush=True)
    total()
