"""C5 R12-3, script 4: Theorem U illustration (continuum, SO(3)-covariant linear Nicolai Hessians on the gauge quotient).
Content: n_V vector fields (first n_G of them gauge), n_S scalars.  Most general SO(3)-covariant, real-field, Hermitian,
linear C1(q):  vector-vector a_{VV'} i eps.q (a real symmetric), scalar-vector K_{sV} q_j (K real), scalar-scalar 0.
Gauge invariance: C1 annihilates the longitudinal direction of each gauge vector => K[:, gauge] = 0.
For random (a, K) we report, at q = z-hat on the physical subspace (gauge longitudinals removed):
  number of zero eigenvalues of C1 (must be 0 for a relativistic, non-degenerate massless sector),
  Chern number of P+ on the unit sphere (Fukui-Hatsugai), and the twisted-helicity multiset of ALL eigenvectors,
  and whether that multiset can be paired into adjacent (h, h-1) doublets (= untwistable to spin-1/2 by an SU(2)_R)."""
import numpy as np, itertools
eps3 = np.zeros((3, 3, 3))
for (i, j, k), s in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
    eps3[i, j, k] = s
def build(a, K, nV, nG, nS, q):
    n = 3 * nV + nS
    C = np.zeros((n, n), complex)
    curl = 1j * np.einsum('ijk,j->ik', eps3, q)
    for V in range(nV):
        for W in range(nV):
            C[3*V:3*V+3, 3*W:3*W+3] = a[V, W] * curl
    for s in range(nS):
        for V in range(nV):
            C[3*nV+s, 3*V:3*V+3] = K[s, V] * q; C[3*V:3*V+3, 3*nV+s] = K[s, V] * q
    # physical subspace: remove longitudinal of gauge vectors
    qh = q / np.linalg.norm(q)
    G = [np.concatenate([np.zeros(3*V), qh, np.zeros(3*(nV-V-1)+nS)]) for V in range(nG)]
    Pphys = np.eye(n) - sum(np.outer(g, g) for g in G) if G else np.eye(n)
    w, U = np.linalg.eigh(Pphys)
    B = U[:, w > 0.5]
    return B.conj().T @ C @ B, B, n
def helicities(Cp, B, nV, nS):
    Lz = -1j * eps3[2]
    J = np.zeros((3*nV+nS, 3*nV+nS), complex)
    for V in range(nV):
        J[3*V:3*V+3, 3*V:3*V+3] = Lz
    Jp = B.conj().T @ J @ B
    w, U = np.linalg.eigh(Cp)
    out = []
    for sgn in (1, -1):
        S = U[:, (w > 1e-9) if sgn > 0 else (w < -1e-9)]
        if S.shape[1]:
            out += list(np.round(np.linalg.eigvalsh(S.conj().T @ Jp @ S), 6))
    return sorted(out), int(np.sum(np.abs(w) < 1e-9))
def pairable(hs):
    from collections import Counter
    c = Counter(int(round(h)) for h in hs)
    # adjacent doublets (h, h-1): greedy from the top
    for h in sorted(c, reverse=True):
        while c[h] > 0:
            if c.get(h-1, 0) > 0:
                c[h] -= 1; c[h-1] -= 1
            else:
                return False
    return True
rng = np.random.default_rng(7)
print(' nV nG nS | zero modes at q=z | twisted helicities (all eigvecs, q=z)        | untwistable | Chern(P+)')
for nV, nG, nS in [(1,1,0),(1,1,1),(2,1,1),(2,1,3),(3,1,2),(3,1,4),(2,2,0),(4,1,3),(4,1,5)]:
    a = rng.normal(size=(nV, nV)); a = a + a.T
    K = rng.normal(size=(nS, nV)); K[:, :nG] = 0
    Cp, B, n = build(a, K, nV, nG, nS, np.array([0, 0, 1.0]))
    hs, nz = helicities(Cp, B, nV, nS)
    # Chern of P+ on the unit sphere (only if no zero modes)
    ch = None
    if nz == 0:
        th = np.linspace(1e-4, np.pi-1e-4, 40); ph = np.linspace(0, 2*np.pi, 40, endpoint=False)
        fr = np.empty((40, 40), object)
        for i, t in enumerate(th):
            for j, p in enumerate(ph):
                q = np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])
                Cq, Bq, _ = build(a, K, nV, nG, nS, q)
                w, U = np.linalg.eigh(Cq); fr[i, j] = Bq @ U[:, w > 1e-9]
        def Uu(X, Y):
            d = np.linalg.det(X.conj().T @ Y); return d/abs(d)
        F = 0
        for i in range(39):
            for j in range(40):
                j2 = (j+1) % 40
                F += np.angle(Uu(fr[i,j], fr[i+1,j])*Uu(fr[i+1,j], fr[i+1,j2])*Uu(fr[i+1,j2], fr[i,j2])*Uu(fr[i,j2], fr[i,j]))
        for i, sg in ((0, 1), (39, -1)):
            pr = 1
            for j in range(40):
                pr *= Uu(fr[i,j], fr[i,(j+1) % 40])
            F += sg*np.angle(pr)
        ch = F/(2*np.pi)
    print('  %d  %d  %d |        %d          | %-44s |    %-5s    | %s' % (nV, nG, nS, nz, hs, pairable(hs) if nz == 0 else '-',
          'n/a (singular)' if ch is None else '%+.3f' % ch))
