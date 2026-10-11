"""M1 (1b): N-body clusters on Z (N=2,3,4), exact in a truncated relative box (fibre H(Q) is an
exactly 2pi-periodic analytic family at every box size R).
Constituents eps(k) = m + 2t(1-cos k) (nearest-neighbour), m=1, t=0.5 -> beta = u''(0) = 2tm = 1.
(a) soft-core contact attraction U (attractive Bose-Hubbard clusters, McGuire-type);
(b) hard-core + NN attraction = ferromagnetic XXZ n-magnon strings; compare exact
    E_n(K) = J sinh(eta) (cosh(n eta) - cos K)/sinh(n eta), Delta = cosh eta.
For the lowest cluster band: u=E^2/2, beta_N = u''(0), anomaly A(Q)=u''/beta - 1, its zone average,
the IR anomaly against the constituent's anomaly at Q/N, and the face concentration.
"""
import numpy as np, itertools, scipy.sparse as sp
from scipy.sparse.linalg import eigsh
np.set_printoptions(precision=5, suppress=True)

def build(N, R, Q, m, t, U0, U1, hardcore):
    # configurations r = (r_2..r_N), relative to particle 1
    if hardcore:
        confs = [c for c in itertools.combinations(range(1, R+1), N-1)]  # ordered 0<r2<...<rN<=R
    else:
        confs = list(itertools.product(range(-R, R+1), repeat=N-1))
    idx = {c: i for i, c in enumerate(confs)}
    rows, cols, vals = [], [], []
    diag = np.zeros(len(confs))
    for i, c in enumerate(confs):
        pos = (0,) + c
        e = N*(m + 2*t)
        for a in range(N):
            for b in range(a+1, N):
                dd = abs(pos[a]-pos[b])
                if dd == 0: e += U0
                elif dd == 1: e += U1
        diag[i] = e
        # particle i>=2 hops
        for j in range(N-1):
            for s in (+1, -1):
                c2 = list(c); c2[j] += s; c2 = tuple(c2)
                if c2 in idx:
                    rows.append(idx[c2]); cols.append(i); vals.append(-t)
        # particle 1 hops by s: phi(r - s)  -> amplitude -t e^{iQs} on <r| from |r - s>  i.e. H[r, r-s]
        for s in (+1, -1):
            c2 = tuple(x - s for x in c)   # source config
            if c2 in idx:
                rows.append(i); cols.append(idx[c2]); vals.append(-t*np.exp(1j*Q*s))
    H = sp.csr_matrix((vals, (rows, cols)), shape=(len(confs), len(confs)), dtype=complex) + sp.diags(diag)
    return H

def lowest(H, k=2):
    n = H.shape[0]
    if n < 400:
        w = np.linalg.eigvalsh(H.toarray()); return w[:k]
    w = eigsh(H, k=k, which='SA', return_eigenvectors=False, tol=1e-12)
    return np.sort(w)

def band(N, R, m, t, U0, U1, hardcore, nQ):
    Qs = np.arange(nQ)*2*np.pi/nQ - np.pi
    E = np.zeros(nQ); gap = np.zeros(nQ)
    for i, Q in enumerate(Qs):
        w = lowest(build(N, R, Q, m, t, U0, U1, hardcore))
        E[i] = w[0]; gap[i] = w[1]-w[0]
    return Qs, E, gap

def spec_d2(f, h):
    n = len(f); kk = np.fft.fftfreq(n, d=h)*2*np.pi
    return np.real(np.fft.ifft(-(kk**2)*np.fft.fft(f)))

if __name__ == "__main__":
    print(__doc__)
    m, t = 1.0, 0.5
    beta = 2*t*m
    print("constituent anomaly A_1(k)=u''-1 for eps=m+2t(1-cos k):  A_1(k) = eps*2t cos k + 4t^2 sin^2 k - 1")
    A1 = lambda k: (m+2*t*(1-np.cos(k)))*2*t*np.cos(k) + 4*t*t*np.sin(k)**2 - 1
    nQ = 64
    for N, R, Us in [(2, 120, [-0.25, -0.5, -1.0, -2.0, -4.0]), (3, 36, [-0.5, -1.0, -2.0, -4.0]), (4, 13, [-1.0, -2.0, -4.0])]:
        for U in Us:
            Qs, E, gap = band(N, R, m, t, U, 0.0, False, nQ)
            h = Qs[1]-Qs[0]; u = 0.5*E**2; upp = spec_d2(u, h)
            i0 = np.argmin(abs(Qs)); iq = np.argmin(abs(Qs-np.pi/4))
            A = upp/beta - 1
            B = N*m - E[i0]
            print(f"N={N} U={U:+.2f} R={R}: E(0)={E[i0]:.5f} B(0)={B:.4f} min gap to next level={gap.min():.4f} "
                  f"(Q at min gap {Qs[np.argmin(gap)]:+.2f})")
            print(f"    beta_N/beta = {upp[i0]/beta:.5f}  [1 - B/(N m) = {1-B/(N*m):.5f}];  zone avg A = {A.mean():+.6f} "
                  f"(sum rule => -1);  avg u''={upp.mean():+.1e}")
            print(f"    A(pi/4) = {A[iq]:+.4f}   constituent A_1(pi/4)={A1(np.pi/4):+.4f}, A_1(pi/(4N))={A1(np.pi/(4*N)):+.4f};"
                  f"  A(face) = {A[0]:+.3f};  min A = {A.min():+.3f}")
            # check sensitivity to box size for the weakest binding
    print()
    print("XXZ ferromagnet n-magnon strings: hard-core, NN attraction -J*Delta, hopping J/2; J=1")
    J = 1.0
    for Delta in [1.5, 3.0]:
        eta = np.arccosh(Delta)
        for n, R in [(1, 40), (2, 120), (3, 40), (4, 24)]:
            Qs, E, gap = band(n, R, J*(Delta-1), J/2, 0.0, -J*Delta, True, 32) if n > 1 else (None, None, None)
            if n == 1:
                Qs = np.arange(32)*2*np.pi/32 - np.pi; E = J*(Delta - np.cos(Qs)); gap = np.ones(32)
            exact = J*np.sinh(eta)*(np.cosh(n*eta) - np.cos(Qs))/np.sinh(n*eta)
            h = Qs[1]-Qs[0]; u = 0.5*E**2; upp = spec_d2(u, h)
            bn = upp[np.argmin(abs(Qs))]
            print(f"  Delta={Delta} n={n}: max|E_num - E_exact| = {np.max(abs(E-exact)):.2e}; band max={E.max():.4f} "
                  f"(n->inf limit J sinh eta={J*np.sinh(eta):.4f}); bandwidth={E.max()-E.min():.3e}; own beta_n={bn:.3e}; "
                  f"<u''>={upp.mean():+.1e}")
