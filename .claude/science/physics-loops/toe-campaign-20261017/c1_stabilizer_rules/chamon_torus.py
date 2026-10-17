"""Chamon rule on L^3 tori: rank, code dimension and sign consistency of generator products."""
import numpy as np, itertools, sys
import galois
GF = galois.GF(2)
def run(L):
    n = L**3; idx = lambda p: ((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)
    rows, labs = [], []
    for v in itertools.product(range(L), repeat=3):
        x = np.zeros(2*n, int); lab = {}
        for a, P in ((0, 'X'), (1, 'Y'), (2, 'Z')):
            for s in (1, -1):
                p = list(v); p[a] += s; i = idx(p)
                if i in lab: lab[i] = None  # same qubit twice (L=2): product of equal Paulis = I
                else: lab[i] = P
        for i, P in lab.items():
            if P is None: continue
            if P in 'XY': x[i] = 1
            if P in 'YZ': x[n+i] = 1
        rows.append(x); labs.append(lab)
    M = GF(np.array(rows))
    r = np.linalg.matrix_rank(M)
    # relations: left null space; check sign of each relation's Pauli product
    N = M.T.null_space()   # vectors c with c M = 0
    bad = 0
    for c in N:
        sel = [k for k in range(len(rows)) if int(c[k])]
        # multiply Pauli strings in order, tracking phase exactly
        phase = 0; cur = {}
        mult = {('X','Y'):('Z',1),('Y','X'):('Z',3),('Y','Z'):('X',1),('Z','Y'):('X',3),('Z','X'):('Y',1),('X','Z'):('Y',3)}
        for k in sel:
            for i, P in labs[k].items():
                if P is None: continue
                Q = cur.get(i)
                if Q is None: cur[i] = P
                elif Q == P: del cur[i]
                else: R_, ph = mult[(Q, P)]; cur[i] = R_; phase += ph
        assert not cur
        if phase % 4 != 0: bad += 1
    print(f'L={L}: qubits {n}, generator rank {r}, log2 code dim {n - r}, relations {len(N)}, relations with product -1 or +-i: {bad}', flush=True)
for L in map(int, sys.argv[1:]): run(L)
