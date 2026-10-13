"""C5 R19-14 (a): V1 (fixed site set, growing physical spacing). Does the vacuum track the
instantaneous lowest state, and what is left over?

Model (per lattice mode; comoving lattice spacing ell0 = 1 at a = 1; cosmic time t):
  minimal coupling, physical units:  H_k = p^2/(2M) + M w^2 x^2/2,  M = a^3,  w^2 = m^2 + Om^2/a^2,
  Om^2 = sum_i 4 sin^2(k_i/2)  (NN lattice symbol).
A time-dependent canonical frame v = a^s x, p_v = a^-s p changes the instantaneous Hamiltonian to
  H'_k = H_k + s*Hub*(v p_v + p_v v)/2, whose ground energy is sqrt(w^2 - s^2 Hub^2)/2 (+O(mass) terms).
Gaussian state psi ~ exp(-A x^2/2): Riccati  dA/dt = -i (A^2/M - M w^2).
Energy  E = (|A|^2/M + M w^2)/(4 Re A);  <(xp+px)/2> = -Im(A)/(2 Re A).
Second-order prediction (derived in the report):  excess_s = Hub^2 (2 + m^2/w^2 - 2 s)^2 / (16 w).
"""
import numpy as np
from scipy.integrate import solve_ivp
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def smooth(x):  # C^infinity-ish smoothstep on [0,1]
    x = np.clip(x, 0, 1)
    f = lambda y: np.where(y > 0, np.exp(-1/np.maximum(y, 1e-300)), 0.0)
    return f(x)/(f(x)+f(1-x))

def run_mode(Om, m, Hf, Tramp, Tflat, s_list=(0.0, 0.5, 1.0)):
    # H(t) ramps 0 -> Hf over Tramp, then constant over Tflat; a(t) from H
    def Hub(t): return Hf*smooth(t/Tramp)
    def rhs(t, y):
        lna, Ar, Ai = y
        a = np.exp(lna); M = a**3; w2 = m*m + Om*Om/a**2
        A = Ar + 1j*Ai
        dA = -1j*(A*A/M - M*w2)
        return [Hub(t), dA.real, dA.imag]
    w0 = np.sqrt(m*m + Om*Om)
    y0 = [0.0, w0, 0.0]          # ground state of the static law at t = 0 (M = 1)
    T = Tramp + Tflat
    sol = solve_ivp(rhs, [0, T], y0, method='DOP853', rtol=1e-12, atol=1e-14, dense_output=True)
    # sample the last 20% and average (removes small residual oscillation)
    ts = np.linspace(T - 0.2*Tflat, T, 400)
    res = {s: [] for s in s_list}; pred = {s: [] for s in s_list}
    for t in ts:
        lna, Ar, Ai = sol.sol(t)
        a = np.exp(lna); M = a**3; w2 = m*m + Om*Om/a**2; w = np.sqrt(w2)
        A = Ar + 1j*Ai
        E = (abs(A)**2/M + M*w2)/(4*Ar)
        xp = -Ai/(2*Ar)
        h = Hub(t)
        for s in s_list:
            Eprime = E + s*h*xp
            # ground energy of H' = p^2/2M + M w^2 v^2/2 + s h (vp+pv)/2  ->  sqrt(w^2 - s^2 h^2)/2
            E0p = 0.5*np.sqrt(w2 - (s*h)**2)
            res[s].append(Eprime - E0p)
            pred[s].append(h*h*(2 + m*m/w2 - 2*s)**2/(16*w))
    return {s: (np.mean(res[s]), np.mean(pred[s])) for s in s_list}, np.exp(sol.y[0, -1])

pr('## (A) Riccati check of the second-order lag, per mode (excess above the instantaneous lowest state of H\'_s)')
pr('   Om    m     Hf     a_end   s=0: num / pred        s=0.5: num / pred      s=1: num / pred')
for Om in (0.5, 1.0, 2.0, 3.4):
    for m in (0.0, 0.5):
        for Hf in (0.02, 0.01):
            r, aend = run_mode(Om, m, Hf, Tramp=400.0, Tflat=200.0)
            row = f'  {Om:4.1f}  {m:3.1f}  {Hf:5.3f}  {aend:7.3f}'
            for s in (0.0, 0.5, 1.0):
                row += f'   {r[s][0]:.4e} / {r[s][1]:.4e}'
            pr(row)
pr('  (num = time-averaged excess after an adiabatic ramp of H from 0; pred = Hub^2 (2 + m^2/w^2 - 2s)^2/(16 w))')

