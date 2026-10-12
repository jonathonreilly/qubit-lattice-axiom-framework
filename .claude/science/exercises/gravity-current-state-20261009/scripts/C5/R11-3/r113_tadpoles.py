"""C5 R11-3 (a): vacuum tadpoles <T^00>, <T^ij> of free box-law scalars on Z^3 x R, zero-point (and Dirac-sea) completion.
Dispersion eps^2 = m^2 + sum_i u(k_i).  Zero-point: +eps/2 per mode (one real scalar).  Sea: -eps per mode (sign/normalisation reading).
Stress forward values:
  U (R8-2 universal, Construction A):  F^{ij}(k,k) = eps v_i v_j = p_i p_j / eps,  p = grad(eps^2/2), p_i = u'(k_i)/2
  M (minimal metric sqrt(g) g^{ij} D_i phi D_j phi):  diag u(k_i)/eps   (strain: eps^2 = m^2 + g^{ij} u_ij)
Vacuum (bilinear, quadratic H): <T^00> = <eps>/2,  <T^ij> = <F^{ij}>/2.  Isotropic: p = <T^ii>/3.
  rho = <eps>/2,  p_U = <|p|^2/eps>/6 = <eps |v|^2>/6,  p_M = <sum u / eps>/6.
Identity (proved by parts on the torus, checked here):  rho + p_U = -(1/6) < eps tr A >,  A = Hess(eps^2/2) - I, tr A = sum(u''/2 - 1).
Box = {all |k_i| <= B}; edge = complement.  <.> = zone average (= int d^3k/(2pi)^3 in lattice units a = 1).
"""
import numpy as np, time
from r113_profiles import profile, B
T0 = time.time(); out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def moments(name, m, N=200):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    u, up, upp = profile(name, k)
    inb = np.abs(k) <= B
    U2x, U2y = np.meshgrid(u, u, indexing='ij'); P1x, P1y = np.meshgrid(up/2, up/2, indexing='ij')
    A1x, A1y = np.meshgrid(upp/2-1, upp/2-1, indexing='ij'); Bx, By = np.meshgrid(inb, inb, indexing='ij')
    acc = dict(eps_b=0., eps_e=0., pU_b=0., pU_e=0., pM_b=0., pM_e=0., etrA_b=0., etrA_e=0., minint=np.inf)
    for iz in range(N):
        uz, pz, az, bz = u[iz], up[iz]/2, upp[iz]/2-1, inb[iz]
        S = U2x + U2y + uz
        eps = np.sqrt(m*m + S)
        if m == 0.0: eps = np.where(eps == 0, 1e-300, eps)
        p2 = P1x**2 + P1y**2 + pz**2
        trA = A1x + A1y + az
        box = Bx & By & bz
        for key, val in (('eps', eps), ('pU', p2/eps), ('pM', S/eps), ('etrA', eps*trA)):
            acc[key+'_b'] += val[box].sum(); acc[key+'_e'] += val[~box].sum()
        acc['minint'] = min(acc['minint'], (eps/2 + p2/(6*eps)).min())
    n3 = float(N)**3
    for kk in list(acc):
        if kk != 'minint': acc[kk] /= n3
    return acc

pr('=== (a) zero-point tadpoles per real scalar, d = 3, lattice units (a = 1); box B = %.1f ===' % B)
pr('cols: rho = <eps>/2 ; p_U = <eps v^2>/6 ; p_M = <sum u/eps>/6 ; w = p/rho ; identity check rho+p_U vs -<eps trA>/6')
res = {}
for name in ['L', 'G', 'NN']:
    for m in [1.0, 0.3, 0.0]:
        a = moments(name, m)
        rb, re_ = a['eps_b']/2, a['eps_e']/2; r = rb + re_
        pUb, pUe = a['pU_b']/6, a['pU_e']/6; pU = pUb + pUe
        pMb, pMe = a['pM_b']/6, a['pM_e']/6; pM = pMb + pMe
        idl = r + pU; idr = -(a['etrA_b'] + a['etrA_e'])/6
        res[(name, m)] = (r, pU, pM, idr)
        pr('%-2s m=%.1f: rho=%.6f (box %.6f, edge %.6f) | p_U=%.6f (box %.6f, edge %.6f) | p_M=%.6f (edge %.6f)' % (name, m, r, rb, re_, pU, pUb, pUe, pM, pMe))
        if name != 'NN':
            pr('        w_U=%.5f (box %.5f, edge %.5f) w_M=%.5f (edge %.5f) | rho+p_U=%.7f ; -<eps trA>/6=%.7f (box part %.1e) ; diff %.1e ; min integrand %.3e' % (pU/r, pUb/rb, pUe/re_, pM/r, pMe/re_, idl, idr, -a['etrA_b']/6, idl-idr, a['minint']))
        else:
            pr('        w_U=%.5f w_M=%.5f | rho+p_U=%.7f ; -<eps trA>/6=%.7f ; diff %.1e' % (pU/r, pM/r, idl, idr, idl-idr))

pr('=== continuum comparator: sharp cube |k_i|<B, eps = sqrt(m^2+k^2) (box part alone, normalised to its own rho) ===')
for m in [1.0, 0.3, 0.0]:
    N = 200; k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; kb = k[np.abs(k) <= B]
    X, Y = np.meshgrid(kb, kb, indexing='ij'); se = sp = 0.
    for kz in kb:
        e = np.sqrt(m*m + X*X + Y*Y + kz*kz); e = np.where(e == 0, 1e-300, e); se += e.sum(); sp += ((X*X+Y*Y+kz*kz)/e).sum()
    pr('  m=%.1f: w_box(cube cutoff) = %.6f  (1/3 = 0.333333 at m = 0: Akhmedov-type momentum-cutoff value)' % (m, (sp/6)/(se/2)))

pr('=== edge family u_t = (1-t)u_L + t u_G: (rho+p)/rho = 1 + w, never 0 (positivity) ===')
for m in [1.0, 0.3]:
    row = []
    for t in np.linspace(0, 1, 11):
        a = moments('T%.3f' % t, m, N=120)
        r = (a['eps_b']+a['eps_e'])/2; pU = (a['pU_b']+a['pU_e'])/6; pM = (a['pM_b']+a['pM_e'])/6
        row.append('t=%.1f: 1+w_U=%.4f 1+w_M=%.4f' % (t, 1+pU/r, 1+pM/r))
    pr('  m=%.1f: ' % m + ' | '.join(row))

pr('=== step (phase transition: one species m 1.0 -> 0.3), per real scalar, lattice units ===')
for name in ['L', 'G', 'NN']:
    r1, pU1, pM1, _ = res[(name, 1.0)]; r2, pU2, pM2, _ = res[(name, 0.3)]
    pr('  %-2s: d rho = %+.6f ; d p_U = %+.6f ; d p_M = %+.6f ; d(rho+p_U) = %+.6f ; ratio d(rho+p_U)/d rho = %.4f' % (name, r2-r1, pU2-pU1, pM2-pM1, (r2+pU2)-(r1+pU1), ((r2+pU2)-(r1+pU1))/(r2-r1)))
pr('=== independence of the two tadpole conditions across species: (rho+p_U)/rho per (profile, m) ===')
pr('  ' + ' ; '.join('%s m=%.1f: %.5f' % (n, m, (v[0]+v[1])/v[0]) for (n, m), v in res.items()))
pr('  A single counterterm with rho_ct = -p_ct (Lambda sqrt(-g)) cancels only the direction (1,-1); the vacuum vector (rho, p) is not along it for any entry above.')
pr('runtime %.1fs' % (time.time()-T0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
