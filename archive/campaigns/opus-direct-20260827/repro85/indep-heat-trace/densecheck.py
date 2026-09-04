"""Independent dense assembly over ALL L^4 unit cells (no translation-invariance
assumption anywhere) vs the Bloch-block spectrum."""
import numpy as np, math, itertools
from geom import W, simplex_geometry
from lattice import build, bloch_spectra

def dense_spectrum(L, eps, P, k, improve=True):
    N = L**4
    idx = lambda v: (((v[0]%L)*L + v[1]%L)*L + v[2]%L)*L + v[3]%L
    Kf = np.zeros((N,N)); M = np.zeros(N)
    cache = {}
    for p in itertools.product(range(L),repeat=4):
        for wi in range(24):
            key = (p[0],wi)
            if key not in cache: cache[key] = simplex_geometry(p[0],wi,eps,P,k)[:2]
            V,K5 = cache[key]
            vs = [idx(np.array(p)+W[wi][a]) for a in range(5)]
            for a in range(5):
                M[vs[a]] += V/5.0
                for b in range(5):
                    Kf[vs[a],vs[b]] += K5[a,b]
    r = 1.0/np.sqrt(M)
    H = Kf*r[:,None]*r[None,:]
    ev = np.linalg.eigvalsh(H)
    if improve: ev = ev+ev*ev/24.0
    return np.sort(ev), M

if __name__=="__main__":
    for L in (4,6):
        for eps,P in ((0.0,(0,0,0,0)),(0.13,(0,1,-1,0)),(0.13,(1,1,1,1))):
            k = 2*math.pi/L
            ev_d, M = dense_spectrum(L,eps,P,k)
            r = build(L,eps,P,k)
            qs = np.array(list(itertools.product(range(L),repeat=3)))*(2*np.pi/L)
            ev_b, herm = bloch_spectra(L, r['stencil'], r['mass'], qs)
            ev_b = np.sort(ev_b.ravel())
            mass_err = np.max(np.abs(M.reshape(L,L,L,L)[:,0,0,0]-r['mass']))
            print("L=%d eps=%.2f P=%-10s  max|d lambda|=%.3e  (spec range %.4f..%.4f)  herm=%.1e  massdiff=%.1e"
                  %(L,eps,str(P),np.max(np.abs(ev_d-ev_b)),ev_d.min(),ev_d.max(),herm,mass_err))
