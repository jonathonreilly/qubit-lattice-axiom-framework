"""R17-13 cloud: necessary-condition / candidate search for the 4-row SM-count root (22.5 Dirac + 4 scalars + 12 VM vectors).
Dirac cloud: points ON the mu_T2^F = 0 set (D1 curve from curve2.out/curve1.out, DG manifold dgman.npy).  Scalars: scalgrid.npy (U, G_w).
Photons: photgrid.npy (VM, gammaGw, N=48).  For each Dirac point F and scalar S, the photon needed is P* = -(22.5 F + 4 S)/12;
report the nearest photon grid point (relative distance) -- candidates for the local solve; not a proof of anything."""
import re, numpy as np
dirac = []
for fn in ('curve2.out', 'curve1.out'):
    for line in open(fn):
        mm = re.search(r'b[*]?=([\d.]+) r[*]?=([\d.]+).*?T2g ([-+.\de]+) Eg ([-+.\de]+) muE ([-+.\de]+)', line)
        if mm and 'VM root' not in line:
            b, r, T, E, mu = map(float, mm.groups()); dirac.append(('D1', b, 0.0, r, T, E, mu))
for row in np.load('dgman.npy'):
    dirac.append(('DG', row[0], row[1], row[2], row[3], row[4], row[5]))
S = np.load('scalgrid.npy'); P = np.load('photgrid.npy')
print('Dirac points on mu_T2=0: %d (D1 %d, DG %d); scalars %d; photons %d' % (len(dirac), sum(d[0] == 'D1' for d in dirac), sum(d[0] == 'DG' for d in dirac), len(S), len(P)))
scale = np.array([5e-3, 2e-2, 5e-3])   # typical per-vector magnitudes for the relative distance
best = []
for d in dirac:
    F = np.array(d[4:7])
    for s in S:
        Pstar = -(22.5*F + 4*s[2:5])/12
        dist = np.sqrt((((P[:, 2:5] - Pstar)/scale)**2).sum(1)); j = np.argmin(dist)
        best.append((dist[j], d, tuple(s[:2]), tuple(P[j, :2]), Pstar, P[j, 2:5]))
best.sort(key=lambda x: x[0])
seen = set(); k = 0
for x in best:
    key = (x[1][0], x[1][1], x[1][2])
    if key in seen: continue
    seen.add(key); k += 1
    print('dist %.3f | Dirac %s(b=%.2f,w=%.2f,r*=%.4f) | scalar (b_s=%.2f,fr=%.2f) | photon (b=%.2f,fw=%.2f) | P* %s vs grid %s' % (x[0], x[1][0], x[1][1], x[1][2], x[1][3], *x[2], *x[3], np.array2string(x[4], precision=4), np.array2string(x[5], precision=4)))
    if k >= 15: break
# D1-only necessary condition (mu_E row): max over scalars/photons of 4 S_mu + 12 P_mu subject to the T2g row
d1 = [d for d in dirac if d[0] == 'D1']
for d in d1[:3] + d1[-2:]:
    F = np.array(d[4:7]); need = -22.5*F
    ok = [(4*s[4] + 12*p[4], 4*s[2] + 12*p[2]) for s in S for p in P]
    feas = [a for a, t in ok if abs(t - need[0]) < 0.25*abs(need[0]) + 2e-3]
    print('D1(b=%.3f, r*=%.4f): rows needed from scalars+vectors (T2g, Eg, muE) = %s ; max (4S_mu+12P_mu) among combos meeting the T2g row within 25%%: %s' % (d[1], d[3], np.array2string(need, precision=4), ('%+.4f' % max(feas)) if feas else 'none'))
