#!/usr/bin/env python3
"""Reduced Gaussian Maxwell comparator and historical fit arithmetic.
Supplied model only. See the bound note for exact hypotheses, estimator biases and historical-input limits.
Numerical PASS thresholds are finite diagnostic checks, not phase or convergence certificates.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import numpy as np

AUDIT_TIMEOUT_SEC = 600          # top-level integer; the cache header repeats it
AUDIT_INPUT_PATHS = ['docs/GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md']

RESULTS = []


def below(x, tol):
    """Print a defect as 'below tolerance' rather than as noise digits."""
    return f"<{tol:g}" if x < tol else f"{x:.1e}"


def check(label, ok, detail=""):
    # Labels describe finite diagnostics; limits in the source note govern interpretation.
    label = "finite diagnostic: " + label
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


# ----------------------------------------------------------------------------------------------------------------
# Lattice geometry: vertices x in Z_L^3, links (x, a), plaquettes (x, a<b) with circulation
# +sigma(x,a) + sigma(x+a,b) - sigma(x+b,a) - sigma(x,b); divergence div(x) = sum_a sigma(x,a) - sigma(x-a,a).
# ----------------------------------------------------------------------------------------------------------------
def geometry(L):
    N = L ** 3
    xs = np.array(list(np.ndindex(L, L, L)))                       # (N, 3)

    def v(x):
        x = np.mod(x, L)
        return x[..., 0] * L * L + x[..., 1] * L + x[..., 2]

    def link(x, a):
        return 3 * v(x) + a

    D = np.zeros((N, 3 * N), dtype=int)
    for a in range(3):
        ea = np.eye(3, dtype=int)[a]
        D[np.arange(N), link(xs, a)] += 1
        D[np.arange(N), link(xs - ea, a)] -= 1
    planes = [(0, 1), (0, 2), (1, 2)]
    C = np.zeros((3 * N, 3 * N), dtype=int)
    plane_of = np.zeros(3 * N, dtype=int)
    for pi, (a, b) in enumerate(planes):
        ea, eb = np.eye(3, dtype=int)[a], np.eye(3, dtype=int)[b]
        rows = 3 * np.arange(N) + pi
        plane_of[rows] = pi
        C[rows, link(xs, a)] += 1
        C[rows, link(xs + ea, b)] += 1
        C[rows, link(xs + eb, a)] -= 1
        C[rows, link(xs, b)] -= 1
    return N, xs, D, C, plane_of


def momenta(L):
    ms = np.array(list(np.ndindex(L, L, L)))
    return 2 * np.pi * ms / L                                          # (N, 3)


def s_abs(k):
    return np.sqrt(np.sum(2 - 2 * np.cos(k), axis=-1))


def fourier_cov(Sigma, L, xs, ks):
    """S_ab(k) = N^{-1} sum_{x,y} e^{ik(x-y)} Sigma[(x,a),(y,b)] for every k."""
    N = L ** 3
    Phi = np.exp(1j * ks @ xs.T)                                       # (N_k, N)
    S = np.zeros((len(ks), 3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            blk = Sigma[a::3, b::3]                                    # (x, y) block for (a, b)
            S[:, a, b] = np.einsum("kx,kx->k", Phi @ blk, Phi.conj()) / N
    return S


def closed_form(ks, A):
    """A |s(k)| (1 - g g^dag), g_a = (1 - e^{-i k_a})/|s|; zero at k = 0."""
    out = np.zeros((len(ks), 3, 3), dtype=complex)
    sa = s_abs(ks)
    for i, k in enumerate(ks):
        if sa[i] < 1e-12:
            continue
        g = (1 - np.exp(-1j * k)) / sa[i]
        out[i] = A * sa[i] * (np.eye(3) - np.outer(g, g.conj()))
    return out


# ---------------------------------------------------------------- check 1: lattice Maxwell on 4^3 and 6^3 tori
U, K = 1.7, 1.2                                                        # generic couplings for the structural check
A_G = np.sqrt(K / U) / 2
ST_pi2 = {}
ok1, det1 = True, []
for L in (4, 8):
    N, xs, D, C, plane_of = geometry(L)
    ks = momenta(L)
    dc = np.abs(D @ C.T).max()
    M = (C.T @ C).astype(float)
    w, V = np.linalg.eigh(M)
    nz = w > 1e-9
    spec = np.sort(w[nz])
    target = np.sort(np.repeat(s_abs(ks)[1:] ** 2, 2))                 # k != 0, two polarisations each
    spec_ok = len(spec) == len(target) and np.abs(spec - target).max() < 1e-9 and int((~nz).sum()) == N + 2
    Sigma = (V[:, nz] * np.sqrt(w[nz])) @ V[:, nz].T * A_G             # (1/2) sqrt(K/U) (C^T C)^{1/2}
    gauss = np.abs(D @ Sigma).max()                                    # every column is divergence free
    S = fourier_cov(Sigma, L, xs, ks)
    dev = np.abs(S - closed_form(ks, A_G)).max()
    zero0 = np.abs(S[0]).max()
    # on-axis k = pi/2 along axis 0: transverse polarisations are exactly axes 1 and 2
    i_ax = int(np.where(np.isclose(ks[:, 0], np.pi / 2) & (ks[:, 1] == 0) & (ks[:, 2] == 0))[0][0])
    Sk = S[i_ax]
    ST_pi2[L] = float(np.real(Sk[1, 1] + Sk[2, 2]) / 2)
    onaxis_ok = abs(Sk[0, 0]) < 1e-12 and abs(Sk[1, 1] - Sk[2, 2]) < 1e-12 and abs(Sk[1, 2]) < 1e-12
    trace_ok = abs(np.trace(Sigma) - A_G * 2 * s_abs(ks)[1:].sum()) < 1e-9
    ok1 &= (dc == 0) and spec_ok and gauss < 1e-9 and dev < 1e-9 and zero0 < 1e-12 and onaxis_ok and trace_ok
    det1.append(f"L={L}: |D C^T|max={dc}, kernel dim {int((~nz).sum())}=N+2, spectrum vs {{|s|^2 x2}} dev "
                f"{'<1e-9' if spec_ok else 'FAIL'}, |D Sigma|max {below(gauss, 1e-9)}, "
                f"|S(k) - A|s|(1-gg^+)|max {below(dev, 1e-9)}, S(0) {below(zero0, 1e-12)}, "
                f"S_T(pi/2)={ST_pi2[L]:.6f}")
same = abs(ST_pi2[4] - ST_pi2[8]) < 1e-12
check("Gaussian lattice Maxwell on 4^3 and 8^3 tori: exact Gauss law, dispersion sqrt(UK)|s(k)|, covariance closed form "
      "A|s(k)|(1-gg^+), zero winding mode, on-axis polarisations, no size dependence at fixed k",
      ok1 and same,
      "; ".join(det1) + f"; closed form A|s(pi/2)|={A_G * np.sqrt(2):.6f}; S_T(pi/2) equal on both sizes: {same}")

# ---------------------------------------------------------------- check 2: spin-1/2 sum rule on sampled ice states
L = 4
N, xs, D, C, plane_of = geometry(L)
ks = momenta(L)
rng = np.random.default_rng(20260924)
sigma = np.zeros(3 * N, dtype=int)
for a in range(3):
    b, c = [i for i in range(3) if i != a]
    sigma[3 * np.arange(N) + a] = (-1) ** (xs[:, b] + xs[:, c])        # zero-winding ice state
assert np.abs(D @ sigma).max() == 0
Phi = np.exp(1j * ks @ xs.T) / np.sqrt(N)                               # O_a(k) = sum_x Phi[k, x] sigma(x, a)
gvec = 1 - np.exp(1j * ks)                                             # Fourier Gauss law: sum_a g_a O_a = 0
n_cfg, n_flip = 24, 400
worst = dict(div=0, wind=0, parseval=0.0, gauss=0.0, onaxis=0.0, flip=0.0, sumrule=0.0)
for _ in range(n_cfg):
    for _ in range(n_flip):
        circ = C @ sigma
        fl = np.where(np.abs(circ) == 4)[0]
        p = fl[rng.integers(len(fl))]
        sigma = sigma - C[p] * (circ[p] // 2)                          # flip the four links of plaquette p
    worst["div"] = max(worst["div"], int(np.abs(D @ sigma).max()))
    sig = sigma.reshape(N, 3)
    worst["wind"] = max(worst["wind"], int(np.abs(sig.sum(axis=0)).max()))
    O = Phi @ sig                                                      # (N_k, 3)
    worst["parseval"] = max(worst["parseval"], abs(np.sum(np.abs(O) ** 2) - 3 * N))
    worst["gauss"] = max(worst["gauss"], np.abs(np.sum(gvec * O, axis=1)).max())
    worst["sumrule"] = max(worst["sumrule"], abs(np.sum(np.abs(O[1:]) ** 2) / N - 3))
    # on-axis momenta: the longitudinal component is the axis component itself
    for ax in range(3):
        on = (ks[:, [i for i in range(3) if i != ax]] == 0).all(axis=1) & (ks[:, ax] != 0)
        worst["onaxis"] = max(worst["onaxis"], np.abs(O[on, ax]).max())
    # per-flip identity for k = pi/2 along axis 0 and a = 1: |Delta O|^2 = (4/N) s^2 on (0,1)-plaquettes, else 0
    ik = int(np.where((ks[:, 0] == np.pi / 2) & (ks[:, 1] == 0) & (ks[:, 2] == 0))[0][0])
    s2 = 2 - 2 * np.cos(np.pi / 2)
    circ = C @ sigma
    for p in np.where(np.abs(circ) == 4)[0]:
        dsig = -C[p] * (circ[p] // 2)
        dO = Phi[ik] @ dsig.reshape(N, 3)[:, 1]
        want = 4 * s2 / N if plane_of[p] == 0 else 0.0
        worst["flip"] = max(worst["flip"], abs(abs(dO) ** 2 - want))
ok2 = worst["div"] == 0 and worst["wind"] == 0 and all(worst[k] < 1e-10 for k in ("parseval", "gauss", "onaxis", "flip", "sumrule"))
check("spin-1/2 sum rule on sampled zero-winding ice states (4^3): Parseval 3N, Fourier Gauss law, on-axis longitudinal "
      "mode zero, zone sum of transverse weight = 3 exactly, per-flip |Delta O|^2 = (4/N) s^2 on (a,k)-plaquettes else 0",
      ok2, f"{n_cfg} states x {n_flip} flips; worst divergence {worst['div']}, winding {worst['wind']}, other defects "
           f"{'all <1e-10' if ok2 else worst}")

# ---------------------------------------------------------------- check 3: zone means and the sum-rule bound
u0 = {4: 0.2926, 6: 0.2889, 8: 0.2880, 10: 0.2880, 12: 0.2880}        # supplied energies per plaquette (8^3 value reused)
mL, Amax, Umin = {}, {}, {}
for L in (4, 6, 8, 10, 12):
    ks = momenta(L)
    mL[L] = float(s_abs(ks)[1:].sum() / L ** 3)
    Amax[L] = 3 / (2 * mL[L])
    Umin[L] = u0[L] / Amax[L] ** 2
m_inf = float(s_abs(momenta(60))[1:].sum() / 60 ** 3)
ok3 = all(2.0 < mL[L] < 2.5 for L in mL) and abs(mL[12] - m_inf) < 0.02
check("zone mean m_L = N^-1 sum_{k!=0} |s(k)| and the sum-rule bound A <= 3/(2 m_L), U >= u_0/A^2 for c >= 0", ok3,
      "; ".join(f"L={L}: m={mL[L]:.4f}, A_max={Amax[L]:.4f}, U_min={Umin[L]:.3f}" for L in mL) + f"; m(60^3)={m_inf:.4f}")

# ---------------------------------------------------------------- check 4: fits to today's numbers
# (L, k, S_T, sigma) -- primary 120-walker certified numbers; k < pi first, then the two zone-edge values
DATA6 = [(4, np.pi / 2, 0.692, 0.013), (6, np.pi / 3, 0.557, 0.022), (8, np.pi / 4, 0.575, 0.028),
         (8, np.pi / 2, 0.833, 0.040), (8, 3 * np.pi / 4, 1.019, 0.085), (6, 2 * np.pi / 3, 0.98, 0.05)]
EDGE = [(6, np.pi, 1.16, 0.03), (4, np.pi, 1.19, 0.04)]
AUX = [(8, np.pi / 4, 0.541, 0.027), (8, np.pi / 2, 0.751, 0.018)]  # 240 walkers


def wls(data, fix_c=None):
    x = np.array([2 * abs(np.sin(k / 2)) for _, k, _, _ in data])
    y = np.array([S for _, _, S, _ in data])
    w = 1 / np.array([e for _, _, _, e in data]) ** 2
    if fix_c is None:
        X = np.column_stack([np.ones_like(x), x])
    else:
        X = x[:, None]
        y = y - fix_c
    cov = np.linalg.inv(X.T @ (w[:, None] * X))
    beta = cov @ X.T @ (w * y)
    res = (y - X @ beta) * np.sqrt(w)
    if fix_c is not None:
        beta, cov = np.array([fix_c, beta[0]]), np.array([[0, 0], [0, cov[0, 0]]])
    return beta, np.sqrt(np.diag(cov)), res, float(np.sum(res ** 2)), len(data) - X.shape[1]


fits = {}
for name, data, fix in (("six k<pi", DATA6, None), ("all eight", DATA6 + EDGE, None), ("8^3 zone", DATA6[2:5], None),
                        ("pure Gaussian c=0, six", DATA6, 0.0)):
    beta, err, res, chi2, dof = wls(data, fix)
    fits[name] = (beta, err, res, chi2, dof)
lines4 = []
for name, (beta, err, res, chi2, dof) in fits.items():
    c, A = beta
    Uf = u0[8] / A ** 2 if A > 0 else float("nan")
    lines4.append(f"{name}: c={c:.3f}+-{err[0]:.3f}, A={A:.3f}+-{err[1]:.3f}, U=u_0/A^2={Uf:.2f}, chi2/dof={chi2:.1f}/{dof}, "
                  f"residuals(sigma)=[{', '.join(f'{r:+.1f}' for r in res)}]")
# quotient consistency of the inputs
qs = [2 * u0[L] * (2 - 2 * np.cos(k)) / S for L, k, S, _ in DATA6[:3]]
q_ok = np.allclose(qs, [1.690, 1.037, 0.587], atol=0.002)
# the level step 6^3 -> 8^3 at k_min against any Gaussian with the 8^3 slope
(_, A8), (_, dA8), *_ = fits["8^3 zone"]
dS = DATA6[1][2] - DATA6[2][2]
dS_err = np.hypot(DATA6[1][3], DATA6[2][3])
ds = 2 * abs(np.sin(np.pi / 6)) - 2 * abs(np.sin(np.pi / 8))
A_level = dS / ds
A_level_err = dS_err / ds
tension = (A8 * ds - dS) / np.hypot(dA8 * ds, dS_err)
(_, A6), (_, dA6), res6, chi6, dof6 = fits["six k<pi"]
tension6 = (A6 * ds - dS) / np.hypot(dA6 * ds, dS_err)
UL = {L: u0[L] / (S / (2 * abs(np.sin(k / 2)))) ** 2 for L, k, S, _ in DATA6[:3]}
ok4 = q_ok and chi6 > 4 * dof6 and tension > 2.5 and fits["pure Gaussian c=0, six"][3] > 4 * fits["pure Gaussian c=0, six"][4]
check("weighted fits S_T = c + A|s(k)| with no size dependence: stored six-input weighted residual statistic (chi2/dof > 4), and the "
      "6^3 -> 8^3 level step at k_min contradicts the 8^3 slope", ok4,
      "; ".join(lines4) + f"; inputs' quotients 2u_0 s^2/S_T = {qs[0]:.3f}, {qs[1]:.3f}, {qs[2]:.3f}; "
      f"level step dS(6->8)={dS:+.3f}+-{dS_err:.3f} needs A_level={A_level:+.2f}+-{A_level_err:.2f}, vs A(8^3 zone)={A8:.2f}+-{dA8:.2f}: "
      f"{tension:.1f} sigma, vs A(six)={A6:.2f}+-{dA6:.2f}: {tension6:.1f} sigma; pure Gaussian per size from S_T(k_min): "
      + ", ".join(f"U({L}^3)={UL[L]:.2f}" for L in UL))

# ---------------------------------------------------------------- check 5: pinch-point constant from K_cont
pp = {L: 3 * L ** 3 / (2 * L ** 3 + 1) for L in (4, 6, 8)}
meas = {4: 1.51, 6: 1.53, 8: 1.50}
# the landed identity sum_{k!=0} P_zz = 2(N-1)/3 with P_zz = 1 - s_z^2/s^2
ident = []
for L in (4, 6, 8):
    ks = momenta(L)[1:]
    Pzz = 1 - (2 - 2 * np.cos(ks[:, 2])) / s_abs(ks) ** 2
    ident.append(abs(Pzz.sum() - 2 * (L ** 3 - 1) / 3))
ok5 = max(ident) < 1e-9 and all(abs(pp[L] - meas[L]) < 0.05 for L in pp) and all(abs(pp[L] - 1.5) < 0.012 for L in pp)
check("classical pinch-point constant 1/K_cont = 3N/(2N+1) (unit variance with a continuous zero mode) against 1.5 and the "
      "uniform-ice inputs", ok5,
      "; ".join(f"L={L}: {pp[L]:.4f} vs input {meas[L]:.2f}" for L in pp) + f"; identity sum P_zz = 2(N-1)/3 defect "
      f"{below(max(ident), 1e-9)}; limit 1.5")

# ---------------------------------------------------------------- check 6: predictions for 10^3 and 12^3
S8, e8 = DATA6[2][2], DATA6[2][3]
s8 = 2 * np.sin(np.pi / 8)
c6, A6 = fits["six k<pi"][0]
pred = {}
for L in (10, 12):
    s = 2 * np.sin(np.pi / L)                                          # |s(k_min)|, k_min = 2 pi / L
    pred[L] = dict(linear_fit=c6 + A6 * s, pure_through_8=S8 * s / s8, pure_sum_rule=Amax[L] * s,
                   level=S8, quadratic=S8 * (s / s8) ** 2)
    pred[L]["sep_level_linear_sigma"] = (pred[L]["level"] - pred[L]["linear_fit"]) / 0.03
    pred[L]["quot_level"] = 2 * u0[L] * s ** 2 / pred[L]["level"]
    pred[L]["quot_linear"] = 2 * u0[L] * s ** 2 / pred[L]["linear_fit"]
ok6 = all(p["level"] > max(p["linear_fit"], p["pure_through_8"]) > p["pure_sum_rule"] > p["quadratic"] > 0 for p in pred.values()) \
    and pred[12]["sep_level_linear_sigma"] > 3
check("10^3 and 12^3 predictions for S_T(k_min): affine-in-momentum and pure-linear ansatz, level residual, quadratic fall; nominal separation "
      "level vs linear at a 0.03 error exceeds 3 sigma at 12^3", ok6,
      "; ".join(f"L={L} (k_min=2pi/{L}, |s|={2 * np.sin(np.pi / L):.4f}): fit c+A|s|={p['linear_fit']:.3f}, pure through 8^3={p['pure_through_8']:.3f}, "
                f"pure sum-rule-saturating={p['pure_sum_rule']:.3f}, level={p['level']:.3f}, quadratic={p['quadratic']:.3f}; "
                f"level-linear={p['sep_level_linear_sigma']:.1f} sigma at 0.03; quotient 2u_0 s^2/S_T level {p['quot_level']:.3f} / linear {p['quot_linear']:.3f}"
                for L, p in pred.items()))

# ---------------------------------------------------------------- check 7: fixed-k growth and forward-walking factors
g1 = (DATA6[3][2] - DATA6[0][2]) / np.hypot(DATA6[3][3], DATA6[0][3])   # 8^3 (120 w) vs 4^3 at pi/2
g2 = (AUX[1][2] - DATA6[0][2]) / np.hypot(AUX[1][3], DATA6[0][3])        # 8^3 (240 w) vs 4^3
g3 = (DATA6[3][2] - AUX[1][2]) / np.hypot(DATA6[3][3], AUX[1][3])        # 120 vs 240 walkers at pi/2
g4 = (DATA6[2][2] - AUX[0][2]) / np.hypot(DATA6[2][3], AUX[0][3])        # 120 vs 240 walkers at k_min
rates = {4: (1.4, 1.6), 6: (0.8, 1.0), 8: (0.5, 0.6)}                    # supplied decay-rate windows of the k_min mode
tau_f = 4.0
fw = {L: (np.exp(-r[1] * tau_f), np.exp(-r[0] * tau_f), np.exp(-2 * r[1] * tau_f), np.exp(-2 * r[0] * tau_f)) for L, r in rates.items()}
s_min = {4: np.sqrt(2.0), 6: 1.0, 8: 2 * np.sin(np.pi / 8)}
v_win = {L: (rates[L][0] / s_min[L], rates[L][1] / s_min[L]) for L in rates}   # a Gaussian gives one constant sqrt(UK)
ok7 = 2.5 < g2 < g1 < 3.5 and g3 < 2 and fw[8][1] > 10 * fw[4][1] and v_win[8][1] < v_win[4][0]
check("fixed k = pi/2: historical S_T input differences in nominal error units while fixed-coupling reduced Gaussian gives zero difference; the 120- vs "
      "240-walker 8^3 runs differ by under 2 sigma; the decay rate per |s| falls with L where a Gaussian has one constant; "
      "forward-walking residual e^{-omega tau_f} at tau_f = 4 grows with L", ok7,
      "rate/|s| windows " + ", ".join(f"L={L}: [{v[0]:.2f}, {v[1]:.2f}]" for L, v in v_win.items()) + f"; 8^3(120w)-4^3: {g1:.2f} sigma; 8^3(240w)-4^3: {g2:.2f} sigma; 120w-240w at pi/2: {g3:.2f} sigma, at k_min: {g4:.2f} sigma; "
      + "; ".join(f"L={L}: e^-omega*4 in [{f[0]:.1e}, {f[1]:.1e}], e^-2omega*4 in [{f[2]:.1e}, {f[3]:.1e}]" for L, f in fw.items()))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
