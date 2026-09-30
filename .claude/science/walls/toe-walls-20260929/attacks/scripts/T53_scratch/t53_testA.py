"""T53 Test A: the four sheets (gamma sign x sigma pairing). Pre-registered in PREREGISTER.md."""
import numpy as np, math
from chart import obs, preimage, SQ
np.random.seed(7)
SIGMAS = {'210': (2, 1, 0), '201': (2, 0, 1)}
GAMMAS = {'g+': 0.5, 'g-': -0.5}
tol = 1e-9
rows = []
# ---- algebra checks on random chart points (chamber interior and exterior alike)
bad = dict(A1=0, A2=0, A3=0, A4=0)
N = 400
for _ in range(N):
    m, d, q = np.random.uniform(0.2, 1.2), np.random.uniform(0.7, 1.1), np.random.uniform(0.4, 0.9)
    S = {(g, s): obs(m, d, q, GAMMAS[g], SIGMAS[s]) for g in GAMMAS for s in SIGMAS}
    ref = S[('g+', '210')]
    for k, o in S.items():
        if abs(o['s12'] - ref['s12']) > tol or abs(o['s13'] - ref['s13']) > tol: bad['A1'] += 1; break
    if abs(S[('g+', '201')]['s23'] - (1 - ref['s23'])) > tol or abs(S[('g-', '201')]['s23'] - (1 - ref['s23'])) > tol or abs(S[('g-', '210')]['s23'] - ref['s23']) > tol: bad['A2'] += 1
    if not (abs(S[('g-', '210')]['sind'] + ref['sind']) < 1e-7 and abs(S[('g+', '201')]['sind'] + ref['sind']) < 1e-7 and abs(S[('g-', '201')]['sind'] - ref['sind']) < 1e-7): bad['A3'] += 1
    if abs(S[('g-', '210')]['cosd'] - ref['cosd']) > 1e-7 or abs(S[('g-', '201')]['cosd'] - S[('g+', '201')]['cosd']) > 1e-7: bad['A4'] += 1
print('algebra violations over', N, 'random chart points:', bad)

# ---- the four sheets at the repo anchor pin (0.307,0.0218,0.545 pin, interior)
pin = (0.657061342210, 0.933806343759, 0.715042329587)
print('\nFour sheets at the repo 3-angle pin', pin)
print('%-8s %-6s %8s %8s %8s %9s %9s %9s' % ('gamma', 'sigma', 's12^2', 's13^2', 's23^2', 'sin d', 'cos d', 'dCP deg'))
for g in GAMMAS:
    for s in SIGMAS:
        o = obs(*pin, GAMMAS[g], SIGMAS[s])
        print('%-8s %-6s %8.5f %8.5f %8.5f %9.5f %9.5f %9.3f' % (g, s, o['s12'], o['s13'], o['s23'], o['sind'], o['cosd'], o['dcp']))

# ---- chamber-boundary Basin-1 preimage of the NuFIT-6.1 rectangle: four sheets
S12 = np.linspace(0.2893, 0.3295, 9)
S13 = np.linspace(0.02070, 0.02420, 9)
out = {(g, s): dict(dcp=[], s23=[], sind=[]) for g in GAMMAS for s in SIGMAS}
fails = 0
for a in S12:
    for b in S13:
        roots = preimage(a, b)
        if len(roots) != 1: fails += 1; print('non-unique/failed', a, b, len(roots)); continue
        m, d = roots[0]; q = SQ - d
        for g in GAMMAS:
            for s in SIGMAS:
                o = obs(m, d, q, GAMMAS[g], SIGMAS[s])
                out[(g, s)]['dcp'].append(o['dcp']); out[(g, s)]['s23'].append(o['s23']); out[(g, s)]['sind'].append(o['sind'])
print('\npreimage solve failures:', fails, 'of', len(S12) * len(S13))
# repo-quoted NuFIT-6.1 comparators
R61 = dict(s23_best=0.470, s23_3s=(0.432, 0.587), s23_3s_sk=(0.435, 0.584), d_best=(207., 212.), d_3s=(114., 405.), d_3s_sk=(125., 365.))
print('\nSheet summaries over the NuFIT-6.1 (s12^2,s13^2) rectangle (float, Basin 1, chamber boundary):')
print('%-8s %-6s %-22s %-22s %-22s' % ('gamma', 'sigma', 'dCP range (deg)', 's23^2 range', 'sin d range'))
summ = {}
for (g, s), v in out.items():
    dc = np.array(v['dcp']); s23 = np.array(v['s23']); sd = np.array(v['sind'])
    # dCP as angle in [0,360)
    dcr = (dc.min(), dc.max()); s23r = (s23.min(), s23.max()); sdr = (sd.min(), sd.max())
    in_d = all(R61['d_3s_sk'][0] <= (x if x >= 100 else x + 360) <= R61['d_3s_sk'][1] for x in dc) or all(R61['d_3s'][0] <= (x if x >= 100 else x + 360) <= R61['d_3s'][1] for x in dc)
    in_d_sk = all(R61['d_3s_sk'][0] <= (x if x >= 100 else x + 360) <= R61['d_3s_sk'][1] for x in dc)
    in_s = all(R61['s23_3s_sk'][0] <= x <= R61['s23_3s_sk'][1] for x in s23)
    in_s_nosk = all(R61['s23_3s'][0] <= x <= R61['s23_3s'][1] for x in s23)
    summ[f'{g}/{s}'] = dict(dcp=[round(dcr[0], 2), round(dcr[1], 2)], s23=[round(s23r[0], 4), round(s23r[1], 4)], sind=[round(sdr[0], 4), round(sdr[1], 4)],
                            dcp_in_3sigma_noSK=bool(in_d), dcp_in_3sigma_SK=bool(in_d_sk), s23_in_3sigma_noSK=bool(in_s_nosk), s23_in_3sigma_SK=bool(in_s))
    print('%-8s %-6s [%7.2f,%7.2f]       [%.4f,%.4f]       [%.4f,%.4f]   dCP3s(noSK/SK)=%s/%s s23_3s(noSK/SK)=%s/%s' %
          (g, s, dcr[0], dcr[1], s23r[0], s23r[1], sdr[0], sdr[1], in_d, in_d_sk, in_s_nosk, in_s))
import json
json.dump(dict(algebra_violations=bad, sheets=summ, comparators=R61), open('testA_result.json', 'w'), indent=1)
