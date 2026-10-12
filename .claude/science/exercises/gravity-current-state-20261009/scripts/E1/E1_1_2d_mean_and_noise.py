"""E1 (1+1): (b) mean dispersion of the BD operator at boosted momenta with equal p^2,
for two non-locality scales on the same sprinkling (one cone in mean);
(c) element-wise noise of B_eps 1 vs eps and IR size U; window-averaged noise vs
window size lam (sharp and smooth windows), compared with the white-noise prediction.
Units rho_k = 1 for the reference operator. Reported quantity: b = B/(4 rho_k).
Conventions: box = -d_t^2 + d_x^2; plane wave exp(i(-w t + k x)); mean B -> -p^2,
p^2 = -w^2 + k^2.  u=(t+x)/sqrt2, v=(t-x)/sqrt2, interval area V = du*dv.
"""
import numpy as np, time
from math import sqrt, cosh, sinh, log
from bd_core import sprinkle2d, bd2d

rng = np.random.default_rng(20261009)
s2 = sqrt(2.0)
S2 = lambda U: 0.1875*log(U*U) + 0.3480   # shell integral (E1_0 fit: S(16)=1.38729)


def tx(u, v): return (u + v)/s2, (u - v)/s2


from math import factorial
def _inner(a, pv, B):
    """int_0^B e^{-(a+i pv) b} (1 - 2ab + a^2 b^2/2) db, closed form."""
    c = a + 1j*pv
    def mom(n):
        cb = c*B; ssum = sum(cb**j/factorial(j) for j in range(n+1))
        return factorial(n)/c**(n+1)*(1 - np.exp(-cb)*ssum)
    return mom(0) - 2*a*mom(1) + 0.5*a*a*mom(2)


def bbar2(w, k, ux, vx, n=1500):
    """Continuum mean b = -1/2 + int_0^ux int_0^vx g(ab) e^{-i(pu a + pv b)} (rho_k=1),
    plane wave exp(i(-w t + k x)), pu=(k-w)/sqrt2, pv=-(k+w)/sqrt2 (Gauss-Legendre in a)."""
    pu = (k - w)/s2; pv = -(k + w)/s2
    if ux > 200:  # infinite past: closed form inner = -pv^2/(a+i pv)^3; outer on [0, inf)
        xs, ws = np.polynomial.legendre.leggauss(n)
        # map [0,inf) via a = z/(1-z)
        z = 0.5*(xs + 1); wz = 0.5*ws
        a = z/(1 - z); jac = 1/(1 - z)**2
        f = np.exp(-1j*pu*a)*(-pv*pv)/(a + 1j*pv)**3
        return -0.5 + np.sum(wz*jac*f)
    xs, ws = np.polynomial.legendre.leggauss(n)
    a = 0.5*ux*(xs + 1); wa = 0.5*ux*ws
    f = np.exp(-1j*pu*a)*_inner(a.astype(complex), pv, vx)
    return -0.5 + np.sum(wa*f)


