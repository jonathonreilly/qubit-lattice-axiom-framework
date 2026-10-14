"""Tiny check: in the K2c proxy (2D U(1), vector-like massive overlap, M=1, m=0.05),
is det D_ov(m)[U] real and positive for admissible links?  If so, the weight is a
positive real measure, theta∘conj = theta on it, and Π-W as defined in
C5_R2-4_report.md:293 ("reflection-positive under Θ = θ∘conj") cannot absorb an
RP failure of that weight.  Also: Wilson det for comparison; antiperiodic time BC."""
import numpy as np
rng = np.random.default_rng(7)
s1 = np.array([[0,1],[1,0]],complex); s2 = np.array([[0,-1j],[1j,0]],complex); s3 = np.diag([1.,-1.]).astype(complex)
g = [s1, s2]; g5 = s3; I2 = np.eye(2)

def wilson(U, Lx, Lt, M, apbc_t=True):
    N = Lx*Lt; D = np.zeros((2*N,2*N),complex)
    idx = lambda x,t: (x%Lx) + Lx*(t%Lt)
    for x in range(Lx):
        for t in range(Lt):
            i = idx(x,t)
            D[2*i:2*i+2,2*i:2*i+2] += (2.0 - M)*I2   # r=1: 2 directions * r - M
            for mu,(dx,dt) in enumerate([(1,0),(0,1)]):
                j = idx(x+dx,t+dt); u = U[mu][x,t]
                ph = -1.0 if (apbc_t and mu==1 and t==Lt-1) else 1.0
                D[2*i:2*i+2,2*j:2*j+2] += -0.5*ph*u*(I2 - g[mu])
                xb, tb = (x-dx)%Lx, (t-dt)%Lt; jb = idx(xb,tb); ub = np.conj(U[mu][xb,tb])
                phb = -1.0 if (apbc_t and mu==1 and t==0) else 1.0
                D[2*i:2*i+2,2*jb:2*jb+2] += -0.5*phb*ub*(I2 + g[mu])
    return D

def overlap(U, Lx, Lt, M, m):
    DW = wilson(U, Lx, Lt, M); G5 = np.kron(np.eye(Lx*Lt), g5)
    H = G5 @ DW; H = 0.5*(H + H.conj().T)
    w, V = np.linalg.eigh(H); S = (V * np.sign(w)) @ V.conj().T
    D = np.eye(len(H)) + G5 @ S
    return (1 - m/2)*D + m*np.eye(len(H)), np.min(np.abs(w))

def admissible_links(Lx, Lt, eps):
    # small random angles -> plaquettes |arg U_p| < ~4 eps
    return [np.exp(1j*eps*rng.uniform(-1,1,(Lx,Lt))) for _ in range(2)]

print("Lx Lt  eps  max|Im det/Re det|  min Re det  min|H_W|   (overlap, M=1, m=0.05)")
for (Lx,Lt) in [(2,12),(2,16),(4,8)]:
    for eps in [0.1, 0.15]:
        worst_im, min_re, min_gap = 0.0, np.inf, np.inf
        for k in range(20):
            U = admissible_links(Lx, Lt, eps)
            Dm, gap = overlap(U, Lx, Lt, 1.0, 0.05)
            sgn, logabs = np.linalg.slogdet(Dm)
            worst_im = max(worst_im, abs(sgn.imag)/max(abs(sgn.real),1e-300))
            min_re = min(min_re, sgn.real); min_gap = min(min_gap, gap)
        print(f"{Lx:2d} {Lt:2d} {eps:5.2f}  {worst_im:.2e}            {min_re:+.3f} (phase)   {min_gap:.3f}")
