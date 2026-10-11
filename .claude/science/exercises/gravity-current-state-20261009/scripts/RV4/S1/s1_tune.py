"""Find a local cubic symbol u (P = energy current) with mu_E = mu_T2 = 0 at m = 1, then show it is a tuning:
the zero moves with m, and the DOS change at the critical points is nonzero."""
import numpy as np, warnings
from scipy.optimize import brentq
warnings.filterwarnings('ignore')
src = open('s1_checks.py').read().split("out = []")[0]
exec(src)
out = []
def P(*s):
    line = ' '.join(str(q) for q in s); print(line); out.append(line)
N = 48
P('separable family u = c + a c^2 (monotone bands need a > -1/4): muE(m=1) at a = -0.249:', mu_channels(1.0, N, a=-0.249))
P('separable, non-monotone a = -0.4, -0.6:', mu_channels(1.0, N, a=-0.4), mu_channels(1.0, N, a=-0.6), 'min u', umin(-0.6,0,0))
def bzero(g, ch):
    f = lambda b: mu_channels(1.0, N, b=b, g=g)[ch]
    return brentq(f, 0.0, 0.2, xtol=1e-12)
P('g, b_E(g), b_T2(g):')
rows = []
for g in (0.2, 0.5, 1.0, 2.0, 4.0):
    try:
        bE = bzero(g, 0); bT = bzero(g, 1)
    except ValueError as e:
        P(g, 'no bracket', e); continue
    rows.append((g, bE, bT)); P(f'  g={g}: b_E={bE:.6f}  b_T2={bT:.6f}  diff={bE-bT:+.3e}')
def diff(g):
    return bzero(g, 0) - bzero(g, 1)
gs = brentq(diff, rows[0][0], rows[-1][0], xtol=1e-10) if np.sign(rows[0][1]-rows[0][2]) != np.sign(rows[-1][1]-rows[-1][2]) else None
P('root g* =', gs)
if gs is not None:
    bs = bzero(gs, 0)
    P(f'tuned symbol: g*={gs:.8f}, b*={bs:.8f}; mu at m=1, N=48:', mu_channels(1.0, 48, b=bs, g=gs), ' N=96:', mu_channels(1.0, 96, b=bs, g=gs))
    P('min u:', umin(0, bs, gs, N=64))
    P('mass dependence of the tuned symbol (muE, muT2), RN-L1 norm:')
    for m in (0.05, 0.2, 0.5, 1.0, 2.0, 4.0):
        Nm = 160 if m < 0.3 else 64
        P(f'   m={m}: {mu_channels(m, Nm, b=bs, g=gs)}')
    P('TRIM Hessians (Theorem C needs Hess ~ I at every nondegenerate critical point):')
    for name, pt in (('G', (0, 0, 0)), ('X', (np.pi, 0, 0)), ('M', (np.pi, np.pi, 0)), ('R', (np.pi, np.pi, np.pi))):
        K = [np.array([[[pt[0]]]]), np.array([[[pt[1]]]]), np.array([[[pt[2]]]])]
        u, gu, H = symbol(K, 0.0, bs, gs)
        HH = np.array([[float(H[i][j].ravel()[0]) for j in range(3)] for i in range(3)])
        P(f'   {name}: u={float(u.ravel()[0]):.4f} Hess eig={np.linalg.eigvalsh(HH)}  psi_E1={HH[0,0]-HH[1,1]:+.4f} psi_E2={(HH[0,0]+HH[1,1]-2*HH[2,2])/np.sqrt(3):+.4f}')
    # second-order DOS (cumulative) for tuned symbol, E and T2
    K = grid(96); u, gu, H = symbol(K, 0.0, bs, gs)
    for lab, phi, psi in (('E', gu[0]**2-gu[1]**2, H[0][0]-H[1][1]), ('T2', 2*gu[0]*gu[1], 2*H[0][1])):
        edges = np.linspace(u.min(), u.max(), 13)[1:]
        C = np.array([-(1/4)*np.mean(phi*psi*(u < e)) for e in edges])
        P(f'   cumulative 2nd-order DOS change C_{lab}(E) at 12 levels:', np.array2string(C, precision=2))
with open('s1_tune.out', 'w') as f:
    f.write('\n'.join(out) + '\n')