pr('\n## (B) zone averages for the 3D NN scalar (a = 1, lattice units)')
N = 96
k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
s1 = 4*np.sin(k/2)**2
O2 = s1[:, None, None] + s1[None, :, None] + s1[None, None, :]
Om = np.sqrt(O2)
inv = np.mean(1/Om)
pr(f'  <1/Om> = {inv:.6f}   (N = {N}; N = 64 check below)')
N2 = 64; k2 = 2*np.pi*(np.arange(N2)+0.5)/N2 - np.pi; s2 = 4*np.sin(k2/2)**2
O22 = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
pr(f'  <1/Om> (N = 64) = {np.mean(1/np.sqrt(O22)):.6f}')
for m in (0.0, 0.1, 0.3, 1.0):
    w = np.sqrt(m*m + O2)
    cX = np.mean((2 + m*m/w**2)**2/(16*w))
    e0 = np.mean(w)/2
    pr(f'  m = {m:3.1f}: c_X(s=0) = <(2+m^2/w^2)^2/(16 w)> = {cX:.6f}   e0 = <w>/2 = {e0:.6f}')
cX0 = inv/4
pr(f'  massless minimal scalar: rho_X = c_X H^2 / ell^2 with c_X = <1/Om>/4 = {cX0:.6f}')

pr('\n## (C) cosmology (Planck units G = c = hbar = 1; inputs RECALLED)')
H0 = 1.1775e-61; OmL = 0.685
rhoL = OmL*3*H0**2/(8*np.pi)
pr(f'  rho_Lambda = {rhoL:.4e};  rho_crit,0 = {3*H0**2/(8*np.pi):.4e}')
x1 = (8*np.pi/3)*cX0     # rho_X/rho_crit per minimal dof at ell = ell_P
pr(f'  per minimally coupled massless real dof, at ell = ell_P:  rho_X/rho_crit = (8 pi/3) c_X = {x1:.4f}')
pr(f'  today (H = H0, ell = ell_P): rho_X/rho_Lambda = {cX0*H0**2/rhoL:.4f} per dof')
for Nd, lab in ((2, 'gravitons only (J2)'), (6, 'gravitons + Higgs doublet (xi = 0)')):
    x = Nd*x1
    pr(f'  N_min = {Nd} ({lab}): x(ell) = rho_X/rho_crit = {x:.3f} (ell_P/ell)^2')
    # Friedmann: 3H^2(1 - x)/(8 pi) = rho_rest  -> G_eff = G/(1-x);  BBN: |G_eff/G - 1| < 0.1 -> x < 0.0909
    ell_bbn_min = np.sqrt(x/0.0909)
    zbbn = 4.0e8   # T ~ 0.1 MeV (RECALLED scale)
    pr(f'    BBN (|dG/G| < 10% at z ~ {zbbn:.0e}): ell(BBN) > {ell_bbn_min:.2f} ell_P  ->  ell_today > {ell_bbn_min*zbbn:.2e} ell_P = {ell_bbn_min*zbbn*1.616e-35:.2e} m')
    # LLR: Gdot/G = 2 H x/(1-x) < 1.5e-13 /yr ; H0 = 7.2e-11/yr
    xLLR = 1.5e-13/(2*7.2e-11)
    pr(f'    LLR (|Gdot/G| < 1.5e-13/yr): x_today < {xLLR:.2e}  ->  ell_today > {np.sqrt(x/xLLR):.2f} ell_P')
    # inflation: Friedmann needs x < 1 at the start of inflation; ell_start = ell_today /((1+z_rh) e^Ne)
    for Trh_GeV, Ne in ((1e-2, 60), (1e9, 60), (1e15, 60)):
        zrh = Trh_GeV/2.35e-13   # T0 = 2.35e-13 GeV (RECALLED), entropy factors ignored
        ell_today = np.sqrt(x)*zrh*np.exp(Ne)
        pr(f'    {Ne} e-folds, T_rh = {Trh_GeV:.0e} GeV: x < 1 at inflation start needs ell_today > {ell_today:.2e} ell_P = {ell_today*1.616e-35:.2e} m')
pr('  LV comparators (RECALLED, labelled): LHC/colliders probe ~1e-19 m = 6e15 ell_P; GRB photon quadratic dispersion')
pr('  E_QG,2 >~ 1e11-1e12 GeV -> ell <~ 1e7-1e8 ell_P for a literal NN photon (not binding on box laws, exact inside the box).')

pr('\n## (D) literal (S) on V1: C fixed, vacuum e0(t) = eps0/ell(t)^4 (massless part)')
eps0 = 1.193801  # NN massless scalar, R11-3 / R19-10
for dz in (1e-3, 1e-2, 0.1, 1.0):
    frac = (1+dz)**4 - 1
    pr(f'  z = {dz:6.3f} after the tuning epoch (ell = ell_P then): Lambda~ residual = {frac*eps0:.3e} M_P^4 = {frac*eps0/rhoL:.3e} rho_Lambda per scalar')
pr('  drift of e0 a^4 from the mass term (eps0(mu) - eps0(0) ~ c_rho mu^2, mu = m ell, c_rho = 0.1138 NN (R11-3)):')
for mu in (1e-17, 1e-5, 1e-2):
    pr(f'    mu = {mu:.0e}: d ln(e0 a^4)/d ln a = 2 c_rho mu^2/eps0(0) = {2*0.1138*mu**2/eps0:.3e}')

open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
