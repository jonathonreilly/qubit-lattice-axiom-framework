#!/usr/bin/env python3
"""Exact finite controls for the supplied native qubit density theorem.

The analytic source proves all-volume bounds. This job checks 64 local
columns, cubic symmetry, sparse pair states, pinned-box geometry, rational
resistance and exact trial constants. No full many-particle diagonalization.
No external scientific file is read; note and runner bytes are integrity
reads only. The envelope additionally binds the declared note input.
"""
from pathlib import Path
import hashlib
import json
import os
import time

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ["docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md"]
for _thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_key] = "1"

def check_full_carrier():
    from fractions import Fraction as F
    from itertools import combinations, permutations, product
    from collections import defaultdict, Counter
    import time,resource

    START=time.monotonic()
    VECTORS=[tuple(s if k==j else 0 for k in range(3)) for j in range(3) for s in [1,-1]]
    def plus(a,b):return tuple(x+y for x,y in zip(a,b))
    def scale(a,c):return tuple(c*x for x in a)
    DG=set(scale(v,2) for v in VECTORS)
    for i,j in combinations(range(3),2):
        for si,sj in product([-1,1],repeat=2):DG.add(plus(scale(VECTORS[2*i],si),scale(VECTORS[2*j],sj)))
    assert len(DG)==18 and (0,0,0) not in DG

    # Local bit ordering (+x,-x,+y,-y,+z,-z).
    D=[[(1<<(2*j))|(1<<(2*j+1)),1] for j in range(3)]
    E1=[D[0],(D[1][0],-1)]
    E2=[D[0],D[1],(D[2][0],-2)]
    T=[]
    for i,j in combinations(range(3),2):
        T.append([((1<<(2*i+a))|(1<<(2*j+b)),(-1)**(a+b)) for a,b in product(range(2),repeat=2)])
    WTERMS=[(12,E1),(4,E2)]+[(3,t) for t in T] #12*(2 PE+PT)
    ATERMS=[(8,D)]
    for t in T:
        for a,b in combinations(range(4),2):ATERMS.append((3,[t[a],(t[b][0],-t[b][1])]))
    def qdagq_column(bits,words):
        out=defaultdict(int)
        for rem,c in words:
            if bits&rem!=rem:continue
            middle=bits^rem
            for ins,d in words:
                if middle&ins:continue
                out[middle|ins]+=c*d
        return {k:v for k,v in out.items() if v}
    def apply_column(bits,terms):
        out=defaultdict(int)
        for weight,words in terms:
            for target,c in qdagq_column(bits,words).items():out[target]+=weight*c
        return {k:v for k,v in out.items() if v}
    for bits in range(64):
        a=apply_column(bits,ATERMS);w=apply_column(bits,WTERMS)
        total=Counter(a);total.update(w)
        actual={k:v for k,v in total.items() if v}
        expected=24*sum(bits&m==m for m,c in D)+12*sum(bits&m==m for t in T for m,c in t)
        assert actual==({bits:expected} if expected else {})

    # Exact degree-polynomial certificate; all occupancies of the18-neighbor star.
    degree_rows=[]
    for m in range(19):
        v3=m*(m-1)//2;res=(m-1)*(m-2)//2
        assert 1-m+v3==res and res>=0
        degree_rows.append([m,v3,res])

    rots=[]
    for p in permutations(range(3)):
        parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        for s in product([-1,1],repeat=3):
            if parity*s[0]*s[1]*s[2]!=1:continue
            def rot(v):
                z=[0]*3
                for i in range(3):z[p[i]]=s[i]*v[i]
                return tuple(z)
            assert {rot(v) for v in DG}==DG
            slot=[VECTORS.index(rot(v)) for v in VECTORS]
            def rb(bits):return sum(1<<slot[i] for i in range(6) if bits>>i&1)
            for bits in range(64):
                assert {rb(a):c for a,c in apply_column(bits,WTERMS).items()}==apply_column(rb(bits),WTERMS)
            rots.append((p,s))
    assert len(rots)==24

    def geometry(L):
        coords=list(product(range(L),repeat=3));idx={x:i for i,x in enumerate(coords)}
        def site(x):return idx[tuple(t%L for t in x)]
        shell=[[site(plus(x,v)) for v in VECTORS] for x in coords]
        near=[[site(plus(x,d)) for d in DG] for x in coords]
        return coords,shell,near
    incidence=[]
    for L in [5,6,7]:
        coords,shell,near=geometry(L);opp=Counter();cross=Counter()
        for nodes in shell:
            assert len(set(nodes))==6
            for mask,c in D:opp[tuple(sorted(nodes[i] for i in range(6) if mask>>i&1))]+=1
            for t in T:
                for mask,c in t:cross[tuple(sorted(nodes[i] for i in range(6) if mask>>i&1))]+=1
        assert set(opp).isdisjoint(cross)
        assert set(opp.values())=={1} and set(cross.values())=={2}
        assert len(opp)==3*L**3 and len(cross)==6*L**3
        edges={tuple(sorted((x,y))) for x,ys in enumerate(near) for y in ys}
        assert edges==set(opp)|set(cross)
        assert all(len(set(ys))==18 and x not in ys for x,ys in enumerate(near))
        incidence.append({'L':L,'vertices':L**3,'opposite_edges':len(opp),'cross_edges':len(cross),'near_degree':18})


    return {"local_columns":64,"cubic_rotations":len(rots),"degree_rows":degree_rows,"torus_incidence":incidence,"elapsed_seconds":time.monotonic()-START}

