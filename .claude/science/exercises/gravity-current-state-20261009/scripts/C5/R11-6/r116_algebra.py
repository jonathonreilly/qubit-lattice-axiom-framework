"""R11-6 (b): Poincare algebra of the assembled packed law on P-packets, FC prescription.
P-fibres at P_k = P_c + k dP, dP = 2 pi / L (ring spacing); X0 = i d/dP (spectral, on the P grid);
X_S = B^dag X0 B (fibrewise B(P)), K_S = (H_S X_S + X_S H_S)/2.  Residuals on Phi(P) = w(P) phi_int."""
import numpy as np, sys, time
from r116_core import *
args = dict(a.split('=') for a in sys.argv[1:])
L = int(args.get('L', 128)); Pc = float(args.get('Pc', 0.3)); wP = float(args.get('wP', 0.06)); half = float(args.get('half', 0.5))
dP = 2*np.pi/L; nk = int(np.ceil(half/dP)); Ps = Pc + dP*np.arange(-nk, nk+1); nP = len(Ps)
t0 = time.time()
import r116_core as C
KS = int(args.get('K', 0))
def s4B(L, P, K):
    Bprev = [None]*3; Id = None; B = None
    for k in range(1, K+1):
        C.LAM = -3.0*k/K
        F = C.Fibre(L, P, 0.55, 0.55)
        if k == K: F.build(); Bl = F.Bc
        else:
            Bm1c = F.chart_Bm1(); wv = np.prod(C.sstep((F.POUT - np.abs(F.mom))/(F.POUT - F.PIN)), axis=0)
            Bl = [np.eye(F.N) + wv[:, None]*(F.interp_chart_to_master(c)@Bm1c@F.interp_master_to_chart(c))*wv[None, :] for c in range(3)]
        if Id is None: Id = np.eye(F.N); Bprev = [Id]*3; B = Id.copy()
        A = Id + sum(Bl[c]@Bprev[c].T - Id for c in range(3)); U, S, Vh = np.linalg.svd(A); B = (U@Vh)@B; Bprev = Bl
    C.LAM = -3.0
    F.B = B; F.HS = B.T@F.HBT@B
    return F
Fs = [Fibre(L, P, 0.55, 0.55).build() for P in Ps] if KS == 0 else [s4B(L, P, KS) for P in Ps]
N = Fs[0].N
phi_int = Fs[0].state(0.0, 'gauss').real.astype(complex)      # smooth interior internal state (P-independent coords)
w = np.exp(-(Ps - Pc)**2/(4*wP*wP))
Phi = w[:, None]*phi_int[None, :]                              # (nP, N)
kk = 2*np.pi*np.fft.fftfreq(nP, d=dP)
def D(F):  # spectral d/dP along axis 0
    return np.fft.ifft(1j*kk[:, None]*np.fft.fft(F, axis=0), axis=0)
def HS(F): return np.array([Fs[i].HS@F[i] for i in range(nP)])
def XS(F):
    BF = np.array([Fs[i].B@F[i] for i in range(nP)]); Y = 1j*D(BF)
    return np.array([Fs[i].B.conj().T@Y[i] for i in range(nP)])
def K(F): return 0.5*(HS(XS(F)) + XS(HS(F)))
def Pm(F): return Ps[:, None]*F
nrm = lambda F: np.sqrt(np.sum(np.abs(F)**2))
KP = K(Pm(Phi)) - Pm(K(Phi)); H = HS(Phi)
KH = K(HS(Phi)) - HS(K(Phi))
r1 = nrm(KP - 1j*H)/nrm(H); r2 = nrm(KH - 1j*Pm(Phi))/nrm(Pm(Phi)); r3 = nrm(HS(Pm(Phi)) - Pm(HS(Phi)))/nrm(H)
# BT reference (B = 1): same residuals for H_BT, X0
def HB(F): return np.array([Fs[i].HBT@F[i] for i in range(nP)])
def KB(F): return 0.5*(HB(1j*D(F)) + 1j*D(HB(F)))
rb2 = nrm(KB(HB(Phi)) - HB(KB(Phi)) - 1j*Pm(Phi))/nrm(Pm(Phi))
smin = min(F.smin for F in Fs)
line = ('L=%d nP=%d N=%d Pc=%.2f wP=%.3f : ||[K_S,P]-iH_S||/||H_S Phi|| = %.2e  ||[K_S,H_S]-iP||/||P Phi|| = %.2e  ||[H_S,P]|| = %.1e | BT ref ||[K,H]-iP|| = %.2e | min_P s_min(A) = %.4f [%.0f s]'
        % (L, nP, N, Pc, wP, r1, r2, r3, rb2, smin, time.time()-t0))
print(line); open('r116_algebra_L%d_K%d.out' % (L, KS), 'w').write(line + '\n')
