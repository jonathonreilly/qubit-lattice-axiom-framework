"""R9-3 script 3 (comparator proxy): Fourier tail of the form factor times a smooth packet weight,
F_s(r) = | int_0^kappa g_s(q) A(q) sin(q r) dq |,  A(q) = exp(-q^2/(2 sq^2)),
for the Gevrey family g_s (s = 0.5, 1 [the law], 2) and the analytic diagnostic g = (q/k')exp(-(q/k')^2).
If ||(B_b - 1) psi_D|| tracks F(D) in shape, its tail is the form factor's Fourier tail (C^inf compact => faster than
any power, standard), not a form-factor-independent threshold term.  Envelope = max over r in [D, 1.2 D].
"""
import numpy as np
KAP = 0.25; sq = 0.07
def sstep_s(x, s):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)**s), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)**s), 0.0)
    return e1/(e1+e2)
q = np.linspace(0, KAP, 400001); dq = q[1]-q[0]
A = np.exp(-q**2/(2*sq*sq))
fams = {'s=0.5': q*sstep_s(1-(q/KAP)**2, 0.5)/KAP, 's=1 (law)': q*sstep_s(1-(q/KAP)**2, 1.0)/KAP,
        's=2': q*sstep_s(1-(q/KAP)**2, 2.0)/KAP}
qg = np.linspace(0, 0.6, 600001); Ag = np.exp(-qg**2/(2*sq*sq))
Ds = [80, 113, 160, 226, 320, 453, 640, 905, 1280, 2560, 5120]
out = ['form-factor Fourier-tail proxy, kappa = %.2f, packet weight sigma_q = %.2f; envelope max_{r in [D,1.2D]} |F(r)|' % (KAP, sq)]
out.append('D      ' + '  '.join('%12s' % k for k in list(fams) + ['analytic k\'=0.08']))
for D in Ds:
    rr = np.linspace(D, 1.2*D, 41)
    row = []
    for k, gq in fams.items():
        w = gq*A
        row.append(max(abs(np.sum(w*np.sin(qq*r_))*dq) for r_ in rr for qq in [q]))
    wg = (qg/0.08)*np.exp(-(qg/0.08)**2)*Ag
    row.append(max(abs(np.sum(wg*np.sin(qg*r_))*(qg[1]-qg[0])) for r_ in rr))
    out.append('%5d  ' % D + '  '.join('%12.3e' % x for x in row))
print('\n'.join(out)); open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
