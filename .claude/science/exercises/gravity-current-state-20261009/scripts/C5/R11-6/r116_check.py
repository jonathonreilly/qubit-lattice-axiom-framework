"""R11-6 driver: (a) assembly checks, (d) trimer invariant mass, (c) small-r subtracted tails on the assembled operators."""
import numpy as np, sys, time
from r116_core import *
args = dict(a.split('=') for a in sys.argv[1:])
L = int(args.get('L', 160)); PA = float(args.get('PA', 0.55)); mode = args.get('mode', 'a')
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
t0 = time.time()
if mode == 'a':
    for P in [float(x) for x in args.get('Ps', '0.0,0.2,0.4').split(',')]:
        F = Fibre(L, P, PA, PA).build()
        uc, uB = F.unitarity()
        inner = np.prod(np.abs(F.mom) < 0.30, axis=0).astype(float)
        uci = [np.linalg.norm(inner[:, None]*(Bc.T@Bc - np.eye(F.N))*inner[None, :], 2) for Bc in F.Bc]
        pr('   interior (|p_i|<0.30) unitarity defect ||Bc^T Bc-1|| (a,b,c) = %.2e %.2e %.2e' % tuple(uci))
        pr('L=%d P=%.4f N=%d mu_b=%.8f | ||Bc^T Bc-1||_2 (a,b,c)=%.2e %.2e %.2e | ||B^T B-1||=%.1e | s_min(A)=%.4f s_max(A)=%.4f | ||B||_(B-1)=%.3f | ||Bc-1||_2=%.3f %.3f %.3f [%.0fs]'
           % (L, P, F.N, F.mu[0], uc[0], uc[1], uc[2], uB, F.smin, F.smax, np.linalg.norm(F.B-np.eye(F.N),2),
              *[np.linalg.norm(X, 2) for X in F.Bm1], time.time()-t0))
        # (d) trimer: lowest eigenvalues of H_S; invariant mass; P12 parity
        w, V = np.linalg.eigh(0.5*(F.HS + F.HS.T))
        # P12: q -> -q on master
        idx = np.arange(F.N).reshape(F.Np, F.Nq)[:, ::-1].ravel()
        par = np.array([np.vdot(V[:, i], V[idx, i]).real for i in range(6)])
        Minv = np.sqrt(w[:6]**2 - P*P)
        pr('   lowest H_S: ' + ' '.join('%.9f' % x for x in w[:6]))
        pr('   invariant mass sqrt(E^2-P^2): ' + ' '.join('%.9f' % x for x in Minv) + '   P12 parity: ' + ' '.join('%+.3f' % x for x in par))
        wb = np.linalg.eigvalsh(F.MBT)[:6]
        pr('   spec M_BT (P-independent by FC): ' + ' '.join('%.9f' % x for x in wb))
        # spectrum check H_S vs sqrt(M_BT^2+P^2)
        pr('   max|spec H_S - sqrt(spec M_BT^2+P^2)| = %.2e' % np.max(np.abs(np.linalg.eigvalsh(0.5*(F.HS+F.HS.T)) - np.sqrt(np.linalg.eigvalsh(F.MBT)**2 + P*P))))
        if P > 0:
            rs = [float(x) for x in args.get('rs', ','.join('%.4f' % (3*2**(k/2)) for k in range(11))).split(',')]
            for kind in ('dimer', 'gauss'):
                for r in rs:
                    psi = F.state(r, kind)
                    TB = np.linalg.norm((F.B - F.Bc[0])@psi); TH = np.linalg.norm((F.HS - F.Ha)@psi)
                    UB = np.linalg.norm((F.B - np.eye(F.N))@psi); UH = np.linalg.norm((F.HS - F.HBT)@psi)
                    cb = np.linalg.norm(F.Bm1[1]@psi); cc = np.linalg.norm(F.Bm1[2]@psi)
                    E = F.Bm1[1] + F.Bm1[2]
                    e2 = np.linalg.norm(E.T@(F.Bc[0]@psi))
                    pr('   %s r=%5.1f  T_B=||(B-B_a)psi||=%.3e  T_H=||(H_S-H_a)psi||=%.3e | U_B=||(B-1)psi||=%.3e U_H=||(H_S-H_BT)psi||=%.3e | ||(B_b-1)psi||=%.2e ||(B_c-1)psi||=%.2e ||E^T B_a psi||=%.2e'
                       % (kind, r, TB, TH, UB, UH, cb, cc, e2))
open('r116_check_L%d_%s%s.out' % (L, mode, args.get('tag','')), 'w').write('\n'.join(out) + '\n')
