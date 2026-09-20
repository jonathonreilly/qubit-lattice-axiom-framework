"""The minimal marked tree of the counted family for a configuration: an integer program.
Family: subtrees T of G through 1-sites containing x, at most one downward arrow per node, every non-seed node with exactly one
downward arrow to a 1-predecessor (an amplified node to its single one), forks between siblings, F = |S| - 1 (automatic).
Cost(T; c) = E - 3(|S| - 1) - c|A|.  c*(config, x) = min_T (E - 3(|S|-1))/|A| over trees with |A| >= 1 (Dinkelbach)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fractions import Fraction as Fr
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
def level(z): return z[0] + z[1] + z[2]
def preds(z): return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]

def run_automaton(sites, zeta):
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if (sum(ps) >= 2 or zeta.get(z, 0)) else 0
    return eta

class MinTree:
    def __init__(self, eta, root):
        self.eta = eta; self.root = root
        ones = [z for z, v in eta.items() if v == 1]
        # restrict to 1-sites at levels <= level(root) (a tree containing x only uses ... no: forks/up-arrows may go above x). keep all.
        self.V = ones; self.idx = {z: i for i, z in enumerate(ones)}
        self.npred = {z: [p for p in preds(z) if eta.get(p, 0) == 1] for z in ones}
        self.kind = {z: ("seed" if len(self.npred[z]) == 0 else "amp" if len(self.npred[z]) == 1 else "proc") for z in ones}
        self.arrows = [(z, u) for z in ones for u in self.npred[z]]           # z -> u (u a 1-predecessor)
        seen = set(); self.forks = []
        for u in ones:
            for off in FORK_OFFSETS:
                v = (u[0] + off[0], u[1] + off[1], u[2] + off[2])
                if v in self.idx and frozenset((u, v)) not in seen:
                    seen.add(frozenset((u, v))); self.forks.append((u, v))
        self.edges = self.arrows + self.forks
        self.nV, self.nA, self.nF = len(ones), len(self.arrows), len(self.forks)
        self.nE = self.nA + self.nF
        # variable layout: n (nV) | a (nA) | f (nF) | g+ (nE) | g- (nE)
        self.off_a = self.nV; self.off_f = self.nV + self.nA; self.off_gp = self.off_f + self.nF; self.off_gm = self.off_gp + self.nE
        self.nvar = self.off_gm + self.nE
        self._build_constraints()

    def _build_constraints(self):
        rows = []; lo = []; hi = []
        N = self.nV
        def add(coefs, l, h):
            rows.append(coefs); lo.append(l); hi.append(h)
        # exactly one downward arrow for non-seed nodes in the tree: sum_u a_zu - n_z = 0
        arr_of = {z: [] for z in self.V}
        for k, (z, u) in enumerate(self.arrows): arr_of[z].append(k)
        for z in self.V:
            if self.kind[z] == "seed": continue
            co = {self.off_a + k: 1 for k in arr_of[z]}; co[self.idx[z]] = -1
            add(co, 0, 0)
        # a_zu <= n_u ; f_uv <= n_u, n_v
        for k, (z, u) in enumerate(self.arrows):
            add({self.off_a + k: 1, self.idx[u]: -1}, -np.inf, 0)
        for k, (u, v) in enumerate(self.forks):
            add({self.off_f + k: 1, self.idx[u]: -1}, -np.inf, 0)
            add({self.off_f + k: 1, self.idx[v]: -1}, -np.inf, 0)
        # edges = nodes - 1
        co = {self.off_a + k: 1 for k in range(self.nA)}
        co.update({self.off_f + k: 1 for k in range(self.nF)})
        for i in range(N): co[i] = co.get(i, 0) - 1
        add(co, -1, -1)
        # flow capacities: g+_e <= (N-1) e ; g-_e <= (N-1) e
        for k in range(self.nE):
            evar = (self.off_a + k) if k < self.nA else (self.off_f + (k - self.nA))
            add({self.off_gp + k: 1, evar: -(N - 1)}, -np.inf, 0)
            add({self.off_gm + k: 1, evar: -(N - 1)}, -np.inf, 0)
        # conservation: for z != root: inflow - outflow - n_z = 0 ; root: outflow - inflow - sum_{z != root} n_z = 0
        # edge k joins (p, q) = edges[k]; g+ flows p -> q, g- flows q -> p
        inc = {z: [] for z in self.V}
        for k, (p, q) in enumerate(self.edges):
            inc[p].append((k, +1)); inc[q].append((k, -1))   # +1: p is the tail of g+
        for z in self.V:
            co = {}
            for k, sgn in inc[z]:
                if sgn == +1:   # z = p: g+ leaves z, g- enters z
                    co[self.off_gp + k] = co.get(self.off_gp + k, 0) - 1; co[self.off_gm + k] = co.get(self.off_gm + k, 0) + 1
                else:           # z = q: g+ enters z, g- leaves z
                    co[self.off_gp + k] = co.get(self.off_gp + k, 0) + 1; co[self.off_gm + k] = co.get(self.off_gm + k, 0) - 1
            if z == self.root:
                for w in self.V:
                    if w != z: co[self.idx[w]] = co.get(self.idx[w], 0) + 1     # inflow - outflow + sum n_w = 0  -> outflow - inflow = sum n_w
                add(co, 0, 0)
            else:
                co[self.idx[z]] = co.get(self.idx[z], 0) - 1
                add(co, 0, 0)
        A = lil_matrix((len(rows), self.nvar))
        for r, co in enumerate(rows):
            for j, v in co.items(): A[r, j] = v
        self.A = csr_matrix(A); self.lo = np.array(lo, dtype=float); self.hi = np.array(hi, dtype=float)
        lb = np.zeros(self.nvar); ub = np.ones(self.nvar)
        ub[self.off_gp:] = N - 1
        lb[self.idx[self.root]] = 1
        self.bounds = Bounds(lb, ub)
        self.integrality = np.zeros(self.nvar); self.integrality[:self.off_gp] = 1

    def solve(self, c, forbid_no_amp=False):
        cost = np.zeros(self.nvar)
        for z in self.V:
            i = self.idx[z]
            cost[i] = {"proc": 1.0, "amp": -float(c), "seed": -3.0}[self.kind[z]]
        cons = [LinearConstraint(self.A, self.lo, self.hi)]
        if forbid_no_amp:
            co = np.zeros(self.nvar)
            for z in self.V:
                if self.kind[z] == "amp": co[self.idx[z]] = 1
            cons.append(LinearConstraint(csr_matrix(co.reshape(1, -1)), 1, np.inf))
        res = milp(cost, constraints=cons, integrality=self.integrality, bounds=self.bounds, options={"disp": False, "time_limit": 60})
        if res.status != 0:
            return None
        xv = res.x
        nodes = [z for z in self.V if xv[self.idx[z]] > 0.5]
        arrows = [(z, u) for k, (z, u) in enumerate(self.arrows) if xv[self.off_a + k] > 0.5]
        forks = [(u, v) for k, (u, v) in enumerate(self.forks) if xv[self.off_f + k] > 0.5]
        E = sum(1 for (z, u) in arrows if self.kind[z] == "proc"); A = sum(1 for (z, u) in arrows if self.kind[z] == "amp")
        S = sum(1 for z in nodes if self.kind[z] == "seed"); F = len(forks)
        ok = self.verify(nodes, arrows, forks)
        return dict(nodes=nodes, arrows=arrows, forks=forks, E=E, A=A, S=S, F=F, cost=E - 3 * (S - 1) - c * A, ok=ok)

    def verify(self, nodes, arrows, forks):
        ns = set(nodes)
        if self.root not in ns: return False
        adj = {z: set() for z in ns}
        for (p, q) in arrows + forks:
            if p not in ns or q not in ns: return False
            adj[p].add(q); adj[q].add(p)
        if len(arrows) + len(forks) != len(ns) - 1: return False
        seen = {self.root}; st = [self.root]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w not in seen: seen.add(w); st.append(w)
        if seen != ns: return False
        down = {z: 0 for z in ns}
        for (z, u) in arrows:
            if u not in self.npred[z]: return False
            down[z] += 1
        for z in ns:
            k = self.kind[z]
            if k == "seed" and down[z] != 0: return False
            if k != "seed" and down[z] != 1: return False
        for (u, v) in forks:
            if tuple(v[i] - u[i] for i in range(3)) not in FORK_OFFSETS: return False
        S = sum(1 for z in ns if self.kind[z] == "seed")
        return len(forks) == S - 1

    def cstar(self, tol=1e-9):
        """min over trees with |A| >= 1 of (E - 3(S-1))/|A| by Dinkelbach; also the best tree without amplification."""
        r0 = self.solve(0.0)            # ignores amplification benefit; if a tree with A = 0 has E - 3(S-1) <= 0 the config needs no amplification
        c = 10.0; best = None
        for it in range(12):
            r = self.solve(c, forbid_no_amp=True)
            if r is None: return None, None, r0
            val = Fr(r["E"] - 3 * (r["S"] - 1), r["A"])
            if best is None or val < best[0]: best = (val, r)
            if abs(r["cost"]) < tol or float(val) >= c - tol:
                break
            c = float(val)
        return best[0], best[1], r0
