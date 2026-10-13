"""C5 R19-14: (1) sub-horizon massless check of the second-order lag and its H^2 scaling;
(2) homogeneous Bianchi bookkeeping for (S) variants on V1 (sympy);
(3) the frame (s) dependence of 'the lowest state' as a zone total."""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def smooth(x):
    x = np.clip(x, 0, 1)
    f = lambda y: np.where(y > 0, np.exp(-1/np.maximum(y, 1e-300)), 0.0)
    return f(x)/(f(x)+f(1-x))

def run(Om, m, Hf, Tramp, Tflat, svals):
    Hub = lambda t: Hf*smooth(t/Tramp)
    def rhs(t, y):
        a = np.exp(y[0]); M = a**3; w2 = m*m + Om*Om/a**2; A = y[1] + 1j*y[2]
        dA = -1j*(A*A/M - M*w2); return [Hub(t), dA.real, dA.imag]
    T = Tramp + Tflat
    sol = solve_ivp(rhs, [0, T], [0.0, np.sqrt(m*m+Om*Om), 0.0], method='DOP853', rtol=1e-12, atol=1e-15, dense_output=True)
    ts = np.linspace(T-0.5*Tflat, T, 300); r = {s: [] for s in svals}; p = {s: [] for s in svals}
    for t in ts:
        lna, Ar, Ai = sol.sol(t); a = np.exp(lna); M = a**3; w2 = m*m + Om*Om/a**2; w = np.sqrt(w2)
        A = Ar + 1j*Ai; E = (abs(A)**2/M + M*w2)/(4*Ar); xp = -Ai/(2*Ar); h = Hub(t)
        for s in svals:
            r[s].append(E + s*h*xp - 0.5*np.sqrt(w2 - (s*h)**2)); p[s].append(h*h*(2 + m*m/w2 - 2*s)**2/(16*w))
    return {s: (np.mean(r[s]), np.mean(p[s])) for s in svals}, np.exp(sol.y[0, -1])

pr('## (1) sub-horizon modes (a_end ~ 1.5, w >> H): excess above the instantaneous lowest state of H\'_s')
pr('   Om   m     Hf     a_end    s=0 num/pred            s=0.5 num/pred          s=1 num/pred      ratio(Hf)/ratio(Hf/2), s=0')
for Om in (0.5, 1.0, 2.0, 3.4):
    for m in (0.0, 0.3):
        rows = []
        for Hf in (0.004, 0.002):
            r, aend = run(Om, m, Hf, Tramp=150.0*0.004/Hf, Tflat=30.0*0.004/Hf, svals=(0.0, 0.5, 1.0))
            rows.append((Hf, aend, r))
        for Hf, aend, r in rows:
            row = f'  {Om:4.1f} {m:3.1f}  {Hf:6.4f}  {aend:6.3f}'
            for s in (0.0, 0.5, 1.0):
                row += f'   {r[s][0]:.4e}/{r[s][1]:.4e}'
            pr(row)
        pr(f'      H^2 scaling (s=0): excess(0.004)/excess(0.002) = {rows[0][2][0.0][0]/rows[1][2][0.0][0]:.4f} (H^2 law: 4)')

pr('\n## (2) homogeneous Bianchi bookkeeping on V1 (sympy)')
t = sp.symbols('t', real=True); a = sp.Function('a', positive=True)(t)
eps = sp.Function('eps')   # vacuum energy per site in lattice units, function of mu = m*ell0*a
m, l0 = sp.symbols('m ell0', positive=True)
mu = m*l0*a
rho = eps(mu)/(l0*a)**4                      # physical vacuum energy density
V3 = (l0*a)**3
p = -sp.diff(rho*V3, a)/sp.diff(V3, a)       # adiabatic pressure p = -d(rho V)/dV at fixed site number
Hb = sp.diff(a, t)/a
cons = sp.simplify(sp.diff(rho, t) + 3*Hb*(rho + p))
pr('  vacuum fluid rho = eps(m ell0 a)/(ell0 a)^4, p = -d(rho V)/dV:  rho_dot + 3H(rho+p) =', cons)
W = sp.simplify(rho + p)
pr('  enthalpy W = rho + p =', W)
# (S) literal: subtract C g with C constant -> gravitating vacuum part (rho - C, p + C); conservation defect:
C = sp.symbols('C')
d_lit = sp.simplify(sp.diff(rho - C, t) + 3*Hb*((rho - C) + (p + C)))
pr('  (S) literal (C const), vacuum part kept as (rho-C, p+C): defect =', d_lit, ' (zero: conserved, but Lambda~ = kappa(rho(t) - C) drifts as a^-4)')
# (S)+N_red as registered: gravitating source T_m - (V - e0) g with e0 = C const; vacuum enthalpy assumed absorbed by (d-i)
d_nred = sp.simplify(sp.diff(rho - C, t) + 3*Hb*((rho - C) + (-(rho - C))))
pr('  N_red source -(V - e0) g with V = rho(t), e0 = C: defect = d(rho)/dt =', sp.simplify(d_nred), '  -> needs a carrier Q_0 = d e0/dt = -3 H W')
# (S-inst): C(t) = rho(t) in C g only -> gravitating vacuum = W h (energy 0, pressure W)
d_inst = sp.simplify(sp.diff(0*rho, t) + 3*Hb*(0 + W))
pr('  (S-inst) C(t) = e0(t) in C g only: gravitating vacuum (0, W): defect = 3 H W =', d_inst, ' = -d e0/dt:', sp.simplify(d_inst + sp.diff(rho, t)) == 0)
pr('  (S_V) full instantaneous vacuum stress removed: gravitating vacuum (0, 0): defect = 0; receiver of W is e0\'s own drift (Q = d e0)')

pr('\n## (3) frame dependence of the lowest state, zone totals (massless NN scalar, per minimal dof)')
N = 96; k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; s1 = 4*np.sin(k/2)**2
Om = np.sqrt(s1[:, None, None] + s1[None, :, None] + s1[None, None, :]); inv = np.mean(1/Om)
for s in (0.0, 0.5, 1.0, 1.5, 2.0):
    cX = (1-s)**2*inv/4
    pr(f'  s = {s:3.1f}: rho_X = {cX:.5f} H^2/ell^2 ;  rho_X/rho_crit at ell = ell_P: {(8*np.pi/3)*cX:.4f}')
pr('  (s = 1: the lowest state of H\'_1 is the first-order adiabatic vacuum; lag is then 4th order, O(H^4))')
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
