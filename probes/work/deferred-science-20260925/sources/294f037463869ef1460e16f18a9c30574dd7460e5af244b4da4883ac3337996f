#!/usr/bin/env python3
"""Own exact spin-one path controls; no parent or author code imported."""
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import math
import time


def clean(v):
    return {k: x for k, x in v.items() if x}


def add(*terms):
    out = defaultdict(Q)
    for coefficient, vector in terms:
        for word, value in vector.items():
            out[word] += coefficient * value
    return clean(out)


class Graph:
    def __init__(self, name, na, nb, edges):
        self.name, self.na, self.nb = name, na, nb
        self.edges = tuple(edges)
        self.adj = {a: [(b, i) for i, (aa, b) in enumerate(edges) if aa == a]
                    for a in range(na)}
        self.near = {(a, c) for a in range(na) for c in range(na)
                     if a == c or set(b for b, _ in self.adj[a]) &
                     set(b for b, _ in self.adj[c])}
        self.outputs_checked = 0

    def gauss(self, word):
        q, e = word
        div = [0] * (self.na+self.nb)
        for field, (a, b) in zip(e, self.edges):
            div[a] += field
            div[b] -= field
        assert div == [charge-(i < self.na) for i, charge in enumerate(q)]
        assert all(abs(x) <= 1 for x in e)
        self.outputs_checked += 1

    def W(self, word):
        return sum(x == 0 for x in word[0][:self.na])

    def project(self, vector, grade):
        return {w: x for w, x in vector.items() if self.W(w) == grade}

    def primitive(self, word, a, b, edge, reverse=False, birth=None):
        q, e = word
        newq, newe = list(q), list(e)
        if birth is not None:
            if q[a] or q[b]:
                return {}
            shift = birth
            newq[a], newq[b] = birth, -birth
        elif reverse:
            if q[a] or not q[b]:
                return {}
            shift = q[b]
            newq[a], newq[b] = q[b], 0
        else:
            if not q[a] or q[b]:
                return {}
            shift = -q[a]
            newq[a], newq[b] = 0, q[a]
        # At S=1 every allowed normalized ladder amplitude is exactly one.
        defect = e[edge] * (e[edge]+shift)
        assert defect in (0, 2)
        if defect == 2:
            return {}
        newe[edge] += shift
        out = tuple(newq), tuple(newe)
        self.gauss(out)
        change = sum(map(abs, out[0]))-sum(map(abs, q))
        assert change == (2 if birth is not None else 0)
        return {out: Q(1)}

    def F(self, vector, a, reverse=False):
        return add(*[(x, self.primitive(w, a, b, i, reverse=reverse))
                     for w, x in vector.items() for b, i in self.adj[a]])

    def T(self, vector):
        return add(*[(-1, self.F(vector, a, rev))
                     for a in range(self.na) for rev in (False, True)])

    def delta(self, vector, a):
        out = {}
        for w, x in vector.items():
            q, e = w
            d = sum(e[i]*(e[i]-q[a]) for b, i in self.adj[a] if q[a] and not q[b])
            assert 0 <= d <= 2*len(self.adj[a])
            if d:
                out[w] = x*Q(d, 2)
        return out

    def C(self, vector):
        pieces = []
        for a in range(self.na):
            gated = {w: x for w, x in vector.items()
                     if all(w[0][c] for c in range(self.na)
                            if c != a and (a, c) in self.near)}
            pieces += [(1, self.F(self.F(gated, a), a, True)),
                       (1, self.delta(gated, a))]
        return add(*pieces)

    def A(self, vector):
        return self.project(self.T(self.project(vector, 0)), 1)

    def Astar(self, vector):
        return self.project(self.T(self.project(vector, 1)), 0)

    def M(self, vector):
        return self.Astar(self.A(vector))

    def Ma(self, vector, a):
        return self.project(self.F(self.F(self.project(vector, 0), a), a, True), 0)

    def C0(self, vector):
        return self.project(self.C(self.project(vector, 0)), 0)

    def Z(self, vector):
        return self.project(self.T(self.A(vector)), 2)

    def Zstar(self, vector):
        return self.Astar(self.project(self.T(self.project(vector, 2)), 1))

    def H4_canonical(self, vector):
        return add((1, self.M(self.M(vector))),
                   (Q(-1,2), self.M(self.C0(vector))),
                   (Q(-1,2), self.C0(self.M(vector))),
                   (1, self.Astar(self.project(self.C(self.A(vector)), 1))),
                   (Q(-1,2), self.Zstar(self.Z(vector))))

    def H4_local(self, vector):
        pieces = []
        for a in range(self.na):
            for c in range(a+1, self.na):
                if (a,c) in self.near:
                    s = self.F(self.F(vector,a),c)
                    ss = self.project(self.F(self.F(s,c,True),a,True),0)
                    pieces.append((-2,ss))
        for a,c in sorted(self.near):
            pieces += [(Q(-1,2),self.Ma(self.delta(vector,c),a)),
                       (Q(-1,2),self.delta(self.Ma(vector,a),c))]
        return add(*pieces)

    def births(self, vector):
        outputs = []
        for i,(a,b) in enumerate(self.edges):
            after = self.F(vector,a)
            for sign in (-1,1):
                result = add(*[(x,self.primitive(w,a,b,i,birth=sign))
                               for w,x in after.items()])
                outputs.extend(result)
        return outputs


