"""C5 R11-3: (1) V1 finite isotropic strain with the registered U coupling (R8-2/R9-2 strain flow dk_i/de = p_i(k_i) = u'(k_i)/2,
separable), E(e) = <(1/2) eps(Phi_{-e} k)> per site, physical volume per site (1+e)^3, rho(e) = E/(1+e)^3.
Linear check: p_U = -E'(0)/3 must equal <eps v^2>/6 from r113_tadpoles.out.  (2) readings: rapidity budgets, site counts."""
import numpy as np
from r113_profiles import profile
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
def flow1(k0, e, name, ns=400):
    x = k0.copy(); h = -e/ns
    f = lambda y: 0.5*profile(name, y)[1]
    for _ in range(ns):
        a1 = f(x); a2 = f(x+h/2*a1); a3 = f(x+h/2*a2); a4 = f(x+h*a3); x = x + h/6*(a1+2*a2+2*a3+a4)
    return x
def E(e, name, m, N=96):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    u = profile(name, flow1(k, e, name))[0]
    Ux, Uy = np.meshgrid(u, u, indexing='ij'); acc = 0.
    for uz in u: acc += np.sqrt(m*m + Ux + Uy + uz).sum()
    return 0.5*acc/float(N)**3
for name in ['L', 'G']:
    for m in [1.0, 0.0]:
        h = 2e-3; E0 = E(0, name, m); Ep = (E(h, name, m) - E(-h, name, m))/(2*h)
        line = '  %s m=%.1f: rho(0)=%.5f, p_U(lin, flow) = -E\'(0)/3 = %.5f ;' % (name, m, E0, -Ep/3)
        for e in [0.1, 0.5, 1.0]:
            r = E(e, name, m)/(1+e)**3
            rp = E(e+h, name, m)/(1+e+h)**3; rm = E(e-h, name, m)/(1+e-h)**3
            w = -(np.log(rp)-np.log(rm))/(2*h)*(1+e)/3 - 1
            line += ' e=%.1f: rho=%.4e w=%.3f res=%+.3e ;' % (e, r, w, r - E0)
        pr(line)
pr('  (res = rho(e) - rho(0): residual after a constant Lambda counterterm tuned at e = 0)')
pr('=== readings: rapidity budget and site counts (inputs RECALLED: m_p = 0.938 GeV, M_Pl = 1.221e19 GeV, l_P = 1.616e-35 m, H0 = 2.2e-18 /s, t_P = 5.39e-44 s, R_obs = 4.4e26 m) ===')
Bbox, mp, MPl = 2.0, 0.938, 1.221e19
eta = lambda a_over_lP: np.arcsinh(Bbox*MPl/(mp*a_over_lP))
pr('  proton budget eta* = asinh(B/(a m_p)): a = l_P: %.2f ; V1 with a = l_P today: z=1e9 (BBN) spacing 1e-9 l_P -> %.2f ; after 35 e-folds of future dS: %.2f' % (eta(1), eta(1e-9), eta(np.exp(35))))
pr('  V1 if a = l_P at T ~ M_Pl: today a ~ (T_P/T_0) l_P = %.2e l_P = %.2e m; box edge momentum B/a = %.2e eV' % (1.221e19/2.35e-13, 1.616e-35*1.221e19/2.35e-13, Bbox*1.97327e-7/(1.616e-35*1.221e19/2.35e-13)))
V = 4*np.pi/3*(4.4e26)**3; N = V/(1.616e-35)**3
pr('  V2/V3 + site creation at fixed a = l_P: sites in the observable universe today N = %.2e (cf. R4-5 cap 8.24e184, TESTS:2941); creation rate 3 H0 N = %.2e /s; per site per Planck time 3 H0 t_P = %.2e' % (N, 3*2.2e-18*N, 3*2.2e-18*5.39e-44))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
