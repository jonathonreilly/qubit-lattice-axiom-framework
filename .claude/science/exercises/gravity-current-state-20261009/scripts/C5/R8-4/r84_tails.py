"""R8-4 script C: quasi-locality and the stability constant, d = 1, model S (same parameters as script B).
Real-space coefficient of the vacuum monomial  kappa(r_A, r_B, r_C) (r = y - y_D) = inverse DFT over the three
independent momenta of the vertex function K0(kA,kB,kC) (kD = -kA-kB-kC); same for the forward monomial
X_{y_X} -> Y Z W (relative to the annihilated X).  ||V_term|| <= N * sum_r |kappa(r)|  (each CAR monomial has norm <= 1),
so H >= -2 g N (sum of these l1 norms): an extensive lower bound.  Tail: max |kappa| on the shell max_i |r_i| = R."""
import numpy as np, sys, itertools
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r84_fock import plateau, P, hfac
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
m = 0.3
def F(s): return plateau(np.sqrt(np.maximum(s, 0.0)), P['L1'], P['L2'])
def wrap(k): return (k + np.pi) % (2*np.pi) - np.pi
for L in [64, 128, 192]:
    k = 2*np.pi*np.fft.fftfreq(L)            # in (-pi, pi]
    kA, kB, kC = np.meshgrid(k, k, k, indexing='ij'); kD = wrap(-(kA + kB + kC))
    ks = [kA, kB, kC, kD]; Es = [np.sqrt(m*m + x*x) for x in ks]
    psi = np.ones_like(kA)
    for i, j in itertools.combinations(range(4), 2):
        psi *= F((Es[i] + Es[j])**2 - (ks[i] + ks[j])**2)
    cut = np.ones_like(kA)
    for x in ks: cut *= plateau(x, P['A1'], P['A2'])
    K0 = psi*cut/np.sqrt(16*Es[0]*Es[1]*Es[2]*Es[3])
    kap = np.fft.ifftn(K0)                    # includes 1/L^3
    # forward X -> (Y Z W): created momenta k1,k2,k3 ; X momentum = k1+k2+k3 (wrapped)
    kX = wrap(kA + kB + kC); EX = np.sqrt(m*m + kX**2); W = Es[0] + Es[1] + Es[2]
    ps3 = F((Es[0]+Es[1])**2-(kA+kB)**2)*F((Es[0]+Es[2])**2-(kA+kC)**2)*F((Es[1]+Es[2])**2-(kB+kC)**2)
    cut3 = plateau(kA, P['A1'], P['A2'])*plateau(kB, P['A1'], P['A2'])*plateau(kC, P['A1'], P['A2'])*plateau(kX, P['C1'], P['C2'])
    KF = ps3*cut3*np.sqrt(hfac(EX, W))/np.sqrt(2*EX*8*Es[0]*Es[1]*Es[2])
    kapF = np.fft.ifftn(KF)
    r = np.fft.fftfreq(L)*L; RA, RB, RC = np.meshgrid(r, r, r, indexing='ij'); R = np.maximum(np.maximum(np.abs(RA), np.abs(RB)), np.abs(RC))
    pr(f'## L={L}: ||kappa_vac||_1 = {np.sum(np.abs(kap)):.8f}   ||kappa_fwd||_1 = {np.sum(np.abs(kapF)):.8f}   max|K0|={np.max(np.abs(K0)):.4f}')
    line = []
    for Rr in [0, 1, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96]:
        if Rr >= L//2: break
        sel = R == Rr
        line.append(f'R={Rr}:{np.max(np.abs(kap[sel])):.2e}/{np.max(np.abs(kapF[sel])):.2e}')
    pr('   tail max|kappa| vac/fwd on shells: ' + '  '.join(line))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(OUT) + '\n')
