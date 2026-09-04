"""bridge_spec.py -- Bloch (partial-Fourier) reduction of the matter operator.

The configuration depends on x0 only, so K commutes with translations in
directions 1,2,3.  For each transverse momentum q the operator reduces to an
L x L PERIODIC TRIDIAGONAL hermitian matrix K^q (offsets in x0 are -1,0,+1).
Diagonalising all L^3 of them gives the exact spectrum and, by inverse
transform, the exact local matrix elements of any function of the operator:

    H(B)_{a,a+delta} = L^-3 sum_q exp(-i q.delta_123) H(B^q)[a0, a0+delta0]

which is all that dW/ds_e needs, because dK/ds_e and dM/ds_e are local.
No stochastic estimation, no Chebyshev: the answer is exact to machine precision.
"""
import numpy as np
from bridge_core import *

# offset index helpers: d123 in {-1,0,1}^3  ->  0..26 ;  band = delta0+1 in {0,1,2}
def _d123idx(v):  return (v[0]+1)*9 + (v[1]+1)*3 + (v[2]+1)
DVECS = np.array([[a,b,c] for a in (-1,0,1) for b in (-1,0,1) for c in (-1,0,1)])

def cband(loc, L):
    """Cband[band, m, d] : coefficient of exp(i q.d) in K^q[m, m+band-1]."""
    C = np.zeros((3, L, 27))
    x0b = np.arange(L)
    for p in range(24):
        a = CORN[p]
        for i in range(NC):
            for j in range(NC):
                b = a[j][0]-a[i][0]+1
                dd = _d123idx(a[j][1:]-a[i][1:])
                np.add.at(C, (b, (x0b+a[i][0]) % L, dd), loc[p, :, i, j])
    return C

def momenta(L):
    n = np.arange(L)
    Q = np.stack(np.meshgrid(n, n, n, indexing='ij'), -1).reshape(-1, 3)
    return 2.0*np.pi*Q/L                      # (L^3, 3)

def phases(L):
    q = momenta(L)
    return np.exp(1j*(q @ DVECS.T)).T         # (27, L^3)

