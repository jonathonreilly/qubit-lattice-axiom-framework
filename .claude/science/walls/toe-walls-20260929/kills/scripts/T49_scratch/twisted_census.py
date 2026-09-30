"""Kill check T49: the massive staggered model H(t,m) has MORE symmetry than the attack's reduced group.
09-03 note Thm 2: C H(t,m) C^-1 = H(t,-m), with C: c_v -> eps_v c_v^dag (checked below: hop invariant, mass flips).
An odd coarse translation flips eps too, so T_a * C is an exact symmetry of H(t,m).
Redo the pairing census for the group G' = (attack's mass-preserving group) U {T_a C}.
Transformation of Delta under c_v -> omega_v c^dag_{pv}, omega=eps*s:  Delta_{pi,pj} = -eps_i eps_j s_i s_j conj(Delta_ij).
Re part: sign -eps eps s s ; Im part: sign +eps eps s s.  Plain elements: +s s on both."""
import sys, itertools
import numpy as np
sys.argv = ['x', sys.argv[1] if len(sys.argv) > 1 else '8']
ATT = '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T49_scratch/'
exec(open(ATT + 'massive_bdg.py').read().split('h = np.zeros((N, N))')[0])   # gens, mg, all_invariants, class_of, rots, coords, idx, hop, N, L
eps = np.array([(-1) ** (sum(coords(i))) for i in range(N)], dtype=int)

# control 1: C: c_v -> eps_v c_v^dag maps hop -> hop (h_ij -> -eps_i eps_j h_ji) and mass -> -mass
ok = all(-eps[i] * eps[j] * hop[(j, i)] == hop[(i, j)] for (i, j) in hop)
print("control C invariance of KS hopping (omega=eps):", ok)

# generators: plain (mass-preserving) + twisted odd translations
plain = mg
twisted = {"tx": gens["tx"], "ty": gens["ty"], "tz": gens["tz"]}

class UF:
    def __init__(self): self.p = {}; self.w = {}; self.bad = set()
    def find(self, a):
        if a not in self.p: self.p[a] = a; self.w[a] = 1; return a, 1
        path = []; cur = a
        while self.p[cur] != cur: path.append(cur); cur = self.p[cur]
        root = cur; acc = 1
        for node in reversed(path):
            acc *= self.w[node]; self.w[node] = acc; self.p[node] = root
        return root, (self.w[a] if a != root else 1)
    def union(self, a, b, sigma):
        ra, sa = self.find(a); rb, sb = self.find(b)
        if ra == rb:
            if sa != sigma * sb: self.bad.add(ra)
            return
        self.p[ra] = rb; self.w[ra] = sa * sigma * sb
        if ra in self.bad: self.bad.add(rb)
    def count(self, nodes):
        roots = set(self.find(n)[0] for n in nodes)
        return sum(1 for r in roots if self.find(r)[0] not in self.bad and r not in self.bad), len(roots)

def census_class(d, kappa, part, use_twist=True):
    """part 'R' or 'I'; kappa=-1 pairing (antisym), +1 hopping (sym; Re only meaningful)."""
    cls = class_of(d)
    nodes = set()
    for i in range(N):
        v = coords(i)
        for dd in cls:
            j = idx(v[0]+dd[0], v[1]+dd[1], v[2]+dd[2])
            if i < j: nodes.add((i, j))
    uf = UF()
    for n in nodes: uf.find(n)
    def apply(perm, s, twist):
        for (i, j) in nodes:
            pi, pj = int(perm[i]), int(perm[j])
            sg = int(s[i] * s[j])
            if twist:
                f = int(eps[i] * eps[j]) * sg
                sg = -f if part == 'R' else f
            if pi < pj: uf.union((pi, pj), (i, j), sg)
            else: uf.union((pj, pi), (i, j), sg * kappa)
    for name, (perm, s) in plain.items(): apply(perm, s, False)
    if use_twist:
        for name, (perm, s) in twisted.items(): apply(perm, s, True)
    return uf.count(nodes)[0]

if __name__ == "__main__":
    ds = [(1,0,0),(1,1,0),(1,1,1),(2,0,0),(2,1,0),(2,1,1),(2,2,0),(2,2,1),(3,0,0),(3,1,0),(3,1,1),(2,2,2),(3,2,0),(3,2,-1)]
    print("\nclass       |d|^2  | reduced group (attack) pairing | twisted G' pairing Re / Im | twisted G' hopping Re (control)")
    tot_short = 0
    for d in ds:
        n2 = sum(x*x for x in d)
        att = census_class(d, -1, 'R', use_twist=False)
        pr = census_class(d, -1, 'R'); pi_ = census_class(d, -1, 'I')
        hr = census_class(d, +1, 'R')
        if n2 < 14: tot_short += pr + pi_
        print(f"{str(d):11s} {n2:4d}   |  {att}                              |  {pr} / {pi_}                     |  {hr}")
    print("twisted-group pairing invariants (Re+Im) summed over |d|^2<14:", tot_short)
