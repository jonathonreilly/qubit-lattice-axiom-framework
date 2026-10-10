"""Joint matrix-valued test, d=3: fermion taste x spin one-body symbol P (range r, all period-2 taste phases, as s2_matrix.py)
and photon POLARIZATION-MATRIX one-body symbol g(p) = E_perp(p)^T M(p) E_perp(p), M(p) a 3x3 Hermitian trig polynomial
of range Rp (all link-component couplings).  Conditions: Moller (P only) and Compton (P and g):
   (P' x 1 + 1 x g') T_C = T_C (P x 1 + 1 x g)   on (+band x transverse pol).
Reports survivors, the fermion taste-averaged slope and the photon polarization-averaged slope (both normalised to 1 along x).
usage: python s2_matrix_compton.py m r Rp nmol ncomp"""
import sys, time, itertools, numpy as np
from s2_core import *
import importlib.util
m = float(sys.argv[1]); r = int(sys.argv[2]); Rp = int(sys.argv[3]); nmol = int(sys.argv[4]); ncomp = int(sys.argv[5])
d = 3; S = Stag(d, m); nn = S.nn; npl = nn//2; rng = np.random.default_rng(31); t0 = time.time()
sys.argv = ['x', '3', str(m), str(r), '0']
# reuse fermion parametrisation
DV = np.array(list(itertools.product(range(-r, r+1), repeat=d)))
fpar = [(dv, tau, part) for dv in DV for tau in S.N for part in (0, 1)]
nf = len(fpar)
DVa = np.array([p[0] for p in fpar], float); TAUa = np.array([p[1] for p in fpar]); PART = np.array([p[2] for p in fpar])
def Pk(k):
    out = np.zeros((nf, nn, nn), complex)
    for a, n in enumerate(S.N):
        ph = np.exp(1j*(DVa @ (k + np.pi*n)))
        b = np.array([S.ix(n + TAUa[t]) for t in range(nf)])
        out[np.arange(nf), b, a] = ph
    M = np.where(PART == 0, 1.0, 1j)[:, None, None]*out
    return M + np.conj(np.transpose(M, (0, 2, 1)))
NV = np.array(list(itertools.product(range(-Rp, Rp+1), repeat=d)))
# photon mode functions carry e^{ip.e_i/2}: under p -> p + 2 pi e_j the frame flips component j, so a local symbol has M_ii with
# integer frequencies and M_ij (i != j) with frequencies shifted by (e_i+e_j)/2.  We include BOTH integer and shifted
# frequencies for i != j (a superset of the local class).
gpar = [(nv.astype(float), i, j, part) for nv in NV for i in range(3) for j in range(3) for part in (0, 1) if i <= j]
gpar += [(nv + 0.5*(np.eye(3)[i] + np.eye(3)[j]), i, j, part) for nv in NV for i in range(3) for j in range(3) for part in (0, 1) if i < j]
ng = len(gpar)
def Mp(p):
    out = np.zeros((ng, 3, 3), complex)
    for t, (nv, i, j, part) in enumerate(gpar):
        out[t, i, j] = np.exp(1j*np.dot(nv, p))*(1 if part == 0 else 1j)
    return out + np.conj(np.transpose(out, (0, 2, 1)))
ncol = nf + ng
spec = importlib.util.spec_from_file_location("sc", "s2_compton_lib.py")
from s2_compton_lib import compton_T, sample_compton
blocks = []; Rf = np.zeros((0, ncol))
def add(A):
    global Rf
    Rf = np.vstack([Rf, A])
    if Rf.shape[0] > 3*ncol: Rf = np.linalg.qr(Rf, mode='r')
