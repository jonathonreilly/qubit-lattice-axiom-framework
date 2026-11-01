# Runner for docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md
# Requirements: Python 3, numpy, scipy (generated with numpy 2.5.4, scipy 1.18.1). No file I/O; output to stdout.
# Run from the repo root:  python3 scripts/mdtn_ed_part2_su2_boxes_2026_10_31.py > logs/runner-cache/mdtn_ed_part2_su2_boxes_2026_10_31.txt
"""Part 2: ED of the canonical-singlet ASQR SU(2) MDTN Hamiltonian on open Z^3 boxes.
On the canonical-singlet sector the model is exactly H = sum_l n_l - delta * sum_P X_P on the Z2 cycle space
(n = binary flux labels, X_P: n -> n xor dP).  Also: (i) full link-qubit space for a single cube, showing the
band structure (charged states near 1,2,3; physical states only from 4); (ii) comparison with second-order
degenerate perturbation theory: gap = 4 + d^2/2 - (d^2/4) * lambda_max(D + A) (D, A: plaquette edge-adjacency).
"""
import numpy as np, itertools, sys, time
import scipy.sparse as sp, scipy.sparse.linalg as sla

def box(a, b, c):
    V = [(x, y, z) for x in range(a+1) for y in range(b+1) for z in range(c+1)]
    links = []
    for (x, y, z) in V:
        for d, (dx, dy, dz) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            w = (x+dx, y+dy, z+dz)
            if w[0] <= a and w[1] <= b and w[2] <= c:
                links.append(((x, y, z), d))
    lid = {l: i for i, l in enumerate(links)}
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    plaqs = []
    for (x, y, z) in V:
        for d1, d2 in [(0, 1), (0, 2), (1, 2)]:
            p = (x, y, z); q = tuple(np.add(p, e[d1])); r = tuple(np.add(p, e[d2]))
            if all(0 <= q[i] <= (a, b, c)[i] and 0 <= r[i] <= (a, b, c)[i] for i in range(3)):
                ls = [(p, d1), (p, d2), (q, d2), (r, d1)]
                if all(l in lid for l in ls):
                    plaqs.append([lid[l] for l in ls])
    return V, links, plaqs

def cycle_states(nlinks, pmasks):
    seen = {0: 0}; order = [0]; k = 0
    while k < len(order):
        s = order[k]; k += 1
        for m in pmasks:
            t = s ^ m
            if t not in seen:
                seen[t] = len(order); order.append(t)
    return np.array(order, dtype=np.int64), seen

def build(nlinks, plaqs):
    pmasks = [sum(1 << l for l in p) for p in plaqs]
    st, idx = cycle_states(nlinks, pmasks)
    N = len(st)
    diag = np.array([bin(int(s)).count('1') for s in st], float)
    rows = []; cols = []
    for m in pmasks:
        tgt = np.array([idx[int(s) ^ m] for s in st], dtype=np.int64)
        rows.append(np.arange(N)); cols.append(tgt)
    X = sp.csr_matrix((np.ones(N*len(pmasks)), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))
    return st, sp.diags(diag).tocsr(), X

def pt2(plaqs):
    P = [set(p) for p in plaqs]; n = len(P)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            if len(P[i] & P[j]) == 1: A[i, j] = A[j, i] = 1
    D = np.diag(A.sum(1))
    return np.linalg.eigvalsh(D+A)[-1]

deltas = [0.0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0]
boxes = [(1, 1, 1), (1, 1, 2), (1, 1, 3), (2, 2, 1), (1, 1, 4)]
print("canonical-singlet ASQR SU(2) MDTN, open boxes; gap = E1 - E0 in the physical (Gauss) sector, units of E(doublet link)=1")
res = {}
for bx in boxes:
    V, links, plaqs = box(*bx)
    t0 = time.time()
    st, N0, X = build(len(links), plaqs)
    lam = pt2(plaqs)
    print(f"box {bx}: links={len(links)} sites={len(V)} plaquettes={len(plaqs)} dim(phys canonical sector)={len(st)} "
          f"(=2^{int(np.log2(len(st)))}); lambda_max(D+A)={lam:.4f}; build {time.time()-t0:.1f}s")
    for d in deltas:
        H = N0 - d*X
        if d == 0.0:   # diagonal; eigsh is unreliable on the exactly degenerate spectrum
            e = np.sort(N0.diagonal())[:2]
        elif len(st) <= 4096:
            e = np.linalg.eigvalsh(H.toarray())[:2]
        else:
            e = np.sort(sla.eigsh(H, k=2, which='SA', tol=1e-10)[0])
        g = e[1]-e[0]
        res[(bx, d)] = g
        print(f"   delta={d:5.2f}  E0={e[0]: .6f}  gap={g:.6f}   PT2: {4+d*d/2-d*d/4*lam:.6f}")
    sys.stdout.flush()

# (i) full link-qubit space for a single cube: H' = sum n_l - delta sum_P X_P on 2^12 states, Gauss parity sectors
V, links, plaqs = box(1, 1, 1)
L = len(links); Nst = 1 << L
pm = [sum(1 << l for l in p) for p in plaqs]
site_masks = []
for v in V:
    m = 0
    for i, (s, d) in enumerate(links):
        t = tuple(np.add(s, [(1, 0, 0), (0, 1, 0), (0, 0, 1)][d]))
        if s == v or t == v: m |= 1 << i
    site_masks.append(m)
states = np.arange(Nst)
pop = np.array([bin(s).count('1') for s in states], float)
gauss = np.array([all(bin(s & m).count('1') % 2 == 0 for m in site_masks) for s in states])
print("\n(i) single cube, FULL link-qubit space (2^12), H' = sum n - delta sum X_P:")
for d in [0.0, 0.1, 0.3]:
    H = np.diag(pop)
    for m in pm:
        H[states ^ m, states] -= d
    e, v = np.linalg.eigh(H)
    # each eigvec lies in one Gauss sector (X_P preserve parities): classify
    isphys = [np.sum(np.abs(v[gauss, k])**2) > 0.5 for k in range(len(e))]
    lowest = [(round(e[k]-e[0], 4), 'phys' if isphys[k] else 'charged') for k in range(8)]
    ephys = e[np.array(isphys)]
    print(f"   delta={d}: lowest 8 levels (rel. to E0) = {lowest}")
    print(f"              ground state physical: {isphys[0]};  physical-sector gap = {ephys[1]-ephys[0]:.6f}")
