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

# SME / LPI mapping
P("\nSME/LPI mapping:")
Kv = 6.203941e-03   # r1_vel.out N=48 Delta=0.5 (0 exactly at Delta=0)
P("  untuned static corner velocity anisotropy per e^2: K_v = %.3e (Delta 0.5), 0 (Delta 0; staggered reflection)." % Kv)
P("  -> electron c_jk ~ e^2 K_v ||n n - 1/3|| = %.1e vs ~1e-21 (x%.0e); quark (C_F g_s^2) %.1e vs neutron-sector 1e-29 (x%.0e) -- generation-blind, removed by one cubic counterterm per field type (set C price)"
  % (0.1 * Kv * np.sqrt(2 / 3), 0.1 * Kv * np.sqrt(2 / 3) / 1e-21, 0.4 * Kv * np.sqrt(2 / 3), 0.4 * Kv * np.sqrt(2 / 3) / 1e-29))
for yname, y in (('y_tau', 0.0102), ('y_b', 0.024), ('y_t', 0.99)):
    P("  suggested flavour-pattern residual: registered formula %s^2/(16 pi^2) x K_v = %.1e; corrected (K_v already contains the loop measure) %s^2 x K_v = %.1e"
      % (yname, y**2 / (16 * np.pi**2) * Kv, yname, y**2 * Kv))
for b, (Uu, Ud, Ue) in branches.items():
    sp = species(Uu, Ud, Ue, 'trace')
    kp = 0.4 * (sum(fN[n] * sp['u'][i] for i, n in enumerate(names_u)) + sum(fN[n] * sp['d'][i] for i, n in enumerate(names_d))); ke = 0.1 * sp['e'][0]
    nrm = np.linalg.norm(kp - ke)
    # static traceless strain of size Phi_sun annual variation (conditional on a registration that gives traceless strain ~ Phi)
    dPhi = 3.3e-10
    P(f"  LPI (conditional: static traceless strain ~ Delta Phi_sun/c^2 = {dPhi:.1e}): |d ln mu| ~ {nrm*dPhi:.1e} vs 7(45)e-8 x dPhi = {4.5e-7*dPhi:.1e}: x{nrm/4.5e-7:.1e}   [{b[:2].strip()}]")

# ---------------------------------------------------------------- R2: Z4 arithmetic
P("\nR2: Z4 audit (exact rationals). X = 5(B-L) - 4Y; Z4 phase of a gauge-invariant operator = i^(X) = i^(B-L) (Y-sum 0)")
fields = {'Q': (Fr(1, 3), Fr(1, 6), 1), 'uc': (Fr(-1, 3), Fr(-2, 3), 1), 'dc': (Fr(-1, 3), Fr(1, 3), 1), 'L': (Fr(-1), Fr(-1, 2), 1),
          'ec': (Fr(1), Fr(1), 1), 'nc': (Fr(1), Fr(0), 1), 'H': (Fr(0), Fr(1, 2), 0)}
X = {k: 5 * bl - 4 * y for k, (bl, y, _) in fields.items()}
P("  X charges:", {k: str(v) for k, v in X.items()}, "; X mod 4 on fermions:", {k: int(v % 4) for k, v in X.items() if fields[k][2]})
P("  sum X^3, sum X, sum X Y^2 ... over the 16 (multiplicities 6,3,3,2,1,1):",
  [str(sum(m * f(k) for k, m in (('Q', 6), ('uc', 3), ('dc', 3), ('L', 2), ('ec', 1), ('nc', 1)))) for f in (lambda k: X[k]**3, lambda k: X[k], lambda k: X[k] * fields[k][1]**2)])
# enumerate monomials (fields and conjugates) up to 6 fermions + 2 Higgs with Y = 0, colour count = 0 mod 3, even # doublets
names = ['Q', 'uc', 'dc', 'L', 'ec', 'nc', 'H']
col = {'Q': 1, 'uc': -1, 'dc': -1, 'L': 0, 'ec': 0, 'nc': 0, 'H': 0}; dbl = {'Q': 1, 'uc': 0, 'dc': 0, 'L': 1, 'ec': 0, 'nc': 0, 'H': 1}
viol = 0; n_ops = 0; classes = {}
for n in range(2, 7):
    for combo in itertools.combinations_with_replacement([(f, s) for f in names for s in (1, -1)], n):
        Ysum = sum(s * fields[f][1] for f, s in combo); csum = sum(s * col[f] for f, s in combo); d = sum(dbl[f] for f, s in combo)
        if Ysum != 0 or csum % 3 != 0 or d % 2 or sum(1 for f, s in combo if fields[f][2]) % 2:   # Lorentz: even # fermions
            continue
        n_ops += 1
        Xs = sum(s * X[f] for f, s in combo); BL = sum(s * fields[f][0] for f, s in combo)
        Fz4 = sum(s * (1 if fields[f][2] else 2) for f, s in combo)    # uniform Z4^F with H charge 2
        if (Xs - BL) % 4 != 0 or (Fz4 - Xs) % 4 != 0:
            viol += 1
        classes.setdefault(int(BL % 4), 0); classes[int(BL % 4)] += 1