def local_Hmatrix(S, L, Hfuncs, deflate_zero=True, chunk=None, geom=None, ret_spec=False,
                  verbose=False):
    """Returns Phi[name][band, m, d] = H(B)_{a, a+delta}, a=(m,0,0,0),
    delta=(band-1, d).  Hfuncs: dict name -> callable on the eigenvalues.
    All functions share one pass over the L^3 Bloch blocks."""
    import time
    from bridge_geom import geometry
    g = geometry(S, L) if geom is None else geom
    C = cband(g['loc'], L)
    Mv = g['Mv']; isq = 1.0/np.sqrt(Mv)
    P = phases(L); nq = P.shape[1]
    if chunk is None: chunk = max(1, min(nq, int(1e7//(L*L))))
    names = list(Hfuncs); nn = len(names)
    acc = np.zeros((nn, 3, L, 27), dtype=complex)
    idx = np.arange(L)
    lam_all = [] if ret_spec else None
    Cflat = C.reshape(3*L, 27); t0 = time.time()
    for s0 in range(0, nq, chunk):
        Pc = P[:, s0:s0+chunk]; nc = Pc.shape[1]
        Kb = (Cflat @ Pc).reshape(3, L, nc)              # (band, m, q)
        Kq = np.zeros((nc, L, L), dtype=complex)
        for b in range(3):
            Kq[:, idx, (idx+b-1) % L] = Kb[b].T
        Kq *= isq[None, :, None]*isq[None, None, :]
        Kq = 0.5*(Kq + np.conj(np.transpose(Kq, (0, 2, 1))))
        w, U = np.linalg.eigh(Kq)                        # w (nc,L), U (nc,L,L)
        del Kq
        if ret_spec: lam_all.append(w.copy())
        H = np.empty((nc, L, nn))
        for a, n in enumerate(names): H[:, :, a] = Hfuncs[n](w)
        if deflate_zero and s0 == 0:
            # lambda_0 == 0 identically for EVERY configuration (K.1 = 0): the zero
            # mode gives a config-independent constant in W and nothing in dW/ds_e.
            H[0, 0, :] = 0.0
        Uc = np.conj(U)
        for b in range(3):
            T = U*Uc[:, (idx+b-1) % L, :]                # (nc,L,L): T[q,m,i]
            D = np.matmul(T, H.astype(complex))          # (nc,L,nn)
            acc[:, b] += np.einsum('qmn,dq->nmd', D, np.conj(Pc))
        if verbose and s0 == 0:
            print(f"      [Bloch] chunk {nc}/{nq} in {time.time()-t0:.2f}s "
                  f"-> est {(time.time()-t0)*nq/nc:.0f}s", flush=True)
    out = {n: acc[a]/nq for a, n in enumerate(names)}
    if ret_spec: return out, np.concatenate(lam_all, 0).ravel()
    return out

def _FG(tau0, m2, improved):
    if improved:
        mu = lambda l: l + l*l/24.0; mup = lambda l: 1.0 + l/12.0
    else:
        mu = lambda l: l;            mup = lambda l: np.ones_like(l)
    def F(l):
        x = mu(l)+m2; ok = x > 1e-12
        return np.where(ok, np.exp(-tau0*np.where(ok, x, 1.0))*mup(l)/np.where(ok, x, 1.0), 0.0)
    def G(l):
        x = mu(l)+m2; ok = x > 1e-12
        return np.where(ok, l*np.exp(-tau0*np.where(ok, x, 1.0))*mup(l)/np.where(ok, x, 1.0), 0.0)
    return F, G

def contract(Phi_F, Phi_G, g, L):
    """dW/ds_e for every (edge class, x0) given the local matrix elements."""
    PF, PG = Phi_F.real, Phi_G.real
    Mv = g['Mv']; isq = 1.0/np.sqrt(Mv); dloc = g['dloc']; dV = g['dV']
    out = np.zeros((NE, L)); x0b = np.arange(L)
    for p in range(24):
        a = CORN[p]
        for k in range(10):
            c = SEC[p, k]; tgt = (x0b + SEX[p, k]) % L
            acc = np.zeros(L)
            for i in range(NC):
                mi = (x0b + a[i][0]) % L
                for j in range(NC):
                    mj = (x0b + a[j][0]) % L
                    b = a[j][0]-a[i][0]+1; dd = _d123idx(a[j][1:]-a[i][1:])
                    acc += dloc[p, :, k, i, j]*PF[b, mi, dd]*isq[mi]*isq[mj]
                acc -= (dV[p, :, k]/5.0)/Mv[mi]*PG[1, mi, 13]
            np.add.at(out, (c, tgt), 0.5*acc)
    return out

def dW_multi(S, L, settings, geom=None, verbose=False):
    """settings: list of (tau0, m2, improved).  Returns list of dW/ds_e arrays."""
    from bridge_geom import geometry
    g = geometry(S, L) if geom is None else geom
    H = {}
    for t, st in enumerate(settings):
        F, G = _FG(*st); H[f'F{t}'] = F; H[f'G{t}'] = G
    Phi = local_Hmatrix(S, L, H, geom=g, verbose=verbose)
    return [contract(Phi[f'F{t}'], Phi[f'G{t}'], g, L) for t in range(len(settings))]

def dW_reduced(S, L, tau0, m2=0.0, improved=True, geom=None):
    return dW_multi(S, L, [(tau0, m2, improved)], geom=geom)[0]

# ---------------------------------------------------------------- cutoff-resolved variant
def _FGheat(s, improved=True):
    """d/ds_e Tr e^{-s Delta} = Tr(F(B) Yhat) - Tr(G(B) Zhat) with F = -s e^{-s mu} mu'."""
    if improved:
        mu = lambda l: l + l*l/24.0; mup = lambda l: 1.0 + l/12.0
    else:
        mu = lambda l: l;            mup = lambda l: np.ones_like(l)
    F = lambda l: -s*np.exp(-s*mu(l))*mup(l)
    G = lambda l: -s*l*np.exp(-s*mu(l))*mup(l)
    return F, G

def dK_multi(S, L, slist, improved=True, geom=None, verbose=False):
    """per-edge gradient of the HEAT TRACE at proper time s (no cutoff integral)."""
    from bridge_geom import geometry
    g = geometry(S, L) if geom is None else geom
    H = {}
    for t, s in enumerate(slist):
        F, G = _FGheat(s, improved); H[f'F{t}'] = F; H[f'G{t}'] = G
    Phi = local_Hmatrix(S, L, H, geom=g, verbose=verbose)
    return [2.0*contract(Phi[f'F{t}'], Phi[f'G{t}'], g, L) for t in range(len(slist))]
