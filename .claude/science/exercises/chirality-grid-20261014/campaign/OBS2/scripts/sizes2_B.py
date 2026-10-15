"""OBS-2 Part B: FLAV2 clock row. OBS-1 sizes.py lines 1-108 run unchanged (E_g, TW-2 estimator), then re-run with the
covariant hw2 condensate (tau_x sigma_c) E_g coefficients from obs1_copy/r1_offdiag_sz.py (offdiag_sz_N48.out).
T2g first-order response of spin-averaged masses = 0 (strain_*.out, offd_*.out; symmetry proof in REPORT), so the five-component
traceless rate equals the E_g rate."""
import sys
"""OBS-1 sizes: R1 clock/SME mapping of the one-loop strain coefficients (r1_*.out, N = 48, m0 = 0.1, Delta = 0.5 unless stated),
R2 Z4 arithmetic, R3 proton-decay floor. All observational inputs are cited in REPORT.md; SM inputs RECALLED (PDG-level)."""
import numpy as np, itertools
from fractions import Fraction as Fr
np.set_printoptions(precision=4, suppress=False)
P = print
# ---------------------------------------------------------------- one-loop inputs (per e^2, per unit SF strain t*h, h = e_a e_a)
C_par, C_perp = -5.595363e-02, -5.746359e-02             # on-site (cubic-singlet) corner mass, incl. wavefunction (r1_loop.out N=48)
dc_par, dc_perp = (-5.214448e-2 + 5.302730e-2) / 0.04, (-5.214326e-2 + 5.302851e-2) / 0.04   # wavefunction c at the corner (r1_loop.out)
own_par, own_perp = -2.469253e-02 + dc_par, -3.692209e-02 + dc_perp   # corner-selective symbol at its own corner (r1_own.out N=48) + c
lk_t, lk_s, lk_o = -7.673881e-03, -1.696664e-02, -8.686443e-03       # leak source s -> target t: strain along t / along s / third axis (r1_leak.out N=48)
off_in, off_n = 2.010493e-02, 2.071273e-02                           # off-diagonal (hw2-momentum) entry: strain in its plane / along its normal (r1_offdiag.out N=48)
P("one-loop inputs per e^2: C_par %.4e C_perp %.4e | own (incl c) par %.4e perp %.4e | leak t %.4e s %.4e o %.4e | off in %.4e normal %.4e"
  % (C_par, C_perp, own_par, own_perp, lk_t, lk_s, lk_o, off_in, off_n))

def dM(M, split):
    """strain response of a corner-basis mass matrix M: list over axes a of dM_a.  split='trace': on-site part = tr/3;
    split='selective': no on-site part (all diagonal masses from corner-selective symbols)."""
    mbar = np.trace(M).real / 3 if split == 'trace' else 0.0
    mu = np.diag(M).real - mbar
    out = []
    for a in range(3):
        D = np.zeros((3, 3), complex)
        for c in range(3):
            D[c, c] = mbar * (C_par if a == c else C_perp) + mu[c] * (own_par if a == c else own_perp)
            for s in range(3):
                if s != c:
                    D[c, c] += mu[s] * (lk_t if a == c else (lk_s if a == s else lk_o))
            for c2 in range(3):
                if c2 != c:
                    D[c, c2] = M[c, c2] * (off_in if a in (c, c2) else off_n)
        out.append(D)
    return out

def kappa(U, m, split):
    """traceless first-order coefficients d ln m_i / d(t h_aa) per e^2 for M = U diag(m) U^dag (corner basis)."""
    M = U @ np.diag(m) @ U.conj().T
    D = dM(M, split)
    k = np.array([[(U.conj().T @ D[a] @ U)[i, i].real / m[i] for a in range(3)] for i in range(3)])
    return k - k.mean(axis=1, keepdims=True)

