"""Exact PXP finite partition trace bounds: integer walks plus rational tails.

No external scientific input is read and no receipt is written.
Only Python integer and Fraction arithmetic is load-bearing. No eigenvalues,
floating-point matrix operation, or fitted number enters the certificate.
The rotation reduction is checked as an exact graph automorphism. Independent
direct closed-walk counts check trace A^2,A^4,A^6 without orbit reduction.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import factorial
import hashlib
import json

AUDIT_TIMEOUT_SEC = 120
ORDER = 256


def decimal(x):
    with localcontext() as ctx:
        ctx.prec = 36
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def graph(length):
    mask = (1 << length) - 1
    rotate = lambda x: ((x << 1) & mask) | (x >> (length - 1))
    states = [x for x in range(1 << length) if not x & rotate(x)]
    where = {s: i for i, s in enumerate(states)}
    neighbors = []
    for x in states:
        row = []
        for i in range(length):
            if not x & ((1 << ((i-1) % length)) | (1 << ((i+1) % length))):
                row.append(where[x ^ (1 << i)])
        neighbors.append(sorted(row))
    assert all(i in neighbors[j] for i, row in enumerate(neighbors) for j in row)
    assert all((states[i].bit_count() - states[j].bit_count()) % 2 == 1
               for i, row in enumerate(neighbors) for j in row)
    permutation = [where[rotate(x)] for x in states]
    assert sorted(permutation) == list(range(len(states)))
    assert all(sorted(permutation[j] for j in neighbors[i]) == neighbors[permutation[i]]
               for i in range(len(states)))
    visited = set()
    orbits = []
    for i in range(len(states)):
        if i in visited:
            continue
        orbit, j = [], i
        while j not in visited:
            orbit.append(j)
            visited.add(j)
            j = permutation[j]
        assert j == i
        orbits.append(orbit)
    assert len(visited) == len(states)
    return states, neighbors, orbits


def moments(length):
    states, neighbors, orbits = graph(length)
    d = len(states)
    traces = [0] * (ORDER + 1)
    for oi, orbit in enumerate(orbits):
        root, weight = orbit[0], len(orbit)
        v = [0] * d
        v[root] = 1
        for k in range(ORDER + 1):
            traces[k] += weight * v[root]
            if k != ORDER:
                v = [sum(v[j] for j in row) for row in neighbors]
    assert traces[0] == d
    assert all(x >= 0 for x in traces)
    assert all(traces[k] == 0 for k in range(1, ORDER+1, 2))
    # Independently count entries of A^p by explicit p-step path enumeration.
    direct = {}
    for half in [1, 2, 3]:
        total = 0
        for source in range(d):
            counts = {source: 1}
            for _ in range(half):
                nxt = {}
                for i, multiplicity in counts.items():
                    for j in neighbors[i]:
                        nxt[j] = nxt.get(j, 0) + multiplicity
                counts = nxt
            total += sum(x*x for x in counts.values())
        direct[2*half] = total
        assert traces[2*half] == total
    assert max(map(len, neighbors)) == length
    payload = {"length": length, "dimension": d, "max_degree": length,
               "rotation_orbits": [len(o) for o in orbits],
               "graph_sha256": hashlib.sha256(json.dumps([states, neighbors]).encode()).hexdigest(),
               "traces": [str(x) for x in traces],
               "independent_even_moment_checks": direct}
    return payload


def enclose(payload, beta):
    traces = list(map(int, payload["traces"]))
    n = len(traces)-1
    numerator = traces[0]
    for k in range(1, n+1):
        numerator = k*numerator + traces[k]*beta**k
    lo = F(numerator, factorial(n))
    x = beta * payload["max_degree"]
    ratio = F(x, n+2)
    assert 0 <= ratio < 1
    tail = F(payload["dimension"]*x**(n+1), factorial(n+1))/(1-ratio)
    hi = lo + tail
    return lo, hi, {"length": payload["length"], "beta": beta, "order": n,
                   "lower_exact": str(lo), "upper_exact": str(hi),
                   "tail_exact": str(tail), "lower_decimal": decimal(lo),
                   "upper_decimal": decimal(hi), "relative_tail_upper": decimal(tail/lo)}


def main():
    p6, p12 = moments(6), moments(12)
    bounds = [enclose(p6, 4), enclose(p12, 4), enclose(p12, 8)]
    report = {"method": __doc__, "order": ORDER,
              "bounds": [row[2] for row in bounds], "seed_families": {}}
    (z64lo,z64hi,_),(z124lo,z124hi,_),(z128lo,z128hi,_) = bounds
    for name, extra in [("dynamic_pxp",0),("full_link_ring_after_all_length_dictionary",2)]:
        slo = (z124lo+extra)/(z64hi+extra)**2
        shi = (z124hi+extra)/(z64lo+extra)**2
        tlo = (z128lo+extra)/(z124hi+extra)**2
        thi = (z128hi+extra)/(z124lo+extra)**2
        assert slo > F(23,25)
        assert tlo > F(23,25)
        report["seed_families"][name] = {
            "n0":6,"beta0":4,"target_purity":str(F(23,25)),
            "S_lower_exact":str(slo),"S_upper_exact":str(shi),
            "T_lower_exact":str(tlo),"T_upper_exact":str(thi),
            "S_lower_decimal":decimal(slo),"S_upper_decimal":decimal(shi),
            "T_lower_decimal":decimal(tlo),"T_upper_decimal":decimal(thi),
            "S_exact_comparison_passes":slo>F(23,25),
            "T_exact_comparison_passes":tlo>F(23,25)}
    u,c=F(2,25),F(7)
    g=sum((1-u)**(-j) for j in [1,2,3])**2/2
    assert 0<u<F(1,6) and g<=c and c*u<1 and c*(1-3*u)>3
    report["bootstrap_scalars"]={"u0":str(u),"C":str(c),"G(u0)":str(g),
                                 "r":str(c*u),"C(1-3u0)":str(c*(1-3*u)),
                                 "gap_bound_expression":"log(25/14)/4",
                                 "all_exact_scalar_checks_pass":True}
    report["integer_moments"]={"6":p6,"12":p12}
    report["exact_Gauss_plaquette_controls"]=dictionary()
    print(json.dumps(report,indent=2),flush=True)
    print("PASS exact finite seeds: both dynamic and full-sector purities exceed 23/25")
    print("PASS scalar bootstrap hypotheses: exact rational comparisons")
    print("PASS finite dictionary controls: Gauss constraints and unit plaquette entries")
    print("per_element: exact integer adjacency, return counts and rational tail bounds are exercised.")
    print("per_site: local plaquette raising/lowering agrees with each permitted spin flip in tested rings.")
    print("per_mode: no individual infinite-volume mode is numerically computed; spectral argument is in the proof.")
    print("per_block: dynamic and both frozen Gauss sectors enter the exact finite seed certificate.")
    print("lattice_wide: all-even-length bound follows from the written kernel and bootstrap proof, not a size fit.")
    print("TOTAL: PASS=3 FAIL=0")



def legal_states(n):
    return [x for x in range(1<<n)
            if all(not ((x>>i)&1 and (x>>((i+1)%n))&1) for i in range(n))]


def encode(n,z):
    bits=[(z>>i)&1 for i in range(n)]
    top=[(-1)**i*(1-2*bits[i]) for i in range(n)]
    bottom=[-x for x in top]
    rung=[(-1)**i*(1-2*(bits[i-1]+bits[i])) for i in range(n)]
    assert all(abs(x)==1 for x in top+bottom+rung)
    return tuple(top+bottom+rung)


def gauss(n,state):
    t,b,r=state[:n],state[n:2*n],state[2*n:]
    return all(t[i]-t[i-1]-r[i]==(-1)**i and
               b[i]-b[i-1]+r[i]==-(-1)**i for i in range(n))


def plaquette(n,state,i,dagger):
    # W_i = U_Ti U^dag_R(i+1) U^dag_Bi U_Ri.
    factors=[(i,1),(2*n+(i+1)%n,-1),(n+i,-1),(2*n+i,1)]
    out=list(state)
    for index,raise_sign in factors:
        sign=-raise_sign if dagger else raise_sign
        if out[index]!=-sign:
            return None
        out[index]=sign
    return tuple(out)


def dictionary():
    rows=[]
    for n in [4,6,8,10,12,14,16]:
        legal=legal_states(n)
        images={encode(n,z):z for z in legal}
        assert len(images)==len(legal)
        frozen=[tuple([sign]*n+[sign]*n+[-(-1)**i for i in range(n)]) for sign in [-1,1]]
        assert all(gauss(n,x) for x in list(images)+frozen)
        # Independent all-top/bottom assignment reconstruction from constant F.
        reconstructed=[]
        for flux in [-2,0,2]:
            for topbits in range(1<<n):
                t=[1 if (topbits>>i)&1 else -1 for i in range(n)]
                b=[flux-x for x in t]
                if any(abs(x)!=1 for x in b):
                    continue
                r=[t[i]-t[i-1]-(-1)**i for i in range(n)]
                if any(abs(x)!=1 for x in r):
                    continue
                state=tuple(t+b+r)
                assert gauss(n,state)
                reconstructed.append(state)
        assert set(reconstructed)==set(images)|set(frozen)
        for state,z in images.items():
            for i in range(n):
                targets=[x for dagger in [False,True]
                         if (x:=plaquette(n,state,i,dagger)) is not None]
                allowed=not (z & ((1<<((i-1)%n))|(1<<((i+1)%n))))
                expected=[encode(n,z^(1<<i))] if allowed else []
                assert targets==expected
        assert all(plaquette(n,x,i,d) is None for x in frozen for i in range(n) for d in [False,True])
        rows.append({'L':n,'dynamic_dimension':len(images),'full_dimension':len(reconstructed),
                     'exact_Gauss_and_plaquette_checks':True})
    return rows


if __name__ == '__main__':
    main()
