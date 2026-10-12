"""C5 R11-3: (i) mass-step coefficients of the two tadpoles (small m), (ii) V1 finite strain (M coupling) and the residual after a
Lambda counterterm, (iii) physical sizes at a = l_P (readings).  Zone averages over d = 3, N^3 midpoint grid.
c_rho = d rho/d m^2 = <1/(4 eps)>, c_pU = d p_U/d m^2 = -<|p|^2/(12 eps^3)>, c_pM = -<sum u/(12 eps^3)>, at m -> 0 (m = 1e-3 used).
"""
import numpy as np
from r113_profiles import profile
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
def zone(name, m, N, f):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; u, up, upp = profile(name, k)
    Ux, Uy = np.meshgrid(u, u, indexing='ij'); Px, Py = np.meshgrid(up/2, up/2, indexing='ij'); acc = 0.
    for iz in range(N):
        S = Ux + Uy + u[iz]; eps = np.sqrt(m*m + S); p2 = Px**2 + Py**2 + (up[iz]/2)**2
        acc += f(eps, S, p2).sum()
    return acc/float(N)**3
pr('=== (i) small-m step coefficients (lattice units, per real scalar; Delta rho = c_rho Delta m^2/a^2 etc.) ===')
for name in ['L', 'G', 'NN']:
    for N in [160, 240]:
        m = 1e-3
        cr = zone(name, m, N, lambda e, S, p2: 1/(4*e))
        cpU = zone(name, m, N, lambda e, S, p2: -p2/(12*e**3))
        cpM = zone(name, m, N, lambda e, S, p2: -S/(12*e**3))
        pr('  %-2s N=%d: c_rho=%.5f c_pU=%+.5f c_pM=%+.5f | c_pU/c_rho=%+.4f c_pM/c_rho=%+.4f (w=-1 would need -1)' % (name, N, cr, cpU, cpM, cpU/cr, cpM/cr))
pr('=== (ii) V1 finite isotropic strain, M coupling: physical spacing a = lam (comoving cutoff fixed), mass fixed in units 1/a0 ===')
pr('    E(lam) = <(1/2) sqrt(m^2 + sum u / lam^2)> per site ; rho(lam) = E/lam^3 ; w_eff = -dln rho/(3 dln lam) - 1')
for name in ['L', 'G']:
    for m in [0.0, 1.0]:
        lams = [0.5, 0.9, 1.0, 1.1, 2.0, 10.0]
        rhos = [zone(name, m, 96, lambda e, S, p2, l=l: 0.5*np.sqrt(m*m + S/l**2))/l**3 for l in lams]
        r1 = rhos[2]
        weff = []
        for l in lams:
            h = 1e-3
            rp = zone(name, m, 96, lambda e, S, p2, l=l*(1+h): 0.5*np.sqrt(m*m + S/l**2))/(l*(1+h))**3
            rm = zone(name, m, 96, lambda e, S, p2, l=l*(1-h): 0.5*np.sqrt(m*m + S/l**2))/(l*(1-h))**3
            weff.append(-(np.log(rp)-np.log(rm))/(2*h)/3 - 1)
        pr('  %s m=%.1f: ' % (name, m) + ' ; '.join('lam=%.1f rho=%.4e w=%.3f res=%+.3e' % (l, r, wv, r - r1) for l, r, wv in zip(lams, rhos, weff)))
pr('    res = rho(lam) - rho(1): what is left after a constant (Lambda) counterterm tuned at lam = 1.')
pr('=== (iii) sizes (readings; inputs RECALLED/repo: M_Pl = 1.221e19 GeV, rho_Lambda = 2.52e-47 GeV^4 per C5_O3_report.md:40) ===')
MPl = 1.221e19; rL = 2.52e-47
pr('  1/a^4 at a = l_P: %.3e GeV^4 = %.2e rho_Lambda' % (MPl**4, MPl**4/rL))
for dm2, lab in [((100.)**2, 'Delta m^2 = (100 GeV)^2'), ((0.2)**2, 'Delta m^2 = (0.2 GeV)^2 (QCD-like)')]:
    pr('  %s, c ~ 0.1: Delta rho ~ %.2e GeV^4 = %.2e rho_Lambda (vs Lemma PT tree EW shift 1.19e8 GeV^4 = 4.7e54 rho_Lambda)' % (lab, 0.1*dm2*MPl**2, 0.1*dm2*MPl**2/rL))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
