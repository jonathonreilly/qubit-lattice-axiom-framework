#!/usr/bin/env python3
"""Exact independent empty-start Taylor checks. No primary-source imports."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json


def prod(xs):
    value = F(1)
    for x in xs:
        value *= x
    return value


def axes_W(j):
    return [[1+j if a == b else 1-j if (a ^ 1) == b else F(1)
             for b in range(6)] for a in range(6)]


def graph_data(n, edges, W):
    adj = [[] for _ in range(n)]
    for x, y, proposal in edges:
        assert proposal > 0
        adj[x].append(y)
        adj[y].append(x)
    assert all(sum(row) == 6 for row in W)
    assert all(W[a][b] == W[b][a] > 0 for a in range(6) for b in range(6))

    def weight(s):
        return prod(W[s[x]][s[y]] for x,y,_ in edges if s[x] >= 0 and s[y] >= 0)

    def hazard(s):
        return sum(prod(W[a][s[y]] for y in adj[x] if s[y] >= 0)
                   for x in range(n) if s[x] < 0 for a in range(6))
    return adj, weight, hazard


def calculate(name, n, edges, W, order=6):
    adj, weight, hazard = graph_data(n, edges, W)
    states = list(product(range(-1,6), repeat=n))
    idx = {s:i for i,s in enumerate(states)}
    counts = [sum(a >= 0 for a in s) for s in states]
    weights = [weight(s) for s in states]
    hazards = [hazard(s) for s in states]
    H, B = [], []
    for i,s in enumerate(states):
        hr, br = {}, {}
        for x,y,proposal in edges:
            if (s[x] < 0) != (s[y] < 0):
                t = list(s)
                t[x],t[y] = t[y],t[x]
                j = idx[tuple(t)]
                rate = proposal * weights[j] / (weights[i]+weights[j])
                hr[j] = hr.get(j,F(0))+rate
        for x in range(n):
            if s[x] < 0:
                for a in range(6):
                    t = list(s)
                    t[x] = a
                    j = idx[tuple(t)]
                    rate = prod(W[a][s[y]] for y in adj[x] if s[y] >= 0)
                    assert weights[i]*rate == weights[j]
                    br[j] = br.get(j,F(0))+rate
        hr[i] = -sum(hr.values())
        br[i] = -sum(br.values())
        assert -br[i] == hazards[i]
        assert sum(hr.values()) == sum(br.values()) == 0
        H.append(hr)
        B.append(br)
    for i,hr in enumerate(H):
        for j,rate in hr.items():
            if i != j:
                assert weights[i]*rate == weights[j]*H[j][i]
                assert counts[i] == counts[j]

    Hb = [sum(rate*hazards[j] for j,rate in row.items()) for row in H]
    minimal_level = min((counts[i] for i in range(len(states)) if Hb[i] != 0), default=None)
    assert all(Hb[i] == 0 for i in range(len(states)) if counts[i] < 2)
    D2 = -sum(weights[i]*hazards[i]*Hb[i] for i in range(len(states)) if counts[i] == 2)
    energy2 = sum(weights[i]*rate*(hazards[j]-hazards[i])**2
                  for i,row in enumerate(H) if counts[i] == 2
                  for j,rate in row.items() if j != i) / 2
    assert D2 == energy2 >= 0

    def apply(row, matrix):
        out = {}
        for i,value in row.items():
            for j,rate in matrix[i].items():
                out[j] = out.get(j,F(0)) + value*rate
        return {i:v for i,v in out.items() if v}

    def add(to, row):
        for i,value in row.items():
            to[i] = to.get(i,F(0))+value

    # coeffs[k][h] is the row coefficient of kappa^h epsilon^(k-h)
    # in delta_empty (kappa H+epsilon B)^k, BEFORE division by k!.
    coeffs = [{0:{idx[tuple([-1]*n)]:F(1)}}]
    for k in range(1,order+1):
        new = {}
        for h,row in coeffs[-1].items():
            add(new.setdefault(h,{}), apply(row,B))
            add(new.setdefault(h+1,{}), apply(row,H))
        new = {h:{i:v for i,v in row.items() if v} for h,row in new.items()}
        new = {h:row for h,row in new.items() if row}
        assert all(sum(row.values()) == 0 for row in new.values())
        coeffs.append(new)
    first_distribution = next((k for k in range(1,order+1)
                               if any(h>0 for h in coeffs[k])), None)
    moments = [{h:sum(value*counts[i] for i,value in row.items())
                for h,row in level.items()} for level in coeffs]
    moments = [{h:v for h,v in level.items() if v} for level in moments]
    first_population = next((k for k in range(1,order+1)
                            if any(h>0 for h in moments[k])), None)
    if minimal_level is None:
        assert first_distribution is None and first_population is None
    else:
        assert first_distribution == minimal_level+2
        assert first_population == minimal_level+3
        dm = -sum(weights[i]*hazards[i]*Hb[i] for i in range(len(states))
                  if counts[i] == minimal_level)
        assert moments[minimal_level+3][1] == factorial(minimal_level)*dm > 0
    for i in range(len(states)):
        expected = -2*weights[i]*Hb[i] if counts[i] == 2 else 0
        assert coeffs[4].get(1,{}).get(i,F(0)) == expected
    assert moments[5].get(1,F(0)) == 2*D2
    assert all(not any(h > 0 for h in moments[k]) for k in range(5))

    # Independently check the explicit pure-birth row coefficients through k=3.
    b0, b1 = 6*n, 6*(n-1)
    for i,s in enumerate(states):
        N, w, b = counts[i], weights[i], hazards[i]
        f1 = -b0 if N == 0 else 1 if N == 1 else 0
        f2 = b0*b0 if N == 0 else -(b0+b1) if N == 1 else 2 if N == 2 else 0
        f3 = (-b0**3 if N == 0 else b0*b0+b0*b1+b1*b1 if N == 1
              else -2*(b0+b1+b) if N == 2 else 6 if N == 3 else 0)
        for k,f in [(1,f1),(2,f2),(3,f3)]:
            assert coeffs[k][0].get(i,F(0)) == w*f
    triangles = sum(all(y in adj[x] for x,y in combinations(triple,2))
                    for triple in combinations(range(n),3))
    trace3 = sum(W[a][b]*W[b][c]*W[c][a] for a,b,c in product(range(6),repeat=3))
    assert moments[1][0] == 6*n
    assert moments[2][0] == -36*n
    assert moments[3][0] == 216*n+6*triangles*(trace3-216)

    result = {'name':name,'states':len(states),'order':order,
              'first_hazard_noninvariant_level':minimal_level,
              'first_motion_distribution_order':first_distribution,
              'first_motion_population_order':first_population,
              'two_record_unnormalized_Dirichlet_energy':str(D2),
              'population_Taylor_coefficients':[
                  {str(h):str(value/F(factorial(k))) for h,value in level.items()}
                  for k,level in enumerate(moments)],
              'coefficient_convention':'entry k,h multiplies t^k kappa^h epsilon^(k-h)',
              'triangles':triangles,'trace_W_cubed':str(trace3)}
    if name == 'path3_axes_j_half':
        assert D2 == F(14,5)
        assert moments[5][1]/factorial(5) == F(7,150)
        adjacent = idx[(0,0,-1)]
        separated = idx[(0,-1,0)]
        assert coeffs[4][1][adjacent]/factorial(4) == F(-1,40)
        assert coeffs[4][1][separated]/factorial(4) == F(1,20)
        result['individual_state_t4_kappa_epsilon3'] = {
            '(0,0,vacant)':'-1/40','(0,vacant,0)':'1/20'}
    return result


def delayed_example():
    # 4x4 rook graph: each distinct pair has exactly two common neighbors.
    vertices = list(product(range(4),repeat=2))
    index = {v:i for i,v in enumerate(vertices)}
    edges = [(i,j,F(1)) for i,j in combinations(range(16),2)
             if vertices[i][0] == vertices[j][0] or vertices[i][1] == vertices[j][1]]
    W = axes_W(F(1,2))
    adj, weight, hazard = graph_data(16,edges,W)
    assert {len(a) for a in adj} == {6}
    assert {len(set(adj[x]) & set(adj[y])) for x,y in combinations(range(16),2)} == {2}
    # This makes the two-record hazard spatially constant for every content pair.
    for b,c in product(range(6),repeat=2):
        target = 6*14+2*(sum(W[a][b]*W[a][c] for a in range(6))-6)
        for x,y in combinations(range(16),2):
            s = [-1]*16
            s[x],s[y] = b,c
            assert hazard(s) == target
    old = [-1]*16
    for site in [(0,0),(0,1),(0,2)]:
        old[index[site]] = 0
    new = old.copy()
    new[index[(0,2)]] = -1
    new[index[(1,2)]] = 0
    assert index[(1,2)] in adj[index[(0,2)]]
    assert hazard(old) == F(159,2) and hazard(new) == 81
    assert weight(old) == F(27,8) and weight(new) == F(3,2)
    rate = weight(new)/(weight(old)+weight(new))
    conductance = weight(old)*rate
    edge_energy = conductance*(hazard(new)-hazard(old))**2
    assert rate == F(4,13) and edge_energy == F(243,104)
    return {'graph':'4x4 rook graph','vertices':16,'degree':6,
            'pair_common_neighbor_count':2,'pair_hazard_checks':36*120,
            'three_record_hazards':[str(hazard(old)),str(hazard(new))],
            'hop_rate':str(rate),'one_edge_Dirichlet_contribution':str(edge_energy),
            'first_noninvariant_hazard_level':3,
            'distribution_order_from_proved_formula':5,
            'population_order_from_proved_formula':6}


def main():
    jhalf = axes_W(F(1,2))
    uniform = [[F(1)]*6 for _ in range(6)]
    chi = [2,-1,-1,0,0,0]
    psi = [0,0,0,1,-1,0]
    general = [[1+F(1,4)*chi[a]*chi[b]+F(1,10)*psi[a]*psi[b]
                for b in range(6)] for a in range(6)]
    results = [
        calculate('path3_axes_j_half',3,[(0,1,F(1)),(1,2,F(1))],jhalf),
        calculate('triangle3_axes_j_half',3,[(0,1,F(1)),(1,2,F(2)),(0,2,F(3))],jhalf),
        calculate('path3_uniform',3,[(0,1,F(1)),(1,2,F(2))],uniform),
        calculate('path4_general_unequal_proposals',4,[(0,1,F(1)),(1,2,F(2)),(2,3,F(3))],general),
    ]
    output={'status':'all exact checks passed','finite_state_cases':results,
            'delayed_order_symbolic_construction':delayed_example(),
            'primary_calculations_read':False}
    text=json.dumps(output,indent=2)+'\n'
    (Path(__file__).parent/'RESULTS.json').write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()
