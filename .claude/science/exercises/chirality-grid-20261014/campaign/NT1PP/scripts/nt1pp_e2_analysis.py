"""NT-1'' E2 analysis: tables, local rates nu_L = 1/2 ln(q(L)/q(L+2)), exp vs power fits over L >= 8 (PREREG section 5).
usage: python3 nt1pp_e2_analysis.py Lt"""
import sys, glob
import numpy as np
Lt = int(sys.argv[1]); T = Lt // 2
for W0 in ('0.3', '0.6'):
    Ls = sorted(int(f.split('_Lx')[1].split('_')[0]) for f in glob.glob(f'e2_Lx*_Lt{Lt}_W{W0}.npz'))
    if not Ls: continue
    Q = {}
    for L in Ls:
        z = np.load(f'e2_Lx{L}_Lt{Lt}_W{W0}.npz')
        for m in ('11112', 'L1'):
            Q.setdefault((m, 'tau_kQ(s*) [decisive]'), []).append(float(z[f'{m}_tq_m']))
            Q.setdefault((m, 'J_Q central row'), []).append(abs(z[f'{m}_rowsK'][T - 1]))
            Q.setdefault((m, 'kQ edge t-row'), []).append(abs(z[f'{m}_rowsK'][0]))
            Q.setdefault((m, 'Abar edge row'), []).append(abs(z[f'{m}_Arow'][0]))
            Q.setdefault((m, '|hbar| edge row'), []).append(np.abs(z[f'{m}_hb'][[0, -1]]).max())
            Q.setdefault((m, '|mbar| central row'), []).append(np.abs(z[f'{m}_mb'][T - 1]).max())
            Q.setdefault((m, '|mbar| edge row'), []).append(np.abs(z[f'{m}_mb'][[0, -1]]).max())
            Q.setdefault((m, 'Lx*tau_kQ(s*)'), []).append(L * float(z[f'{m}_tq_m']))
    print(f"=== Lt={Lt} W0={W0}  Lx = {Ls}")
    for (m, name), v in Q.items():
        v = np.array(v); Larr = np.array(Ls)
        print(f"{m:5s} {name:24s}: " + " ".join(f"{x:.3e}" for x in v))
        if m == 'L1' and name != 'Lx*tau_kQ(s*)': continue
        rates = 0.5 * np.log(v[:-1] / v[1:]) if np.all(v > 0) else None
        if rates is not None:
            print(f"{'':5s} {'local rates':24s}: " + " ".join(f"{x:+.3f}" for x in rates))
            sel = Larr >= 8
            if sel.sum() >= 3 and np.all(v[sel] > 1e-12):
                y = np.log(v[sel]); pe = np.polyfit(Larr[sel], y, 1); pp = np.polyfit(np.log(Larr[sel]), y, 1)
                re = np.sum((np.polyval(pe, Larr[sel]) - y) ** 2); rp = np.sum((np.polyval(pp, np.log(Larr[sel])) - y) ** 2)
                mx = rates.max(); last = rates[-1]; r8 = rates[Larr[:-1] >= 8]
                cls = 'E2-ALG' if (last < 0.5 * mx and rp < re) else ('E2-EXP' if np.all(r8 >= 0.5 * mx) else 'E2-UNDECIDED')
                print(f"{'':5s} {'fits L>=8':24s}: exp nu={-pe[0]:.3f} resid {re:.2e} | power p={-pp[0]:.2f} resid {rp:.2e} | class {cls}")
