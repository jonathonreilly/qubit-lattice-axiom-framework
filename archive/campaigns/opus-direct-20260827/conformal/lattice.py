import math, itertools
from collections import defaultdict
import numpy as np
from geom import W, PERMS, simplex_geometry, hinge_area_angle, HINGES

def build(L, eps, P, k):
    """Assemble translation-reduced stencil, lumped mass, total volume, Regge action.
    Only simplices with spatial base xvec=0 are enumerated; the rest follow by
    translation invariance in x_1,x_2,x_3 (exact for g = g(x_0))."""
    stencil = defaultdict(float)      # (x0, d0,d1,d2,d3) -> K value
    mass = np.zeros(L)
    vol = 0.0
    hinge_ang = defaultdict(float)    # key -> sum of dihedral angles
    hinge_area = {}
    for p0 in range(L):
        for wi in range(24):
            w = W[wi]
            V, K5, Gtil, l2 = simplex_geometry(p0, wi, eps, P, k)
            vol += V
            for a in range(5):
                mass[(p0+w[a][0]) % L] += V/5.0
                for b in range(5):
                    d = w[b]-w[a]
                    s0 = (p0+w[a][0]) % L
                    stencil[(s0,)+tuple(int(t) for t in d)] += K5[a,b]
            for tri, rest in HINGES:
                area, th = hinge_area_angle(Gtil, tri, rest)
                vs = sorted(tuple([p0+w[a][0]]+[int(t) for t in w[a][1:]]) for a in tri)
                v0 = vs[0]
                key = (v0[0] % L,
                       tuple(np.array(vs[1])-np.array(v0)),
                       tuple(np.array(vs[2])-np.array(v0)))
                hinge_ang[key] += th
                hinge_area[key] = area
    S = sum(hinge_area[kk]*(2*math.pi - hinge_ang[kk]) for kk in hinge_ang)
    # local improvement coefficient c(x) = tr g(x)/96 = C(x)/24, with
    # C(x) = (1/8) sum_{mu,+-} l^2(x, x +- e_mu)  -- from squared edge lengths only.
    from geom import gdiag
    C = np.zeros(L)
    for x0 in range(L):
        tot = 0.0
        for mu in range(4):
            for sgn in (+1,-1):
                xm = x0 + (0.5*sgn if mu==0 else 0.0)
                tot += gdiag(xm, eps, P, k)[mu]
        C[x0] = tot/8.0
    return dict(stencil=dict(stencil), mass=mass, vol=vol*L**3, S=S*L**3,
                nhinge=len(hinge_ang), C=C)

def bloch_spectra(L, stencil, mass, qchunk, improve=True, C=None):
    """Eigenvalues of M^-1 K for a batch of transverse momenta qchunk (n,3)."""
    off0 = defaultdict(lambda: np.zeros(L)); offp = defaultdict(lambda: np.zeros(L))
    offm = defaultdict(lambda: np.zeros(L))
    for kk, v in stencil.items():
        x0, d0, d1, d2, d3 = kk
        if   d0 == 0: off0[(d1,d2,d3)][x0] += v
        elif d0 == 1: offp[(d1,d2,d3)][x0] += v
        elif d0 == -1: offm[(d1,d2,d3)][x0] += v
        else: raise RuntimeError("unexpected d0 %d" % d0)
    q = np.asarray(qchunk, dtype=float)               # (n,3)
    n = q.shape[0]
    A = np.zeros((n,L), dtype=complex); B = np.zeros((n,L), dtype=complex)
    Bm = np.zeros((n,L), dtype=complex)
    for dd, arr in off0.items():
        A += np.exp(1j*(q@np.array(dd,dtype=float)))[:,None]*arr[None,:]
    for dd, arr in offp.items():
        B += np.exp(1j*(q@np.array(dd,dtype=float)))[:,None]*arr[None,:]
    for dd, arr in offm.items():
        Bm += np.exp(1j*(q@np.array(dd,dtype=float)))[:,None]*arr[None,:]
    # hermiticity cross-check: K[x0,x0-1] must equal conj(K[x0-1,x0])
    herm_err = np.max(np.abs(Bm - np.conj(np.roll(B,1,axis=1))))
    M = np.asarray(mass); r = 1.0/np.sqrt(M)
    H = np.zeros((n,L,L), dtype=complex)
    idx = np.arange(L)
    H[:, idx, idx] = A*(r*r)[None,:]
    H[:, idx, (idx+1) % L] += B*(r*np.roll(r,-1))[None,:]
    H[:, (idx+1) % L, idx] += np.conj(B)*(r*np.roll(r,-1))[None,:]
    if improve:
        if C is None:
            H = H + (H@H)/24.0                       # plain  Delta + Delta^2/24
        else:
            H = H + (H*np.asarray(C)[None,None,:])@H/24.0   # Delta + Delta C Delta /24
    ev = np.linalg.eigvalsh(H)
    return ev, herm_err
