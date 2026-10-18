"""Reviewer checks of the structural steps of Theorem K and of the slice/index (second-proof) identity.
(a) random M = diag(c z^m,1,1) * E_1...E_s over C[Z^3] (non-unitary, Laurent inverse): W3 = 0 on grids
    exceeding the trig-degree bound (exact up to rounding);
(b) stabilisation W3[V2 (+) 1] = W3[V2], additivity W3[V2 * E] = W3[V2] for Laurent elementary E, W3[V2 V2] = 2 W3[V2];
(c) slice identity used by the second proof: for U = 1 - Q + z3 Q with Q(k1,k2) a smooth rank-1 projector of
    Chern number C (QWZ), |W3[U]| = |C| (and the Toeplitz coker bundle in z3 is range Q)."""
import sys, numpy as np
from rlib import S, Ck, w3_GL, grid
ck = Ck(); rng = np.random.default_rng(3)
def lp_eval(terms, K, n):
    """terms: list of (exponent vector, matrix); returns U, dU on grid K."""
    U = np.zeros(K[0].shape+(n,n), complex); dU = [np.zeros_like(U) for _ in range(3)]
    for e, A in terms:
        ph = np.exp(1j*(e[0]*K[0]+e[1]*K[1]+e[2]*K[2]))[...,None,None]
        U += ph*A
        for b in range(3): dU[b] += 1j*e[b]*ph*A
    return U, dU
def rand_elem(n, rng):
    i, j = rng.choice(n, 2, replace=False)
    terms = [((0,0,0), np.eye(n, dtype=complex))]
    for _ in range(3):
        e = tuple(rng.integers(-1, 2, 3)); A = np.zeros((n,n), complex); A[i,j] = rng.normal()+1j*rng.normal()
        terms.append((e, A))
    return terms
def mat_prod_fields(factors):
    U, dU = factors[0]
    for V, dV in factors[1:]:
        dU = [dU[b]@V + U@dV[b] for b in range(3)]; U = U@V
    return U, dU
for trial in range(3):
    n, s = 3, 3
    m = tuple(rng.integers(-1, 2, 3)); D = np.eye(3, dtype=complex); D[0,0] = 0
    Dt = [((0,0,0), D), (m, np.diag([0.7+0.2j,0,0]).astype(complex))]
    Es = [rand_elem(n, rng) for _ in range(s)]
    # range bound: M range <= s+1, M^-1 range <= s+1 ; integrand degree <= 3*(2s+2) = 24 per axis
    vals = []
    for N in (26, 31):
        K = grid(N, 0.0)
        M, dM = mat_prod_fields([lp_eval(Dt, K, n)] + [lp_eval(E, K, n) for E in Es])
        vals.append(w3_GL(M, dM)); mind = np.abs(np.linalg.det(M)).min()
    print(f'trial {trial}: m={m}, W3 (N=26,31) = {vals[0]:+.2e}, {vals[1]:+.2e}; min|det| {mind:.3f} (= 0.728 expected, |0.7+0.2i|)')
    ck(f'trial {trial}: Laurent-GL product diag(c z^m,1,1)*E1*E2*E3 has W3 = 0 (exact grid, |W3|<1e-9)', max(abs(v) for v in vals) < 1e-9)
# (b) with the analytic V2 (non finite range)
def V2(K, M=2.0):
    K1,K2,K3 = K
    d = np.stack([M-np.cos(K1)-np.cos(K2)-np.cos(K3), np.sin(K1), np.sin(K2), np.sin(K3)], -1)
    W = lambda x: x[...,0,None,None]*S[0] + 1j*sum(x[...,a+1,None,None]*S[a+1] for a in range(3))
    dd = []
    for b,Kb in enumerate(K):
        v = np.zeros_like(d); v[...,0] = np.sin(Kb); v[...,1+b] = np.cos(Kb); dd.append(W(v))
    return W(d), dd
