"""
T202 - EXACT continuum reference for the conformal heat-trace channel.

Both prior lanes compared the lattice measurement against a TRUNCATED
Seeley-DeWitt series (a0 + s a1 + s^2 a2).  The residual therefore mixes
    (i)  lattice discretisation error   -- what we want,
    (ii) series truncation error O(x^3) -- an artefact of the diagnostic.
That is why neither lane could tell a non-plateau from a bad window.

Here the continuum operator on the SAME perturbed torus is diagonalised exactly
in a truncated plane-wave basis, giving K2_cont(s) with NO series truncation.
Then
    Rlat - Rcont  =  pure lattice error      (must vanish as a^2)
    Rcont - Rser  =  pure series truncation  (must vanish as x^3)

CONTINUUM OPERATOR  (g = e^{2w} delta, e^{2w} = 1 + eps cos(kappa x0), d=4)
  stiffness  a(f,g) = int W  grad f . grad g ,  W = e^{2w}
  mass       m(f,g) = int rho f g ,             rho = e^{4w} = W^2
  plane waves e^{ikx}/sqrt(V):
     A[k,k'] = (k.k') What(k-k'),  What(0)=1, What(+-kappa)=eps/2
     M[k,k'] = rhohat(k-k'),       rhohat(0)=1+eps^2/2, (+-kappa)=eps, (+-2kappa)=eps^2/4
  kappa = 2 pi n / L couples j0 -> j0 +- n, so the basis splits into chains
  indexed by (j0 mod n, q^2).  Exact, not perturbative.
"""
import numpy as np, sys, time
from collections import Counter
from opus_t200 import heat, K2, winding, qspec

def conv(ca, cb):
    c = Counter()
    for a, na in ca.items():
        for b, nb in cb.items():
            c[a+b] += na*nb
    return c

def q2_buckets(J):
    j = np.arange(-J, J+1)
    c1 = Counter((j*j).tolist())
    return conv(conv(c1, c1), c1)

def cont_heat(L, eps, n_mode, svals, J):
    """exact continuum Tr e^{-s Delta} on the perturbed torus, basis |j|<=J."""
    tp = 2*np.pi/L
    kap_i = n_mode
    Wh   = {0: 1.0, 1: eps/2, -1: eps/2}
    Rh   = {0: 1.0+eps*eps/2, 1: eps, -1: eps, 2: eps*eps/4, -2: eps*eps/4}
    QB = q2_buckets(J)
    sv = np.asarray(svals, float)
    out = np.zeros(len(sv))
    chains = []
    for r in range(n_mode):
        j0 = np.array([v for v in range(-J, J+1) if (v - r) % n_mode == 0], dtype=float)
        chains.append(j0*tp)
    for q2i, mult in QB.items():
        q2 = q2i*tp*tp
        for k0 in chains:
            nb = len(k0)
            A = np.zeros((nb, nb)); M = np.zeros((nb, nb))
            for d, wv in Wh.items():
                if d == 0:
                    A[np.arange(nb), np.arange(nb)] = (k0*k0 + q2)*wv
                else:
                    i = np.arange(max(0, -d), min(nb, nb-d))
                    A[i, i+d] = (k0[i]*k0[i+d] + q2)*wv
            for d, rv in Rh.items():
                i = np.arange(max(0, -d), min(nb, nb-d))
                M[i, i+d] = rv
            ev, U = np.linalg.eigh(M)
            Mih = (U/np.sqrt(ev)) @ U.T
            B = Mih @ A @ Mih
            B = 0.5*(B+B.T)
            lam = np.linalg.eigvalsh(B)
            np.maximum(lam, 0.0, out=lam)
            out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

def cont_K2(L, n_mode, svals, h, J):
    f = {e: cont_heat(L, e*h, n_mode, svals, J) for e in (-2, -1, 0, 1, 2)}
    d2 = (-f[2] + 16*f[1] - 30*f[0] + 16*f[-1] - f[-2])/(12*h*h)
    return 0.5*d2, f[0]

if __name__ == "__main__":
    L = int(sys.argv[1]); n_mode = 2
    Js = [int(a) for a in sys.argv[2:]] or [26]
    kappa = 2*np.pi*n_mode/L; k2 = kappa**2
    xs = np.array([0.25, 0.4, 0.6, 0.8, 1.0, 1.4, 2.0, 3.0])
    sv = xs/k2
    V2 = L**4/2.0
    print(f"=== L={L} n={n_mode} kappa^2={k2:.6f} ===")
    print("  x      : " + " ".join(f"{q:9.3f}" for q in xs))
    print("  s      : " + " ".join(f"{q:9.3f}" for q in sv))
    Rser = 1 + xs/4 + xs**2/8
    for J in Js:
        t0 = time.time()
        c2, cflat = cont_K2(L, n_mode, sv, 0.05, J)
        Rcont = (4*np.pi*sv)**2 * c2 / V2
        wr = cflat/winding(L, sv) - 1.0
        print(f"  J={J:3d} flat vs winding : " + " ".join(f"{q:9.2e}" for q in wr))
        print(f"  J={J:3d} Rcont           : " + " ".join(f"{q:9.5f}" for q in Rcont))
        print(f"  J={J:3d} Rcont-Rser      : " + " ".join(f"{q:9.5f}" for q in Rcont-Rser))
        print(f"        [{time.time()-t0:.1f}s]")
    QC = qspec(L)
    for improved in (True, False):
        lk2, _ = K2(L, kappa, sv, 0.05, improved, QC)
        Rlat = (4*np.pi*sv)**2 * lk2 / V2
        tag = "IMPR" if improved else "plain"
        print(f"  {tag} Rlat            : " + " ".join(f"{q:9.5f}" for q in Rlat))
        print(f"  {tag} Rlat-Rcont      : " + " ".join(f"{q:9.5f}" for q in Rlat-Rcont))