def main():
    started = time.perf_counter()
    graphs = [
        Graph("square",2,2,[(0,2),(0,3),(1,2),(1,3)]),
        Graph("three_star_tree_with_distant_pair",3,4,
              [(0,3),(0,4),(1,4),(1,5),(2,5),(2,6)]),
        Graph("K3_3",3,3,[(a,b) for a in range(3) for b in range(3,6)])
    ]
    rows, totals = [], []
    for g in graphs:
        initial = tuple([1]*g.na+[0]*g.nb), tuple([0]*len(g.edges))
        words = {initial}
        words.update(g.births({initial:Q(1)}))
        # Actual primitive outputs, including both placements of the new minus.
        for w in sorted(words):
            g.gauss(w)
            v={w:Q(1)}
            delta = add(*[(1,g.delta(v,a)) for a in range(g.na)])
            assert g.C0(v) == add((1,g.M(v)),(1,delta))
            canonical, local = g.H4_canonical(v), g.H4_local(v)
            assert canonical == local
            wrong = add((1,canonical),(-1,add(*[
                (-2,g.project(g.F(g.F(g.F(g.F(v,a),c),c,True),a,True),0))
                for a in range(g.na) for c in range(a+1,g.na)
                if (a,c) in g.near])))
            rows.append({"graph":g.name,"q":w[0],"E":w[1],
                         "number":sum(map(abs,w[0])),
                         "D":str(2*delta.get(w,Q(0))),
                         "H4_output_words":len(canonical),
                         "H4_diagonal":str(canonical.get(w,Q(0))),
                         "canonical_equals_local":True,
                         "dropping_finite_spin_correction_is_wrong":bool(wrong)})
        totals.append({"graph":g.name,"input_columns":len(words),
                       "primitive_Gauss_outputs_checked":g.outputs_checked,
                       "distant_unordered_A_pairs":sum((a,c) not in g.near
                         for a in range(g.na) for c in range(a+1,g.na))})
    scalar_rows=[]
    for S in (1,2,3,4,8,16,32):
        C=S*(S+1);checked=0
        for e,q,sign in product(range(-S,S+1),(-1,1),(-1,1)):
            d=e*(e-q); birth=e*(e+sign)
            assert 0 <= d <= C and 0 <= birth <= C
            assert e*e <= 2*d+1
            assert birth <= 4*d+2
            checked+=1
        scalar_rows.append({"S":S,"C":C,"integer_shift_cases":checked,
                            "gate_weight_and_birth_comparison_exact":True})
    escaping_rows=[]
    for S in (2,4,8,16,32,64,128,256):
        t=S//2;C=S*(S+1)
        # K3,3: B charges (+,-,0); occupied-link cycle is unconfined by D.
        initial_E=(t-1,1-t,0,-t,t,0,0,0,0)
        assert max(map(abs,initial_E)) <= S
        d_after=2*t*t
        coefficient=-Q(t*t,C)*math.sqrt(1-Q(t*(t-1),C))
        assert d_after > 0
        escaping_rows.append({"S":S,"cycle_flux":t,"initial_D":0,
             "new_vacancy_D":d_after,"exact_prefactor":str(-Q(t*t,C)),
             "exact_return_weight_squared":str(1-Q(t*(t-1),C)),
             "finite_spin_H4_offdiagonal":coefficient,
             "rotor_H4_entire_sector":0,
             "nonzero_limit":-math.sqrt(3)/8,
             "interpretation":"No uniform operator-norm replacement on D-bounded inputs; quadratic-form comparison is still possible."})
    assert any(r["dropping_finite_spin_correction_is_wrong"] for r in rows)
    result={"source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope":"Own exact spin-one primitive columns and integer weight comparisons; higher-spin displayed scalar amplitudes are floating evaluations of exact fractions.",
            "local_identity_rows":rows,"graph_totals":totals,
            "scalar_weight_rows":scalar_rows,
            "unconfined_flux_operator_counterexample_rows":escaping_rows,
            "all_assertions_passed":True,
            "elapsed_seconds":time.perf_counter()-started}
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
