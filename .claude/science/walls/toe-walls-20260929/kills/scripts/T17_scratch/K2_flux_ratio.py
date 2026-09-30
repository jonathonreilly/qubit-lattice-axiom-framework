"""K2: in the stationary state of each closed class (N=3 records, 4x4 torus), compare the mean energy current
E[J_tot] with the (conserved) momentum P.  'Energy flows as momentum' would give E[J_tot] = P.
The 2026-09-21 wind-potential note predicts J = (1 - rho) g for the original clause (product states).
Uses K1's independent event generator."""
import itertools, sys
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
import K1_energy_current as K
K.Lx = 4
N = 3
Lx = 4
cfgs = []
for occ in itertools.combinations(range(Lx*Lx), N):
    for ks in itertools.product(range(4), repeat=N):
        cfgs.append(dict(zip(occ, ks)))
key = lambda c: tuple(sorted(c.items()))
idx = {key(c): i for i, c in enumerate(cfgs)}
for clause in ('orig', 'vstar'):
    rows, cols, vals = [], [], []
    J = np.zeros((len(cfgs), 2)); Pm = np.zeros((len(cfgs), 2))
    for i, c in enumerate(cfgs):
        for r, n, d in K.events(c, clause):
            j = idx[key(n)]
            if j != i:
                rows.append(i); cols.append(j); vals.append(r)
            J[i] += r * np.array(d)
        Pm[i] = K.Ptot(c)
    R = sp.csr_matrix((vals, (rows, cols)), shape=(len(cfgs),)*2)
    nc, lab = sp.csgraph.connected_components(R, directed=True, connection='strong')
    sizes = np.bincount(lab)
    print(f'clause {clause}: {len(cfgs)} configs, {nc} strong classes')
    seen = 0
    for c in np.argsort(-sizes):
        ii = np.where(lab == c)[0]
        if len(ii) < 300: break
        sub = R[ii][:, ii]
        if R[ii].sum() - sub.sum() > 1e-12: continue        # not closed
        Pc = Pm[ii[0]]
        if np.abs(Pc).max() == 0: continue
        Q = sub - sp.diags(np.asarray(sub.sum(axis=1)).ravel())
        A = Q.T.tolil(); A[0, :] = 1.0
        b = np.zeros(len(ii)); b[0] = 1.0
        pi = spl.spsolve(A.tocsc(), b)
        EJ = pi @ J[ii]
        m = np.argmax(np.abs(Pc))
        print(f'   closed class size {len(ii)}: P={Pc}, E_stationary[J_tot]={np.round(EJ,4)}, ratio E[J]/P (component {m}) = {EJ[m]/Pc[m]:.4f}')
        seen += 1
        if seen >= 3: break
print('uniform-measure expectation for the original clause: (NS-N)/(NS-1) =', (Lx*Lx-N)/(Lx*Lx-1))