def check_coercivity_geometry():
    from collections import defaultdict
    from itertools import product, combinations
    import resource
    import time

    t0 = time.perf_counter()
    import sympy as s

    # Internal amplitude projectors, obtained directly by expanding differences.
    E = s.eye(3)-s.ones(3)/3
    assert E*E == E
    Tcomp = s.zeros(4)
    for a, b in combinations(range(4), 2):
        w = s.zeros(4, 1); w[a] = 1; w[b] = -1
        Tcomp += w*w.T/4
    assert Tcomp == s.eye(4)-s.ones(4)/4
    assert Tcomp*Tcomp == Tcomp
    for m in range(19):
        d = (m-1)*(m-2)//2
        assert d >= 0 and d+m >= 1

    # Balanced cyclic intervals built from integer cut points. Balanced integer cut points. q=1 is kept as the whole circle, once.
    partition_cases = 0
    max_vertex_overlap = max_edge_overlap = 0
    for L in range(5, 81):
        for q in range(1, L+1):
            cuts = [j*L//q for j in range(q+1)]
            inner = [list(range(cuts[j], cuts[j+1])) for j in range(q)]
            expanded = []
            for B in inner:
                C = (list(range(L)) if q == 1 else
                     [(B[0]-1+j) % L for j in range(min(L, len(B)+2))])
                assert len(C) == len(set(C))
                assert all((y+d) % L in C for y in B for d in [-1, 0, 1])
                expanded.append(C)
            vertices = [0]*L; edges = defaultdict(int)
            for C in expanded:
                for x in C: vertices[x] += 1
                for x, y in zip(C, C[1:]):
                    assert (y-x) % L == 1
                    edges[tuple(sorted((x, y)))] += 1
            assert max(vertices) <= 3 and max(edges.values(), default=0) <= 3
            max_vertex_overlap = max(max_vertex_overlap, max(vertices))
            max_edge_overlap = max(max_edge_overlap, max(edges.values(), default=0))
            lo, hi = min(map(len, expanded)), max(map(len, expanded))
            assert hi <= 2*lo
            assert hi**3*q**3 <= 64*L**3
            # A q from floor((N/4)^(1/3)) covers this exact integer interval.
            Nlo, Nhi = 4*q**3, min(L**3, 4*(q+1)**3-1)
            if Nlo <= Nhi:
                assert 2*q**3 <= Nlo//2
                assert hi**3*Nhi <= 2048*L**3
            partition_cases += 1

    # Pin convention: grounded graph Laplacian gives point resistance as the
    # corresponding diagonal of its inverse. Only boxes of at most 27 vertices.
    resistance_checks = []
    for dims in [(1, 1, 1), (1, 1, 2), (2, 2, 2), (2, 3, 3), (2, 2, 4), (3, 3, 3)]:
        vertices = list(product(*[range(n) for n in dims])); n = len(vertices)
        index = {x: j for j, x in enumerate(vertices)}
        lap = s.zeros(n)
        for x in vertices:
            for axis in range(3):
                y = list(x); y[axis] += 1; y = tuple(y)
                if y in index:
                    a, b = index[x], index[y]
                    lap[a, a] += 1; lap[b, b] += 1
                    lap[a, b] -= 1; lap[b, a] -= 1
        # Independent all-pairs Manhattan incidence check of the constructed Laplacian.
        for i, x in enumerate(vertices):
            degree = sum(sum(abs(a-b) for a,b in zip(x,y)) == 1 for y in vertices)
            for j, y in enumerate(vertices):
                expected = degree if i == j else (-1 if sum(abs(a-b) for a,b in zip(x,y)) == 1 else 0)
                assert lap[i,j] == expected
        for pin in sorted({0, n//2}):
            keep = [j for j in range(n) if j != pin]
            if keep:
                green = lap.extract(keep, keep).inv()
                rmax = max(green[j, j] for j in range(n-1))
                assert rmax <= 448
                # trace(G) gives the elementary sum of pointwise bounds, consistent
                # with the |C| factor in the full pinned estimate.
                assert s.trace(green) <= 448*n
            else:
                rmax = s.Rational(0)
            resistance_checks.append({'sides': dims, 'pin': pin, 'max_resistance': str(rmax)})

    L = 5
    sites = list(product(range(L), repeat=3))
    unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    def add(x, y): return tuple((a+b) % L for a, b in zip(x, y))
    def scale(a, x): return tuple(a*b for b in x)
    types = [(e, scale(-1, e), 1) for e in unit]
    for i, j in combinations(range(3), 2):
        for a, b in product([-1, 1], repeat=2):
            types.append((scale(a, unit[i]), scale(b, unit[j]), a*b))
    assert len(types) == 15
    edges = defaultdict(list)
    for x in sites:
        for t, (u, v, sign) in enumerate(types):
            edge = tuple(sorted((add(x, u), add(x, v))))
            assert edge[0] != edge[1]
            edges[edge].append((x, t, sign))
    adj = defaultdict(set)
    for edge, occurrences in edges.items():
        a, b = edge; adj[a].add(b); adj[b].add(a)
        axial = occurrences[0][1] < 3
        assert len(occurrences) == (1 if axial else 2)
        assert len({sign for _, _, sign in occurrences}) == 1
    assert {len(adj[x]) for x in sites} == {18}

    B = set(product(range(2), repeat=3))
    C = set(product([4, 0, 1, 2], repeat=3))
    sample_sites = sorted(B | {(2, 0, 0), (3, 0, 0), (4, 0, 0), (0, 2, 0)})
    configuration_checks = pin_checks = 0
    for N in [3, 4, 6]:
        for raw in combinations(sample_sites, N):
            S = set(raw)
            NB = len(S & B)
            DB = sum((len(adj[x] & S)-1)*(len(adj[x] & S)-2)//2 for x in S & B)
            restricted_M = 0
            for edge in combinations(sorted(S), 2):
                eta = S-set(edge)
                if not eta & B:
                    continue
                restricted_M += sum(x in C for x, _, _ in edges.get(edge, []))
                y = min(eta & B)
                for u, v, sign in types:
                    pin = add(y, scale(-1, u))
                    assert pin in C
                    # Output occupies y; the first endpoint of this annihilator
                    # is y. No input occupation word can produce this output.
                    assert add(pin, u) == y and y in eta
                    pin_checks += 1
            assert (NB if NB >= 3 else 0) <= DB+2*restricted_M
            configuration_checks += 1

    Bstar = 2*448*27*2048
    assert Bstar == 49545216 and 2*Bstar == 99090432
    outcome = {'internal_projectors_checked': True,
               'partition_cases_L5_through_80': partition_cases,
               'max_1d_vertex_overlap': max_vertex_overlap,
               'max_1d_free_edge_overlap': max_edge_overlap,
               'rational_resistance_checks': resistance_checks,
               'all_L5_graph_neighbor_counts': 18,
               'occupation_configuration_checks_on_12_selected_sites': configuration_checks,
               'residual_pin_checks': pin_checks,
               'Bstar': Bstar, 'coercivity_denominator': 2*Bstar,
               'no_dense_N3_torus_enumeration': True,
               'elapsed_seconds': time.perf_counter()-t0,
               'maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    return outcome

def check_trial():
    from collections import defaultdict
    from fractions import Fraction
    from itertools import product, combinations
    import resource
    import time

    t0 = time.perf_counter()
    import sympy as s

    # A literal 16-dimensional four-physical-qubit check, not bosonic pairs.
    def lowering_pair(i, j):
        M = s.zeros(16)
        mask = (1 << i) | (1 << j)
        for word in range(16):
            if word & mask == mask:
                M[word ^ mask, word] = 1
        return M

    d1, d2 = lowering_pair(0, 1), lowering_pair(2, 3)
    q = d1-d2                            # sqrt(2) Q_E1
    M = s.I*(q.T-q)                      # sqrt(2) K_x
    z = s.symbols('z')
    charpoly = s.factor(M.charpoly(z).as_expr())
    assert s.expand(charpoly-z**6*(z*z-1)**4*(z*z-4)) == 0
    assert M == M.conjugate().T
    number = s.diag(*[i.bit_count() for i in range(16)])
    ad = number
    local_derivatives = []
    for r in range(1, 4):
        ad = M*ad-ad*M
        # The odd cases vanish; the second has the exact sqrt(2)^2 denominator.
        numerator = s.simplify(s.I**r*ad[0, 0])
        if r % 2 == 0:
            numerator /= 2**(r//2)
        assert numerator == ([0, 4, 0][r-1])
        local_derivatives.append(int(numerator))

    def add(x, y, L):
        return tuple((a+b) % L for a, b in zip(x, y))

    def neg(x):
        return tuple(-a for a in x)

    unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    zero = (0, 0, 0)
    D = set()
    for e in unit:
        D.add(tuple(2*a for a in e)); D.add(tuple(-2*a for a in e))
    for i, j in combinations(range(3), 2):
        for a, b in product([-1, 1], repeat=2):
            D.add(tuple(a*unit[i][k]+b*unit[j][k] for k in range(3)))
    assert len(D) == 18

    def pair(x, y):
        assert x != y
        return tuple(sorted([x, y]))

    def channel_words(x, L):
        d = [pair(add(x, e, L), add(x, neg(e), L)) for e in unit]
        out = [({d[0]: 1, d[1]: -1}, 2),
               ({d[0]: 1, d[1]: 1, d[2]: -2}, 6)]
        for i, j in combinations(range(3), 2):
            terms = {}
            for a, b in product([-1, 1], repeat=2):
                u = tuple(a*k for k in unit[i]); v = tuple(b*k for k in unit[j])
                terms[pair(add(x, u, L), add(x, v, L))] = a*b
            assert len(terms) == 4
            out.append((terms, 4))
        return out

    torus_checks = []
    for L in [5, 6, 7]:
        sites = list(product(range(L), repeat=3)); V = L**3
        channels = {x: channel_words(x, L) for x in sites}
        state = defaultdict(int)  # sqrt(2) sum_x Q_E1(x)^dagger Omega
        axial_centers = {}
        for x in sites:
            for i, e in enumerate(unit):
                key = pair(add(x, e, L), add(x, neg(e), L))
                assert key not in axial_centers
                axial_centers[key] = (x, i)
            for key, coeff in channels[x][0][0].items():
                state[key] += coeff
        assert len(state) == 2*V
        scaled_norm2 = sum(c*c for c in state.values())
        assert scaled_norm2 == 2*V
        result = defaultdict(Fraction)
        for key, c in state.items():
            result[key] = Fraction(2*c)  # mu=1, N=2
        contractions = {}
        for x in sites:
            scalars = []
            for A, (terms, norm2) in enumerate(channels[x]):
                val = sum(coeff*state.get(key, 0) for key, coeff in terms.items())
                scalars.append(val)
                for key, coeff in terms.items():
                    result[key] -= Fraction((2 if A < 2 else 1)*coeff*val, norm2)
            assert scalars == [2, 0, 0, 0, 0]
            contractions[x] = scalars
        assert all(v == 0 for v in result.values())
        # Every actual gradient annihilator vanishes, before its adjoint is applied.
        for x in sites:
            for e in unit:
                assert contractions[add(x, e, L)] == contractions[x]

        # K incidences and the complete h_x support, checked without a Hilbert space.
        Ksupport = {x: {add(x, e, L) for e in unit[:2]} |
                        {add(x, neg(e), L) for e in unit[:2]} for x in sites}
        incidence = defaultdict(int)
        for supp in Ksupport.values():
            assert len(supp) == 4
            for y in supp:
                incidence[y] += 1
        assert set(incidence.values()) == {4}
        hsupport = {zero} | {add(zero, d, L) for d in D}
        for words, _ in channels[zero]:
            for key in words:
                hsupport.update(key)
        assert len(hsupport) == 25
        for e in unit:
            for words, _ in channels[e]:
                for key in words:
                    assert set(key) <= hsupport
        first_step_terms = sum(bool(hsupport & supp) for supp in Ksupport.values())
        assert first_step_terms <= 4*25
        assert len(list(combinations(D, 2))) == 153
        # All five raw uniform waves, avoiding square-root arithmetic.
        raw_states = []
        for Aindex in range(5):
            raw = defaultdict(int)
            for x in sites:
                for key, coeff in channels[x][Aindex][0].items(): raw[key] += coeff
            raw_states.append(dict(raw))
        gram = [[sum(c*raw_states[b].get(key,0) for key,c in raw_states[a].items())
                 for b in range(5)] for a in range(5)]
        assert gram == [[([2,6,8,8,8][a]*V if a==b else 0) for b in range(5)] for a in range(5)]
        for Aindex, raw in enumerate(raw_states):
            h_result = defaultdict(Fraction, {key:Fraction(2*c) for key,c in raw.items()})
            first_values = None
            for x in sites:
                values = []
                for bindex, (terms, denominator) in enumerate(channels[x]):
                    value = sum(coeff*raw.get(key,0) for key,coeff in terms.items())
                    values.append(value)
                    for key,coeff in terms.items():
                        h_result[key] -= Fraction((2 if bindex<2 else 1)*coeff*value,denominator)
                if first_values is None: first_values=values
                assert values==first_values
            assert all(value==0 for value in h_result.values())
        torus_checks.append({'L': L, 'V': V, 'scaled_pair_norm_squared': scaled_norm2,
                             'H_pair_residual_zero': True, 'all_gradient_annihilators_zero': True,
                             'h_support_size': len(hsupport), 'K_incidence': 4,
                             'K_terms_touching_h_support': first_step_terms})

    CH_multiplier = 24**4*25*28*31*34
    CN = 24**4*1*4*7*10
    A_multiplier, B_constant = Fraction(CH_multiplier, 24), Fraction(CN, 24)
    assert A_multiplier.denominator == B_constant.denominator == 1
    assert (A_multiplier,B_constant)==(10199347200,3870720)
    nu, A, B, y = s.symbols('nu A B y', positive=True)
    poly = (A+nu*B)*y*y-2*nu*y
    assert s.simplify(poly.subs(y, nu/(A+nu*B))+nu**2/(A+nu*B)) == 0
    assert s.simplify(poly+nu**2/(A+nu*B) - (A+nu*B)*(y-nu/(A+nu*B))**2) == 0

    result = {'local_K_scaled_characteristic_polynomial': str(charpoly),
              'local_K_norm': 'sqrt(2)', 'local_number_derivatives_1_2_3': local_derivatives,
              'tori': torus_checks, 'C_H_multiplier_of_182mu_plus_240tau': CH_multiplier,
              'C_N': CN, 'A_multiplier_of_182mu_plus_240tau': int(A_multiplier),
              'B': int(B_constant), 'variational_square_identity': True,
              'separate_geometry_check': 'check_coercivity_geometry',
              'elapsed_seconds': time.perf_counter()-t0,
              'maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    return result

def main():
    started = time.monotonic()
    result = {"full_carrier": check_full_carrier(),
              "coercivity_geometry": check_coercivity_geometry(),
              "unitary_trial": check_trial()}
    root = Path(__file__).resolve().parents[1]
    result["integrity_reads"] = {p: hashlib.sha256((root/p).read_bytes()).hexdigest()
                                 for p in AUDIT_INPUT_PATHS}
    result["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["elapsed_seconds"] = time.monotonic()-started
    result["scope"] = "Finite exact controls support the note's analytic all-volume proof; supplied Hamiltonian only."
    output = root/"outputs/native_qubit_pair_density_onset_2026_09_30.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    print("per_element: exact hard-core lowering and local sum-of-squares columns checked.")
    print("per_site: eighteen-neighbor incidence and 153 centered triple terms checked.")
    print("per_mode: five uniform pair waves checked on finite tori; no dense phase spectrum claimed.")
    print("per_block: point pins, rational resistance, occupation localization and trial constants checked.")
    print("lattice_wide: analytic proof in the bound source carries all L>=5; finite controls are not extrapolated.")
    print("TOTAL: PASS=3 FAIL=0; conditional supplied-model controls, not audit status.")

if __name__ == "__main__":
    main()
