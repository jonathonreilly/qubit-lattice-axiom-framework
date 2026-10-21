"""General (quantum) G-covariant pair walks W at range r on Z^3: parametrisation by amplitudes on
orbit representatives, and the exact constraint system:
  (U)  unitarity of W on near pairs (W = 1 on far pairs, phase convention),
  (S)  3-magnon spectator isometry for U:     <W p1 (x) w1 | W p2 (x) w2> = 0,
  (Sd) the same for U^dagger with W^dagger.
All constraint *structures* are enumerated exactly; values are evaluated numerically."""
import itertools
import numpy as np
from c4d_common import cheb, add, sub, rot, ball, canon_rho, near_rhos, pair, box, dist_set
from c4d_monomial import orbit_reps, stabiliser, act


class PairWalkSpace:
    def __init__(self, G, r):
        self.G, self.r = G, r
        self.reps = [rho for rho, _ in orbit_reps(G, r)]
        self.rep_of = {}
        for rho0 in self.reps:
            for R in G:
                c = canon_rho(rot(R, rho0))
                if c not in self.rep_of:
                    self.rep_of[c] = (rho0, R)
        # unknowns: per rep, stabiliser orbits of near pairs sigma in box(rep)
        self.var = {}      # (rho0, sigma) -> index
        self.nvar = 0
        self.var_info = []
        for rho0 in self.reps:
            p = pair((0, 0, 0), rho0)
            st = stabiliser(G, rho0)
            B = box(p, r)
            for a, b in itertools.combinations(B, 2):
                s = pair(a, b)
                if cheb(a, b) > r or (rho0, s) in self.var:
                    continue
                orb = {act(g, s) for g in st}
                for s2 in orb:
                    self.var[(rho0, s2)] = self.nvar
                self.var_info.append((rho0, s, len(orb)))
                self.nvar += 1
        self.cache = {}

    def frame(self, p):
        """(rho0, R, t) with (R,t){0,rho0} = p."""
        x, y = sorted(p)
        rho = sub(y, x)
        rho0, R = self.rep_of[canon_rho(rho)]
        v = rot(R, rho0)
        t = x if v == rho else y
        return rho0, R, t

    def index(self, sigma, p):
        """unknown index for W[sigma, p] (p near), or None if structurally zero."""
        key = (sigma, p)
        if key in self.cache:
            return self.cache[key]
        rho0, R, t = self.frame(p)
        Rinv = R.T
        s0 = frozenset(rot(Rinv, sub(s, t)) for s in sigma)
        out = self.var.get((rho0, s0))
        self.cache[key] = out
        return out

    def column(self, p):
        """list of (sigma, idx) for W|p> (p near)."""
        rho0, R, t = self.frame(p)
        out = []
        for (r0, s0), idx in self.var.items():
            if r0 == rho0:
                out.append((act((R, t), s0), idx))
        return out


def build_constraints(S):
    """Returns lists of bilinear constraints. Each constraint: (const, [(i, j, conj_flag_pattern)])
    meaning sum over terms conj(x_i) * x_j (+ const) = 0, where x = amplitudes, for kind 'W' and
    for kind 'Wd' (adjoint: W^dag[sigma,p] = conj(W[p,sigma]))."""
    r = S.r
    unit = []   # (pi1-type, pi2): sum_sigma conj(W[s,p1]) W[s,p2] - delta
    unit_keys = []
    for rho in near_rhos(r):
        p1 = pair((0, 0, 0), rho)
        col1 = dict((s, i) for s, i in S.column(p1))
        # candidate p2: near pairs whose box can meet box(p1)
        seen = set()
        for x in ball(2 * r, (0, 0, 0)):
            for rho2 in near_rhos(r):
                p2 = pair(x, add(x, rho2))
                if p2 in seen:
                    continue
                seen.add(p2)
                col2 = dict((s, i) for s, i in S.column(p2))
                terms = [(col1[s], col2[s]) for s in col1 if s in col2]
                if terms or p2 == p1:
                    unit.append((-1.0 if p2 == p1 else 0.0, terms))
                    unit_keys.append((p1, p2))
    spec = {"W": {}, "Wd": {}}
    for rho in near_rhos(r):
        p1 = pair((0, 0, 0), rho)
        B1 = box(p1, r)
        for w2 in B1:
            if w2 in p1:
                pass
            for u in B1:
                if u == w2 or cheb(u, w2) > r:
                    continue
                sig1 = pair(w2, u)
                # p2: near pairs with u in box(p2)
                for x in ball(r, u):
                    for rho2 in near_rhos(r):
                        for p2 in (pair(x, add(x, rho2)),):
                            if cheb(u, x) > r or cheb(u, add(x, rho2)) > r:
                                continue
                            if dist_set(w2, p2) <= r:
                                continue
                            B2 = box(p2, r)
                            for w1 in B2:
                                if w1 == w2 or w1 == u or cheb(w1, u) > r:
                                    continue
                                if dist_set(w1, p1) <= r:
                                    continue
                                key = (p1, w1, p2, w2)
                                for kind in ("W", "Wd"):
                                    spec[kind].setdefault(key, set()).add(u)
    out = {}
    keys = {"W": [], "Wd": []}
    for kind in ("W", "Wd"):
        lst = []
        for (p1, w1, p2, w2), us in spec[kind].items():
            terms = []
            for u in us:
                s1, s2 = pair(w2, u), pair(w1, u)
                if kind == "W":
                    i, j = S.index(s1, p1), S.index(s2, p2)
                    if i is not None and j is not None:
                        terms.append(("W", i, j))
                else:
                    # W^dag[s1,p1] = conj(W[p1,s1]) ; W^dag[s2,p2] = conj(W[p2,s2])
                    # need p1 in box(s1) etc: index(p1, s1) requires s1 near: yes
                    i, j = S.index(p1, s1), S.index(p2, s2)
                    if i is not None and j is not None:
                        terms.append(("Wd", i, j))
            if terms:
                lst.append(terms)
                keys[kind].append((p1, w1, p2, w2))
        out[kind] = lst
    build_constraints.keys = {"U": unit_keys, "W": keys["W"], "Wd": keys["Wd"]}
    return unit, out


def residuals(x, S, unit, spec):
    res = []
    for c, terms in unit:
        v = c + sum(np.conj(x[i]) * x[j] for i, j in terms)
        res.append(v)
    for terms in spec["W"]:
        res.append(sum(np.conj(x[i]) * x[j] for _, i, j in terms))
    for terms in spec["Wd"]:
        # conj(Wd[s1,p1]) * Wd[s2,p2] = W[p1,s1] * conj(W[p2,s2])
        res.append(sum(x[i] * np.conj(x[j]) for _, i, j in terms))
    return np.array(res)
