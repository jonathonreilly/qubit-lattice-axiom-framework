"""Transfer-matrix log quasilocality — bilinear-sector narrow theorem runner.

Companion to
`docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`.

Object: the framework's free staggered two-step transfer
matrix T_hat^2 (in-repo derivation,
`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`)
has single-particle kernel e^{-2E(p)} with the exact action-derived
dispersion E(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)).  The exact
reconstructed Hamiltonian H = -log(T_hat^2)/(2 a_tau) is therefore the
translation-invariant bilinear with position-space hopping kernel

    h(z) = (1/a_tau) * (2 pi)^{-d} \\int_{T^d} E(p) e^{i p.z} d^d p.

The note proves (Q1) the explicit exponential bound

    |h(z)| <= (1/a_tau) * C_d(eta, m) * exp(-eta * ||z||_inf),
    C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta),    0 < eta < eta* = arcsinh(m),

(Q2) sharpness: the optimal rate is exactly eta* = arcsinh(m) (branch
point of the symbol at p = i*arcsinh(m); E'(p) blows up there), (Q3) the
support-family translation: per-site overlap weight W_H = ||h||_l1 < inf,
finite-range truncations H_R with tail weight W_tail(R) <= shell-sum
bound ~ (1+R)^{d-1} e^{-eta R}, and the negative finding that the exact
H is NOT finite-range (h(z) != 0 at l1-range 4), so the strict R <= 2
form of the microcausality bridge note's (F5) hypothesis fails on this
sector and must be read in the quasilocal form proved here.

This runner verifies every quantitative claim numerically and includes
two falsification legs (m = 0 gapless boundary; a long-range-perturbed
positive symbol that violates the derived bound), showing the checks
have teeth.

Check classes per the audit rubric: [A] exact algebraic identity check,
[B] cross-note input verification, [C] first-principles compute from the
framework baseline, [D] external comparator (none used here).

Reproducibility: deterministic; no random input; runtime well under
5 minutes (numpy FFTs on fixed grids).
"""
from __future__ import annotations

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def eta_star(m: float) -> float:
    return float(np.arcsinh(m))


def C_strip(eta: float, m: float, d: int) -> float:
    """Derived strip constant C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)."""
    return float(np.sqrt(m * m + (d - 1) + np.cosh(eta) ** 2))


def dispersion(m: float, *p):
    """E(p) = arcsinh sqrt(m^2 + sum_mu sin^2 p_mu) (vectorized)."""
    s = m * m
    for comp in p:
        s = s + np.sin(comp) ** 2
    return np.arcsinh(np.sqrt(s))


def kernel_1d(m: float, N: int = 8192) -> np.ndarray:
    """h(n), n = 0..N-1 (n > N/2 are negative offsets), a_tau = 1."""
    p = 2.0 * np.pi * np.arange(N) / N
    return np.fft.ifft(dispersion(m, p)).real


def kernel_3d(m: float, N: int = 128) -> np.ndarray:
    p = 2.0 * np.pi * np.arange(N) / N
    P1, P2, P3 = np.meshgrid(p, p, p, indexing="ij", sparse=True)
    return np.fft.ifftn(dispersion(m, P1, P2, P3)).real