I4 = np.eye(npl); I2 = np.eye(2)
for (k1, k2, k3, k4) in sample_moller(S, nmol//2, rng, 'generic') + sample_moller(S, nmol//2, rng, 'lowE'):
    T, U = moller_T(S, k1, k2, k3, k4); T = T/np.linalg.norm(T)
    Pt = [np.einsum('ai,tab,bj->tij', Uk.conj(), Pk(k), Uk) for Uk, k in zip(U, (k1, k2, k3, k4))]
    Do = np.einsum('tab,cd->tacbd', Pt[2], I4).reshape(nf, 16, 16) + np.einsum('ab,tcd->tacbd', I4, Pt[3]).reshape(nf, 16, 16)
    Di = np.einsum('tab,cd->tacbd', Pt[0], I4).reshape(nf, 16, 16) + np.einsum('ab,tcd->tacbd', I4, Pt[1]).reshape(nf, 16, 16)
    C = (np.einsum('tij,jk->tik', Do, T) - np.einsum('ij,tjk->tik', T, Di)).reshape(nf, -1).T
    A = np.zeros((2*C.shape[0], ncol)); A[:, :nf] = np.vstack([C.real, C.imag])
    add(rng.normal(size=(64, A.shape[0])) @ A)
for (k, p, kq, pq) in sample_compton(S, ncomp//2, 'generic', rng) + sample_compton(S, ncomp//2, 'low', rng):
    T = compton_T(S, k, p, kq, pq); T = T/np.linalg.norm(T)
    U, Uq = S.Uplus(k), S.Uplus(kq); Ep, Eq = transverse(p, d), transverse(pq, d)
    P1 = np.einsum('ai,tab,bj->tij', U.conj(), Pk(k), U); P2 = np.einsum('ai,tab,bj->tij', Uq.conj(), Pk(kq), Uq)
    g1 = np.einsum('ia,tij,jb->tab', Ep, Mp(p), Ep); g2 = np.einsum('ia,tij,jb->tab', Eq, Mp(pq), Eq)
    Cf = np.einsum('tab,cd->tacbd', P2, I2).reshape(nf, 8, 8) @ T - T @ np.einsum('tab,cd->tacbd', P1, I2).reshape(nf, 8, 8)
    Cg = np.einsum('ab,tcd->tacbd', I4, g2).reshape(ng, 8, 8) @ T - T @ np.einsum('ab,tcd->tacbd', I4, g1).reshape(ng, 8, 8)
    C = np.concatenate([Cf.reshape(nf, -1), Cg.reshape(ng, -1)]).T
    add(np.vstack([C.real, C.imag]))
print(f"[photon class: diag integer freq; off-diag integer + (e_i+e_j)/2-shifted freq]\nm={m} r={r} Rp={Rp}: fermion params {nf}, photon params {ng}; Moller {nmol}, Compton {ncomp} shells ({time.time()-t0:.1f}s)", flush=True)
_, sv, Vt = np.linalg.svd(Rf); V = Vt.T
sv = np.concatenate([sv, np.zeros(ncol - len(sv))])
thr = max(1e-10, 1e-9*sv[0]); Z = V[:, sv < thr]
# quotient by redundancy: evaluate + band symbols and transverse photon symbols
ev = []
for t in range(max(60, 3*ncol//16)):
    k = wrapr(rng.uniform(-np.pi/2, np.pi/2, d)); p = wrapf(rng.uniform(-np.pi, np.pi, d))
    Uk = S.Uplus(k); Pt = np.einsum('ai,tab,bj->tij', Uk.conj(), Pk(k), Uk).reshape(nf, -1)
    Ep = transverse(p, d); gt = np.einsum('ia,tij,jb->tab', Ep, Mp(p), Ep).reshape(ng, -1)
    row = np.zeros((16 + 4, ncol), complex); row[:16, :nf] = Pt.T; row[16:, nf:] = gt.T
    ev.append(np.vstack([row.real, row.imag]))
E = np.vstack(ev); tolE = 1e-8*np.linalg.norm(E, 2)
print(f"  null dim {Z.shape[1]}; class dim {np.linalg.matrix_rank(E, tol=tolE)}; surviving symbol dim {np.linalg.matrix_rank(E@Z, tol=tolE) if Z.shape[1] else 0}")
above = sv[sv >= thr]; print(f"  sv max {sv[0]:.3e}; smallest non-null {above[-1]:.3e}; threshold {thr:.1e}")
h = 1e-4
def fslope():
    e = np.zeros(d); e[0] = h; v = []
    for s in (1, -1):
        Uk = S.Uplus(s*e); v.append(np.einsum('ai,tab,bi->t', Uk.conj(), Pk(s*e), Uk).real/npl)
    out = np.zeros(ncol); out[:nf] = (v[0]-v[1])/(2*h); return out
def gslope():
    e = np.zeros(d); e[0] = h; v = []
    for s in (1, -1):
        Ep = transverse(s*e, d); v.append(np.einsum('ia,tij,ja->t', Ep, Mp(s*e), Ep).real/2)
    out = np.zeros(ncol); out[nf:] = (v[0]-v[1])/(2*h); return out
Nf, Ng = fslope(), gslope()
if Z.shape[1]:
    print(f"  survivors: max |fermion taste-avg slope| {np.max(np.abs(Nf@Z)):.2e}; max |photon pol-avg slope| {np.max(np.abs(Ng@Z)):.2e}")
# control: the free photon momentum exists in the class? (Poynting-like symbol with slope 1): report best photon-slope-normalised defect
G = Rf.T @ Rf
for name, N in (("fermion slope=1", Nf), ("photon slope=1", Ng)):
    y = np.linalg.lstsq(G + 1e-14*sv[0]**2*np.eye(ncol), N, rcond=None)[0]; x = y/(N@y)
    print(f"  min ||C x|| s.t. {name}: {np.sqrt(max(x@G@x,0)):.3e}")
print(f"time {time.time()-t0:.1f}s")