def part_b():
    print("== (b) mean dispersion b(p) = <B e^{ipy}>(x) e^{-ipx}/(4 rho_k), two scales ==")
    print("   species A: l_k = 1 (eps_A = 1/64); species B: l_k = 2 on the same sprinkling")
    print("   (eps_B = eps_A/4 in its own units).  Expect b depends on p^2 only, b ~ -p^2/4")
    U = 14.0; epsA = 1/64; rho = 1/epsA
    moms = []
    for p in [0.25, 0.5]:
        for eta in [0.0, 0.5, 1.0]:
            moms.append(("timelike", p, eta, p*cosh(eta), p*sinh(eta)))
            moms.append(("spacelike", p, eta, p*sinh(eta), p*cosh(eta)))
    acc = {}
    for r in range(160):
        u, v = sprinkle2d(rho, U, rng)
        tg = np.nonzero((u > U - 1.0) & (v > U - 1.0))[0]
        t, x = tx(u, v)
        F = []
        for (_, _, _, w, k) in moms:
            ph = -w*t + k*x
            F += [np.cos(ph), np.sin(ph)]
        F = np.array(F)
        for lk, eps in [(1.0, epsA), (2.0, epsA/4)]:
            # species with l_k: rho_k = 1/l_k^2 -> eps = rho_k/rho. Coordinates rescaled by 1/l_k
            out, _, _ = bd2d(u/lk, v/lk, U/lk, tg, eps, F, F[:, tg])
            phx = np.array([-w*t[tg] + k*x[tg] for (_, _, _, w, k) in moms])
            Bc = (out[:, 0::2] + 1j*out[:, 1::2]) * np.exp(-1j*phx.T)
            Bc = Bc / lk**2    # b in units of 1/l_k^2 -> physical units (l_k=1 ref)
            acc.setdefault(lk, []).append(Bc)
    for lk in acc:
        A = np.vstack(acc[lk]); mu = A.mean(0)
        R = np.array([a.mean(0) for a in acc[lk]])  # per-realization means
        se = R.std(0, ddof=1)/sqrt(R.shape[0])      # realization-level standard error
        print(f" l_k={lk}: N_targets={A.shape[0]} realizations={R.shape[0]} (se from realizations)")
        for i, (typ, p, eta, w, k) in enumerate(moms):
            p2 = -w*w + k*k
            # exact continuum mean for the finite past diamonds of the targets (grid average)
            grid = np.linspace(U - 1.0 + 0.1, U - 0.1, 5)
            cm = np.mean([bbar2(w*lk, k*lk, uu/lk, vv/lk) for uu in grid for vv in grid])/lk**2
            cinf = bbar2(w*lk, k*lk, 1e4, 1e4)/lk**2
            print(f"   {typ:9s} |p|={p:.2f} eta={eta:.1f} p^2={p2:+.3f}  "
                  f"b={mu[i].real:+.4f}{mu[i].imag:+.4f}i (se {se[i]:.4f})"
                  f"  cont(finite)={cm.real:+.4f}{cm.imag:+.4f}i  cont(inf)={cinf.real:+.4f}{cinf.imag:+.4f}i"
                  f"  -p^2/4={-p2/4:+.4f}")


def part_c_element(eps_list, U_list, nreal):
    print("\n== (c1) element-wise noise of b1 = B_eps 1/(4 rho_k) at top elements ==")
    print("   white/first-chaos prediction: Var b1 = eps*S(U), S(U) = int g^2 over past diamond")
    rows = []
    for eps in eps_list:
        for U in U_list:
            vals = []; gains = []
            for r in range(nreal if eps < 1 else 10*nreal):
                u, v = sprinkle2d(1/eps, U, rng)
                wtg = max(0.3, sqrt(6*eps)); tg = np.nonzero((u > U - wtg) & (v > U - wtg))[0]
                if tg.size == 0: continue
                F = np.ones((1, u.size))
                out, gain, ns = bd2d(u, v, U, tg, eps, F, F[:, tg])
                vals.append(out[:, 0]); gains.append(gain)
            b = np.concatenate(vals); gn = np.concatenate(gains)
            pred = eps*S2(U)
            rows.append((eps, U, b.mean(), b.var(), pred, gn.mean()))
            print(f" eps={eps:.5f} U={U:5.1f} n={b.size:6d} <b1>={b.mean():+.4f} Var={b.var():.5f}"
                  f"  eps*S(U)={pred:.5f}  ratio={b.var()/pred:.3f}  <A^2>={gn.mean():.5f}")
    return rows


