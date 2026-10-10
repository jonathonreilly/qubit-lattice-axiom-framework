"""Matrix-valued (taste x spin) one-body charges vs the O(e^2) Moller condition, d=2,3.
Class: every translation-covariant one-body operator of range r on the period-2 cell (all 2^d taste/sublattice phases),
  P(k)[n+tau, n] = sum_{dv,tau} B_{dv,tau} e^{i(k+pi n).dv},  B complex (Hermitian part used).  [h,P]=0 is NOT imposed
  (enlarges the class; only the + band block U^+ P U enters).
Condition per regular Moller shell: (P3 x 1 + 1 x P4) T = T (P1 x 1 + 1 x P2)  on the + band.
Reports: dimension of surviving + band symbol space; trace-slope feasibility (taste-averaged slope = 1 along x);
taste-universal slope feasibility (Pi P Pi slope = identity); slope matrices of survivors.
usage: python s2_matrix.py d m r ns"""
import sys, time, itertools, numpy as np
from s2_core import *
d = int(sys.argv[1]); m = float(sys.argv[2]); r = int(sys.argv[3]); ns = int(sys.argv[4])
rng = np.random.default_rng(11 + d + r)
S = Stag(d, m); nn = S.nn; npl = nn//2; t0 = time.time()
DV = np.array(list(itertools.product(range(-r, r+1), repeat=d)))
TAU = S.N
params = [(dv, tau, part) for dv in DV for tau in TAU for part in (0, 1)]
npar = len(params)
DVa = np.array([p[0] for p in params], float); TAUa = np.array([p[1] for p in params]); PART = np.array([p[2] for p in params])
def Pk(k, deriv=None):
    """(npar, nn, nn) Hermitian symbols at reduced k"""
    out = np.zeros((npar, nn, nn), complex)
    for a, n in enumerate(S.N):
        ph = np.exp(1j*(DVa @ (k + np.pi*n)))
        if deriv is not None: ph = ph*1j*DVa[:, deriv]
        for t in range(npar):
            pass
        b = np.array([S.ix(n + TAUa[t]) for t in range(npar)])
        out[np.arange(npar), b, a] = ph
    coef = np.where(PART == 0, 1.0, 1j)
    M = coef[:, None, None]*out
    return M + np.conj(np.transpose(M, (0, 2, 1)))
samp = []
for mode, frac in (('generic', 0.5), ('lowK', 0.25), ('lowE', 0.25)):
    samp += sample_moller(S, int(ns*frac), rng, mode=mode)
Rf = np.zeros((0, npar)); nrow = 0
I = np.eye(npl)
for (k1, k2, k3, k4) in samp:
    T, U = moller_T(S, k1, k2, k3, k4)
    T = T/np.linalg.norm(T)
    Pt = [np.einsum('ai,tab,bj->tij', Uk.conj(), Pk(k), Uk) for Uk, k in zip(U, (k1, k2, k3, k4))]
    Dout = np.einsum('tab,cd->tacbd', Pt[2], I).reshape(npar, npl*npl, npl*npl) + np.einsum('ab,tcd->tacbd', I, Pt[3]).reshape(npar, npl*npl, npl*npl)
    Din = np.einsum('tab,cd->tacbd', Pt[0], I).reshape(npar, npl*npl, npl*npl) + np.einsum('ab,tcd->tacbd', I, Pt[1]).reshape(npar, npl*npl, npl*npl)
    C = np.einsum('tij,jk->tik', Dout, T) - np.einsum('ij,tjk->tik', T, Din)
    A = C.reshape(npar, -1).T
    A = np.vstack([A.real, A.imag])
    if A.shape[0] > 6*nn*nn: A = rng.normal(size=(6*nn*nn, A.shape[0])) @ A   # random sketch: per-shell constraint rank <= 4*npl^2 real, row space kept w.p.1
    nrow += A.shape[0]
    Rf = np.vstack([Rf, A])
    if Rf.shape[0] > 3*npar: Rf = np.linalg.qr(Rf, mode='r')
