"""R19-11: fit the twisted-mass Dirac rows (twisted.out) as c0 + c1 m + c2 m^2 + c4 m^4 (c1 must vanish: rows even in m),
then residuals of the 0+ law at the SM spectrum with a twisted-mass Dirac edge (scalar/vector parts as fitres_root0_dense.out)."""
import re, numpy as np
D = {}
for l in open('twisted.out'):
    mm = re.match(r'm=(\S+)\s+twisted \(T2g, Eg, muE, muT2\) \[([^\]]+)\]', l)
    if mm: D[float(mm.group(1))] = np.array([float(v) for v in mm.group(2).split()])
    if l.startswith('validation'): D[0.0] = np.array([float(v) for v in re.findall(r'twisted \[([^\]]+)\]', l)[0].split()])
ms = sorted(D); Y = np.array([D[m] for m in ms]); A = np.array([[1, m, m*m, m**4] for m in ms])
C, *_ = np.linalg.lstsq(A, Y, rcond=None); res = np.abs(A@C - Y).max(0)
S2D, S2S, S2V = 6.0061e-34, 2.4771e-34, 1.4247e-34; wa = 2*np.pi*100*5.391e-44
cS = {'muE': -1.36080e-03}; cV = {'muE': -2.99321e-03}
for j, k in enumerate(['T2g', 'Eg', 'muE', 'muT2']):
    R = C[2, j]*S2D + cS.get(k, 0)*S2S + cV.get(k, 0)*S2V
    conv = 'dc = 8 pi Xi = %.2e' % (8*np.pi*abs(R)) if not k.startswith('mu') else 'dc(100 Hz) = 8 pi mu/(omega a)^2 = %.2e; |mu|/3.2e-98 = %.1e' % (8*np.pi*abs(R)/wa**2, abs(R)/3.2e-98)
    print('%-5s twisted Dirac: c0 %+.9e c1 %+.2e c2 %+.4e (fit res %.1e) | residual at SM spectrum (D+S+V) %+.3e -> %s' % (k, C[0, j], C[1, j], C[2, j], res[j], R, conv))
