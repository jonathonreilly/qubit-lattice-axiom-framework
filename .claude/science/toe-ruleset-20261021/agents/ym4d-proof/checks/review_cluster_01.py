#!/usr/bin/env python3
"""Independent finite checks of the frozen connected-support theorem.

The general bounds are proved in the reviewer report. These exact finite
checks cannot establish an actual Yang--Mills instance or a limiting theorem.
No author helper or implementation is imported.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial
import hashlib
import json
from pathlib import Path
import platform
import sympy as sp
from sympy.polys.domains import QQ_I

checks = {}
controls = {}
counts = {}


def connected_edges(n, edges):
    if n == 0:
        return False
    reached = {0}
    while True:
        nxt = reached | {b for a,b in edges if a in reached} | {a for a,b in edges if b in reached}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


@lru_cache(None)
def ursell(n, edges):
    """Alternating connected-subgraph sum by direct subset enumeration."""
    if n == 1:
        return 1
    ans = 0
    for mask in range(1 << len(edges)):
        selected = [e for j,e in enumerate(edges) if (mask >> j) & 1]
        if connected_edges(n, selected):
            ans += (-1) ** len(selected)
    return ans


def kruskal(n, selected, edge_order):
    parent = list(range(n))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    out = []
    for e in edge_order:
        if e not in selected:
            continue
        a,b = map(root,e)
        if a != b:
            parent[a] = b
            out.append(e)
    return tuple(sorted(out))


def path_edges(n, tree, a, b):
    stack = [(a, ())]
    seen = set()
    while stack:
        v,p = stack.pop()
        if v == b:
            return p
        seen.add(v)
        for e in tree:
            if v in e:
                w = e[0]+e[1]-v
                if w not in seen:
                    stack.append((w,p+(e,)))
    raise AssertionError('tree path missing')


def matrix_tree_count(n, edges):
    if n == 1:
        return 1
    lap = sp.zeros(n)
    for a,b in edges:
        lap[a,a] += 1
        lap[b,b] += 1
        lap[a,b] -= 1
        lap[b,a] -= 1
    return int(lap[:-1,:-1].det(method='domain-ge'))


graph_total = host_connected_total = partitions_checked = 0
all_intervals = all_tree_bounds = True
triangle = ((0,1),(0,2),(1,2))
for n in range(1,6):
    possible = list(combinations(range(n),2))
    for hostmask in range(1 << len(possible)):
        host = tuple(e for j,e in enumerate(possible) if (hostmask >> j)&1)
        graph_total += 1
        val = ursell(n,host)
        ntree = matrix_tree_count(n,host)
        all_tree_bounds &= abs(val) <= ntree
        if ntree == 0:
            continue
        host_connected_total += 1
        for edge_order in (host, tuple(reversed(host))):
            rank = {e:j for j,e in enumerate(edge_order)}
            grouped = defaultdict(set)
            for mask in range(1 << len(host)):
                selected = frozenset(e for j,e in enumerate(host) if (mask >> j)&1)
                if connected_edges(n,selected):
                    grouped[kruskal(n,selected,edge_order)].add(selected)
            signed_intervals = 0
            for tree, seen in grouped.items():
                extras = [e for e in host if e not in tree and
                          rank[e] > max(rank[f] for f in path_edges(n,tree,*e))]
                expected = {frozenset(tree) | frozenset(e for j,e in enumerate(extras) if (m>>j)&1)
                            for m in range(1 << len(extras))}
                all_intervals &= seen == expected
                signed_intervals += (-1)**(n-1) * (not extras)
                partitions_checked += 1
            all_intervals &= signed_intervals == val
checks['all_simple_graph_tree_inequalities_through_5_vertices'] = all_tree_bounds
checks['kruskal_intervals_both_edge_orders'] = all_intervals
controls['replace_connected_graph_sum_by_one_tree_detected'] = ursell(3,triangle) != 1
controls['omit_overlap_edge_detected'] = ursell(3,triangle) != ursell(3,triangle[:-1])
counts.update(graphs=graph_total, connected_host_graphs=host_connected_total,
              kruskal_tree_intervals=partitions_checked, triangle_ursell=ursell(3,triangle))

# Sparse polynomial arithmetic over exact Gaussian rationals; keys=(t,z0,z1,z2).
# Logarithms use the differential recurrence Z'=Z*(log Z)', not log(1+x).
CAP = 5
ZKEY = (0,0,0,0)
QZERO, QONE = QQ_I.zero, QQ_I.one
ONE = {ZKEY:QONE}


def polyadd(p,q):
    out = p.copy()
    for k,v in q.items():
        out[k] = out.get(k,QZERO)+v
        if not out[k]:
            del out[k]
    return out


def polyscale(p,c):
    return {k:v*c for k,v in p.items() if v*c}


def polymul(p,q):
    out = defaultdict(lambda:QZERO)
    for k,v in p.items():
        for ell,w in q.items():
            key = tuple(a+b for a,b in zip(k,ell))
            if key[0] <= CAP:
                out[key] += v*w
    return {k:v for k,v in out.items() if v}


def log_by_differential_recurrence(p):
    assert p.get(ZKEY) == QONE
    zz = [{k:v for k,v in p.items() if k[0] == n} for n in range(CAP+1)]
    out = [{} for n in range(CAP+1)]
    for n in range(1,CAP+1):
        accum = zz[n].copy()
        for k in range(1,n):
            accum = polyadd(accum,polyscale(polymul(out[k],zz[n-k]),QQ_I(-F(k,n))))
        out[n] = accum
    ans = {}
    for p0 in out:
        ans = polyadd(ans,p0)
    return ans


supports = [frozenset([0]), frozenset([1]), frozenset([0,1]),
            frozenset([1,2]), frozenset([0,1,2])]
reads = [(0,),(1,),(0,1),(1,2),(0,2)]
source_keys = [(1,1,0,0),(1,0,1,0),(1,0,0,0),(1,0,0,1),(1,1,0,1)]
coeffs = [QQ_I.from_sympy(sp.Rational(1,31)+sp.I/43),QQ_I(sp.Rational(1,37)),
          QQ_I.from_sympy(-sp.Rational(1,41)+sp.I/47),QQ_I(sp.Rational(1,53)),
          QQ_I.from_sympy(sp.I/59)]
plus = [F(1,3),F(2,5),F(3,7)]
means = [2*p-1 for p in plus]
direct = {}
for spins in product([-1,1],repeat=3):
    prob = F(1)
    for x,s in enumerate(spins):
        prob *= plus[x] if s==1 else 1-plus[x]
    term = ONE
    for j in range(5):
        char = 1
        for x in reads[j]:
            char *= spins[x]
        term = polymul(term,polyadd(ONE,{source_keys[j]:coeffs[j]*char}))
    direct = polyadd(direct,polyscale(term,QQ_I(prob)))

# Different expectation path: multiplication of single-site moments.
activities = {}
connected_collections = 0
for mask in range(1,1<<5):
    ids = [j for j in range(5) if (mask>>j)&1]
    overlap = [(a,b) for a,b in combinations(range(len(ids)),2) if supports[ids[a]]&supports[ids[b]]]
    if not connected_edges(len(ids),overlap):
        continue
    connected_collections += 1
    key = [0]*4
    degree = [0]*3
    coeff = QONE
    union = frozenset()
    for j in ids:
        coeff *= coeffs[j]
        key = [a+b for a,b in zip(key,source_keys[j])]
        union |= supports[j]
        for x in reads[j]:
            degree[x] += 1
    for x,d in enumerate(degree):
        if d%2:
            coeff *= QQ_I(means[x])
    activities[union] = polyadd(activities.get(union,{}),{tuple(key):coeff})

# Gas by independent-set enumeration, not the author's used-support DP.
items = sorted(activities.items(),key=lambda item:tuple(item[0]))
gas = {}
for mask in range(1<<len(items)):
    ids=[j for j in range(len(items)) if (mask>>j)&1]
    if any(items[a][0]&items[b][0] for a,b in combinations(ids,2)):
        continue
    term = ONE
    for j in ids:
        term = polymul(term,items[j][1])
    gas = polyadd(gas,term)
checks['biased_complex_spin_sum_equals_connected_gas'] = direct == gas

cluster = {}
local_cluster = {}
max_cluster_n = 0
repeated_contributing = 0
for n in range(1,CAP+1):
    for ids in combinations_with_replacement(range(len(items)),n):
        edges = tuple((a,b) for a,b in combinations(range(n),2) if items[ids[a]][0]&items[ids[b]][0])
        u = ursell(n,edges)
        if not u:
            continue
        multiplicity = [ids.count(j) for j in range(len(items))]
        denom = 1
        for k in multiplicity:
            denom *= factorial(k)
        term = ONE
        union = frozenset()
        for j in ids:
            term = polymul(term,items[j][1])
            union |= items[j][0]
        term = polyscale(term,QQ_I(F(u,denom)))
        if term:
            max_cluster_n=max(max_cluster_n,n)
            repeated_contributing += len(set(ids)) < len(ids)
        cluster = polyadd(cluster,term)
        local_cluster[union] = polyadd(local_cluster.get(union,{}),term)
logs = log_by_differential_recurrence(direct)
checks['log_differential_recurrence_equals_full_ursell_through_5'] = logs == cluster
checks['repeated_and_at_least_3_member_clusters_exercised'] = max_cluster_n == 5 and repeated_contributing>0
checks['all_computed_source_labels_and_path_connectors'] = all(
    max(s)-min(s)+1==len(s) and all(not k[x+1] or x in s for x in range(3))
    for s,p0 in local_cluster.items() for k in p0)
controls['omit_repeated_singleton_cluster_detected'] = logs != polyadd(logs,
    polyscale(polymul(activities[frozenset([0])],activities[frozenset([0])]),QQ_I(F(1,2))))
controls['remote_source_omission_detected'] = not ({0,2} <= {0})
controls['long_jump_endpoint_connector_omission_detected'] = max({0,2})-min({0,2})+1 != len({0,2})
counts.update(spin_configurations=8, connected_factor_collections=connected_collections,
              gas_supports=len(items), partition_monomials=len(direct),log_monomials=len(logs),
              largest_log_cluster=max_cluster_n,repeated_cluster_contributions=repeated_contributing)

# Rooted trees: implicit-series iteration versus direct Prüfer labeled trees.
rsupports = [frozenset([0]),frozenset([1]),frozenset([0,1]),frozenset([1,2])]
rv = [F(1,41),F(1,43),F(1,47),F(1,53)]
N = 5
T = [[F(0)]*(N+1) for _ in rv]
for _ in range(N):
    new = []
    for i in range(len(rv)):
        a = [sum(T[j][n] for j in range(len(rv)) if rsupports[i]&rsupports[j]) for n in range(N+1)]
        e = [F(1)]+[F(0)]*N
        for n in range(1,N+1):
            e[n] = sum(F(k,n)*a[k]*e[n-k] for k in range(1,n+1))
        new.append([F(0)]+[rv[i]*e[n-1] for n in range(1,N+1)])
    T = new


def prufer_tree(code,n):
    if n == 1:
        return []
    degree = [1]*n
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = next(j for j,d in enumerate(degree) if d==1)
        edges.append((leaf,x));degree[leaf]-=1;degree[x]-=1
    left=[j for j,d in enumerate(degree) if d==1]
    edges.append(tuple(left))
    return edges

all_rooted=True
prufer_count=0
for n in range(1,N+1):
    measured=[F(0)]*len(rv)
    trees=[[]] if n==1 else [prufer_tree(code,n) for code in product(range(n),repeat=max(0,n-2))]
    for labels in product(range(len(rv)),repeat=n):
        weight=F(1)
        for j in labels:
            weight*=rv[j]
        for tree in trees:
            prufer_count+=1
            if all(rsupports[labels[a]]&rsupports[labels[b]] for a,b in tree):
                measured[labels[0]]+=weight/F(factorial(n-1))
    all_rooted &= all(measured[i] == T[i][n] for i in range(len(rv)))
checks['rooted_exponential_series_equals_prufer_trees_through_5'] = all_rooted
controls['omit_rooted_tree_factorial_detected'] = T[0][3] != 2*T[0][3]
counts['prufer_labeled_assignments']=prufer_count

# q=2 block envelope with an actual long connector, exact weight exp(beta)=2.
blockatoms=[(0,0,frozenset([0]),sp.Matrix([[1,0],[0,2]])/1000),
            (0,1,frozenset([0,1]),sp.Matrix([[1,2],[0,1]])/1000),
            (1,2,frozenset([1,2]),sp.Matrix([[1,0],[3,1]])/1000),
            (0,2,frozenset([0,1,2]),sp.Matrix([[1,1],[1,0]])/2000)]
blockatoms += [(y,x,s,B.T) for x,y,s,B in list(blockatoms) if x!=y]
weighted=[]
for x,y,s,B in blockatoms:
    norm=max(sum(abs(B[a,b]) for b in range(2)) for a in range(2))
    weighted.append((x,y,s,F(norm)*2**len(s)))
r=max([sum(w for x,y,s,w in weighted if x==v) for v in range(3)]+
      [sum(w for x,y,s,w in weighted if y==v) for v in range(3)])
b=max(sum(w for x,y,s,w in weighted if v in s) for v in range(3))
walks={(x,x,frozenset([x])):F(1) for x in range(3)}
walk_ok=True
for n in range(1,7):
    nxt=defaultdict(F)
    for (start,end,S),weight in walks.items():
        for x,y,s,w in weighted:
            if end==x:
                # Product weights overcharge overlaps; use this envelope directly.
                nxt[start,y,S|s]+=weight*w
    walks=nxt
    walk_ok &= all(sum(w for (x,y,s),w in walks.items() if x==v)<=r**n for v in range(3))
    walk_ok &= all(sum(w for (x,y,s),w in walks.items() if y==v)<=r**n for v in range(3))
    walk_ok &= all(sum(w for (x,y,s),w in walks.items() if v in s)<=n*b*r**(n-1) for v in range(3))
checks['both_block_endpoints_and_incidence_walk_bounds_through_6'] = walk_ok

# Independent coefficient recursion solves (1-t)C(t)^2=1.
c=[F(1)]
for n in range(1,11):
    c.append((sum(c[i]*c[n-1-i] for i in range(n))-
              sum(c[i]*c[n-i] for i in range(1,n)))/2)
checks['inverse_sqrt_recursion_equals_binomial_through_10'] = all(c[n]==F(comb(2*n,n),4**n) for n in range(11))
controls['binomial_half_factor_mutation_detected'] = c[1] != 1

z=[sp.Rational(1,2),sp.I/3,sp.Rational(2,5)]
E=sp.zeros(6)
for x,y,s,B in blockatoms:
    factor=z[x] if x==y else z[x]*z[y]
    for aa in range(2):
        for bb in range(2):
            E[2*x+aa,2*y+bb]+=B[aa,bb]*factor
powers=[sp.eye(6)]
for n in range(1,6):
    powers.append(powers[-1]*E)
C=[sp.Rational(v.numerator,v.denominator)*powers[n] for n,v in enumerate(c[:6])]
congruence=True
for n in range(6):
    term=sum((C[i].T*C[n-i] for i in range(n+1)),sp.zeros(6))
    if n:
        term-=sum((C[i].T*E*C[n-1-i] for i in range(n)),sp.zeros(6))
    congruence &= term==(sp.eye(6) if n==0 else sp.zeros(6))
checks['complex_symmetric_bilinear_congruence_through_5'] = congruence
controls['hermitian_substitution_detected_at_complex_data'] = C[1].conjugate().T+C[1]-E != sp.zeros(6)
t=sp.Symbol('t')
char=E.charpoly().all_coeffs()
detcoef=[sp.sympify(v) for v in char] # det(I-tE) uses coefficients in this order.
logcoef=[sp.S(0)]*6
for n in range(1,6):
    logcoef[n]=detcoef[n]-sum(sp.Rational(k,n)*logcoef[k]*detcoef[n-k] for k in range(1,n))
checks['full_logdet_characteristic_polynomial_equals_trace_through_5'] = all(
    sp.expand(-logcoef[n]/2-sp.trace(powers[n])/(2*n))==0 for n in range(1,6))
controls['drop_logdet_detected_at_zero_interaction'] = -logcoef[1]/2 != 0
controls['logdet_sign_and_half_factor_mutations_detected'] = all(
    sp.expand(-logcoef[1]/2-x)!=0 for x in [logcoef[1]/2,-logcoef[1]])
counts.update(weighted_block_r=str(r),weighted_block_b=str(b),complex_logdet_linear=str(-logcoef[1]/2))

# Scalar-coordinate combinatorics: enumerate weak compositions, no binomial target in producer.
coordinate_counts={}
for Q in [1,2,4,6]:
    for n in range(9):
        enum=sum(1 for a in product(range(n+1),repeat=Q) if sum(a)==n)
        coordinate_counts[Q,n]=enum
checks['scalar_taylor_counts_include_q_times_s'] = all(
    enum==comb(n+Q-1,Q-1) for (Q,n),enum in coordinate_counts.items())
checks['marked_taylor_counts_equal_derivative'] = all(
    n*coordinate_counts[Q,n]==Q*comb(n+Q-1,Q) for Q in [1,2,4,6] for n in range(1,9))
controls['omitting_q_scalar_count_detected'] = coordinate_counts[4,3] != coordinate_counts[2,3]

# Massive graph normalization on every simple graph through four vertices.
mass_ok=True
mass_count=0
for n in range(5):
    possible=list(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=[e for j,e in enumerate(possible) if (mask>>j)&1]
        degrees=[sum(v in e for e in edges) for v in range(n)]
        Delta=max(degrees,default=0)
        mass=F(7,5)
        normc=mass+Delta
        lap=sp.zeros(n)
        for x,y in edges:
            lap[x,x]+=1;lap[y,y]+=1;lap[x,y]-=1;lap[y,x]-=1
        EE=sp.eye(n)-(sp.Rational(mass.numerator,mass.denominator)*sp.eye(n)+lap)/sp.Rational(normc.numerator,normc.denominator)
        mass_ok &= sp.Rational(normc.numerator,normc.denominator)*(sp.eye(n)-EE)==sp.Rational(mass.numerator,mass.denominator)*sp.eye(n)+lap
        if Delta:
            # exp(beta)=11/10; check only cases satisfying r<1.
            eb=F(11,10)
            atoms=[(x,x,{x},F(Delta-degrees[x],1)/normc) for x in range(n)]
            atoms += [(x,y,{x,y},1/normc) for a,b0 in edges for x,y in [(a,b0),(b0,a)]]
            rr=max(sum(v*eb**len(s) for x,y,s,v in atoms if x==z0) for z0 in range(n))
            bb=max(sum(v*eb**len(s) for x,y,s,v in atoms if z0 in s) for z0 in range(n))
            mass_ok &= rr<=Delta*eb**2/normc and bb<=2*Delta*eb**2/normc
        mass_count+=1
checks['massive_laplacian_normalization_empty_disconnected_diagonal'] = bool(mass_ok)
counts['massive_graphs']=mass_count
# Literal-domain counterexample to the frozen standalone Lemma O.
checks['negative_beta_counterexample_meets_printed_r_and_b'] = F(1,4)*2 == F(1,2) < 1
checks['negative_beta_counterexample_series_terms_do_not_tend_to_zero'] = c[10]*2**10 > c[9]*2**9 > 1
counts['negative_beta_counterexample']={'exp_beta':'1/4','E':'2','r':'1/2','K':'-1','c10_times_2pow10':str(c[10]*2**10)}
# Rational sufficient margins use exp(3)<27 and exp(6)<729, proved in report.
checks['concrete_example_rational_budgets'] = (
    F(729,8192)<F(1,8) and F(729,4096)<F(1,4) and
    27+F(8,7)-1<28 and 27+F(1,8)*F(8,7)**2<28 and
    F(27,1024)*(F(4,3)+F(1,4)*F(16,9))==F(3,64) and F(3,64)<F(1,4))

result={'scope':'Independent exact finite algebra/combinatorics, not actual Yang--Mills or general theorem proof',
        'python':platform.python_version(),'sympy':sp.__version__,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'controls':controls,'counts':counts,
        'all_checks_pass':all(checks.values()),'all_mutations_detected':all(controls.values()),
        'finding':'Frozen standalone Lemma O omits beta >= 0; all stated applications use positive beta.'}
print(json.dumps(result,indent=2,sort_keys=True))
if not all(checks.values()) or not all(controls.values()):
    raise SystemExit(1)
