"""Scale-ladder probe 1 (finite-spin EM response lane).

Supplied model (same as docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md):
cubic-ice occupation carrier on the periodic L=2 torus, component of n_i(r)=r_i mod 2,
H_V[b]_{n,n^p} = -J exp(i eps(r) s_p(n) b_p), H_nn = V N_f(n), E_i(r)=eps(r)(n_i(r)-1/2).

Computes the FULL 24x24 plaquette-source Hessian R_pq = d^2 E_0 / db_p db_q at b=0 and
decomposes it by (i) exact 2-forms (gauge; must be annihilated), (ii) harmonic (q=0)
and (iii) co-exact at each nonzero lattice momentum q in {0,pi}^3.
Scale-ladder question: which momentum component of the transverse magnetic stiffness
K_T(q) did the frozen #7946 occupation-sign source measure, and how far is it from q->0?
Exploratory probe; no claim.
"""
import itertools, numpy as np

L = 2
sites = list(itertools.product(range(L), repeat=3))
sidx = {r: k for k, r in enumerate(sites)}
def add(r, i, s=1):
    r = list(r); r[i] = (r[i] + s) % L; return tuple(r)
def link(r, i): return 3 * sidx[r] + i
eps = {r: (-1) ** sum(r) for r in sites}
ORI = [(0, 1), (1, 2), (2, 0)]              # cyclic: dual vector components z, x, y
plaqs = []                                   # (root, orientation index, links, bsigns)
for r in sites:
    for o, (i, j) in enumerate(ORI):
        ls = [link(r, i), link(add(r, i), j), link(add(r, j), i), link(r, j)]
        plaqs.append((r, o, ls, (1, 1, -1, -1)))
NP, NL = len(plaqs), 3 * len(sites)

# BFS component
start = np.zeros(NL, dtype=np.int8)
for r in sites:
    for i in range(3): start[link(r, i)] = r[i] % 2
def key(n): return n.tobytes()
states = [start]; index = {key(start): 0}; moves = []   # (row, col, plaq, s)
k = 0
while k < len(states):
    n = states[k]
    for p, (r, o, ls, _) in enumerate(plaqs):
        a = n[ls[0]]
        if n[ls[1]] == 1 - a and n[ls[2]] == a and n[ls[3]] == 1 - a:
            m = n.copy(); m[ls] = 1 - m[ls]
            kk = key(m)
            if kk not in index: index[kk] = len(states); states.append(m)
            moves.append((k, index[kk], p, 2 * int(a) - 1))
    k += 1
N = len(states)
print(f"component states={N}, directed moves={len(moves)}")
# ice check
for n in states:
    for v in sites:
        tot = sum(n[link(v, i)] for i in range(3)) + sum(n[link(add(v, i, -1), i)] for i in range(3))
        assert tot == 3

def hessian(V, J=1.0):
    H = np.zeros((N, N)); Nf = np.zeros(N)
    D1 = np.zeros((NP, N, N))                 # dH/db_p (imaginary part stored, H' = i*D1)
    D2 = np.zeros((NP, N, N))
    for (a, b, p, s) in moves:
        H[a, b] += -J; Nf[a] += 1
        e = eps[plaqs[p][0]]
        D1[p, a, b] += -J * e * s             # H' = i * (-J eps s)
        D2[p, a, b] += J                      # H'' = -J (i eps s)^2 = +J
    H += np.diag(V * Nf)
    w, U = np.linalg.eigh(H)
    g = U[:, 0]; gap = w[1] - w[0]
    Vp = np.array([U.T @ (1j * D1[p]) @ g for p in range(NP)])   # <m|H'_p|0>
    den = w[1:] - w[0]
    R = np.zeros((NP, NP))
    for p in range(NP):
        R[p, p] += g @ D2[p] @ g
    M = (Vp[:, 1:] / den) @ Vp[:, 1:].conj().T
    R -= 2 * M.real
    return R, w[0], gap

# exact 2-forms: d1 (links -> plaquettes) with the boundary signs
d1 = np.zeros((NP, NL))
for p, (r, o, ls, sg) in enumerate(plaqs):
    for l, s in zip(ls, sg): d1[p, l] += s
# Fourier basis vectors
moms = list(itertools.product([0, 1], repeat=3))
def fvec(q, o):
    v = np.zeros(NP)
    for p, (r, oo, ls, _) in enumerate(plaqs):
        if oo == o: v[p] = (-1) ** sum(qi * ri for qi, ri in zip(q, r))
    return v / np.linalg.norm(v)

rows = []
for V in [1.0, 0.95, 0.9, 0.5, 0.0, -1.0]:
    R, E0, gap = hessian(V)
    Ex = d1 @ np.linalg.pinv(d1) ; gauge_resid = np.abs(R @ d1).max()
    vol = L ** 3
    b_unif_xy = np.array([1.0 if o == 0 else 0 for (r, o, ls, _) in plaqs])
    b_stag_xy = np.array([eps[r] if o == 0 else 0 for (r, o, ls, _) in plaqs])
    chi_u = b_unif_xy @ R @ b_unif_xy / vol
    chi_s = b_stag_xy @ R @ b_stag_xy / vol
    # momentum-resolved: for each q, 3x3 block in orientation space
    out = {}
    for q in moms:
        B = np.array([fvec(q, o) for o in range(3)])
        Rq = B @ R @ B.T                      # per-plaquette-normalised quadratic form
        ev = np.linalg.eigvalsh(Rq)
        out[q] = ev
    ev_all = np.linalg.eigvalsh(R)
    nzero = int((np.abs(ev_all) < 1e-9).sum())
    print(f"\nV={V:+.2f} E0={E0:.6f} gap={gap:.6f} |R d1|max={gauge_resid:.2e} zero-modes={nzero}")
    print(f"  chi uniform-xy (per vol) = {chi_u:.12f}   occupation-sign(xy staggered) = {chi_s:.12f}  ratio={chi_s/chi_u:.4f}")
    for q in moms:
        print(f"  q={tuple(np.pi*np.array(q)/np.pi)} (units of pi): 3x3 eigenvalues {np.round(out[q],6)}")
    # K_T(q): the single nonzero eigenvalue at q!=0 (per plaquette normalised -> multiply by 1)
    KQ = out[(1, 1, 1)].max(); K0 = out[(0, 0, 0)].mean()
    Kpi00 = out[(1, 0, 0)].max(); Kpipi0 = out[(1, 1, 0)].max()
    rows.append((V, K0, Kpi00, Kpipi0, KQ, chi_u, chi_s))
print("\nSummary  (K in units: d2E0/dtheta^2 per plaquette of one orientation, i.e. per volume)")
print(" V      K(0)harm   K(pi,0,0)  K(pi,pi,0) K(pi,pi,pi)  chi_s/K(Q)  K(Q)/K(0)")
for (V, K0, K1, K2, KQ, cu, cs) in rows:
    print(f"{V:+.2f}  {K0:.6f}  {K1:.6f}  {K2:.6f}  {KQ:.6f}   {cs/KQ:.4f}     {KQ/K0:.4f}")
