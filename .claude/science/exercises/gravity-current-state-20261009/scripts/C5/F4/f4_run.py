"""F4 (b): additive-mass E_g Hessian per path family on F1's SF-strained root law (branch B1: Dirac flow at m = 0.01, photon own flow,
Feynman gauge, critical m = 0 at t = 0).  Evenness in t is exact for every family (C2 about [110] maps each family to itself), so
Hess = 2[f(d) - f(0)]/d^2, Richardson over d, 2d.  Families: P = Psym (F1), J = Psym-J, S<M> = M-round staircase (W-average),
SL = straight line (M -> inf, fit f(M) = f_inf + c/M^2 on the two largest M).  Mixtures: V = (1-lam) V_a + lam V_b.
usage: f4_run.py label n hmax mph d nrk root(R|0) M1,M2,... [fb]   (fb: add staircase-corner panel breaks)
"""
import numpy as np, time, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f4_lib import *
lab, n, hm, mph, d, nrk, rt, Ms = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), \
    int(sys.argv[6]), sys.argv[7], tuple(int(v) for v in sys.argv[8].split(','))
root = ROOT if rt == 'R' else ROOT0
F = Ferm(*root, mflow=0.01); G = Phot(CPH)
fbarg = sys.argv[9] if len(sys.argv) > 9 else ''
fb = fbarg.startswith('fb')
fbMs = tuple(M for M in Ms if (fbarg[2:] == '' or M <= int(fbarg[2:])))
g = mkgrid(root[0], n, hm, mph, fbMs if fb else None)
print('[%s] root %s, grid n=%d hmax=%.2f mph=%d fracbreaks=%s (%d nodes), d=%.4f, nrk=%d, Ms=%s' % (lab, root, n, hm, mph, (fbMs if fb else None), len(g.x), d, nrk, Ms), flush=True)
T0 = time.time()
Ps = {}
for t in (0.0, d, 2*d):
    t1 = time.time()
    Ps[t] = pieces(F, G, g, t, Ms=Ms, nrk=nrk)
    print('  pass t=%.4f done (%.0fs)' % (t, time.time() - t1), flush=True)
json.dump({str(t): dict(base=P['base'], Tad={str(k): v for k, v in P['Tad'].items()}, E={str(k): v for k, v in P['E'].items()})
           for t, P in Ps.items()}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw_%s.json' % lab), 'w'), indent=1)
def H(fn):
    f0, f1, f2 = fn(Ps[0.0]), fn(Ps[d]), fn(Ps[2*d])
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    return f0, (4*h1 - h2)/3, h1, h2
res = {}
fams = [('P (Psym, F1)', lambda P: fam_dm(P, 1, ('M', 1))), ('J (Psym-J)', lambda P: fam_dm(P, 1, 'J'))]
fams += [('S%d (staircase M=%d)' % (M, M), (lambda M: (lambda P: fam_dm(P, M, ('M', M))))(M)) for M in Ms if M > 1]
for name, fn in fams:
    f0, hr, h1, h2 = H(fn)
    res[name] = hr
    print('  %-22s dm %+.12f  Hess_t (d) %+.8e (2d) %+.8e  Rich %+.8e  [x4 %+.6e]' % (name, f0, h1, h2, hr, 4*hr), flush=True)
HP = res['P (Psym, F1)']
print('  differences from P (Rich):')
for name in res:
    if name != 'P (Psym, F1)':
        print('    %-22s  H - H_P = %+.6e   rel %+.4e' % (name, res[name] - HP, (res[name] - HP)/HP))
# parts: tadpole vs exchange
for name, a, s in [('P', 1, ('M', 1)), ('J', 1, 'J')] + [('S%d' % M, M, ('M', M)) for M in Ms if M > 1]:
    _, ht, _, _ = H(lambda P: P['Tad'][s]); _, he, _, _ = H(lambda P: P['E'][(a, a)])
    print('    parts %-4s Hess tadpole %+.6e  exchange(fam) %+.6e' % (name, ht, he))
_, hb, _, _ = H(lambda P: P['base']); print('    common exchange base part Hess %+.6e' % hb)
# SL extrapolation
Mh = [M for M in Ms if M > 1]
if len(Mh) >= 2:
    a, b = Mh[-2], Mh[-1]
    fa, fb = res['S%d (staircase M=%d)' % (a, a)], res['S%d (staircase M=%d)' % (b, b)]
    c = (fa - fb)/(1/a**2 - 1/b**2); finf = fb - c/b**2
    print('  SL (M->inf, c/M^2 fit on M=%d,%d): Hess %+.8e  H - H_P %+.6e rel %+.4e  (c = %+.3e)' % (a, b, finf, finf - HP, (finf - HP)/HP, c))
    if len(Mh) >= 3:
        a2, b2 = Mh[-3], Mh[-2]
        fa2, fb2 = res['S%d (staircase M=%d)' % (a2, a2)], res['S%d (staircase M=%d)' % (b2, b2)]
        c2 = (fa2 - fb2)/(1/a2**2 - 1/b2**2); print('     (fit on M=%d,%d: %+.8e)' % (a2, b2, fb2 - c2/b2**2))
    res['SL'] = finf
# mixtures: P <-> S_Mmax (W-average, signed weights allowed): H(lam) = HP + L lam + Q lam^2
for b in Mh[-1:]:
    hm1 = H(lambda P: mix_dm(P, 1, b, -1.0, ('M', 1), ('M', b)))[1]
    hp1 = res['S%d (staircase M=%d)' % (b, b)]
    Q = 0.5*(hp1 + hm1) - HP; L = 0.5*(hp1 - hm1)
    roots = np.roots([Q, L, HP]) if abs(Q) > 0 else np.array([-HP/L])
    print('  mixture P<->S%d: H(lam) = %+.6e %+.6e lam %+.6e lam^2 ; zeros at lam = %s' % (b, HP, L, Q, roots))
LJ = res['J (Psym-J)'] - HP
print('  mixture P<->J (seagull only, exactly linear): H(lam) = %+.6e %+.6e lam ; zero at lam = %+.4e' % (HP, LJ, -HP/LJ))
print('[%s] total %.0f s' % (lab, time.time() - T0), flush=True)
