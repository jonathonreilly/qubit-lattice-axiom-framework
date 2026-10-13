"""R19-32 s4 (pre-registered 07:33Z): SPECTRAL lowering parts (the energy-lowering components of the local de Donder field
chi_n(x) with respect to the actual truncated H) -- the alternative reading of "lowering parts" that keeps V H-invariant
by construction. V_spec = (+)_E V_E, V_E = {v in eigenspace E : P_{<E} chi_n(x) v = 0 for all n, x} (proved equivalent to
cap_{w>0} ker chi_n(x)_w). The ground state is always in V_spec. Questions: Krein Gram on low V_E (one-particle level:
CCR gives null), quotient signature in a low-energy window, and CCR-consistency of chi^+ (s1/mb).
Prediction (07:33Z): one-particle V_E states have Gram ~ (Omega_k^2 - w_k^2)/w_k^2 + top-level terms != 0 (truncated
one-particle energy Omega_k vs the constraint's lattice symbol w_k): spurious non-null states at every finite d.
"""
import numpy as np, scipy.sparse as sp, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *
sec, L, tw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ds = [int(a) for a in sys.argv[4].split(',')]; nu = float(sys.argv[5]); nlev = int(sys.argv[6]) if len(sys.argv) > 6 else 12
for d in ds:
    t0 = time.time(); S = Sector(sec, L, d, nu, tw)
    if S.dim <= 4100:
        H = S.H.toarray(); assert np.abs(H - H.conj().T).max() < 1e-12
        E, U = np.linalg.eigh(H)
    else:                                   # low-energy window only (07:52Z): lowest nwin eigenpairs, last cluster dropped
        import scipy.sparse.linalg as sla
        nwin = int(sys.argv[7]) if len(sys.argv) > 7 else 60
        E, U = sla.eigsh(S.H, k=nwin, which='SA', tol=1e-12); o = np.argsort(E); E, U = E[o], U[:, o]
    # clusters
    cl = []; i = 0
    while i < len(E):
        j = i
        while j + 1 < len(E) and E[j+1] - E[i] < 1e-8: j += 1
        cl.append((i, j + 1)); i = j + 1
    if S.dim > 4100: cl = cl[:-1]
    chis = [S.chi(r, x) for r in range(len(S.rows)) for x in range(L)]
    Xs = [U.conj().T@(c@U) for c in chis]
    eta = S.eta
    E0 = E[0]
    print(f"{sec} L={L} {'AP' if tw<0 else 'P '} d={d} nu={nu}: dim {S.dim}; ws={np.round(S.ws,4)}; E0={E0:.6f}; first levels (E-E0, degeneracy):",
          [(round(E[a]-E0, 5), b - a) for (a, b) in cl[:8]], flush=True)
    tot_pos = tot_neg = tot_null = 0
    for ci, (a, b) in enumerate(cl[:nlev]):
        Uc = U[:, a:b]
        if a == 0:
            V = np.eye(b - a)
        else:
            Mrows = np.vstack([X[:a, a:b] for X in Xs])
            uu, s, vh = np.linalg.svd(Mrows); r = int((s > 1e-9*max(1, s.max())).sum()); V = vh[r:].conj().T
        if V.shape[1] == 0:
            print(f"   level {ci}: E-E0={E[a]-E0:.5f} deg {b-a}: dim V_E = 0"); continue
        W = Uc@V; Gram = W.conj().T@(eta[:, None]*W); Gram = (Gram + Gram.conj().T)/2
        ev = np.linalg.eigvalsh(Gram)
        p = int((ev > 1e-9).sum()); n = int((ev < -1e-9).sum()); z = len(ev) - p - n
        tot_pos += p; tot_neg += n; tot_null += z
        print(f"   level {ci}: E-E0={E[a]-E0:.5f} deg {b-a}: dim V_E = {V.shape[1]}, Gram eigenvalues {np.round(ev, 7)}")
    print(f"   window of {nlev} levels: V_spec inertia (+,-,0) = ({tot_pos},{tot_neg},{tot_null}); quotient (+,-) = ({tot_pos},{tot_neg})  [{time.time()-t0:.1f}s]", flush=True)