K = grid(40, 0.5)
V, dV = V2(K)
w = w3_GL(V, dV).real
pad = lambda U, n: np.block([[U, np.zeros(U.shape[:-2]+(U.shape[-2], n), complex)], [np.zeros(U.shape[:-2]+(n, U.shape[-1]), complex), np.broadcast_to(np.eye(n), U.shape[:-2]+(n,n))]])
padd = lambda dU, n: np.block([[dU, np.zeros(dU.shape[:-2]+(dU.shape[-2], n), complex)], [np.zeros(dU.shape[:-2]+(n, dU.shape[-1]), complex), np.zeros(dU.shape[:-2]+(n,n), complex)]])
wpad = w3_GL(pad(V,2), [padd(x,2) for x in dV]).real
E = lp_eval(rand_elem(4, rng), K, 4)
wE = w3_GL(*mat_prod_fields([(pad(V,2), [padd(x,2) for x in dV]), E])).real
wVV = w3_GL(*mat_prod_fields([(V, dV), (V, dV)])).real
print(f'W3[V2]={w:+.8f}  W3[V2+1_2]={wpad:+.8f}  W3[(V2+1_2)E]={wE:+.8f}  W3[V2 V2]={wVV:+.8f}')
ck('stabilisation: W3[V2 (+) 1_2] = W3[V2] = -1', abs(wpad-w) < 1e-9 and abs(w+1) < 1e-6)
ck('elementary factor (Laurent p, 4x4) does not change W3: W3[(V2(+)1)E] = -1', abs(wE+1) < 1e-6)
ck('additivity: W3[V2 V2] = -2', abs(wVV+2) < 1e-6)
# (c) slice identity
def chern_FHS(m, L=60):
    k = 2*np.pi*np.arange(L)/L; K1,K2 = np.meshgrid(k,k,indexing='ij')
    h = np.stack([np.sin(K1), np.sin(K2), m-np.cos(K1)-np.cos(K2)], -1)
    H = sum(h[...,a,None,None]*S[a+1] for a in range(3))
    _, v = np.linalg.eigh(H); u = v[...,:,1]  # upper band, Q = projector on +h.sigma eigenvector
    U1 = np.sum(u.conj()*np.roll(u,-1,0),-1); U2 = np.sum(u.conj()*np.roll(u,-1,1),-1)
    F = np.angle(U1*np.roll(U2,-1,0)/np.roll(U1,-1,1)/U2)
    return F.sum()/(2*np.pi)
def W3_slice(m, N=48):
    K = grid(N, 0.5); K1,K2,K3 = K
    h = np.stack([np.sin(K1), np.sin(K2), m-np.cos(K1)-np.cos(K2)], -1); hn = np.linalg.norm(h, axis=-1)
    nvec = h/hn[...,None]
    Q = 0.5*(S[0] + sum(nvec[...,a,None,None]*S[a+1] for a in range(3)))
    dh = [np.stack([np.cos(K1), 0*K1, np.sin(K1)], -1), np.stack([0*K1, np.cos(K2), np.sin(K2)], -1)]
    dn = [x/hn[...,None] - h*((h*x).sum(-1)/hn**3)[...,None] for x in dh]
    dQ = [0.5*sum(x[...,a,None,None]*S[a+1] for a in range(3)) for x in dn]
    z = np.exp(1j*K3)[...,None,None]
    U = S[0] - Q + z*Q
    dU = [(z-1)*dQ[0], (z-1)*dQ[1], 1j*z*Q]
    return w3_GL(U, dU).real
for m in (1.0, -1.0, 3.0):
    C = chern_FHS(m); w = W3_slice(m)
    print(f'QWZ m={m}: Chern(Q) = {C:+.6f}, W3[1-Q+z3 Q] = {w:+.8f}')
    ck(f'slice identity m={m}: |W3| = |Chern| (integers)', abs(abs(w)-abs(C)) < 1e-6 and abs(C-round(C)) < 1e-6)
sys.exit(ck.total())
