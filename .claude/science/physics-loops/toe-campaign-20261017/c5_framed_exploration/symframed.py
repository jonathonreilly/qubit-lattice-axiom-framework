"""Fermionic framed toric codes with an imposed rotation symmetry H (edge qubits, labels fixed)."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts'); sys.path.insert(0, '../c4')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from stats import t_junction
exec(open('framed.py').read().split("cands = [()]")[0])
O = c1.O
def m(rows): return np.array(rows)
def find(M): return next(i for i, g in enumerate(O) if np.array_equal(g, M))
def closure(gens):
    G = [np.eye(3, dtype=int)]
    while True:
        new = [g @ h for g in G for h in gens if not any(np.array_equal(g @ h, k) for k in G)]
        if not new: return G
        for x in new:
            if not any(np.array_equal(x, k) for k in G): G.append(x)
C4z = m([[0,-1,0],[1,0,0],[0,0,1]]); C2x = m([[1,0,0],[0,-1,0],[0,0,-1]]); C2z = m([[-1,0,0],[0,-1,0],[0,0,1]])
C3 = m([[0,0,1],[1,0,0],[0,1,0]]); C2d = m([[0,-1,0],[-1,0,0],[0,0,-1]])
SUB = {'O': closure([C4z, C3]), 'T': closure([C3, C2z]), 'D4z': closure([C4z, C2x]), 'D3': closure([C3, C2d]),
       'C4z': closure([C4z]), 'D2': closure([C2x, C2z]), 'C3': closure([C3])}
def rot_edge(M, base, a):
    v = tuple(int(x) for x in M @ np.array(base)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
    return (v if d[b] == 1 else tuple(v[i] - (1 if i == b else 0) for i in range(3))), b
CAND = [(d, b) for d in itertools.product((-1,0,1), repeat=3) for b in range(3)]
def framings(H, maxk=2):
    """All S = (S_0,S_1,S_2) with |S_a| <= maxk, invariant: R(S_a around edge (0,a)) = S_{pi a} around R(edge)."""
    reps = []; seen = set()
    for a in range(3):
        if a in seen: continue
        orb = {rot_edge(M, (0,0,0), a)[1] for M in H}; seen |= orb; reps.append(a)
    subsets = [()] + [tuple(c) for k in range(1, maxk + 1) for c in itertools.combinations(CAND, k)]
    def transport(M, a, Sa):
        w, b = rot_edge(M, (0,0,0), a)
        out = set()
        for (d, q) in Sa:
            p, c = rot_edge(M, d, q); out.add((tuple(p[i] - w[i] for i in range(3)), c))
        return b, frozenset(out)
    for choice in itertools.product(subsets, repeat=len(reps)):
        S = [None] * 3; ok = True
        for a, Sa in zip(reps, choice):
            for M in H:
                b, T = transport(M, a, Sa)
                if S[b] is None: S[b] = T
                elif S[b] != T: ok = False; break
            if not ok: break
        if ok and all(s is not None for s in S): yield [tuple(sorted(s)) for s in S]
def run(name, maxk):
    H = SUB[name]; t0 = time.time(); n = nc = 0; fer = []
    for S in framings(H, maxk):
        n += 1
        P = [plaq(c, S) for c in range(3)]
        if not commute(P): continue
        nc += 1
        r = t_junction([A] + P, 3, 0, [(1,0,0),(0,1,0),(0,0,1)], R=3)
        if r[0] == -1: fer.append(S); print('  FERMION', name, S, flush=True)
    print(f'{name} (|H|={len(H)}): invariant framings {n}, commuting {nc}, fermionic {len(fer)}  [{time.time()-t0:.0f}s]', flush=True)
for name in sys.argv[2:]: run(name, int(sys.argv[1]))