def fit_rate_with_log_prefactor(ns: np.ndarray, vals: np.ndarray) -> tuple[float, float]:
    """Fit log|h(n)| = -eta*n - beta*log(n) + c; return (eta, beta)."""
    y = np.log(np.abs(vals))
    A = np.column_stack([ns, np.log(ns), np.ones_like(ns, dtype=float)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return -float(coef[0]), -float(coef[1])


def fit_rate_4param(ns: np.ndarray, vals: np.ndarray) -> tuple[float, float]:
    """Fit log|h(n)| = -eta*n - beta*log(n) + c + g/n; return (eta, beta)."""
    y = np.log(np.abs(vals))
    A = np.column_stack([ns, np.log(ns), np.ones_like(ns, dtype=float), 1.0 / ns])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return -float(coef[0]), -float(coef[1])


def axis_kernel_3d(m: float, nmax: int, N1: int = 8192, Nt: int = 256) -> np.ndarray:
    """High-accuracy h(n,0,0) on Z^3: FFT in p_1, spectral trapezoid in (p_2,p_3).

    Trapezoid quadrature of a smooth periodic integrand is spectrally
    accurate, so the axis values are good to near machine precision in
    absolute terms (the 128^3 FFT block is kept for the full-block bound
    checks; this routine extends the resolvable axis window).
    """
    p1 = 2.0 * np.pi * np.arange(N1) / N1
    pt = 2.0 * np.pi * np.arange(Nt) / Nt
    s2 = np.sin(pt) ** 2
    acc = np.zeros(nmax + 1)
    sin2_p1 = np.sin(p1)[:, None] ** 2
    for i in range(Nt):
        w = m * m + s2[i] + s2[None, :] + sin2_p1
        h1 = np.fft.ifft(np.arcsinh(np.sqrt(w)), axis=0).real
        acc += h1[: nmax + 1, :].sum(axis=1)
    return acc / Nt**2


FLOOR = 1e-12  # numerically-resolvable threshold for pointwise bound checks


def resolvable_nmax(C: float, eta: float) -> int:
    """Largest n with C e^{-eta n} >= FLOOR (window where the pointwise
    bound is testable above double-precision FFT noise ~1e-16)."""
    return int(np.floor(np.log(C / FLOOR) / eta))


# ----------------------------------------------------------------------------
# T1 [B] cross-note symbol anchor: the action-derived 2-step classical
# transfer matrix T_odd . T_even (construction of the in-repo
# two-step RP note, Steps 1-3) has decaying eigenvalue exactly e^{-2E(p)}.
# ----------------------------------------------------------------------------

def test_T1_symbol_anchor() -> None:
    print("T1 — cross-note anchor: action-derived T_odd.T_even decaying eigenvalue")
    worst = 0.0
    for m in (0.3, 0.5, 1.0):
        ps = np.linspace(-np.pi, np.pi, 1001)
        for p in ps:
            a_even = m + 1j * np.sin(p)
            a_odd = m - 1j * np.sin(p)
            T_even = np.array([[-2 * a_even, 1.0], [1.0, 0.0]])
            T_odd = np.array([[-2 * a_odd, 1.0], [1.0, 0.0]])
            lam = np.linalg.eigvals(T_odd @ T_even)
            lam_min = lam[np.argmin(np.abs(lam))]
            resid = abs(lam_min - np.exp(-2.0 * dispersion(m, p)))
            worst = max(worst, resid)
    check("T1 [B] decaying eigenvalue of T_odd.T_even equals e^{-2E(p)} over the BZ "
          "(m in {0.3, 0.5, 1.0})", worst < 1e-10, f"max residual {worst:.2e}")


# ----------------------------------------------------------------------------
# T2/T3 [A] the strip inequalities behind (Q1): on |Im p_1| <= eta < eta*,
# Re(radicand) >= m^2 - sinh^2 eta > 0 and |E| <= C_d(eta, m).
# ----------------------------------------------------------------------------

def test_T2_T3_strip_bounds() -> None:
    print("T2/T3 — strip positivity and sup bound for the complexified symbol")
    ok_pos, ok_sup = True, True
    detail_pos, detail_sup = [], []
    for (m, d) in ((0.3, 1), (1.0, 1), (0.3, 3), (0.6, 3)):
        est = eta_star(m)
        for frac in (0.3, 0.6, 0.9, 0.99):
            eta = frac * est
            pr = np.linspace(-np.pi, np.pi, 41)
            if d == 1:
                grids = [pr[:, None] + 1j * np.array([eta, -eta])[None, :]]
                w = m * m + np.sin(grids[0]) ** 2
            else:
                P1 = (pr[:, None, None] + 1j * eta)
                P2 = pr[None, :, None]
                P3 = pr[None, None, :]
                w = m * m + np.sin(P1) ** 2 + np.sin(P2) ** 2 + np.sin(P3) ** 2
            floor = m * m - np.sinh(eta) ** 2
            min_re = float(np.min(w.real))
            if not (min_re >= floor - 1e-12 and floor > 0):
                ok_pos = False
            E = np.arcsinh(np.sqrt(w))
            sup_E = float(np.max(np.abs(E)))
            Cd = C_strip(eta, m, d)
            if not (sup_E <= Cd + 1e-12):
                ok_sup = False
            if frac == 0.99:
                detail_pos.append(f"d={d},m={m}: min Re w={min_re:.4f} >= {floor:.4f}")
                detail_sup.append(f"d={d},m={m}: sup|E|={sup_E:.4f} <= C={Cd:.4f}")
    check("T2 [A] Re(radicand) >= m^2 - sinh^2(eta) > 0 on the shifted strip "
          "(d in {1,3}, eta up to 0.99 eta*)", ok_pos, "; ".join(detail_pos))
    check("T3 [A] sup_strip |E| <= C_d(eta,m) = sqrt(m^2 + (d-1) + cosh^2 eta)",
          ok_sup, "; ".join(detail_sup))


# ----------------------------------------------------------------------------
# T4/T5 [C] d = 1 kernel: derived bound holds; measured rate = arcsinh(m).
# ----------------------------------------------------------------------------

def test_T4_T5_kernel_1d() -> None:
    print("T4/T5 — d=1 kernel decay: derived bound and sharp rate")
    ok_bound, ok_rate = True, True
    details_b, details_r = [], []
    windows = {0.1: (60, 200), 0.3: (30, 80), 0.5: (20, 50), 1.0: (10, 30)}
    for m in (0.1, 0.3, 0.5, 1.0):
        est = eta_star(m)
        eta = 0.95 * est
        C = C_strip(eta, m, 1)
        h = kernel_1d(m)
        nmax = resolvable_nmax(C, eta)
        ns = np.arange(1, nmax + 1)
        bound = C * np.exp(-eta * ns)
        margin = float(np.max(np.abs(h[1:nmax + 1]) / bound))
        if margin > 1.0:
            ok_bound = False
        lo, hi = windows[m]
        ev = np.arange(lo + lo % 2, hi + 1, 2)
        rate, beta = fit_rate_with_log_prefactor(ev.astype(float), h[ev])
        rel = abs(rate - est) / est
        if rel > 0.02:
            ok_rate = False
        details_b.append(f"m={m}: max ratio {margin:.3f} over n <= {nmax}")
        details_r.append(f"m={m}: rate {rate:.4f} vs arcsinh(m)={est:.4f} "
                         f"({100*rel:.2f}%, prefactor exp {beta:.2f})")
    check("T4 [C] |h(n)| <= C_1(eta,m) e^{-eta n} at eta = 0.95 arcsinh(m), "
          "m in {0.1,0.3,0.5,1.0}, over the numerically resolvable window",
          ok_bound, "; ".join(details_b))
    check("T5 [C] measured d=1 decay rate equals arcsinh(m) within 2% "
          "(log-prefactor fit)", ok_rate, "; ".join(details_r))


# ----------------------------------------------------------------------------
# T6 [A] sharpness mechanism: E'(p) blows up at the branch point
# p* = i arcsinh(m); closed form vs finite differences; divergent growth.
# No exponential rate faster than eta* is possible.
# ----------------------------------------------------------------------------

def test_T6_branch_point() -> None:
    print("T6 — branch-point obstruction: |E'(i theta)| diverges as theta -> arcsinh(m)")
    m = 0.3
    est = eta_star(m)

    def dE_closed(theta: float) -> complex:
        w = m * m - np.sinh(theta) ** 2
        return 1j * np.sinh(theta) * np.cosh(theta) / (np.sqrt(w) * np.sqrt(1.0 + w))

    def E_at(pc: complex) -> complex:
        return complex(np.arcsinh(np.sqrt(m * m + np.sin(pc) ** 2)))

    ok = True
    mags = []
    for frac in (0.9, 0.99, 0.999):
        theta = frac * est
        eps = 1e-7
        fd = (E_at(1j * (theta + eps)) - E_at(1j * (theta - eps))) / (2j * eps)
        cf = dE_closed(theta)
        if abs(fd - cf) / abs(cf) > 1e-4:
            ok = False
        mags.append(abs(cf))
    growth = mags[-1] / mags[0]
    check("T6 [A] closed-form E'(i theta) matches finite differences and grows "
          "without bound toward theta = arcsinh(m)",
          ok and growth > 5.0,
          f"|E'| = {mags[0]:.3f} -> {mags[1]:.3f} -> {mags[2]:.3f} "
          f"(growth x{growth:.1f}); no faster exponential rate is available")


# ----------------------------------------------------------------------------
# T7/T8 [C] d = 3 kernel on Z^3 blocks: derived l_inf bound; sharp axis rate.
# ----------------------------------------------------------------------------

def test_T7_T8_kernel_3d(h3_by_m: dict) -> None:
    print("T7/T8 — d=3 (Z^3) kernel decay: derived bound and sharp axis rate")
    ok_bound, ok_rate = True, True
    details_b, details_r = [], []
    for m in (0.3, 0.6):
        est = eta_star(m)
        eta = 0.9 * est
        C = C_strip(eta, m, 3)
        h = h3_by_m[m]
        N = h.shape[0]
        idx = np.arange(N)
        off = np.minimum(idx, N - idx)
        Z1, Z2, Z3 = np.meshgrid(off, off, off, indexing="ij", sparse=True)
        linf = np.maximum(np.maximum(Z1, Z2), Z3)
        sel = (linf <= 40) & (linf >= 1)
        margin = float(np.max(np.abs(h[sel]) / (C * np.exp(-eta * linf[sel]))))
        if margin > 1.0:
            ok_bound = False
        lo, hi = (20, 60) if m == 0.3 else (10, 36)
        ax = axis_kernel_3d(m, hi)
        ev = np.arange(lo, hi + 1, 2)
        rate, beta = fit_rate_4param(ev.astype(float), ax[ev])
        rel = abs(rate - est) / est
        if rel > 0.03:
            ok_rate = False
        details_b.append(f"m={m}: max ratio {margin:.3f} over ||z||_inf <= 40")
        details_r.append(f"m={m}: axis rate {rate:.4f} vs arcsinh(m)={est:.4f} "
                         f"({100*rel:.2f}%)")
    check("T7 [C] |h(z)| <= C_3(eta,m) e^{-eta ||z||_inf} at eta = 0.9 arcsinh(m) "
          "on the Z^3 block (m in {0.3, 0.6})", ok_bound, "; ".join(details_b))
    check("T8 [C] measured Z^3 axis decay rate equals arcsinh(m) within 3% "
          "(spectral transverse quadrature, 4-parameter asymptotic fit)",
          ok_rate, "; ".join(details_r))


# ----------------------------------------------------------------------------
# T9 [A] parity: the two-step symbol is pi-periodic per axis, so h(z) is
# supported on all-even z (the blocked H hops on the even sublattice).
# T10 [C] NOT finite-range: nonzero coefficients at l1-range 4 (the strict
# R <= 2 reading of the bridge note's (F5) hypothesis fails on this sector).
# ----------------------------------------------------------------------------

def test_T9_T10_parity_and_range(h3_by_m: dict) -> None:
    print("T9/T10 — even-sublattice parity; exact H is not finite-range")
    m = 0.3
    h1 = kernel_1d(m)
    odd_1d = float(np.max(np.abs(h1[1:h1.size // 2:2])))
    h3 = h3_by_m[m]
    N = h3.shape[0]
    idx = np.arange(N)
    par = (idx % 2)
    P1, P2, P3 = np.meshgrid(par, par, par, indexing="ij", sparse=True)
    any_odd = (P1 + P2 + P3) > 0
    odd_3d = float(np.max(np.abs(h3[any_odd])))
    check("T9 [A] h(z) = 0 whenever any z_mu is odd (pi-periodic symbol; "
          "even-sublattice support)", max(odd_1d, odd_3d) < 1e-13,
          f"max |h| on odd offsets: {odd_1d:.1e} (d=1), {odd_3d:.1e} (d=3)")
    v400 = abs(float(h3[4, 0, 0]))
    v220 = abs(float(h3[2, 2, 0]))
    floor = 1e-13
    check("T10 [C] |h(4,0,0)| and |h(2,2,0)| are nonzero far above the numeric "
          "floor: the exact bilinear H has hopping range > 2, so no support-family "
          "decomposition with diameter <= 2 exists (strict (F5) form fails)",
          v400 > 1e-4 and v220 > 1e-4 and v400 > 1e6 * floor,
          f"|h(4,0,0)| = {v400:.3e}, |h(2,2,0)| = {v220:.3e}, floor ~ {floor:.0e}")


# ----------------------------------------------------------------------------
# T11/T12/T13 [C] support-family weights: W_H = ||h||_l1 finite; tail
# weights W_tail(R) below the derived shell bound with slope eta*; the
# single-particle truncation error ||h - h_R||_op <= W_tail(R), exponential.
# ----------------------------------------------------------------------------

def test_T11_T12_T13_weights(h3_by_m: dict) -> None:
    print("T11/T12/T13 — overlap weight, tail weights, truncation operator norm")
    m = 0.3
    est = eta_star(m)
    eta = 0.9 * est
    C = C_strip(eta, m, 3)
    h = h3_by_m[m]
    N = h.shape[0]
    idx = np.arange(N)
    off = np.minimum(idx, N - idx)
    Z1, Z2, Z3 = np.meshgrid(off, off, off, indexing="ij", sparse=True)
    linf = np.maximum(np.maximum(Z1, Z2), Z3)
    absh = np.abs(h)
    # W_H partial sums over ||z||_inf <= r  (alias-clean region r <= 40)
    radii = np.arange(0, 41)
    partial = np.array([float(absh[linf <= r].sum()) for r in radii])
    incr_last = partial[-1] - partial[-7]
    W_H = partial[-1]
    check("T11 [C] per-site overlap weight W_H = ||h||_l1 is finite "
          "(partial sums Cauchy)", incr_last < 1e-6 and np.isfinite(W_H),
          f"W_H = {W_H:.6f} at m=0.3 (last 6-shell increment {incr_last:.1e})")
    # tail weights vs derived shell-sum bound:
    #   W_tail(R) <= C * sum_{r>R} [(2r+1)^3 - (2r-1)^3] e^{-eta r}
    ok_tail, ok_slope = True, True
    Rs = np.arange(2, 30, 2)
    tails = np.array([float(absh[linf > R].sum()) - float(absh[linf > 40].sum())
                      for R in Rs])
    rr = np.arange(1, 200)
    shell = (2 * rr + 1) ** 3 - (2 * rr - 1) ** 3
    for R, t in zip(Rs, tails):
        # derived shell-sum bound: C * sum_{r > R} [(2r+1)^3 - (2r-1)^3] e^{-eta r}
        bound = C * float((shell[R:] * np.exp(-eta * rr[R:])).sum())
        if t > bound:
            ok_tail = False
    slope, _ = fit_rate_with_log_prefactor(Rs[4:].astype(float), tails[4:])
    if abs(slope - est) / est > 0.10:
        ok_slope = False
    check("T12 [C] tail weights W_tail(R) lie below the derived shell-sum bound "
          "and decay at the sharp rate", ok_tail and ok_slope,
          f"m=0.3: W_tail(10) = {tails[Rs == 10][0]:.3e}, measured slope "
          f"{slope:.4f} vs arcsinh(m) = {est:.4f}")
    # single-particle truncation error on a d=1 ring (exact circulant norm)
    h1 = kernel_1d(m)
    N1 = h1.size
    ks = np.linspace(-np.pi, np.pi, 4001)
    E_exact = dispersion(m, ks)
    ok_op, ok_exp = True, True
    norms = []
    Rs1 = np.arange(4, 65, 4)
    for R in Rs1:
        n_in = np.arange(1, R + 1)
        E_R = h1[0] + 2.0 * np.sum(h1[n_in][:, None] * np.cos(np.outer(n_in, ks)), axis=0)
        opnorm = float(np.max(np.abs(E_exact - E_R)))
        wtail = float(2.0 * np.abs(h1[R + 1:N1 // 2]).sum())
        if opnorm > wtail + 1e-14:
            ok_op = False
        norms.append(opnorm)
    norms = np.array(norms)
    sl, _ = fit_rate_with_log_prefactor(Rs1[2:12].astype(float), norms[2:12])
    if abs(sl - est) / est > 0.10:
        ok_exp = False
    check("T13 [C] single-particle truncation ||h - h_R||_op <= W_tail(R) and "
          "decays exponentially at the sharp rate", ok_op and ok_exp,
          f"m=0.3: ||h-h_R||_op at R=20: {norms[Rs1 == 20][0]:.3e}, "
          f"slope {sl:.4f} vs {est:.4f}")


# ----------------------------------------------------------------------------
# T14 [A] a_tau enters only as the overall 1/a_tau scale: rates unchanged.
# ----------------------------------------------------------------------------

def test_T14_atau_scaling() -> None:
    print("T14 — a_tau dependence: pure 1/a_tau amplitude scale, rate unchanged")
    m = 0.3
    h = kernel_1d(m)
    ok = True
    details = []
    for a_tau in (0.5, 1.0, 2.0):
        h_a = h / a_tau
        ev = np.arange(30, 81, 2)
        rate, _ = fit_rate_with_log_prefactor(ev.astype(float), h_a[ev])
        scale_err = float(np.max(np.abs(h_a * a_tau - h)))
        if scale_err > 1e-15 or abs(rate - eta_star(m)) / eta_star(m) > 0.02:
            ok = False
        details.append(f"a_tau={a_tau}: rate {rate:.4f}")
    check("T14 [A] kernel = (1/a_tau) x (a_tau-independent kernel); decay rate "
          "identical for a_tau in {0.5, 1, 2}", ok, "; ".join(details))


# ----------------------------------------------------------------------------
# T15/T16 [C] falsification legs.
# ----------------------------------------------------------------------------

def test_T15_gapless_boundary() -> None:
    print("T15 — falsification: m = 0 closes the strip; kernel is power-law")
    N = 8192
    p = 2.0 * np.pi * np.arange(N) / N
    h = np.fft.ifft(np.arcsinh(np.abs(np.sin(p)))).real
    ev = np.arange(20, 401, 2)
    vals = np.abs(h[ev])
    # power-law fit: log|h| vs log n
    A = np.column_stack([np.log(ev.astype(float)), np.ones(ev.size)])
    coef, res, *_ = np.linalg.lstsq(A, np.log(vals), rcond=None)
    pred = A @ coef
    ss_res = float(np.sum((np.log(vals) - pred) ** 2))
    ss_tot = float(np.sum((np.log(vals) - np.mean(np.log(vals))) ** 2))
    r2 = 1.0 - ss_res / ss_tot
    # exponential rate fit on the same window
    rate, _ = fit_rate_with_log_prefactor(ev.astype(float), h[ev])
    # any positive-rate exponential bound is violated at large n
    eta_try = 0.05
    viol = float(np.max(vals / (C_strip(eta_try, 0.0, 1) * np.exp(-eta_try * ev))))
    check("T15 [C] at m = 0 the kernel is power-law (exp rate ~ 0; power fit "
          "R^2 > 0.999; the eta = 0.05 exponential bound is violated): the mass "
          "gap is load-bearing",
          abs(coef[0] + 2.0) < 0.05 and r2 > 0.999 and abs(rate) < 5e-3 and viol > 1e3,
          f"power {coef[0]:.3f} (~ -2), R^2 = {r2:.5f}, exp-rate {rate:.4f}, "
          f"bound violation x{viol:.1e}")


def test_T16_long_range_countermodel() -> None:
    print("T16 — falsification: long-range-perturbed positive symbol breaks the bound")
    m, eps = 0.5, 0.05
    est = eta_star(m)
    N = 8192
    p = 2.0 * np.pi * np.arange(N) / N
    E = dispersion(m, p)
    g = np.zeros_like(p)
    for k in range(1, 301):
        g += (k ** -3.0) * np.cos(2.0 * k * p)
    E_pert = E + eps * g
    gap = float(np.min(E_pert))
    h_pert = np.fft.ifft(E_pert).real
    eta = 0.95 * est
    C = C_strip(eta, m, 1)
    nmax = resolvable_nmax(C, eta)
    ns = np.arange(10, nmax + 1, 2)
    viol = float(np.max(np.abs(h_pert[ns]) / (C * np.exp(-eta * ns))))
    # same check on the unperturbed kernel stays inside the bound
    h0 = np.fft.ifft(E).real
    ok0 = float(np.max(np.abs(h0[ns]) / (C * np.exp(-eta * ns))))
    check("T16 [C] a positive, gapped, long-range-perturbed symbol (eps k^-3 "
          "cosine tail) VIOLATES the derived exponential bound that the framework "
          "kernel satisfies: analyticity is load-bearing and the check has teeth",
          gap > 0.4 and viol > 50.0 and ok0 <= 1.0,
          f"perturbed symbol gap {gap:.3f} > 0; bound violation x{viol:.2e} on "
          f"the resolvable window n <= {nmax}; unperturbed max ratio {ok0:.3f} <= 1")


# ----------------------------------------------------------------------------
# T17 [A/C] Step 1 contour-shift orientation. For the e^{+i p z} convention
# of (2), shifting to Im p = +eta*sgn(z) (a) leaves the integral unchanged
# (strip analyticity + 2pi-periodicity) and (b) carries the decay factor
# |e^{i p z}| = e^{-eta|z|}; the opposite orientation -eta*sgn(z) carries
# e^{+eta|z|} (growth) and cannot produce bound (3). This witnesses the
# 2026-07-01 repair of the Step 1 shift direction.
# ----------------------------------------------------------------------------

def test_T17_contour_orientation() -> None:
    print("T17 — Step 1 contour orientation: +eta*sgn(z) decays; -eta*sgn(z) grows")
    m = 0.3
    est = eta_star(m)
    eta = 0.8 * est
    N = 8192
    a = 2.0 * np.pi * np.arange(N) / N  # periodic uniform grid, no dup endpoint
    ok_id, ok_decay, ok_growth = True, True, True
    details = []
    for z in (3, -4, 7):
        sz = 1.0 if z > 0 else -1.0
        # real-axis kernel value (normalized measure, a_tau = 1)
        h_real = complex(np.mean(dispersion(m, a) * np.exp(1j * a * z)))
        # shifted contour Im p = +eta*sgn(z): identity + decay factor
        p_plus = a + 1j * eta * sz
        E_plus = np.arcsinh(np.sqrt(m * m + np.sin(p_plus) ** 2))
        h_plus = complex(np.mean(E_plus * np.exp(1j * p_plus * z)))
        if abs(h_plus - h_real) > 1e-10 * max(1.0, abs(h_real)):
            ok_id = False
        mod_plus = np.abs(np.exp(1j * p_plus * z))
        if not np.allclose(mod_plus, np.exp(-eta * abs(z)), rtol=1e-12):
            ok_decay = False
        # pre-repair orientation Im p = -eta*sgn(z): growth factor
        p_minus = a - 1j * eta * sz
        mod_minus = np.abs(np.exp(1j * p_minus * z))
        if not np.allclose(mod_minus, np.exp(+eta * abs(z)), rtol=1e-12):
            ok_growth = False
        details.append(f"z={z:+d}: |h_shift - h_real| = {abs(h_plus - h_real):.1e}")
    check("T17a [A] shifted-contour integral at Im p = +eta*sgn(z) equals the "
          "real-axis kernel (periodicity + strip analyticity)", ok_id,
          "; ".join(details))
    check("T17b [A] on the +eta*sgn(z) contour |e^{i p z}| = e^{-eta|z|} exactly: "
          "the decaying orientation for the e^{+i p z} convention of (2)",
          ok_decay, f"m = {m}, eta = {eta:.4f} = 0.8 eta*")
    check("T17c [C] the opposite orientation -eta*sgn(z) carries |e^{i p z}| = "
          "e^{+eta|z|} (growth): the pre-repair shift direction cannot yield (3)",
          ok_growth, f"growth factor at |z| = 7: x{np.exp(eta * 7):.1f}")


# ----------------------------------------------------------------------------

def main() -> None:
    print()
    print("=" * 72)
    print("TRANSFER-MATRIX LOG QUASILOCALITY — BILINEAR-SECTOR NARROW THEOREM RUNNER")
    print("=" * 72)
    print()
    print("Companion: docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md")
    print("Object: H = -log(T_hat^2)/(2 a_tau) for the free staggered")
    print("two-step transfer matrix; symbol E(p) = arcsinh sqrt(m^2 + sum sin^2 p_mu).")
    print("Claims verified: derived bound |h(z)| <= C_d(eta,m) e^{-eta ||z||_inf} for")
    print("every eta < arcsinh(m); sharp rate eta* = arcsinh(m); finite overlap weight")
    print("W_H = ||h||_l1; exponential tail weights; exact H not finite-range.")
    print()

    print("Precomputing Z^3 kernels (128^3 FFT, m in {0.3, 0.6}) ...")
    h3_by_m = {m: kernel_3d(m) for m in (0.3, 0.6)}
    print()

    test_T1_symbol_anchor()
    test_T2_T3_strip_bounds()
    test_T4_T5_kernel_1d()
    test_T6_branch_point()
    test_T7_T8_kernel_3d(h3_by_m)
    test_T9_T10_parity_and_range(h3_by_m)
    test_T11_T12_T13_weights(h3_by_m)
    test_T14_atau_scaling()
    test_T15_gapless_boundary()
    test_T16_long_range_countermodel()
    test_T17_contour_orientation()

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("  Scope: free (U=1) staggered bilinear two-step sector only; d=1 is the")
    print("  in-repo anchor, the Z^3 symbol is the declared d=3")
    print("  carrier of the same construction. Gauged/interacting T remains open.")
    print(f"  TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"  OVERALL: {'PASS' if FAIL_COUNT == 0 else 'FAIL'}")
    print()
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
