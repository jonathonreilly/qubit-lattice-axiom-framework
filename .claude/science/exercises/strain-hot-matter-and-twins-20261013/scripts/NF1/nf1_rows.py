"""NF-1 (d): the four cone/shear rows for the staggered edge, and a sampled re-solve map (estimate; R18-9's method and archived scans).
Staggered rows per field = 1/4 of the naive (r = 0) D1(b_f, 0) rows per 4-component field: the Kawamoto-Smit map takes the naive law to
4 identical staggered copies for any per-axis odd-range operator; UD (the SF generator) is of that form at r = 0 (E_g: alpha_j s'(k_j) p_j(k_j);
T2g: alpha_x s'(k_x) p_y(k_y), p_y = s s' even-harmonic -> even hop along y, odd along x), and the SF free energies are traces.
Rows (R18-9): Xi_T2g, Xi_Eg, mu_E, mu_T2 per field at m = 0.01 (archived smud_lib.dirac, UD vertex, dfam GL (3,8)).
mu_T2 = 0 for every separable band (R18-9 (S1)); the staggered band E^2 = sum s(k_j)^2 + m^2 is separable.
Re-solve map: R18-9's feas.py logic, with the Dirac weight 22.5 replaced by w_F = N_s/4 (N_s staggered fields) and the r* curve replaced by
r = 0 (mu_T2 = 0 identically): rows Xi_T2g (solved by the stencil a), mu_E (scalar level set), Xi_Eg residual reported.
argv: q1 q2 (GL panels, nodes)"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
os.chdir(os.path.join(HERE, '..', 'flat'))
import smud_lib
t00 = time.time()
q = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (3, 8)
AR = os.path.join(HERE, '..', 'arch', 'R18-9')
m = 0.01
print('NF-1 (d) rows: naive D1(b_f, r=0) per 4-comp field under UD at m = %g, GL %s; staggered per field = 1/4 of these' % (m, q), flush=True)
rows = []
for bf in (0.3, 0.5, 0.7, 0.8, 0.9, 0.909103708, 1.0, 1.1, 1.2, 1.3, 1.4):
    F = smud_lib.dirac(bf, 0.0, m=m, q=q)
    rows.append([bf, 0.0, *F])
    print('  b_f=%.6f naive: T2g %+.6e Eg %+.6e muE %+.6e muT2 %+.1e | staggered/field: T2g %+.6e Eg %+.6e muE %+.6e'
          % (bf, *F, *(F[:3]/4)), flush=True)
R = np.array(rows); np.save(os.path.join(HERE, 'nf1_rows_naive.npy'), R)
# reference: Wilson root rows per field (R18-9 record at N = 224: T +1.98457e-3, E +1.3215e-4, muE -1.70941e-2)
Fw = smud_lib.dirac(0.909103708, 0.555604226, m=m, q=q)
print('  check: Wilson root D1(0.909103708, 0.555604226): T2g %+.6e Eg %+.6e muE %+.6e muT2 %+.1e  (R18-9 record +1.98457e-3, +1.3215e-4, -1.70941e-2)' % tuple(Fw))

# ---- sampled re-solve map ----
ph = np.load(os.path.join(AR, 'photscan_N48.npy')); sc = np.load(os.path.join(AR, 'scalscan_m0.01.npy'))
p160 = np.load(os.path.join(AR, 'photres2_N160_parsed.npy'))
NS, NV = 4.0, 12.0
bss = np.unique(sc[:, 0])
def a_of(T, rhs):
    c0, c1, c2 = T[0] - rhs, T[1], T[2]
    if abs(c2) < 1e-14: return -c0/c1
    disc = c1*c1 - 4*c2*c0
    if disc < 0: return np.nan
    r = np.array([(-c1 + np.sqrt(disc))/(2*c2), (-c1 - np.sqrt(disc))/(2*c2)])
    return r[np.argmin(abs(r))]
dc = np.column_stack([R[:, 0], R[:, 1], R[:, 2]/4, R[:, 3]/4, R[:, 4]/4])      # per staggered field
PH = np.vstack([ph, p160])
print('\n  per-species budget: scalar mu_E in [%.3e, %.3e] (x4); photon mu_E in [%.3e, %.3e] (x12); staggered mu_E/field in [%.3e, %.3e]'
      % (sc[:, 4].min(), sc[:, 4].max(), PH[:, 8].min(), PH[:, 8].max(), dc[:, 4].min(), dc[:, 4].max()))
for lab, NSt in (('N_s = 11.25 (22.5 Dirac as tastes; formal, non-integer)', 11.25), ('N_s = 16 (charge-identical taste pairs: SM + 3 nu_R + one vector-like family = 32 Dirac)', 16.0),
                 ('N_s = 22.5 (one staggered field per SM Dirac field: 22.5 twins)', 22.5)):
    wF = NSt/4.0
    summ = []
    for p in PH:
        bg, fw = p[0], p[1]; T = p[2:5]; E = p[5:8]; Vmu = p[8]
        for d in dc:
            bf, _, FT, FE, Fmu = d
            sols = []
            for bs in bss:
                S = sc[sc[:, 0] == bs]
                gmu = NS*S[:, 4] + wF*Fmu + NV*Vmu
                for i in range(len(S) - 1):
                    if gmu[i]*gmu[i+1] <= 0:
                        tt = gmu[i]/(gmu[i] - gmu[i+1]); Si = S[i] + tt*(S[i+1] - S[i])
                        a = a_of(T, -(NS*Si[2] + wF*FT)/NV)
                        if not np.isfinite(a) or abs(a) > 1:
                            continue
                        gE = NS*Si[3] + wF*FE + NV*(E[0] + E[1]*a + E[2]*a*a)
                        sols.append(gE)
            if sols:
                summ.append([bg, fw, bf, min(sols), max(sols), len(sols)])
            else:
                gmax = NS*sc[:, 4].max() + wF*Fmu + NV*Vmu
                summ.append([bg, fw, bf, np.nan, np.nan, 0 if gmax < 0 else -1])
    A = np.array(summ); ok = A[:, 5] > 0
    print('\n  %s: w_F = %.4f' % (lab, wF))
    print('    (edge, b_f) pairs: %d; mu_E row solvable on %d; too negative %d; too positive %d' % (len(A), ok.sum(), (A[:, 5] == 0).sum(), (A[:, 5] == -1).sum()))
    if ok.any():
        B = A[ok]
        chg = (B[:, 3] <= 0) & (B[:, 4] >= 0)
        print('    E-residual on the mu_E level set: [%+.4e, %+.4e]; pairs with a sign change (=> a 3-row root nearby): %d'
              % (np.nanmin(B[:, 3]), np.nanmax(B[:, 4]), chg.sum()))
        for row in B[np.argsort(np.minimum(abs(B[:, 3]), abs(B[:, 4])))][:6]:
            print('      gGw(%.2f,fw=%.2f) stag b_f=%.3f: gE range [%+.4e, %+.4e] over %d points' % tuple(row))
print('time %.0f s' % (time.time() - t00))
