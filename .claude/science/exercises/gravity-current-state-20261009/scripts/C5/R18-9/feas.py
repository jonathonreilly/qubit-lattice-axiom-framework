"""R18-9 feasibility map (sampled; not an enclosure).
Rows: T: 4S_T + 22.5F_T + 12(T0+T1 a+T2 a^2) = 0 -> a (root nearest 0, |a|<=1);  E-residual gE at that a;
      muE: gmu = 4S_mu + 22.5F_mu + 12V_mu;  mu_T2 = 0 by construction (Dirac on r*(b_f)).
For each photon edge x Dirac point: over the scalar grid, find the mu_E level set (sign change of gmu along fr at fixed b_s,
by linear interpolation) and report the E-residual range on it."""
import sys, numpy as np
ph = np.load(sys.argv[1]); dc = np.load(sys.argv[2]); sc = np.load(sys.argv[3])
NS, ND, NV = 4.0, 22.5, 12.0
bss = np.unique(sc[:, 0]); best = []
def a_of(T, rhs):
    c0, c1, c2 = T[0] - rhs, T[1], T[2]
    if abs(c2) < 1e-14: return -c0/c1
    disc = c1*c1 - 4*c2*c0
    if disc < 0: return np.nan
    r = np.array([(-c1 + np.sqrt(disc))/(2*c2), (-c1 - np.sqrt(disc))/(2*c2)])
    return r[np.argmin(abs(r))]
summary = []
for p in ph:
    bg, fw = p[0], p[1]; T = p[2:5]; E = p[5:8]; Vmu = p[8]
    for d in dc:
        bf, r, FT, FE, Fmu = d[0], d[1], d[2], d[3], d[4]
        sols = []
        for bs in bss:
            S = sc[sc[:, 0] == bs]
            gmu = NS*S[:, 4] + ND*Fmu + NV*Vmu
            for i in range(len(S) - 1):
                if gmu[i]*gmu[i+1] <= 0:
                    t = gmu[i]/(gmu[i] - gmu[i+1]); Si = S[i] + t*(S[i+1] - S[i])
                    a = a_of(T, -(NS*Si[2] + ND*FT)/NV)
                    gE = NS*Si[3] + ND*FE + NV*(E[0] + E[1]*a + E[2]*a*a)
                    sols.append((gE, a, bs, Si[1]))
        if sols:
            g = np.array([s[0] for s in sols])
            summary.append([bg, fw, bf, g.min(), g.max(), len(sols)])
        else:
            gmin = NS*sc[:, 4].min() + ND*Fmu + NV*Vmu; gmax = NS*sc[:, 4].max() + ND*Fmu + NV*Vmu
            summary.append([bg, fw, bf, np.nan, np.nan, 0 if gmax < 0 else -1])
A = np.array(summary)
ok = A[:, 5] > 0
print('photon edges %d x Dirac points %d; (edge, Dirac) pairs with a solvable mu_E row: %d' % (len(ph), len(dc), ok.sum()))
print('mu_E row unsolvable: total too negative (scalars at max) for %d pairs, too positive (scalars at min) for %d' % ((A[:, 5] == 0).sum(), (A[:, 5] == -1).sum()))
if ok.any():
    B = A[ok]
    print('E-residual on the mu_E level set: overall range [%+.4e, %+.4e]' % (np.nanmin(B[:, 3]), np.nanmax(B[:, 4])))
    print('pairs with an E-residual sign change (=> a 4-row root nearby): %d' % ((B[:, 3] <= 0) & (B[:, 4] >= 0)).sum())
    for row in B[np.argsort(-B[:, 4])][:25]:
        print('  gGw(%.2f,fw=%.2f) D1 b_f=%.3f: gE range [%+.4e, %+.4e] over %d scalar level-set points' % tuple(row))
