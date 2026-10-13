"""R19-3 (b): the box-regulator sums.  R9-9's N-type box graviton: TT frequency w(q) = |d(q)| (Jg = 1), with the per-axis
symbol d(q) = rho(q) q + (1 - rho(q)) 2 sin(q/2), rho = 1 on |q| <= c1 = 1, 0 on |q| >= c2 = 2.5 (r99_graviton.py:19-21).
Every N-type identity is algebraic in the commuting real symbols d_a(q) (vR9-9:5), so each lattice mode q is a continuum
linearized-gravity mode at wave vector d(q), frequency w(q) = |d(q)|.  Under the symbol-substitution forward vertex
(each derivative in G2 / t_LL / the gauge-fixing term -> i d_a(q)), the per-mode tensors of r193_onepoint/gauge_family
apply with k -> ktilde = (w(q), d(q)):  t_mn(q) = c * ktilde_m ktilde_n / w(q)  (units 1/V), c = 1 for TT.
Outputs (lattice units hbar = c = a = 1):
  - whole-zone v_max of the graviton symbol (max |grad_q w|);
  - e_g = <w>_BZ (two polarizations x w/2), p_g, W_g = e_g + p_g; anisotropy of <d_i d_j / w>;
  - cubic covariance of the symbol, d(Rq) = R d(q) for all 48 signed permutations (checked on random q);
  - the harmonic-gauge remainders (c - 1) e_g, and sizes at a = l_P in units of rho_Lambda (RECALLED 5.3e-10 J/m^3).
"""
import numpy as np, itertools, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R9-9'))
from r99_profiles import plateau, wrap
C1, C2 = 1.0, 2.5
def dsym(q):
    q = wrap(q); r = plateau(q, C1, C2)
    return r*q + (1-r)*2*np.sin(q/2)

# v_max: |grad w|^2 = sum_i d_i^2 d_i'^2 / sum d^2 <= max d'^2, equality along an axis
# d is odd and jumps from +2 to -2 across the zone face (only |d| = w and D = d e^{iq/2} are periodic), so the
# derivative is taken on the open interval (-pi, pi); w = |d| has d w/dq -> 0 at the face (d ~ 2 sin(q/2)).
qq = np.linspace(-np.pi, np.pi, 2000001)[1:-1]
dd = dsym(qq)
dp = np.gradient(dd, qq)
print(f'v_max (whole zone, TT graviton) = max|d\'(q)| = {np.max(np.abs(dp)):.6f} at q = {qq[np.argmax(np.abs(dp))]:.4f}'
      f'   (box value 1; NN 2sin(q/2) would give 1)')
print(f'  min d\'(q) on the zone = {np.min(dp):.6f}  (a negative value means a backward-moving edge)')

# cubic covariance of the symbol
rng = np.random.default_rng(1)
Q = rng.uniform(-np.pi, np.pi, size=(2000, 3))
worst = 0.0
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = sg[i]
        lhs = np.stack([dsym(c) for c in (Q @ R.T).T], axis=1)
        rhs = np.stack([dsym(c) for c in Q.T], axis=1) @ R.T
        worst = max(worst, np.max(np.abs(lhs - rhs)))
print(f'cubic covariance d(Rq) = R d(q), all 48 signed permutations, 2000 random q: max error {worst:.1e}')

# zone sums (midpoint grid, excludes q = 0 automatically for even N)
for N in (96, 160, 256):
    k = 2*np.pi*(np.arange(N) + 0.5)/N - np.pi
    d1 = dsym(k)
    DX, DY, DZ = np.meshgrid(d1, d1, d1, indexing='ij')
    w = np.sqrt(DX**2 + DY**2 + DZ**2)
    eg = np.mean(w)                                   # two polarizations x w/2, per unit volume (BZ volume (2pi)^3 / (2pi)^3)
    S = np.array([[np.mean(Di*Dj/w) for Dj in (DX, DY, DZ)] for Di in (DX, DY, DZ)])
    p = np.trace(S)/3
    aniso = np.max(np.abs(S - p*np.eye(3)))/p
    print(f'N = {N:3d}: e_g = <w> = {eg:.8f}   p_g = <|d|^2/(3w)> = {p:.8f}   p/e = {p/eg:.12f}   '
          f'W_g = {eg + p:.8f}   anisotropy {aniso:.1e}')
# box-only and edge parts
N = 256
k = 2*np.pi*(np.arange(N) + 0.5)/N - np.pi
d1 = dsym(k); DX, DY, DZ = np.meshgrid(d1, d1, d1, indexing='ij'); w = np.sqrt(DX**2 + DY**2 + DZ**2)
KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
box = (np.abs(KX) <= C1) & (np.abs(KY) <= C1) & (np.abs(KZ) <= C1)
eg = np.mean(w)
print(f'  box part of e_g: {np.mean(w*box):.6f} ({np.mean(w*box)/eg:.3f} of e_g); edge part {np.mean(w*~box):.6f}')
# strain-response alternative (lattice spacing responds, not the symbol): p_strain = <q . grad w>/3
dpk = np.gradient(dsym(qq), qq)
dp1 = np.interp(k, qq, dpk)
DPX, DPY, DPZ = np.meshgrid(dp1, dp1, dp1, indexing='ij')
ps = np.mean((KX*DX*DPX + KY*DY*DPY + KZ*DZ*DPZ)/w)/3
print(f'  alternative pressure (spacing-strain response) p = <q.grad w>/3 = {ps:.6f}  (W only; e unchanged)')

# sizes
hbar, c, lP, rhoL = 1.0546e-34, 2.998e8, 1.616e-35, 5.3e-10   # RECALLED
unit = hbar*c/lP**4
print(f'\nat a = l_P: e_g = {eg*unit/rhoL:.2e} rho_Lambda;  W_g = {(4/3)*eg*unit/rhoL:.2e} rho_Lambda')
for name, cval in (('(B) harmonic, Feynman (c = 4)', 4), ('(A) harmonic, Feynman (c = 2)', 2)):
    print(f'  remainder {name}: Lambda-type energy (c - 1) e_g = {(cval-1)*eg:.6f} /a^4 = {(cval-1)*eg*unit/rhoL:.2e} rho_Lambda')
print('  a remainder below rho_Lambda would need a >= ' + f'{(eg*unit/rhoL)**0.25:.2e} l_P' + ' (for c - 1 = 1), i.e. a ~ '
      + f'{(eg*unit/rhoL)**0.25*lP:.1e} m')

# fine check of v_max in the plateau-to-edge transition (central differences away from the zone face)
q = np.linspace(0.9, 2.6, 400001); hq = 1e-6
dpq = (dsym(q+hq) - dsym(q-hq))/(2*hq)
q2 = np.linspace(0, 3.14, 200001)
print(f'[appended check] max d\'(q) - 1 on [0.9, 2.6] (central differences, h = 1e-6) = {np.max(dpq) - 1:.3e} at q = {q[np.argmax(dpq)]:.4f};  '
      f'min d\' on [0, pi) = {np.min((dsym(q2+hq)-dsym(q2-hq))/(2*hq)):.4f}')
