#!/usr/bin/env python3
"""Finite controls for supplied local qubit ports and polynomial mixing.

Deterministic; Python 3, NumPy, SciPy and SymPy. No runtime file inputs,
repository imports, network, or output artifacts. Exact algebra/combinatorics
are separated from explicitly labelled floating matrix controls. All-size
claims rely on the paired analytic proof, not finite sampling or PASS counts.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp, isqrt, log, sqrt
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import json
import numpy as np
from scipy.linalg import expm
import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/LOCAL_QUBIT_PORT_REALIZATION_WITH_POLYNOMIAL_MIXING_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md',
    'docs/SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
]
START=perf_counter()

checks = 0
def check(ok, name):
    global checks
    assert bool(ok), name
    checks += 1

def bit(z, j):
    return (z >> j) & 1
def occ(z, K=2, d=4):
    return tuple(sum(bit(z, K*a+j) for j in range(K)) for a in range(d))
def reaction(z, ports):
    p = tuple(bit(z, j) for j in ports)
    return z ^ sum(1 << j for j in ports) if p in [(1,1,0,0),(0,0,1,1)] else None
def jump_matrix(d, mapping):
    J = np.zeros((d,d), dtype=np.int64)
    for a,b in mapping.items():
        J[b,a] = 1
    return J

for title, d, mapping in [
    ('directed bond', 4, {1:2}),
    ('fast exchange', 4, {1:2,2:1}),
    ('collision plaquette', 16, {3:12,12:3}),
]:
    J = jump_matrix(d, mapping)
    P = J.T @ J
    for a,b in product(range(d), repeat=2):
        diag_twice = [2*int(J[s,a])*int(J[s,b])-int(P[s,a])*(b==s)-(s==a)*int(P[b,s]) for s in range(d)]
        if a != b:
            check(not any(diag_twice), title + ': off-diagonal unit feeds populations')
        else:
            expected = [2*(int(s == mapping[a])-int(s == a)) if a in mapping else 0 for s in range(d)]
            check(diag_twice == expected, title + ': exact diagonal classical generator entries')
print('Exact partial-permutation channel controls: 288 complete matrix units, arbitrary off-diagonal inputs included.')

K = 2
base = sp.Rational(2,3)  # c*kappa/Omega; independent mathematical fixture
lam = base * K*K
ports = [0,2,4,6]
fibers = defaultdict(list)
for z in range(1 << 8):
    fibers[occ(z)].append(z)
for n, words in fibers.items():
    actual = defaultdict(lambda:sp.Rational(0))
    for z in words:
        zz = reaction(z, ports)
        if zz is not None:
            actual[occ(zz)] += lam/len(words)
    expected = defaultdict(lambda:sp.Rational(0))
    for i,j,k,l in [(0,1,2,3),(2,3,0,1)]:
        if n[i] and n[j] and n[k]<K and n[l]<K:
            nn=list(n); nn[i]-=1; nn[j]-=1; nn[k]+=1; nn[l]+=1
            vacancy = (1-sp.Rational(n[k],K))*(1-sp.Rational(n[l],K))
            expected[tuple(nn)] += base*n[i]*n[j]*vacancy
    check(dict(actual) == dict(expected), 'all-fiber collision count at '+str(n))
print('Exact collision port average: 256 microstates, 81 count fibers; both directions and all vacancy sectors.')

hop_fibers = defaultdict(list)
for z in range(16):
    hop_fibers[occ(z,d=2)].append(z)
q=sp.Rational(7,5)
for n,words in hop_fibers.items():
    actual=sum((q*K for z in words if bit(z,0)==1 and bit(z,2)==0), sp.Rational(0))/len(words)
    check(actual == q*n[0]*(1-sp.Rational(n[1],K)), 'hop port capacity normalization')
print('Exact hop port average: 16 microstates, 9 fibers; rate q*K produces q*n_source*(1-n_target/K).')

# Exact microscopic and averaged count generators on the N=3 carrier.
states=[z for z in range(256) if z.bit_count()==3]
ix={z:i for i,z in enumerate(states)}
ns=sorted({occ(z) for z in states})
ni={n:i for i,n in enumerate(ns)}
dim=len(states)
A=sp.zeros(dim); B=sp.zeros(dim); P=sp.zeros(dim); lift=sp.zeros(dim,len(ns))
for z in states:
    i=ix[z]; n=occ(z); lift[i,ni[n]]=1
    for zz in fibers[n]:
        P[i,ix[zz]]=sp.Rational(1,len(fibers[n]))
    for a in range(4):
        if bit(z,2*a)!=bit(z,2*a+1):
            zz=z^(3<<(2*a)); A[i,ix[zz]]+=1; A[i,i]-=1
    zz=reaction(z,ports)
    if zz is not None:
        B[i,ix[zz]]+=lam; B[i,i]-=lam
check(A*P == sp.zeros(dim) and P*A == sp.zeros(dim), 'uniform fast-fiber stationarity')
check(P*P == P, 'fiber averaging is a projection')
C=sp.zeros(len(ns))
for n in ns:
    for i,j,k,l in [(0,1,2,3),(2,3,0,1)]:
        if n[i] and n[j] and n[k]<K and n[l]<K:
            nn=list(n);nn[i]-=1;nn[j]-=1;nn[k]+=1;nn[l]+=1
            rate=base*n[i]*n[j]*(1-sp.Rational(n[k],K))*(1-sp.Rational(n[l],K))
            C[ni[n],ni[tuple(nn)]]+=rate;C[ni[n],ni[n]]-=rate
check(P*B*lift == lift*C, 'actual averaged generator equals independent capacity-rate matrix')
check(B*lift != P*B*lift, 'finite-rate count process is not exactly lumped')
print('Exact micro/count generator: 56 microstates, 16 count states; uniform fast fibers; averaged capacity rates; finite-rate non-lumping.')
An=np.array(A).astype(float);Bn=np.array(B).astype(float)
Cn=np.array(C).astype(float);Ln=np.array(lift).astype(float)

# A finite multi-time discriminator for the separate uniformization proof.
# With K=2 each nontrivial compartment is a two-state rate-one exchange.
# Its distance to uniform is exp(-2t)/2, so four compartments have integrated
# worst-case mixing distance at most 1. No inverse-operator norm is substituted.
multi_rows=[]
for nu in [16,64,256]:
    T=1.0
    E=expm((T/2)*(nu*An+Bn)); F=expm((T/2)*Cn)
    actual_blocks=[]; target_blocks=[]
    first=Ln @ F
    for a,n in enumerate(ns):
        inds=[ix[z] for z in states if occ(z)==n]
        actual_blocks.append(E[:,inds] @ E[inds,:] @ Ln)
        target_blocks.append(first[:,a,None] * F[a,None,:])
    joint=np.concatenate(actual_blocks,axis=1)
    ideal=np.concatenate(target_blocks,axis=1)
    error=float(np.max(np.sum(np.abs(joint-ideal),axis=1))/2)
    bound=float(lam*(1+lam)/nu)
    check(error <= bound+1e-12,'two-time count law uniformization control')
    multi_rows.append({'T':T,'nu':nu,'worst_two_time_TV':error,'path_bound_using_integrated_mixing_le_1':bound})
    print('Two-time averaging:',json.dumps(multi_rows[-1],sort_keys=True))
u,t,rate=sp.symbols('u t rate',positive=True)
check(sp.simplify(sp.integrate(rate*sp.exp(-rate*u)*(1+rate*(t-u)),(u,0,t))-rate*t)==0,'Poisson renewal identity including the first waiting gap')

# The uniform capacity coupling constants, exhaustively at small N/K.
for total in range(1,10):
    for n in product(range(total+1),repeat=4):
        if sum(n)!=total: continue
        for cap in [max(1,total),total+2]:
            a,b,c,d=map(sp.Integer,n)
            defect=a*b*(1-(1-c/cap)*(1-d/cap))+c*d*(1-(1-a/cap)*(1-b/cap))
            check(0 <= defect <= sp.Rational(total**3,16*cap), 'collision capacity bound N^3/(16K)')
print('Uniform collision-rate deficit bound checked on every four-count composition through N=9.')

# Literal cubic tile: all 288 reaction ports plus all 54 streaming ports.
V=list(product([-1,0,1],repeat=3))
groups=defaultdict(list)
for i,j in combinations(range(27),2):
    key=tuple(V[i][a]+V[j][a] for a in range(3))+(sum(t*t for t in V[i]+V[j]),)
    groups[key].append((i,j))
reactions=[]
for pairs in groups.values():
    for ab,cd in combinations(pairs,2):
        check(len(set(ab+cd))==4,'conservative nontrivial pair uses four species')
        check(all(V[ab[0]][d]+V[ab[1]][d]==V[cd[0]][d]+V[cd[1]][d] for d in range(3)) and sum(t*t for a in ab for t in V[a])==sum(t*t for a in cd for t in V[a]), 'collision preserves assigned momentum and kinetic energy')
        reactions.append(ab+cd)
check(len(reactions)==288,'D3Q27 full reaction census')
patch=[set() for _ in V]
port_rows=[]
side=4*len(reactions)
z_columns={}
for r,vs in enumerate(reactions):
    pts=[(4*r+2,2,0),(4*r+3,2,0),(4*r+3,3,0),(4*r+2,3,0)]
    for v,(x,y,z) in zip(vs,pts):
        height=v+1
        patch[v].update((x,y,h) for h in range(height+1))
        yy=0 if y==2 else 5
        patch[v].update((x,t,height) for t in range(min(y,yy),max(y,yy)+1))
        z_columns.setdefault(v,(x,y))
    check(max(sum(abs(a-b) for a,b in zip(p,q)) for p,q in combinations(pts,2))==2,'collision patch diameter two')
    port_rows.append({'reaction':r,'velocities':vs,'ports':pts})
for v in range(27):
    height=v+1
    patch[v].update((x,y,height) for x in range(side) for y in [0,5])
    patch[v].update((0,y,height) for y in range(side))
    x,y=z_columns[v]
    patch[v].update((x,y,z) for z in range(side))
before=[len(s) for s in patch]
incidence=[sum(v in r for r in reactions) for v in range(27)]
offsets=[incidence[v]*(v+3)-v-4 for v in range(27)]
check(before == [4*side+q for q in offsets],'independent exact compartment-size formula')
check(min(offsets)==104 and max(offsets)==1259,'capacity offsets match the all-size geometry interval')
capacity=max(before)
tree_edges=[]
for v,s in enumerate(patch):
    deficit=capacity-len(s)
    check(deficit <= (side-6)*(side-1),'padding stays in cubic tile')
    s.update((1+j%(side-1),6+j//(side-1),v+1) for j in range(deficit))
    check(len(s)==capacity,'equal qubit capacities')
    seen={min(s)}; todo=deque(seen); edges=[]
    while todo:
        p=todo.popleft()
        for d in range(3):
            for sign in [-1,1]:
                q=list(p); q[d]+=sign; q=tuple(q)
                if q in s and q not in seen:
                    seen.add(q); todo.append(q); edges.append((p,q))
    check(seen==s,'nearest-neighbor connected compartment')
    check(len(edges)==capacity-1,'actual fast spanning tree')
    tree_edges.append(edges)
check(len(set().union(*patch))==sum(map(len,patch)),'physical site compartments disjoint')
coords=set().union(*patch)
extent=[[min(p[d] for p in coords),max(p[d] for p in coords)] for d in range(3)]
check(all(0<=p[d]<side for p in coords for d in range(3)),'all active sites lie in cubic tile')
hop_rows=[]
for v,velocity in enumerate(V):
    for d in range(3):
        if not velocity[d]: continue
        if d==0: a=(0,0,v+1); b=(side-1,0,v+1)
        elif d==1: a=(0,0,v+1); b=(0,side-1,v+1)
        else:
            x,y=z_columns[v]; a=(x,y,0); b=(x,y,side-1)
        source,target=(b,a) if velocity[d]>0 else (a,b)
        shift=[0,0,0]; shift[d]=velocity[d]*side
        translated=tuple(target[j]+shift[j] for j in range(3))
        check(source in patch[v] and target in patch[v],'streaming endpoints belong to same velocity compartments')
        check(tuple(translated[j]-source[j] for j in range(3))==tuple(velocity[d] if j==d else 0 for j in range(3)), 'streaming is an actual nearest-neighbor bond across tiles')
        hop_rows.append({'velocity':v,'axis':d,'sign':velocity[d],'source':source,'target_in_adjacent_tile':target})
check(len(hop_rows)==54,'all D3Q27 directed streaming ports')
print('Literal cubic tile:',len(reactions),'plaquettes;',len(hop_rows),'streaming ports;',27,'disjoint compartments; K=',capacity,'active sites=',len(coords),'all physical sites=',side**3)
# Independent BFS-distance reconstruction, with no coordinate file input.
def distances(adj,root):
    out={root:0};queue=deque([root])
    while queue:
        a=queue.popleft()
        for b in adj[a]:
            if b not in out:out[b]=out[a]+1;queue.append(b)
    return out
radii=[];diameters=[]
for v,vertices in enumerate(patch):
    root=min(vertices);adj={a:[] for a in vertices};full={a:[] for a in vertices}
    check(root==(0,0,v+1),'native BFS root coordinate')
    for a,b in tree_edges[v]:
        check(sum(abs(a[j]-b[j]) for j in range(3))==1,'fast tree edge is a unit cubic bond')
        adj[a].append(b);adj[b].append(a)
    for a in vertices:
        for j in range(3):
            for sign in [-1,1]:
                b=list(a);b[j]+=sign;b=tuple(b)
                if b in vertices:full[a].append(b)
    td=distances(adj,root);gd=distances(full,root)
    check(td==gd,'native tree is breadth-first for its actual coordinate graph')
    radius=max(td.values());diameter=max(distances(adj,max(td,key=td.get)).values())
    check(radius<=2*side+5 and diameter<=4*side+10,'BFS radius and diameter bounds')
    radii.append(radius);diameters.append(diameter)
for S0 in [1152,1153,1200,2048,10**6]:
    K0=S0*S0//2
    check(4*S0+1259<=K0<=4*S0+104+(S0-6)*(S0-1),'growing geometric capacity family')
print('Native BFS geometry: maximum radius',max(radii),'maximum diameter',max(diameters),'; large-family size inequalities checked without allocating large cubes.')

def swap(z,i,j):
    return z ^ ((1<<i)|(1<<j)) if ((z>>i)^(z>>j))&1 else z

def lap(K,n,edges):
    states=[sum(1<<j for j in inds) for inds in combinations(range(K),n)]
    lookup={z:i for i,z in enumerate(states)}
    L=np.zeros((len(states),len(states)),dtype=np.int64)
    for i,z in enumerate(states):
        for a,b in edges:
            zz=swap(z,a,b)
            if zz!=z:
                L[i,i]+=1; L[i,lookup[zz]]-=1
    return L

# Exact rational positive-definiteness on the zero-mean subspace.
# This verifies all functions in each finite complete-graph fiber, not samples.
complete_rows=[]
for K in range(2,8):
    for n in range(1,K):
        L=sp.Matrix(lap(K,n,list(combinations(range(K),2))))
        d=L.rows
        H=sp.zeros(d,d-1)
        for j in range(d-1): H[j,j]=1; H[d-1,j]=-1
        factor=sp.Rational(2,K)
        G=H.T*(factor*L-sp.eye(d))*H
        _,DD=G.LDLdecomposition(hermitian=False)
        check(all(DD[i,i]>0 for i in range(DD.rows)), 'complete-graph Poincare positive-definite Gram')
        complete_rows.append({'K':K,'n':n,'dimension':d,'minimum_exact_LDL_pivot':str(min(DD[i,i] for i in range(DD.rows)))})
print('Exact complete-graph Poincare controls:',len(complete_rows),'fibers, K=2..7, all zero-mean functions.')

def prufer(seq):
    K=len(seq)+2; degree=[1]*K
    for x in seq: degree[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i,d in enumerate(degree) if d==1)
        edges.append((leaf,x)); degree[leaf]-=1; degree[x]-=1
    leaves=[i for i,d in enumerate(degree) if d==1]
    edges.append(tuple(leaves)); return edges

def route(K,edges,u,v):
    adj=[[] for _ in range(K)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    parent={u:None};q=deque([u])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if b not in parent: parent[b]=a;q.append(b)
    if v not in parent: return None
    path=[v]
    while path[-1]!=u:path.append(parent[path[-1]])
    return path[::-1]

def edge_word(path):
    forward=list(zip(path[:-1],path[1:]))
    return forward+forward[-2::-1]

route_count=0;tree_count=0;min_scaled_gap=float('inf');rows=[]
for K in range(2,7):
    for seq in product(range(K),repeat=K-2):
        edges=prufer(seq);tree_count+=1
        congestion={tuple(sorted(e)):0 for e in edges}
        for u,v in combinations(range(K),2):
            word=edge_word(route(K,edges,u,v)); labels=list(range(K))
            for a,b in word: labels[a],labels[b]=labels[b],labels[a]
            expected=list(range(K));expected[u],expected[v]=expected[v],expected[u]
            check(labels==expected,'endpoint transposition routing must restore interior sites')
            for e in word:congestion[tuple(sorted(e))]+=len(word)
            route_count+=1
        comparison=2*(2*K-3)*(K*K//4)
        check(max(congestion.values())<=comparison,'tree edge congestion constant')
        # Every finite n sector; eigensolver is a numerical control only.
        for n in range(1,K):
            vals=np.linalg.eigvalsh(lap(K,n,edges))
            check(abs(vals[0])<1e-10 and vals[1]>0,'connected exclusion fiber has one zero mode')
            scaled=float(vals[1]*K*(2*K-3));min_scaled_gap=min(min_scaled_gap,scaled)
            check(scaled>=1-1e-10,'tree exclusion gap lower bound')
        if not seq or all(x==seq[0] for x in seq):
            rows.append({'K':K,'prufer':seq,'congestion':max(congestion.values()),'comparison_bound':comparison})
print('Exact route/congestion controls:',tree_count,'labelled trees; endpoint routes:',route_count)
print('Finite spectral controls: all fixed-occupation fibers in those trees; minimum gap*K*(2K-3) =',min_scaled_gap)

# Additional geometries beyond exhaustive labelled-tree range.
large_rows=[]
for K in [7,8,9]:
    families={'path':[(j,j+1) for j in range(K-1)],'star':[(0,j) for j in range(1,K)],'binary':[((j-1)//2,j) for j in range(1,K)]}
    for name,edges in families.items():
        for n in range(1,K):
            L=lap(K,n,edges);ev=np.linalg.eigvalsh(L);gap=float(ev[1])
            check(gap*K*(2*K-3)>=1-1e-9,'additional finite tree gap')
            H=0.5*sqrt(comb(K,n)-1)
            times=[0.0,0.01,0.1,0.5,1.0,2.0]
            worst=0.0
            for t in times:
                P=expm(-t*L);tv=float(np.max(np.sum(np.abs(P-1/len(L)),axis=1))/2)
                bound=min(1.0,H*exp(-t*gap))
                check(tv<=bound+1e-10,'finite L2-to-TV amplitude and decay')
                worst=max(worst,tv)
            large_rows.append({'K':K,'family':name,'n':n,'dimension':len(L),'numerical_gap':gap,'analytic_gap_lower':1/(K*(2*K-3))})
print('Additional path/star/binary controls:',len(large_rows),'fibers, K=7..9; direct TV checked at six times.')

# Exact product witness: two independent K=2 one-particle components.
# Single-component distance exp(-2t)/2 integrates to 1/4.
# Two-component distance exp(-2t)/2+exp(-4t)/4 integrates to 5/16.
t=sp.symbols('t',nonnegative=True)
one_generator=sp.Matrix([[-1,1],[1,-1]])
one_semigroup=(t*one_generator).exp()
joint_semigroup=sp.kronecker_product(one_semigroup,one_semigroup)
# For t>=0 only the initial-state entry exceeds uniform in this two-component row.
one_distance=sp.simplify(one_semigroup[0,0]-sp.Rational(1,2))
joint_distance=sp.simplify((joint_semigroup[0,0]-sp.Rational(1,4)-sum(joint_semigroup[0,j]-sp.Rational(1,4) for j in range(1,4)))/2)
check(sp.integrate(one_distance,(t,0,sp.oo))==sp.Rational(1,4),'single-component integrated TV from its generator')
product_integral=sp.integrate(joint_distance,(t,0,sp.oo))
claimed=sp.Rational(5,16)
check(product_integral==claimed,'integrated product TV differs from one-compartment TV')
print('Exact integrated product control: one component 1/4, two components 5/16.')

L=lap(4,1,[(0,1),(2,3)]);zero_count=int(np.sum(np.abs(np.linalg.eigvalsh(L))<1e-10))
check(zero_count==2,'disconnected graph retains multiple zero modes')
print('Retained connectedness counterexample: two disjoint bonds, one particle, two zero modes; global-uniform mixing fails.')

# Exact finite resource choices, including a capacity requirement above the
# minimum cube size. Set b/ell=1 and c=1; all remaining arithmetic is rational.
def ceil_fraction(x):
    return (x.numerator+x.denominator-1)//x.denominator
for N0,m0,T0,eps0 in [(5,3,Fraction(10000),Fraction(1,10)),(20,4,Fraction(100),Fraction(1,100)),(2,3,Fraction(1),Fraction(1,10))]:
    w0=Fraction(1,m0**3);Omega0=N0*w0;ksum=288
    Ccap=Fraction(3*N0*N0,2)+Fraction(ksum*N0**3,16)/Omega0
    required=max(N0,2,ceil_fraction(2*T0*Ccap/eps0))
    S0=max(1152,isqrt(2*(required+1)))
    if S0*S0<2*(required+1):S0+=1
    K0=S0*S0//2;D0=27*m0**3
    check(K0>=required,'resource capacity reaches the requested target')
    check(T0*Ccap/K0<=eps0/2,'capacity part of epsilon allocation')
    B0=54*K0/w0+Fraction(K0*K0*ksum,N0)/(w0*w0)
    cp=min(K0*(2*K0-3),K0*(8*S0+19))
    # log D<=D and (K/2)log2<=K: a simple integer upper bound for tau.
    tau0=cp*(1+D0+K0)
    chosen_nu=ceil_fraction(2*tau0*B0*(1+T0*B0)/eps0)
    check(tau0*B0*(1+T0*B0)/chosen_nu<=eps0/2,'mixing part of epsilon allocation')
print('Exact epsilon allocation: three finite parameter sets, including growing-cube capacity; both error terms <= epsilon/2.')
# Fixed-model constants and the target's stopped capacity-rate envelope.
# These are algebraic controls of the new coupling, not a duplicate PDE runner.
weights=[Fraction(2,3)**(3-sum(x*x for x in v))*Fraction(1,6)**sum(x*x for x in v) for v in V]
lookup_v={v:i for i,v in enumerate(V)}
axial=set()
for axis in range(3):
    a,b=[j for j in range(3) if j!=axis]
    for shift in [-1,0,1]:
        pair=[]
        for direction in [a,b]:
            ends=[]
            for sign in [-1,1]:
                v=[0,0,0];v[axis]=shift;v[direction]=sign;ends.append(lookup_v[tuple(v)])
            pair.append(tuple(sorted(ends)))
        axial.add(tuple(sorted(pair)))
check(len(axial)==9,'fixed-model axial reaction identification')
T4parts=[Fraction(0),Fraction(0)];axial_count=0
omega=Fraction(216);capacity_box=5832
for i,j,k,l in reactions:
    check(weights[i]*weights[j]==weights[k]*weights[l],'stopped deficit detailed-balance product')
    is_axial=tuple(sorted([(i,j),(k,l)])) in axial;axial_count+=is_axial
    contribution=weights[i]*weights[j]*sum(weights[v] for v in [i,j,k,l])
    T4parts[int(is_axial)]+=contribution
    upper=[2*omega*weights[v] for v in [i,j,k,l]]
    for counts in product(*[[Fraction(0),x/2,x] for x in upper]):
        a,b,c,d=counts
        actual=(a*b*(1-(1-c/capacity_box)*(1-d/capacity_box))+c*d*(1-(1-a/capacity_box)*(1-b/capacity_box)))/omega
        stopped_bound=8*omega**2*contribution/capacity_box
        check(0<=actual<=stopped_bound,'stopped collision deficit includes both directions')
check(axial_count==9,'all nine axial reactions occur in full census')
hop_weight=sum(sum(abs(x) for x in v)*weights[j]**2 for j,v in enumerate(V))
check(hop_weight==Fraction(1,24),'stopped hopping coefficient from actual equilibrium weights')
check(4*hop_weight==Fraction(1,6),'stopped hopping rate-deficit factor')
print('Exact stopped capacity controls: all 288 reaction boxes, 81 points each; T4 =',T4parts[0],'+ alpha_* *',T4parts[1],'; hopping weight =',hop_weight)

# Actual quantum count instruments on four active qubits at active N=2,
# with an additional inert qubit entangled with the active carrier.
active_states=[z for z in range(16) if z.bit_count()==2]
active_index={z:i for i,z in enumerate(active_states)}
adim=len(active_states);fdim=2*adim
local_jumps=[]
for a,b,reversible,rate_q in [(0,1,True,Fraction(2)),(2,3,True,Fraction(2)),(1,2,False,Fraction(3,5)),(3,0,False,Fraction(7,5))]:
    J=np.zeros((adim,adim),dtype=int)
    for z in active_states:
        if bit(z,a) and not bit(z,b) or reversible and bit(z,b) and not bit(z,a):
            J[active_index[z^((1<<a)|(1<<b))],active_index[z]]=1
    local_jumps.append((J,rate_q))
Q=np.zeros((adim,adim));superop=np.zeros((fdim*fdim,fdim*fdim),dtype=complex)
for J,rate_q in local_jumps:
    P=J.T@J
    for a,b in product(range(adim),repeat=2):
        E=np.zeros_like(J);E[a,b]=1
        twice=2*J@E@J.T-P@E-E@P
        if a!=b:check(not np.any(np.diag(twice)),'active-sector exact arbitrary-coherence closure')
        else:Q[:,a]+=float(rate_q)*np.diag(twice)/2
    JJ=np.kron(J,np.eye(2));PP=JJ.T@JJ;identity=np.eye(fdim)
    superop+=float(rate_q)*(np.kron(JJ.conj(),JJ)-0.5*np.kron(identity,PP)-0.5*np.kron(PP.T,identity))
psi=np.array([complex((a+1)*(s+1),(-1)**a*(s+2)) for a in range(adim) for s in range(2)])
rho=np.outer(psi,psi.conj())/np.vdot(psi,psi).real
rho4=rho.reshape(adim,2,adim,2)
rho_active=np.trace(rho4,axis1=1,axis2=3);rho_inert=np.trace(rho4,axis1=0,axis2=2)
check(np.linalg.norm(rho-np.kron(rho_active,rho_inert))>1e-3,'readout fixture has correlated inactive factors')
check(np.linalg.norm(rho_active-np.diag(np.diag(rho_active)))>1e-3,'readout fixture retains active coherences')
pop=np.diag(rho_active).real
count_A=np.array([bit(z,0)+bit(z,1) for z in active_states])
projectors=[np.kron(np.diag((count_A==n).astype(float)),np.eye(2)) for n in range(3)]
branches=[(rho,pop)]
for dt in [0.17,0.29,0.43]:
    E=expm(dt*superop);Pclassic=expm(dt*Q);next_branches=[]
    for density,probability in branches:
        evolved=(E@density.reshape(-1,order='F')).reshape(fdim,fdim,order='F')
        evolved_classic=Pclassic@probability
        for n,P in enumerate(projectors):
            post=P@evolved@P
            next_branches.append((post,evolved_classic*(count_A==n)))
    branches=next_branches
readout_error=max(abs(np.trace(density).real-sum(probability)) for density,probability in branches)
check(readout_error<2e-12,'actual quantum selective count-instrument joint law')
check(abs(sum(np.trace(density).real for density,_ in branches)-1)<2e-12,'actual quantum readout joint law normalization')
print('Floating quantum instrument control: 27 three-time outcomes, 6 active states plus a correlated inert qubit; maximum joint probability error =',readout_error)

# Exact delta-pole arithmetic derived from the displayed resource formulas.
# All constants are positive and independent of delta; logarithms are tracked
# separately. This control verifies substitution, not the parent PDE theorem.
delta=sp.symbols('delta',positive=True)
def pole(expr):
    return max(-term.as_powers_dict().get(delta,0) for term in sp.expand(expr).as_ordered_terms())
Nm=delta**-19;wm=delta**6;em=delta**2;bm=delta**-1;cm=delta**-2
local_hop=Nm**2*wm*bm/(6*em);local_collision=8*Nm**2*wm*cm
capacity_pole=max(sp.Integer(19),pole((local_hop+local_collision)/delta**2))
Km=delta**(-capacity_pole);Sm=delta**(-capacity_pole/2)
hop_exit=54*Km*bm/(wm*em)
collision_exit=Km**2*cm/(Nm*wm**2)
mix_comparison=Km*(8*Sm+19)
mix_time=mix_comparison*Nm
fast_rate=2*mix_time*(hop_exit+collision_exit)*(1+hop_exit+collision_exit)/delta**2
resource_poles={'local_hop':pole(local_hop),'local_collision':pole(local_collision),'K':capacity_pole,'S':capacity_pole/2,'volume':pole(delta**-6*Sm**3),'hop_exit':pole(hop_exit),'collision_exit':pole(collision_exit),'comparison':pole(mix_comparison),'mix_time':pole(mix_time),'fast_rate':pole(fast_rate),'active_sites':pole(delta**-6*Km),'individual_hop':pole(Km*bm/em),'individual_collision':pole(Km**2*cm/(Nm*wm)),'log_coefficient':6+capacity_pole}
expected_poles={'local_hop':35,'local_collision':34,'K':37,'S':sp.Rational(37,2),'volume':sp.Rational(123,2),'hop_exit':46,'collision_exit':69,'comparison':sp.Rational(111,2),'mix_time':sp.Rational(149,2),'fast_rate':sp.Rational(429,2),'active_sites':43,'individual_hop':40,'individual_collision':63,'log_coefficient':43}
check(resource_poles==expected_poles,'stopped nonlinear resource exponent substitution')
print('Exact stopped nonlinear resource poles:',json.dumps({k:str(v) for k,v in resource_poles.items()},sort_keys=True))

# Finite stopped-capacity choices with certified rational enclosures for pi
# and alpha_*. Algebraic upper bounds may enlarge K but keep the same theorem.
pi_lower=Fraction('3.14159265358979323846264338327950288419716939937510')
pi_upper=pi_lower+Fraction(1,10**50)
def arctan_bounds(q,terms):
    assert terms%2==0
    lower=sum(((-1)**j*q**(2*j+1)/(2*j+1) for j in range(terms)),Fraction(0))
    return lower,lower+q**(2*terms+1)/(2*terms+1)
a0,a1=arctan_bounds(Fraction(1,5),40);b0,b1=arctan_bounds(Fraction(1,239),12)
# Machin's identity, certified by the tangent-addition rational calculation.
tan2=2*Fraction(1,5)/(1-Fraction(1,25));tan4=2*tan2/(1-tan2**2)
check((tan4-Fraction(1,239))/(1+tan4*Fraction(1,239))==1,'Machin tangent identity')
check(pi_lower<=16*a0-4*b1 and 16*a1-4*b0<=pi_upper,'rational pi enclosure from alternating series')
alpha=sp.Rational(-4579,1072)+sp.Rational(3,1072)*sp.sqrt(7614177)
check(bool(1<alpha) and bool(alpha<4),'fixed algebraic collision rate enclosure')
T4_upper=T4parts[0]+4*T4parts[1]
for accuracy in [Fraction(1),Fraction(1,2),Fraction(1,4)]:
    def odd_ceiling(x):
        value=max(3,ceil_fraction(x))
        return value if value%2 else value+1
    grid=odd_ceiling(2*pi_upper/accuracy**2)
    check(grid==odd_ceiling(2*pi_lower/accuracy**2),'certified odd-grid ceiling')
    check(grid>=2*pi_upper/accuracy**2 and grid-2<2*pi_lower/accuracy**2,'odd-grid lower bound and minimality')
    total=max(2,ceil_fraction(accuracy**-19));weight=Fraction(1,grid**3)
    mesh_lower=2*pi_lower/grid
    local_upper=total**2*weight*(1/(6*accuracy*mesh_lower)+8*T4_upper/accuracy**2)
    required_local=max(total,2,ceil_fraction(2*local_upper/accuracy**2))
    side_local=max(1152,isqrt(2*(required_local+1)))
    if side_local**2<2*(required_local+1):side_local+=1
    cap_local=side_local**2//2
    check(cap_local>=required_local,'stopped resource capacity and initial-law support')
    check(local_upper/cap_local<=accuracy**2/2,'stopped resource capacity allocation')
    check(4*side_local+1259<=cap_local<=4*side_local+104+(side_local-6)*(side_local-1),'stopped resource literal geometry interval')
print('Exact stopped-capacity choices: delta=1,1/2,1/4; certified odd grid, full multinomial support, geometric interval, and capacity error <= delta^2/2.')

print('Coverage: local matrix units; all small port fibers; exact finite generator; two-time floating count law; full periodic-port tile; rational variance forms; tree routes; spectral/TV examples; epsilon choices; stopped capacity; quantum count instruments; nonlinear resource substitutions.')
print('Boundary: supplied local GKSL, tensor carrier, role pattern, clock and preparation; four-site collision support; nonlinear corollary conditional on the supplied particle theorem; no native Record law asserted.')
print('TOTAL: PASS='+str(checks)+' FAIL=0')
print('Elapsed seconds:',format(perf_counter()-START,'.3f'))
print('Runner SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
