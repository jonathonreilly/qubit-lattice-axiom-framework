"""Kill check K4: SAT-free, rigorous (Pauli class) counting form of Lemma S, and its true scaling.
F_s(q) = 1 iff the image a_u of a Majorana u at site s may have support on qubit q, i.e. iff site s is NOT
connected to the reference site in the graph G_q = (grid minus every NN edge whose r-dilated box contains q).
[This is exactly the ZERO-class of the attacker's union-find, computed by BFS.]
For a set S of sites (one Majorana each), R = union of pairwise F_s & F_t.  omega(a_s,a_t) is then carried
by the qubits of R only, and must be 1 for all pairs, so |S| <= 2|R|+1 (max anticommuting Paulis on |R| qubits).
|S| > 2|R|+1 => no Pauli images exist at that (L,r).  Attacker's preregistered bound used ALL far modes
((L-4)^2), which is not admissible: nearby far modes also overlap near their own ends."""
import itertools, sys, collections

def component_of_ref(L, r, q, ref=(0, 0)):
    qx, qy = q
    def edge_ok(a, b):
        lox, hix = min(a[0], b[0]) - r, max(a[0], b[0]) + r
        loy, hiy = min(a[1], b[1]) - r, max(a[1], b[1]) + r
        return not (lox <= qx <= hix and loy <= qy <= hiy)
    seen = {ref}; dq = collections.deque([ref])
    while dq:
        a = dq.popleft()
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            b = (a[0]+d[0], a[1]+d[1])
            if 0 <= b[0] < L and 0 <= b[1] < L and b not in seen and edge_ok(a, b):
                seen.add(b); dq.append(b)
    return seen

def analyse(L, r):
    sites = [(x, y) for x in range(L) for y in range(L)]
    F = {s: set() for s in sites}
    for q in sites:
        comp = component_of_ref(L, r, q)
        for s in sites:
            if s not in comp: F[s].add(q)
    sep = 2 * r + 1
    S = []
    for c in sites:
        if c == (0, 0): continue
        if all(max(abs(c[0]-d[0]), abs(c[1]-d[1])) >= sep for d in S):
            S.append(c)
    R = set()
    for a, b in itertools.combinations(S, 2):
        R |= (F[a] & F[b])
    return len(S), len(R), 2 * len(R) + 1

if __name__ == '__main__':
    for r in (1, 2, 3, 4):
        print(f"--- r={r}", flush=True)
        for L in range(4, 61, 4):
            if L * L * L * L > 6e6 * 4: break
            s, m, cap = analyse(L, r)
            print(f"L={L:2d} r={r}: |S|={s:3d} |R|={m:3d} capacity 2|R|+1={cap:4d} -> {'CONTRADICTION: no Pauli images exist' if s > cap else 'no contradiction from this S'}", flush=True)