print(f"d={d} m={m} r={r}: params {npar}, Moller shells {len(samp)}, real rows {nrow}  ({time.time()-t0:.1f}s)", flush=True)
# evaluation map onto + band symbols at random k (to quotient the redundant parametrisation)
kev = [wrapr(rng.uniform(-np.pi/2, np.pi/2, d)) for _ in range(max(40, 3*npar//(npl*npl)))]
E = []
for k in kev:
    Uk = S.Uplus(k); Pt = np.einsum('ai,tab,bj->tij', Uk.conj(), Pk(k), Uk).reshape(npar, -1).T
    E.append(np.vstack([Pt.real, Pt.imag]))
E = np.vstack(E)
_, sv, Vt = np.linalg.svd(Rf, full_matrices=True); V = Vt.T
if len(sv) < npar: sv = np.concatenate([sv, np.zeros(npar-len(sv))])
G = Rf.T @ Rf
thr = max(1e-10, 1e-9*sv[0])
Z = V[:, sv < thr]
rkE = np.linalg.matrix_rank(E, tol=1e-8*np.linalg.norm(E, 2))
EZ = E @ Z if Z.shape[1] else np.zeros((E.shape[0], 0))
rkEZ = np.linalg.matrix_rank(EZ, tol=1e-8*np.linalg.norm(E, 2)) if Z.shape[1] else 0
print(f"  Gram sv: max {sv[0]:.3e}; null (abs 1e-10, rel 1e-9) dim {Z.shape[1]}; class dim (+ band symbols) {rkE}; surviving + band symbol dim {rkEZ}")
# gap diagnostics: sv just above threshold
above = sv[sv >= thr]
print(f"  smallest non-null sv {above[-1]:.3e}, next {above[-2]:.3e}; ratio to max {above[-1]/sv[0]:.3e}")
# Normalisations
h = 1e-4
def trslope(j):
    e = np.zeros(d); e[j] = h
    vals = []
    for s in (+1, -1):
        k = s*e; Uk = S.Uplus(k)
        vals.append(np.einsum('ai,tab,bi->t', Uk.conj(), Pk(k), Uk).real/npl)
    return (vals[0]-vals[1])/(2*h)
N1 = trslope(0)
# taste-universal: projected slope matrix at k=0 (degenerate subspace at k=0): Pi0 dP/dk_x Pi0 = 1 on + space at k->0 (m>0)
U0 = S.Uplus(np.zeros(d)); Pi0 = U0 @ U0.conj().T
def PiPPi(k):
    Uk = S.Uplus(k); Pk_ = Pk(k); Pi = Uk @ Uk.conj().T
    return np.einsum('ab,tbc,cd->tad', Pi, Pk_, Pi)
eh = np.zeros(d); eh[0] = h
dPP = (PiPPi(eh) - PiPPi(-eh))/(2*h)
SL = np.einsum('ai,tab,bj->tij', U0.conj(), dPP, U0).reshape(npar, -1)   # projected slope matrix of the + band symbol at k=0
# feasibility of trace slope within near-null space: minimise ||A x||^2 subject to N1 x = 1
Ginv_dir = np.linalg.lstsq(G + 1e-14*sv[0]**2*np.eye(npar), N1, rcond=None)[0]
x = Ginv_dir/(N1 @ Ginv_dir); defect = np.sqrt(max(x @ G @ x, 0))
print(f"  taste-averaged slope=1 along x: in exact null space N1.Z max |.| = {np.max(np.abs(N1 @ Z)) if Z.shape[1] else 0:.2e};  min ||C x|| s.t. N1.x=1 : {defect:.3e} (relative to ||C|| scale {sv[0]:.2e})")
# slope matrices of survivors
if Z.shape[1]:
    S0 = SL.T @ Z
    tr = np.array([np.trace(S0[:, c].reshape(npl, npl)) for c in range(Z.shape[1])])
    print(f"  survivors: max |slope matrix at k=0| {np.max(np.abs(S0)):.2e}; max |trace of slope| {np.max(np.abs(tr)):.2e}")
# e=0 control: the free taste-universal momentum (1/2) sin(2 k_x) * 1 is in the class for r>=2
if r >= 2:
    xf = np.zeros(npar)
    for t, (dv, tau, part) in enumerate(params):
        if part == 1 and not tau.any() and dv[0] == 2 and not dv[1:].any(): xf[t] = -1/8.0  # (i e^{2ik}c) + h.c. -> -1/2 sin... normalise below
    s = N1 @ xf; xf = xf/s
    print(f"  e=0 control: free momentum (1/2)sin(2k_x)1: slope {N1@xf:.6f}, + band slope matrix diag = {np.round(np.diag((SL.T@xf).reshape(npl,npl)).real, 6)}, Moller defect ||C x|| = {np.sqrt(xf@G@xf):.3e}  (free conservation [h,P]=0 exact by construction)")
print(f"time {time.time()-t0:.1f}s")
