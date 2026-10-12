"""R15-5 s3: static scalar-source energy for the h-side forms of the compactness ladder (pre-registered:
h:R(h) [CCR and dual rotor, h integer] -> -rho^2/(4 qhat^2) (attractive 1/r);
|R(h)|^2 [rotor with compact h, and both-compact H_L] -> +rho^2/4, k-independent (contact, no 1/r))."""
import numpy as np
src = open(__file__.replace('s3_ladder_static.py', 's1_ntype_reduced.py')).read().split('J, g = 1.0, 1.0')[0]
ns = {}; exec(src, ns); ops = ns['ops']; null = ns['null']
for form in ['h:R(h)', '|R(h)|^2']:
    for kk in [0.3, 0.1, 0.03]:
        k = kk*np.array([1, 2, 5.])/np.sqrt(30)
        q, G, S, R, C, K = ops(k)
        Q = R if form == 'h:R(h)' else R.T@R
        Pg = null(G); Qr = Pg.T@Q@Pg; Sr = S@Pg; n = Pg.shape[1]
        KKT = np.block([[Qr, Sr.T], [Sr, np.zeros((1, 1))]])
        sol = np.linalg.lstsq(KKT, np.concatenate([np.zeros(n), [1.0]]), rcond=None)[0]
        h = sol[:n]; En = 0.5*h@Qr@h
        # positivity of the form on the gauge-fixed constraint-free directions (TT) -> stationary point is the minimum
        V = null(np.vstack([G, S])); mtt = np.linalg.eigvalsh(V.T@Q@V).min()
        print("%-9s |k|=%.2f  E(rho=1)=%+.6f  E*qhat^2=%+.6f  min form on TT=%.3e" % (form, kk, En, En*(q@q), mtt))