def rot(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = np.sin(t12), np.cos(t12), np.sin(t23), np.cos(t23), np.sin(t13), np.cos(t13)
    e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
deg = np.pi / 180
VCKM = rot(13.04 * deg, 2.38 * deg, 0.201 * deg, 1.20)        # PDG central (RECALLED)
UPMNS = rot(33.4 * deg, 49.0 * deg, 8.57 * deg, 197 * deg)      # NuFIT-like NO central (RECALLED)
w = np.exp(2j * np.pi / 3); F = np.array([[w**(c * j) for j in range(3)] for c in range(3)]) / np.sqrt(3)
mu_q = np.array([2.16e-3, 1.27, 172.69]); md_q = np.array([4.67e-3, 0.0934, 4.18]); me_l = np.array([0.511e-3, 0.10566, 1.77686])
fN = {'u': 0.020, 'd': 0.030, 's': 0.040, 'c': 0.0674, 'b': 0.0674, 't': 0.0674}   # d ln m_p / d ln m_q (RECALLED/ESTIMATE)
P("checks: |V_us| %.4f |V_cb| %.4f |V_ub| %.5f unitary %.1e; DFT unitary %.1e" % (abs(VCKM[0, 1]), abs(VCKM[1, 2]), abs(VCKM[0, 2]),
  np.abs(VCKM @ VCKM.conj().T - np.eye(3)).max(), np.abs(F @ F.conj().T - np.eye(3)).max()))
# T-aligned sanity: a circulant sector has zero traceless first-order response (X2-L8, H = T)
P("T-aligned (circulant) sector, both splits: max |kappa| =", max(np.abs(kappa(F, mu_q, s)).max() for s in ('trace', 'selective')))

# ---------------------------------------------------------------- clock estimator (copied from TW-2 tw2_sizes.py:80-94, unchanged)
A_, gam = 2.4e-15, 13 / 3; alpha_ = (3 - gam) / 2
def comp_slope(fmin, Tobs, fmax=50.0, nf=4000, nt=801):
    f = np.exp(np.linspace(np.log(fmin), np.log(fmax), nf)); hc2 = (A_ * f**alpha_)**2; S = 0.4 * hc2 / f; lnf = np.log(f)
    def integ(y, mask=None):
        if mask is not None: y = np.where(mask, y, 0.0)
        return float(np.sum(0.5 * (y[1:] + y[:-1]) * np.diff(lnf)))
    tau = np.linspace(-Tobs / 2, Tobs / 2, nt); dg = np.linspace(0, Tobs, nt)
    Cg = np.array([integ(S * f * np.cos(2 * np.pi * f * dd)) for dd in dg])
    C = np.interp(np.abs(tau[:, None] - tau[None, :]), dg, Cg)
    wts = np.full(nt, tau[1] - tau[0]); wts[0] *= 0.5; wts[-1] *= 0.5
    slope = np.sqrt((wts[:, None] * wts[None, :] * tau[:, None] * tau[None, :] * C).sum()) * 12 / Tobs**3
    hdot = np.sqrt(integ((2 * np.pi * f)**2 * S * f, f < 1 / Tobs))
    return slope, hdot
S1 = []
for fmin_yr in (16.0, 30.0):
    for Tobs in (10.0, 5.0):
        sl, hd = comp_slope(1 / fmin_yr, Tobs); S1 += [sl, hd]
        P("   NANOGrav one-component slope: f_min 1/%2.0f yr, T_obs %4.1f yr: LS %.3e /yr, rms hdot %.3e /yr" % (fmin_yr, Tobs, sl, hd))
S1lo, S1hi = min(S1), max(S1); BOUND = 3.6e-17
P("   S1 range %.3e .. %.3e /yr; clock bound %.1e /yr (Lange 2021, 1 sigma)" % (S1lo, S1hi, BOUND))

# ---------------------------------------------------------------- branches
def species(Uu, Ud, Ue, split):
    return {'u': kappa(Uu, mu_q, split), 'd': kappa(Ud, md_q, split), 'e': kappa(Ue, me_l, split)}
branches = {
    'A  corner-aligned (U_u = 1, U_d = V, U_e = 1)': (np.eye(3), VCKM, np.eye(3)),
    'B  minimal: u and e T-aligned, CKM in d, PMNS in nu (U_u = F, U_d = F V, U_e = F)': (F, F @ VCKM, F),
    "B' u and nu T-aligned, CKM in d, PMNS in e (U_u = F, U_d = F V, U_e = F U^dag)": (F, F @ VCKM, F @ UPMNS.conj().T),
}
P("\nR1: traceless first-order coefficients and the clock row (couplings: e^2 = 0.1 leptons, C_F g_s^2 = 0.4 quarks; bracket x0.5..x2)")
names_u, names_d = ('u', 'c', 't'), ('d', 's', 'b')
summary = []
for bname, (Uu, Ud, Ue) in branches.items():
    for split in ('trace', 'selective'):
        sp = species(Uu, Ud, Ue, split)
        kp = 0.4 * (sum(fN[n] * sp['u'][i] for i, n in enumerate(names_u)) + sum(fN[n] * sp['d'][i] for i, n in enumerate(names_d)))
        ke = 0.1 * sp['e'][0]
        kmu = kp - ke
        nrm = np.linalg.norm(kmu); nrm_e = np.linalg.norm(ke); nrm_p = np.linalg.norm(kp)
        lo, hi = nrm * S1lo / BOUND, nrm * S1hi / BOUND
        summary.append((bname[:2].strip(), split, lo, hi))
        P(f" {bname} [{split}]")
        P("    per-e^2 |kappa| (Frobenius, traceless): " + ", ".join(f"{n} {np.linalg.norm(sp['u'][i]):.3e}" for i, n in enumerate(names_u)) + "; "
          + ", ".join(f"{n} {np.linalg.norm(sp['d'][i]):.3e}" for i, n in enumerate(names_d)) + f"; e {np.linalg.norm(sp['e'][0]):.3e}")
        P(f"    d ln m_e: {nrm_e:.3e}   d ln m_p: {nrm_p:.3e}   d ln(m_p/m_e): {nrm:.3e} per unit strain (E_g components only: lower bound)")
        P(f"    clock: rate {nrm*S1lo:.2e} .. {nrm*S1hi:.2e} /yr = x{lo:.3g} .. x{hi:.3g} of the bound;  coupling bracket x{lo*0.5:.3g} .. x{hi*2:.3g}")
P("\nR1 summary (ratio to the clock bound, central couplings):")
for b, s, lo, hi in summary:
    P(f"   branch {b:2s} [{s:9s}]: x{lo:.3g} .. x{hi:.3g}")


P("\n=== OBS-2: T2g components added: 0 at first order (checked) -> five-component rate = E_g rate above (registered tau_x completion)")
reg = list(summary)
off_in, off_n = -3.373659e-02, -3.383934e-02     # offdiag_sz_N48.out (gauge loop, B = tau_x sigma_z), same N as OBS-1 inputs
P(f"=== covariant completion: off_in {off_in:.4e} off_n {off_n:.4e} (N=48); OBS-1 registered tau_x: 2.0105e-2, 2.0713e-2")
summary2 = []
for bname, (Uu, Ud, Ue) in branches.items():
    for split in ('trace', 'selective'):
        sp = species(Uu, Ud, Ue, split)
        kp = 0.4 * (sum(fN[n] * sp['u'][i] for i, n in enumerate(names_u)) + sum(fN[n] * sp['d'][i] for i, n in enumerate(names_d)))
        ke = 0.1 * sp['e'][0]; nrm = np.linalg.norm(kp - ke)
        summary2.append((bname[:2].strip(), split, nrm * S1lo / BOUND, nrm * S1hi / BOUND))
P("FLAV2 summary (ratio to 3.6e-17/yr; central couplings; E_g + T2g):")
for (b, s, lo, hi), (b2, s2, lo2, hi2) in zip(reg, summary2):
    P(f"   branch {b:2s} [{s:9s}]: registered tau_x completion x{lo:.3g} .. x{hi:.3g} (coupling bracket x{lo/2:.3g} .. x{hi*2:.3g});  covariant tau_x.sigma_c completion x{lo2:.3g} .. x{hi2:.3g} (x{lo2/2:.3g} .. x{hi2*2:.3g})")
