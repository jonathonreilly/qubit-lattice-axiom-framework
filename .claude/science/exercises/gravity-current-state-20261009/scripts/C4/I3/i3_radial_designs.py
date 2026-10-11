"""Lane RI, probe I3, script 2: 'coarse-cell' designs where every mode above |k| ~ pi/L is flat (gapped, no
group velocity), built as a radial C-infinity single-band dispersion on the fine Z^3 zone, plus the
multi-band variant (internal flat bands at energy M) and a Bose-Fermi paired variant.

omega^2 = m^2 + g(s), s = |k|^2, g'(s) = S((sqrt(s)-kappa)/kappa), kappa = pi/L, so
  omega^2 = m^2 + |k|^2 exactly for |k| <= kappa (A = u_xx - 1 = 0 there: exact relativistic IR),
  flat for |k| >= 2 kappa (needs 2 kappa < pi, L > 2; the function is then smooth and periodic).
Quantities per fine site, as in script 1, by radial quadrature (angular averages exact):
  rho, p_x, a_x = <E_x - H>_vac (identity a_x = -(rho + p_x)), mu_E = mu_T2 (isotropic design),
  zone mean of u_xx (sum rule), loop-weighted anomaly.
Then: fitted power laws in L and the L* that would meet the P0 bound (5.7e-99 of natural).
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

B_P0 = 5.7e-99          # refereed P0 bound: residual shear number / natural (reduced-Planck cell)
B_P0_fw = 9.0e-102      # framework convention (lane P arithmetic, not refereed)


def S(t):
    t = np.clip(t, 0.0, 1.0)
    def psi(x):
        out = np.zeros_like(x); pos = x > 0; out[pos] = np.exp(-1.0 / x[pos]); return out
    a, b = psi(1 - t), psi(t)
    return a / (a + b)


def Sd(t, h=1e-7):
    return (S(t + h) - S(t - h)) / (2 * h)


def radial(L, m=0.0, n=400):
    kap = np.pi / L
    assert 2 * kap < np.pi
    x0, w0 = leggauss(n)
    ks, ws = [], []
    for a, b in ((0, kap), (kap, 2 * kap)):
        ks.append(0.5 * (b - a) * x0 + 0.5 * (b + a)); ws.append(0.5 * (b - a) * w0)
    k = np.concatenate(ks); wk = np.concatenate(ws)
    t = (k - kap) / kap
    gp = S(t)                                   # dg/ds
    gpp = Sd(t) / kap / (2 * k)                  # d^2 g / ds^2 = dS/dk / (2k)
    # g(s) = int_0^s g'(s') ds' = int_0^k g'(k') 2k' dk'
    kt = np.linspace(0, 2 * kap, 400001)
    gt = np.concatenate([[0.0], np.cumsum(0.5 * (S((kt[1:] - kap) / kap) * 2 * kt[1:] + S((kt[:-1] - kap) / kap) * 2 * kt[:-1]) * np.diff(kt))])
    g = np.interp(k, kt, gt); gmax = gt[-1]
    om = np.sqrt(m * m + g)
    omf = np.sqrt(m * m + gmax)
    vol = (2 * np.pi) ** 3
    shell = 4 * np.pi * k ** 2 * wk / vol        # measure of the ball, normalized to the zone
    ball = (4.0 / 3.0) * np.pi * (2 * kap) ** 3 / vol
    # derivatives: d_i u = g' k_i ; u_xx = g' + 2 g'' k_x^2 ; angular <k_x^2> = k^2/3, <k_x^4> = k^4/5
    rho = np.sum(shell * 0.5 * om) + (1 - ball) * 0.5 * omf
    rho_flat = (1 - ball) * 0.5 * omf
    px = np.sum(shell * 0.5 * gp ** 2 * (k ** 2 / 3) / om)
    uxx_mean = np.sum(shell * (gp + 2 * gpp * k ** 2 / 3))            # flat region contributes u_xx = 0
    ax = np.sum(shell * 0.5 * (gp + 2 * gpp * k ** 2 / 3 - 1) * om) + (1 - ball) * 0.5 * (0 - 1) * omf
    # X_E = g'^2 (k_x^2 - k_y^2): <X_E^2>_ang = g'^4 k^4 * 4/15 ; X_T = 2 g'^2 k_x k_y: <X_T^2> = g'^4 k^4 * 4/15
    X2 = gp ** 4 * k ** 4 * 4.0 / 15.0
    muE = -np.sum(shell * X2 / om ** 3) / 8
    # loop-weighted anomaly with the T2 measure: need <(u_xx - 1) X_T^2>_ang
    # <k_x^2 k_x^2 k_y^2>_ang = k^6 * <n_x^4 n_y^2> = k^6 * 3/105 ; <n_x^2 n_y^2> = 1/15
    num = np.sum(shell * 4 * gp ** 4 * ((gp - 1) * k ** 4 / 15 + 2 * gpp * k ** 6 * 3 / 105) / om ** 3)
    den = np.sum(shell * 4 * gp ** 4 * k ** 4 / 15 / om ** 3)
    return dict(rho=rho, rho_flat=rho_flat, px=px, ax=ax, ident=ax + rho + px, uxx=uxx_mean,
                muE=muE, Aw=num / den, omf=omf, flatfrac=1 - ball)


if __name__ == "__main__":
    print("== Radial coarse-flat(L) design, m = 0: per fine site ==")
    print(" L      rho        rho_flat   omega_flat  p_x         a_x=<E_x-H>  a+rho+p   <u_xx>     mu_E=mu_T2   A_w(T2)")
    Ls = [3, 4, 6, 8, 16, 32, 64, 128, 256, 1024, 4096]
    res = {}
    for L in Ls:
        o = radial(L); res[L] = o
        print(f"{L:5d} {o['rho']:.4e} {o['rho_flat']:.4e} {o['omf']:.4e} {o['px']:.4e} {o['ax']:+.4e} "
              f"{o['ident']:+.1e} {o['uxx']:+.1e} {o['muE']:+.4e} {o['Aw']:+.3f}")
    print("\n== scaled values (Q * L^p) at large L: test of pure power laws ==")
    for L in (64, 256, 1024, 4096):
        o = res[L]
        print(f"L={L:5d}: rho*L = {o['rho']*L:.6f}   p_x*L^4 = {o['px']*L**4:.6f}   mu*L^4 = {o['muE']*L**4:.6f}"
              f"   (rho+p_x - rho_flat)*L^4 = {(o['rho'] + o['px'] - o['rho_flat'])*L**4:.6f}")
    # comparison with natural (fine NN) values from script 1: mu_T2(NN, m=0) = -1.17819e-2, rho = 1.19380, p_x = 0.110001
    muNN, rhoNN, pNN = 1.17819e-2, 1.19380, 0.110001
    cmu = abs(res[4096]['muE']) * 4096 ** 4 / muNN
    cp = res[4096]['px'] * 4096 ** 4 / pNN
    crho = res[4096]['rho'] * 4096 / rhoNN
    print(f"\nrelative to the fine-NN natural values: mu/mu_NN = {cmu:.4e} L^-4 ; p/p_NN = {cp:.4e} L^-4 ; rho/rho_NN = {crho:.4f} L^-1")
    for name, c, pw in (("mu (TT Hessian, linear-only)", cmu, 4), ("vacuum pressure p", cp, 4), ("vacuum anomaly incl. flat zero-point", crho, 1)):
        for tag, B in (("refereed 5.7e-99", B_P0), ("framework 9.0e-102", B_P0_fw)):
            Lstar = (c / B) ** (1.0 / pw)
            print(f"L* for {name:38s} at P0 ({tag}): L* = {Lstar:.3e}")
    lP_red = 8.10e-35  # reduced Planck length, m
    hbarc_eVm = 1.97327e-7
    Lstar = (cmu / B_P0) ** 0.25
    print(f"\nmu-based L* = {Lstar:.3e}: coarse cell ell* = {Lstar*lP_red:.3e} m ; coarse cutoff pi/ell* = {np.pi*hbarc_eVm/(Lstar*lP_red):.3e} eV")
    MPl_red_eV = 2.435e27
    for E_eV in (1e13, 1e14):  # 10 TeV, 100 TeV: modes that must lie in the relativistic band
        Lmax = np.pi * MPl_red_eV / E_eV
        print(f"good band must reach {E_eV:.0e} eV: L <= {Lmax:.3e}; then mu/natural >= {cmu*Lmax**-4:.3e}")
    print("\n== multi-band variant: internal bands exactly flat at energy M (no group velocity, no stress) ==")
    print("contribution per internal mode: rho = M/2, p = 0, mu = 0 (any completion), <E_x - H> = -M/2, A = -1 per quantum.")
    for M in (1.0, 2.0):
        for L in (8, 64, 1024):
            frac = 1 - 1.0 / L ** 3
            print(f"M={M}, L={L}: internal fraction {frac:.6f}; rho+p from internal = {0.5*M*frac:.4f} per fine site (does not fall)")
    print("\n== Bose-Fermi paired variant (one complex boson + one two-band fermion with |eps| = omega, same flow coupling) ==")
    print("vacuum energy E0_B(h) + E0_F(h) = sum_k omega_h(k) - sum_k omega_h(k) = 0 for every h and every design: rho, p, a_x, mu all cancel")
    print("mode by mode (construction-level identity). The operator anomaly sum_k (u_xx-1) eps_k n_k on real quanta has the same sign")
    print("for both statistics and does NOT cancel.")