P(f"  enumerated {n_ops} candidate gauge-invariant monomials (<= 6 legs): identity X = (B-L) = F_Z4 mod 4 violated in {viol}; counts by (B-L) mod 4: {classes}")
for nm, ops in (('nu^c nu^c', [('nc', 1), ('nc', 1)]), ('L L H H', [('L', 1), ('L', 1), ('H', 1), ('H', 1)]), ('Q Q Q L', [('Q', 1)] * 3 + [('L', 1)]),
                ('uc uc dc ec', [('uc', 1), ('uc', 1), ('dc', 1), ('ec', 1)]), ('(uc dc dc)^2', [('uc', 1), ('dc', 1), ('dc', 1)] * 2),
                ('dc dc dc L H^dag (dim 7, B-L violating)', [('dc', 1), ('dc', 1), ('dc', 1), ('L', 1), ('H', -1)]), ('nu^c^4 (Delta L = 4)', [('nc', 1)] * 4),
                ('Q u^c H^dag-type Yukawa', [('Q', 1), ('uc', 1), ('H', 1)])):
    BL = sum(s * fields[f][0] for f, s in ops); Ys = sum(s * fields[f][1] for f, s in ops)
    P(f"   {nm:30s} Y-sum {str(Ys):>5s}  B-L {str(BL):>3s}  Z4 {'allowed' if BL % 4 == 0 else 'FORBIDDEN'}")

# ---------------------------------------------------------------- R3: proton decay floor
P("\nR3: p -> e+ pi0 floor on 1/a.  Gamma = (m_p/32 pi)(1 - m_pi^2/m_p^2)^2 |C W0 A_R|^2, C = c_eff a^2")
hbar = 6.582e-25; yr = 3.156e7; mp, mpi = 0.938272, 0.134977; MPl = 1.22089e19
tau_b = 2.4e34
Gmax = hbar / (tau_b * yr)
ph = mp / (32 * np.pi) * (1 - (mpi / mp)**2)**2
for W0 in (0.10, 0.15):
    for AR in (1.0, 2.5):
        Cmax = np.sqrt(Gmax / ph) / (W0 * AR)
        P(f"  W0 {W0} GeV^2, A_R {AR}: |C| < {Cmax:.2e} GeV^-2  (unit-coefficient Lambda > {1/np.sqrt(Cmax):.2e} GeV)")
Cmax_strict = np.sqrt(Gmax / ph) / (0.15 * 2.5); Cmax_loose = np.sqrt(Gmax / ph) / (0.10 * 1.0)
br = {'(i) link-pair conversion W eps^2, eps 0.02..0.13, W 1..10': (1 * 0.02**2, 10 * 0.13**2),
      '(ii) loop filter offset W df^4, df ~ 0.1 e^2 (checked toy: 0.094 e^2 per unit Delta), e^2 0.1..0.4': (1 * (0.0094)**4, 10 * (0.038)**4),
      '(iii) worst case allowed with light corners light: c_eff = W <= 10': (1.0, 10.0)}
for nm, (clo, chi) in br.items():
    floor_lo = np.sqrt(clo / Cmax_loose); floor_hi = np.sqrt(chi / Cmax_strict)
    P(f"  {nm}: c_eff {clo:.1e}..{chi:.1e} -> floor 1/a > {floor_lo:.1e} .. {floor_hi:.1e} GeV;  at a = l_P lifetime margin >= {(MPl/floor_hi)**4:.1e}")
P("  (iv) direct filtered quartic: 4 light legs x f ~ (qa)^2/4 each -> dimension-14; negligible at any a with 1/a > 1e3 GeV")
P("  skeptic recheck: Gamma = m_p^5/Lambda^4 overstates the rate by m_p^4/((1/32pi)(0.96) W0^2) = %.0f (W0 = 0.13)" % (mp**4 / (ph / mp * 0.13**2)))
for Lam in (1e16, 1.22e19):
    G = ph * (0.13 / Lam**2)**2
    P(f"  unit coefficient, Lambda {Lam:.2e} GeV, W0 0.13, A_R 1: tau = {hbar/G/yr:.1e} yr (bound 2.4e34): margin {hbar/G/yr/2.4e34:.1e}")
