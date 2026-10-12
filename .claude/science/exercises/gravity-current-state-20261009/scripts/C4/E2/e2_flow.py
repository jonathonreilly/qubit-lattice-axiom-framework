"""E2 (lane RE, C4): integrate the one-loop speed flows from the cutoff (a^-1 = M_Pl) down, for
(a) QED-like, QCD-like and SM-like gauge content with running couplings;
(b) power-law (strongly coupled / large-N / epsilon-expansion) exponents;
(c) the F2 lattice initial split c_e - c_gamma = -8.5e-3 propagated down and compared with bounds;
(d) graviton: TT stiffness scaling and graviton-speed relaxation from matter loops.
Coefficients from e2_coeffs.py (derived; checked by e2_numcheck.py):
  fermion <- gauge  dv/dL = (1/(3 pi^2)) C g^2 (c_A - v)      [= (4/3) C alpha/pi]
  scalar  <- gauge  dv/dL = (1/(4 pi^2)) C g^2 (c_A - v)      [= C alpha/pi]
  gauge   <- matter dc/dL = g^2/(8 pi^2) w (c_i - c_A), w = 4/3 T (Dirac), 2/3 T (Weyl), 1/3 T (cplx scalar)
  fermion <- scalar dv/dL = (1/(24 pi^2)) y^2 (c_phi - v);  scalar <- fermion loop: 4 N_D y^2/(16 pi^2)
L = ln(Lambda/mu).  Bounds are literature values quoted from memory (COMPARATOR), not re-verified.
Usage: python e2_flow.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import svdvals

pi = np.pi
MPl = 1.22e19          # GeV, framework convention (non-reduced), a^-1 = M_Pl
MZ = 91.1876
TeV = 1.0e3
lnPT = np.log(MPl / TeV)
print(f"M_Pl -> 1 TeV: {np.log10(MPl/TeV):.2f} decades, L = {lnPT:.2f}")
print()

# ---------------------------------------------------------------- (a1) QED-like, analytic + matrix
print("== (a1) QED with N_f unit-charge Dirac fermions; alpha(1 TeV) = 1/128 ==")
print("   singlet (all fermions vs photon): d delta/d ln mu = ((2N_f+4)/3)(alpha/pi) delta ;"
      " nonsinglet (fermion vs fermion): (4/3)(alpha/pi)")
for Nf in (1, 3, 8):
    ainv_T = 128.0
    ainv_P = ainv_T - (2 * Nf / (3 * pi)) * lnPT
    S_sing = (ainv_P / ainv_T) ** ((Nf + 2) / Nf)
    S_ns = (ainv_P / ainv_T) ** (2 / Nf)       # (4/3)/(2Nf/3) = 2/Nf
    print(f"  N_f = {Nf}: 1/alpha(M_Pl) = {ainv_P:6.1f};  suppression M_Pl->TeV: singlet {S_sing:.3f}, nonsinglet {S_ns:.3f}")
print("  (N_f = 1 to m_e instead of TeV, F2's b=1 guess gave 0.887; b = 2 derived here gives "
      f"{np.exp(-2*np.log(MPl/0.511e-3)/(137.0*pi)):.3f} at fixed alpha = 1/137)")
print()

# ---------------------------------------------------------------- (a2) QCD-like
print("== (a2) QCD: gluon + n_f = 6 quark flavours (same speed), alpha_s(1 TeV) = 0.0885 ==")
nf, b0 = 6, 11 - 2 * 6 / 3
rate = nf / 3 + 16 / 9          # coefficient of alpha_s/pi for the singlet delta = c_g - c_q
as_T = 0.0885
asinv_P = 1 / as_T + (b0 / (2 * pi)) * lnPT
as_P = 1 / asinv_P
p = rate * 2 / b0
S_qcd = (as_P / as_T) ** p
print(f"  singlet rate = {rate:.3f} alpha_s/pi ; alpha_s(M_Pl) = {as_P:.4f} ; S = (alpha_P/alpha_T)^{p:.3f} = {S_qcd:.3f}")
p_ns = (16 / 9) * 2 / b0
print(f"  nonsinglet (quark vs quark): S = (alpha_P/alpha_T)^{p_ns:.3f} = {(as_P/as_T)**p_ns:.3f}")
# continue to 1 GeV with n_f=4..5 roughly (illustrative; nonperturbative below)
print()

# ---------------------------------------------------------------- (a3) SM-like matrix
print("== (a3) SM-like: fields B, W, G, Q, u, d, L, e, H (3 flavour-universal generations, no Yukawas) ==")
names = ['B', 'W', 'G', 'Q', 'u', 'd', 'L', 'e', 'H']
kF, kS = 1 / (3 * pi ** 2), 1 / (4 * pi ** 2)
Y2 = {'Q': 1 / 36, 'u': 4 / 9, 'd': 1 / 9, 'L': 1 / 4, 'e': 1.0, 'H': 1 / 4}
C2W = {'Q': 3 / 4, 'L': 3 / 4, 'H': 3 / 4}
C3 = {'Q': 4 / 3, 'u': 4 / 3, 'd': 4 / 3}
wB = {'Q': 1 / 3, 'u': 8 / 3, 'd': 2 / 3, 'L': 1.0, 'e': 2.0, 'H': 1 / 6}
wW = {'Q': 3.0, 'L': 1.0, 'H': 1 / 6}
wG = {'Q': 2.0, 'u': 1.0, 'd': 1.0}
assert abs(sum(wB.values()) - 41 / 6) < 1e-12 and abs(sum(wW.values()) - 25 / 6) < 1e-12 and sum(wG.values()) == 4
bSM = np.array([41 / 6, -19 / 6, -7.0])
aem, s2w = 1 / 127.95, 0.2312
ainvZ = np.array([(1 - s2w) / aem, s2w / aem, 1 / 0.1180])


def alphas(mu):
    ainv = ainvZ - bSM / (2 * pi) * np.log(mu / MZ)
    return 1 / ainv


def Mmat(mu):
    aY, a2, a3 = alphas(mu)
    gY2, g22, g32 = 4 * pi * aY, 4 * pi * a2, 4 * pi * a3
    idx = {n: i for i, n in enumerate(names)}
    M = np.zeros((9, 9))
    for f in ['Q', 'u', 'd', 'L', 'e', 'H']:
        k = kS if f == 'H' else kF
        M[idx[f], idx['B']] += k * Y2[f] * gY2
        if f in C2W: M[idx[f], idx['W']] += k * C2W[f] * g22
        if f in C3: M[idx[f], idx['G']] += k * C3[f] * g32
        M[idx['B'], idx[f]] += gY2 / (8 * pi ** 2) * wB[f]
        if f in wW: M[idx['W'], idx[f]] += g22 / (8 * pi ** 2) * wW[f]
        if f in wG: M[idx['G'], idx[f]] += g32 / (8 * pi ** 2) * wG[f]
    # dc_i/dL = sum_j M_ij (c_j - c_i)
    return M - np.diag(M.sum(1))


def propagate(mu_hi, mu_lo, Mfun, n):
    def rhs(L, y):
        mu = mu_hi * np.exp(-L)
        return (Mfun(mu) @ y.reshape(n, n)).ravel()
    sol = solve_ivp(rhs, [0, np.log(mu_hi / mu_lo)], np.eye(n).ravel(), rtol=1e-10, atol=1e-12)
    return sol.y[:, -1].reshape(n, n)


P = np.eye(9) - np.ones((9, 9)) / 9
for mu_lo, lab in ((1e11, '1e11 GeV (UHECR p)'), (1.4e6, '1.4 PeV (LHAASO photon)'), (TeV, '1 TeV')):
    U = propagate(MPl, mu_lo, Mmat, 9)
    Us, sv, Vh = np.linalg.svd(P @ U @ P)
    # single-species kick: c_e = 1, all others 0 (initial c_e - mean = 8/9)
    e_vec = np.zeros(9); e_vec[7] = 1
    out = U @ e_vec
    q_vec = np.zeros(9); q_vec[3] = 1
    outq = U @ q_vec
    print(f"  M_Pl -> {lab}: worst-case relative-speed suppression sigma_max = {sv[0]:.3f}; "
          f"next {sv[1]:.3f}; best {sv[-2]:.3f}")
    print(f"     slowest initial pattern: " + ", ".join(f"{n}:{v:+.2f}" for n, v in zip(names, Vh[0])))
    print(f"     kick c_e=1: (c_e - c_B) -> {out[7]-out[0]:.3f}, (c_e - mean) -> {(out[7]-out.mean())/(8/9):.3f} of initial;"
          f"  kick c_Q=1: (c_Q - c_G) -> {outq[3]-outq[2]:.3f}")
print(f"  couplings at M_Pl: alpha_Y, alpha_2, alpha_3 = {np.round(alphas(MPl), 4)}")
print()

# ---------------------------------------------------------------- (b) power laws
print("== (b) power-law exponents z (delta ~ (mu/Lambda)^z) and suppression over D decades ==")
def gny(Nf, eps):
    y2 = eps / (2 * (2 * Nf + 3))      # y*^2/(16 pi^2), chiral-Ising GNY, Nf four-component Dirac
    return (4 * Nf + 2 / 3) * y2
rows = [("GNY chiral Ising, 4-eps, eps=1, N_f=1 (one-loop, derived)", gny(1, 1)),
        ("GNY chiral Ising, 4-eps, eps=1, N_f=2 (graphene-like)", gny(2, 1)),
        ("GNY, eps=1, N_f -> inf (= 4 - d)", 1.0),
        ("GNY in d=4 (eps=0): marginal -> logs only", 0.0),
        ("QED3 large N, nonsinglet, N=4 two-comp (64/(5 pi^2 N), derived)", 64 / (5 * pi ** 2 * 4)),
        ("QED3 large N, singlet fermion vs bare Maxwell (4 - d)", 1.0),
        ("GN large N, nonsinglet, N=4 (16/(15 pi^2 N), derived)", 16 / (15 * pi ** 2 * 4)),
        ("weakly coupled 4D, gamma ~ 2 alpha/pi at alpha=1/128", 2 / (128 * pi)),
        ("4D strongly coupled CFT, z = Delta(T1-T2) - 4 (BPS-type, model-dependent)", 0.5),
        ("same, z = 1", 1.0), ("same, z = 2", 2.0)]
D = np.log10(MPl / TeV)
for lab, z in rows:
    print(f"  {lab:72s} z = {z:6.4f}: factor over {D:.1f} decades = {10**(-z*D):.2e}")
print()

# ---------------------------------------------------------------- (c) F2 initial split vs bounds
print("== (c) F2 initial split delta0 = c_e - c_gamma = -8.55e-3 at a^-1 = M_Pl ==")
d0 = 8.55e-3
bounds = [("gamma -> e+e- (LHAASO 1.4 PeV), lattice sign", 2.66e-19, 1.4e6),
          ("IceCube PeV neutrinos (nu vs gamma), either sign", 1e-20, 1e6),
          ("UHECR p vacuum Cherenkov (c_p > c_gamma) at 1e20 eV", 4.4e-23, 1e11),
          ("gamma -> p pbar (c_gamma > c_p) at 1.4 PeV", 9.0e-13, 1.4e6)]
S_qed = (128.0 - (2 / (3 * pi)) * np.log(MPl / 1e6)) / 128.0
for lab, b, E in bounds:
    dec = np.log10(MPl / E)
    zreq = np.log10(d0 / b) / dec
    S_log = ((128.0 - (2 * 1 / (3 * pi)) * np.log(MPl / E)) / 128.0) ** 3   # QED N_f=1 singlet
    print(f"  {lab:55s}: bound {b:.1e} at {E:.1e} GeV ({dec:.2f} decades): "
          f"QED log flow gives {d0*S_log:.2e} (miss x{d0*S_log/b:.1e}); power law needs z >= {zreq:.2f}")
print("  GW170817 (c_g vs c_gamma, 3e-15): not reachable by any matter-sector flow; see (d)")
print()

# ---------------------------------------------------------------- (d) graviton
print("== (d) graviton TT stiffness and speed ==")
print("  canonical h_c = M_Pl h/2: mass term mu_TT h^2 = (4 mu_TT/M_Pl^2) h_c^2 -> m_g^2 ~ mu_TT/M_Pl^2 (dimension-2 coefficient)")
for E, lab in ((TeV, '1 TeV'), (1e-24, '~1e-15 eV (LIGO band, 100 Hz ~ 4e-13 eV order)')):
    print(f"  growth of (m_g/E)^2 from E = M_Pl to E = {lab}: x{(MPl/E)**2:.1e}")
for z in (0.0, 0.5, 1.0, 2.0):
    for frac_scale in (1e-1, 1e-3):
        f = frac_scale ** (4 + z)
        print(f"  stiffness share from modes below {frac_scale:.0e} Lambda with LV profile (k/Lambda)^{z}: {f:.1e}"
              f"  -> flow can remove at most this share; UV share 1 - {f:.0e} untouched")
# graviton speed relaxation via matter loops: induced EH term ~ N_dof mu^2/(96 pi^2) per shell vs M_Pl^2
for Ndof in (100, 1000):
    tot = Ndof / (96 * pi ** 2) * 0.5     # int_0^inf (mu/M_Pl)^2 dL from M_Pl down = 1/2
    print(f"  graviton-speed pull from {Ndof} matter dof (Sakharov-type estimate): integrated rate {tot:.3f}"
          f" -> suppression factor >= {np.exp(-tot):.3f} (GW170817 needs 3e-15/8.5e-3 = {3e-15/8.55e-3:.0e})")
print("  h anomalous dimension from matter at scale mu ~ c_T mu^2/M_Pl^2: at 1 TeV ~ (1e3/1.22e19)^2 = "
      f"{(TeV/MPl)**2:.1e} x c_T -> cannot turn the dimension-2 mass into an irrelevant operator")
