"""R19-11 (a) fits and (c) SM-mass residuals of the m->0+ law.
Inputs: mscan_*.out files (rows vs m per field), vmu.out (vector mu_E vs mass).
(a) Dirac: fit row(m) = c0 + c1 m + c2 m^2 [+ c3 m^3] and, separately, + d m^2 ln m; scalars/vectors: c0 + c1 m + c2 m^2 + c4 m^4 (+ d m^2 ln m).
(c) residual R = sum_i n_i [row(m_i a) - row(0)], masses RECALLED (PDG-like, GeV), a = l_P (m a = m / 1.22089e19 GeV).
Conversions (reading; R9-9 normalization as quoted at C5_R16-3_report.md:276): c_T^2 - 1 = 16 pi Xi  ->  dc = 8 pi Xi;
mass-type rows: omega^2 = q^2 + 16 pi mu (same prefactor, a graviton mass only for a supplied dynamical metric, PRICE_NOTE:22),
so dc(omega) = 8 pi mu / (omega a)^2 at f = 100 Hz (omega a = 2 pi 100 Hz * 5.391e-44 s)."""
import sys, re, numpy as np
MP = 1.22089e19
def parse(fn, keys):
    D = {}
    for line in open(fn):
        mm = re.match(r'm=(\S+)', line)
        if not mm: continue
        m = float(mm.group(1)); vals = {}
        for k in keys:
            hit = re.findall(r'%s ([+-]\d\.\d+e[+-]\d+)' % k, line)
            if hit: vals[k] = float(hit[0])
        D[m] = vals
    return D
def fit(ms, ys, basis):
    A = np.array([[b(m) for b in basis] for m in ms]); c, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return c, np.abs(A@c - ys).max()
L = lambda m: m*m*np.log(m) if m > 0 else 0.0
out = {}
def do(fn, keys, kind, mmax):
    D = parse(fn, keys); ms = sorted(m for m in D if m <= mmax)
    print('== %s (%s), m in [%g, %g], %d points' % (fn, kind, min(ms), max(ms), len(ms)))
    for k in keys:
        mk = [m for m in ms if k in D[m]]; y = np.array([D[m][k] for m in mk])
        if kind == 'dirac':
            b1 = [lambda m: 1, lambda m: m, lambda m: m*m, lambda m: m**3]
        else:
            b1 = [lambda m: 1, lambda m: m, lambda m: m*m, lambda m: m**4]
        c, e = fit(mk, y, b1); c2_, e2 = fit(mk, y, b1 + [L])
        print('  %-6s c0 %+.10e c1 %+.5e c2 %+.5e c3/c4 %+.3e | maxres %.1e || with m^2 ln m: d %+.3e (c1 %+.5e c2 %+.4e) maxres %.1e'
              % (k, c[0], c[1], c[2], c[3], e, c2_[4], c2_[1], c2_[2], e2))
        out[(kind, k)] = c
    return D
fd, fs = sys.argv[1], sys.argv[2]
do(fd, ['T2g', 'Eg', 'muE', 'muT2', 'face1', 'face2', 'd1', 'd2'], 'dirac', 2.6e-3)
do(fs, ['T2g', 'Eg', 'muE', 'face1', 'face2', 'd1'], 'scalar', 2.6e-2)
do('vmu.out', ['vector'], 'vector', 2.6e-2) if False else None
V = {}
for line in open('vmu.out'):
    mm = re.match(r'm=(\S+)\s+muE/vector (\S+)', line); V[float(mm.group(1))] = float(mm.group(2))
vm = sorted(m for m in V if m <= 0.026); cv, ev = fit(vm, np.array([V[m] for m in vm]), [lambda m: 1, lambda m: m, lambda m: m*m, lambda m: m**4])
print('== vector muE (per vector): c0 %+.10e c1 %+.3e c2 %+.5e c4 %+.3e maxres %.1e' % (*cv, ev))
# SM spectrum (RECALLED), GeV, with counts in the 4 + 22.5 + 12 bookkeeping
dirac = [(3, 172.69), (3, 4.18), (3, 1.27), (3, 0.0934), (3, 0.00467), (3, 0.00216), (1, 1.77686), (1, 0.1056584), (1, 0.000511), (1.5, 1e-10)]
scal_F = [(1, 125.25), (2, 80.377), (1, 91.1876)]   # Feynman-'t Hooft Goldstones; Landau gauge: Goldstones massless
scal_L = [(1, 125.25)]
vec = [(2, 80.377), (1, 91.1876)]
S1 = sum(n*m/MP for n, m in dirac); S2 = sum(n*(m/MP)**2 for n, m in dirac)
print('\nDirac: sum n m a = %.4e, sum n (m a)^2 = %.4e ; top m a = %.4e' % (S1, S2, 172.69/MP))
s2F = sum(n*(m/MP)**2 for n, m in scal_F); s2L = sum(n*(m/MP)**2 for n, m in scal_L); v2 = sum(n*(m/MP)**2 for n, m in vec)
print('scalar edge: sum (m a)^2 = %.4e (Feynman gauge) / %.4e (Landau) ; vectors sum (m a)^2 = %.4e' % (s2F, s2L, v2))
wa = 2*np.pi*100*5.391e-44
print('omega a at 100 Hz = %.4e' % wa)
print('\n(c) residuals of the m->0+ law at the SM spectrum (per row, totals):')
rows = ['T2g', 'Eg', 'face1', 'face2', 'muE', 'muT2']
for k in rows:
    cd = out.get(('dirac', k)); cs = out.get(('scalar', k))
    Rd = cd[1]*S1 + cd[2]*S2 if cd is not None else 0.0
    Rs = cs[2]*s2F if cs is not None else 0.0
    Rv = cv[2]*v2 if k == 'muE' else float('nan')
    tot = Rd + Rs + (Rv if k == 'muE' else 0.0)
    if k.startswith('mu'):
        print('  %-5s Dirac %+.3e scalar %+.3e vector %+.3e TOTAL %+.3e -> 16 pi mu = %.2e (a=l_P units); dc at 100 Hz = 8 pi mu/(omega a)^2 = %.2e (GW170817 band 7e-16)'
              % (k, Rd, Rs, Rv, tot, 16*np.pi*abs(tot), 8*np.pi*abs(tot)/wa**2))
    else:
        print('  %-5s Dirac %+.3e scalar %+.3e vector (not computed; massless evaluator) TOTAL(D+S) %+.3e -> dc = 8 pi Xi = %.2e (GW170817 7e-16; R16-2 photon comparator 2.66e-19)'
              % (k, Rd, Rs, tot, 8*np.pi*abs(tot)))
print('\nthresholds: |Xi| <= 7e-16/(8 pi) = %.2e (GW170817 upper), 2.66e-19/(8 pi) = %.2e (R16-2); |mu| <= 7e-16 (omega a)^2/(8 pi) = %.2e'
      % (7e-16/(8*np.pi), 2.66e-19/(8*np.pi), 7e-16*wa**2/(8*np.pi)))
