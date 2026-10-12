"""R11-6 packing choice S4 (discretized ordered exponential, R7-6 Construction S):
   B = U_K ... U_1,  U_k = polar( 1 + sum_c [B_c(s_k) B_c(s_{k-1})^dag - 1] ),  s_k = k/K,
   B_c(s) = packing unitary of channel c with pair coupling s*lam (B_c(0) = 1).
   Cluster limit: if B_b(s), B_c(s) -> 1 for all s, the product telescopes to B_a(1) = B_a exactly.
Checks: per-step s_min, ||B^T B - 1||, symmetry, spec H_S vs sqrt(spec M_BT^2+P^2), trimer at P = 0, +-P1, +-P2,
and the subtracted tails T_B = ||(B - B_a) psi_r||, T_H = ||(H_S - H_a) psi_r|| on the assembled operators."""
import numpy as np, sys, time
import r116_core as C
args = dict(a.split('=') for a in sys.argv[1:])
L = int(args.get('L', 160)); K = int(args.get('K', 8)); PA = float(args.get('PA', 0.55))
Ps = [float(x) for x in args.get('Ps', '0.4').split(',')]
rs = [float(x) for x in args.get('rs', ','.join('%.4f' % (3*2**(k/2)) for k in range(11))).split(',')]
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
t0 = time.time()
for P in Ps:
    Bcs = []
    for k in range(K+1):
        sv = k/K
        C.LAM = -3.0*sv
        F = C.Fibre(L, P, PA, PA)
        if k == 0:
            Bcs.append([np.eye(F.N)]*3); continue
        F.build() if k == K else None
        if k < K:
            # build only the packing unitaries at coupling s
            Bm1c = F.chart_Bm1()
            wv = np.prod(C.sstep((F.POUT - np.abs(F.mom))/(F.POUT - F.PIN)), axis=0)
            Bl = []
            for c in range(3):
                I = F.interp_master_to_chart(c); E = F.interp_chart_to_master(c)
                Bl.append(np.eye(F.N) + wv[:, None]*(E@Bm1c@I)*wv[None, :])
            Bcs.append(Bl)
        else:
            Bcs.append(F.Bc); Ffull = F
    C.LAM = -3.0
    N = Ffull.N; Id = np.eye(N); B = Id.copy(); smins = []
    for k in range(1, K+1):
        A = Id + sum(Bcs[k][c]@Bcs[k-1][c].T - Id for c in range(3))
        U, S, Vh = np.linalg.svd(A); smins.append(S.min())
        B = (U@Vh)@B
    F = Ffull
    HS = B.T@F.HBT@B
    pr('L=%d K=%d P=%.3f N=%d mu_b=%.8f | per-step s_min(A_k): min %.4f max %.4f | ||B^T B-1||=%.1e | ||B-1||_2=%.3f ||B-B_a||_2=%.3f [%.0fs]'
       % (L, K, P, N, F.mu[0], min(smins), max(smins), np.linalg.norm(B.T@B - Id, 2), np.linalg.norm(B - Id, 2), np.linalg.norm(B - F.Bc[0], 2), time.time()-t0))
    w = np.linalg.eigvalsh(0.5*(HS + HS.T))
    pr('   trimer: lowest H_S = %.10f ; invariant mass = %.10f ; max|spec H_S - sqrt(spec M_BT^2+P^2)| = %.2e'
       % (w[0], np.sqrt(w[0]**2 - P*P), np.max(np.abs(w - np.sqrt(np.linalg.eigvalsh(F.MBT)**2 + P*P)))))
    if P != 0:
        for kind in args.get('kinds', 'dimer').split(','):
            for r in rs:
                psi = F.state(r, kind)
                TB = np.linalg.norm((B - F.Bc[0])@psi); TH = np.linalg.norm((HS - F.Ha)@psi)
                UB = np.linalg.norm((B - Id)@psi); UH = np.linalg.norm((HS - F.HBT)@psi)
                # discretization diagnostic: unitarity defect of B_a on this state
                ua = np.linalg.norm((F.Bc[0].T@F.Bc[0] - Id)@psi)
                pr('   %s r=%7.3f  T_B=%.4e  T_H=%.4e | U_B=||(B-1)psi||=%.4e  U_H=||(H_S-H_BT)psi||=%.4e | ||(B_a^T B_a-1)psi||=%.1e'
                   % (kind, r, TB, TH, UB, UH, ua))
open('r116_s4_L%d_K%d%s.out' % (L, K, args.get('tag', '')), 'w').write('\n'.join(out) + '\n')