def window_noise(eps, U, lam, nreal, smooth=True, field="one", k0=0.0):
    """Window centred at (uc,vc)=(U-4lam, U-4lam) (sharp: square [uc-lam,uc+lam]^2;
       smooth: Gaussian sd lam, truncated at 3.5 lam). Returns window means per realization."""
    uc = vc = U - 4.0*lam
    vals = []
    for r in range(nreal):
        u, v = sprinkle2d(1/eps, U, rng)
        if smooth:
            sel = (np.abs(u - uc) < 3.5*lam) & (np.abs(v - vc) < 3.5*lam)
        else:
            sel = (np.abs(u - uc) < lam) & (np.abs(v - vc) < lam)
        tg = np.nonzero(sel)[0]
        t, x = tx(u, v)
        if field == "one":
            F = np.ones((1, u.size))
        else:  # null wave cos(k0 (t - x)): on-shell, mean B = 0
            F = np.cos(k0*(t - x))[None, :]
        out, _, _ = bd2d(u, v, U, tg, eps, F, F[:, tg])
        if smooth:
            w = np.exp(-((u[tg]-uc)**2 + (v[tg]-vc)**2)/(2*lam*lam))
        else:
            w = np.ones(tg.size)
        if field == "one":
            vals.append((w*out[:, 0]).sum()/w.sum())
        else:
            vals.append((w*out[:, 0]*F[0, tg]).sum()/(w*F[0, tg]**2).sum())
    return np.array(vals)


def part_c_window():
    print("\n== (c2) window-averaged b_lam (mass^2 felt by a lam-size mode, /4rho_k) ==")
    print("   white prediction (independent elements): Var = eps*S(U_eff) * eps/(lam^2*Weff)")
    print("   Weff = (sum w)^2/(sum w^2) per unit density: sharp 4 lam^2; Gaussian 4 pi lam^2")
    for eps in [1/16, 1/64]:
        for smooth in [False, True]:
            print(f" eps={eps:.4f} window={'Gauss' if smooth else 'sharp'}")
            for lam in [0.5, 1.0, 2.0, 4.0]:
                U = 8.0*lam + 6.0
                nreal = 120 if lam <= 2 else 60
                vals = window_noise(eps, U, lam, nreal, smooth)
                Weff = (4*np.pi if smooth else 4.0)*lam*lam
                # S at the window centre: past diamond side ~ U-4lam
                pred = eps*S2(U - 4*lam) * eps / Weff
                sd = vals.std(ddof=1)
                print(f"   lam={lam:4.1f} U={U:5.1f} <b>={vals.mean():+.5f} sd={sd:.5f} "
                      f"sd*lam={sd*lam:.5f} white_pred_sd={sqrt(pred):.5f} ratio={sd/sqrt(pred):.2f}")


def part_c_IR():
    print("\n== (c3) IR dependence of the smooth-window noise at fixed lam=1, eps=1/64 ==")
    for Uextra in [2.0, 8.0, 32.0, 96.0]:
        lam = 1.0; eps = 1/64
        U = 8.0*lam + Uextra
        vals = window_noise(eps, U, lam, 80, True)
        pred = eps*S2(U - 4*lam)*eps/(4*np.pi*lam*lam)
        print(f"   past side U-4lam={U-4*lam:6.1f}  sd={vals.std(ddof=1):.5f}  white_pred_sd={sqrt(pred):.5f}")


def part_c_wave():
    print("\n== (c4) noise felt by an on-shell null wave cos(k0(t-x)), smooth window ==")
    for eps in [1/64]:
        for k0 in [0.1, 0.3]:
            for lam in [1.0, 2.0, 4.0]:
                U = 8*lam + 6
                vals = window_noise(eps, U, lam, 60, True, field="wave", k0=k0)
                print(f"   eps={eps:.4f} k0={k0} lam={lam}: <b>={vals.mean():+.5f} sd={vals.std(ddof=1):.5f}")


if __name__ == "__main__":
    t0 = time.time()
    part_b(); print(f"   [{time.time()-t0:.0f}s]")
    part_c_element([1.0, 1/4, 1/16, 1/64, 1/256], [4.0, 8.0, 16.0, 32.0], 40)
    print(f"   [{time.time()-t0:.0f}s]")
    part_c_window(); print(f"   [{time.time()-t0:.0f}s]")
    part_c_IR(); print(f"   [{time.time()-t0:.0f}s]")
    part_c_wave(); print(f"   [{time.time()-t0:.0f}s]")
