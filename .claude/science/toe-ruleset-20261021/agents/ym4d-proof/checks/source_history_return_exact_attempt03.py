"""Author diagnostics for H9/H14/H23. Exact arithmetic, not a YM simulation."""
from fractions import Fraction as F
from itertools import product, combinations
from functools import lru_cache
from math import factorial
from dataclasses import dataclass
from pathlib import Path
import hashlib, json, time
started = time.monotonic()
checks, controls = {}, {}

def ck(name, condition, control=False):
    (controls if control else checks)[name] = bool(condition)
    assert condition, name

@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)
    def __add__(self, other):
        other = oq(other); return Q(self.a+other.a, self.b+other.b)
    __radd__ = __add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self, other): return self+-oq(other)
    def __rsub__(self, other): return oq(other)+-self
    def __mul__(self, other):
        other=oq(other)
        return Q(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self, other):
        other=oq(other); d=other.a**2+other.b**2
        return Q((self.a*other.a+self.b*other.b)/d,
                 (self.b*other.a-self.a*other.b)/d)
    def __rtruediv__(self, other): return oq(other)/self
    def __pow__(self,n):
        if n<0:return (Q(F(1))/self)**(-n)
        out=Q(F(1)); z=self
        while n:
            if n%2:out=out*z
            z=z*z; n//=2
        return out

def oq(x):return x if isinstance(x,Q) else Q(F(x))
def mul(xs):
    out=1
    for x in xs:out=out*x
    return out

def digestq(q):
    q=oq(q)
    return hashlib.sha256(f'{q.a.numerator}/{q.a.denominator};{q.b.numerator}/{q.b.denominator}'.encode()).hexdigest()

# Four interiors, two good and two bad states. Actual kernels in this
# finite fixture are normalized two-output rational probability kernels.
# The fixture tests identities only, not the nonabelian Yang--Mills price.
V=(0,1,1)
vertex=tuple(range(4))
plaquettes=[(i,) for i in vertex]+[(i,i+1) for i in range(3)]
z=Q(F(19,20),F(1,20)); z_external=Q(F(21,20),F(-1,40))
vacuum=F(7,5)
source_external=z_external**2

def energy(p,x):
    return x[p[0]]**2 if len(p)==1 else (x[p[0]]-x[p[1]])**2

def pweight(p,x):return F(1,2)**energy(p,x)

def kernel(i,x,normalized=True):
    left,right=x[i:i+2]
    n0=1+left+right; n1=2+left+2*right
    return F((n0,n1)[V[i]],n0+n1 if normalized else 1)

def source_p(p,x):return z**energy(p,x)

def full0(x):return vacuum*mul(pweight(p,x) for p in plaquettes)*mul(kernel(i,x) for i in range(3))
def fullsource(x):return source_external*mul(source_p(p,x) for p in plaquettes)

def comps(B, radius=2):
    unseen=set(B); out=[]
    while unseen:
        root=min(unseen); unseen.remove(root); comp={root}; stack=[root]
        while stack:
            i=stack.pop()
            for j in tuple(unseen):
                if abs(i-j)<=radius:unseen.remove(j);comp.add(j);stack.append(j)
        out.append(tuple(sorted(comp)))
    return tuple(sorted(out))

subsets=[tuple(i for i in vertex if mask>>i&1) for mask in range(16)]
polys=[Y for Y in subsets if Y and len(comps(Y))==1]
collections=sorted({comps(B) for B in subsets})

def collar(Y):return {j for i in Y for j in vertex if abs(i-j)<=1}
def allowed(Y,Z):return min(abs(i-j) for i in Y for j in Z)>=3

def h(Y,x):return len(Y)<=2 and sum(x[i] for i in collar(Y)-set(Y))%2==0

def local0(Y,x,normalized=True):
    return mul(pweight(p,x) for p in plaquettes if set(p)&set(Y))*mul(
        kernel(i,x,normalized) for i in range(3) if set((i,i+1))&set(Y))

def local_source(Y,x):return mul(source_p(p,x) for p in plaquettes if set(p)&set(Y))
def replace(x,Y,values):
    v=list(x)
    for i,a in zip(Y,values):v[i]=a
    return tuple(v)

@lru_cache(None)
def den(Y,x):
    return sum((local0(Y,replace(x,Y,values)) for values in product((0,1),repeat=len(Y))),F(0))
@lru_cache(None)
def num(Y,x,normalized=True):
    return sum((local0(Y,y,normalized)*local_source(Y,y)
                for values in product((2,3),repeat=len(Y))
                for y in [replace(x,Y,values)]),Q())

def ty(Y,x,compensate=True,correct_reference=True,normalized=True):
    ref=x if correct_reference else (0,0,0,0)
    return num(Y,x,normalized)/den(Y,ref)/(local_source(Y,x) if compensate else 1)

states=list(product(range(4),repeat=4)); sea=list(product((0,1),repeat=4))
Zcut=sum((full0(x) for x in sea),F(0))
Z=sum((full0(x)*fullsource(x) for x in states),Q())
ck('all_local_zero_source_denominators_positive',all(den(Y,x)>0 for Y in polys for x in sea))
ck('collections_biject_bad_sets',len(collections)==16 and len({tuple(sorted(i for Y in G for i in Y)) for G in collections})==16)
ck('disjoint_collars_for_compatible_components',all(not(collar(Y)&collar(Z)) for G in collections for Y,Z in combinations(G,2)))

# Exact source-dressed gas versus full direct summation.
def return_rhs(compensate=True,correct_reference=True,normalized=True):
    return sum((full0(x)*fullsource(x)*sum((mul(ty(Y,x,compensate,correct_reference,normalized) for Y in G)
                                          for G in collections),Q()) for x in sea),Q())
rhs=return_rhs()
ck('direct_raw_sum_equals_compensated_return',rhs==Z)
ck('remove_compensator_rejected',return_rhs(False)!=Z,True)
ck('wrong_frozen_boundary_reference_rejected',return_rhs(True,False)!=Z,True)
ck('drop_local_kernel_normalizer_rejected',return_rhs(True,True,False)!=Z,True)
ck('drop_external_source_only_factor_rejected',rhs/source_external!=Z,True)
ck('drop_reference_vacuum_factor_rejected',rhs/Zcut!=Z/(Zcut/vacuum),True)

# Actual failure history classification before replacement versus the
# independently collected failure/success gas at the sea configuration.
def failure(x):
    return tuple(Y for Y in comps(i for i in vertex if x[i]>=2) if not h(Y,x))
direct_hist={G:Q() for G in collections}
for x in states:direct_hist[failure(x)]+=full0(x)*fullsource(x)
return_hist={G:Q() for G in collections}
for x in sea:
    a={Y:ty(Y,x) if h(Y,x) else Q() for Y in polys}
    f={Y:Q() if h(Y,x) else ty(Y,x) for Y in polys}
    for Fset in collections:
        fs=mul(f[Y] for Y in Fset)
        good=sum((mul(a[Y] for Y in G) for G in collections
                  if all(allowed(Y,Z) for Y in G for Z in Fset)),Q())
        return_hist[Fset]+=full0(x)*fullsource(x)*fs*good
ck('all_failure_history_integrals_match',direct_hist==return_hist)
ck('failure_histories_partition_full_raw_integral',sum(direct_hist.values(),Q())==Z)
ck('dropping_failure_complement_rejected',return_hist[()]!=Z,True)
impossible_history=((0,),(1,))
ck('zero_mass_histories_retained_as_zero',sum((full0(x)*fullsource(x)*int(failure(x)==impossible_history) for x in states),Q())==Q() and all(failure(x)!=impossible_history for x in states))

# Bounded correlated Xi retained in the joint replaced interior integral.
def Xi(x):return int(x[0]==x[3])
Zxi=sum((full0(x)*fullsource(x)*Xi(x) for x in states),Q())
def replacement_sum(read_replaced=True):
    total=Q()
    for x in sea:
        inside=Q()
        for B in subsets:
            G=comps(B)
            integr=Q()
            for values in product((2,3),repeat=len(B)):
                y=replace(x,B,values)
                integr+=mul(local0(Y,y)*local_source(Y,y) for Y in G)*Xi(y if read_replaced else x)
            inside+=integr/mul(den(Y,x)*local_source(Y,x) for Y in G)
        total+=full0(x)*fullsource(x)*inside
    return total
ck('joint_hard_history_replacement_matches',replacement_sum()==Zxi)
ck('read_history_on_sea_instead_of_replaced_links_rejected',replacement_sum(False)!=Zxi,True)
xx=(0,0,1,0); BB=(0,3)
joint=sum((mul(local0(Y,y)*local_source(Y,y) for Y in comps(BB))*Xi(y)
           for vals in product((2,3),repeat=2) for y in [replace(xx,BB,vals)]),Q())
product_event=sum((mul(local0(Y,y)*local_source(Y,y) for Y in comps(BB))*int(y[0]==2 and y[3]==2)
           for vals in product((2,3),repeat=2) for y in [replace(xx,BB,vals)]),Q())
ck('correlated_history_replaced_by_product_event_rejected',joint!=product_event,True)
# A selector reading an integrated neighbour cannot be evaluated on the sea.
bad_original=(2,3,0,0); good_sea=(0,0,0,0)
ck('overlapping_unmerged_collar_selector_control',not allowed((0,),(1,)) and bool(collar((0,))&{1}) and h((0,),bad_original)!=h((0,),good_sea),True)
ck('merging_overlapping_replacements_preserves_selector',h((0,1),bad_original)==h((0,1),good_sea))
# A complex numerator may vanish: that is not a singularity of the new reference.
iunit=Q(F(0),F(1)); bad_num=1+iunit**2
ck('zero_complex_history_numerator_allowed',bad_num==Q() and (2+bad_num)/2==Q(F(1)))

# Source support is a property of the exact factor allocation, not a
# background substitution. No local density factor reads separated interiors.
ck('density_factor_allocation_covers_once',all(
    all(sum(bool(set(p)&set(Y)) for Y in G)<=1 for p in plaquettes)
    and all(sum(bool(set((i,i+1))&set(Y)) for Y in G)<=1 for i in range(3))
    for G in collections))
ck('source_stencils_inside_actual_collars',all(set(p)<=collar(Y) for Y in polys for p in plaquettes if set(p)&set(Y)))

# Independent formal connected-graph calculation for a three-polymer path.
# Z=1+a+b+c+ac; supports are {0,1},{1,2},{2,3}.
SUP=({0,1},{1,2},{2,3}); order=4

def pmul(A,B):
    C={}
    for x,v in A.items():
        for y,w in B.items():
            z=tuple(a+b for a,b in zip(x,y))
            if sum(z)<=order:C[z]=C.get(z,F(0))+v*w
    return {k:v for k,v in C.items() if v}
xpoly={(1,0,0):F(1),(0,1,0):F(1),(0,0,1):F(1),(1,0,1):F(1)}
power={(0,0,0):F(1)}; logcoef={}
for k in range(1,order+1):
    power=pmul(power,xpoly)
    for e,v in power.items():logcoef[e]=logcoef.get(e,F(0))+F((-1)**(k+1),k)*v
logcoef={e:v for e,v in logcoef.items() if v}

def ursell(tup):
    n=len(tup)
    if n==1:return 1
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if SUP[tup[i]]&SUP[tup[j]]]
    out=0
    for bits in range(1<<len(edges)):
        selected=[edge for k,edge in enumerate(edges) if bits>>k&1]
        seen={0}
        for _ in range(n):
            for i,j in selected:
                if i in seen or j in seen:seen.update((i,j))
        if len(seen)==n:out+=(-1)**len(selected)
    return out
coef={}; union_coefs={}
for n in range(1,order+1):
    for tup in product(range(3),repeat=n):
        phi=ursell(tup)
        if not phi:continue
        e=tuple(tup.count(i) for i in range(3)); val=F(phi,factorial(n))
        coef[e]=coef.get(e,F(0))+val
        X=frozenset().union(*(SUP[i] for i in tup))
        union_coefs[X,e]=union_coefs.get((X,e),F(0))+val
coef={e:v for e,v in coef.items() if v}
ck('log_gas_matches_connected_graphs_through_degree_four',coef==logcoef)
ck('all_cluster_unions_connected',all(max(X)-min(X)+1==len(X) for X,e in union_coefs))
ck('remote_source_connector_coefficient',coef[(1,1,1)]==1 and coef.get((1,0,1),0)==0)
ck('drop_remote_connector_rejected',coef[(1,1,1)]!=coef.get((1,0,1),0),True)
O={0,1}
left={e:v for (X,e),v in union_coefs.items() if X<=O and v}
right={e:v for (X,e),v in union_coefs.items() if X<=set(range(4))-O and v}
cross={}
for (X,e),v in union_coefs.items():
    if X&O and X-O:cross[e]=cross.get(e,F(0))+v
reconstructed={}
for A in (left,right,cross):
    for e,v in A.items():reconstructed[e]=reconstructed.get(e,F(0))+v
reconstructed={e:v for e,v in reconstructed.items() if v}
ck('boundary_cluster_cancellation_exact',reconstructed==coef)
ck('crossing_clusters_meet_inner_boundary',all(1 in X for (X,e),v in union_coefs.items() if v and X&O and X-O))
without_cross=dict(left)
for ee,vv in right.items():without_cross[ee]=without_cross.get(ee,F(0))+vv
ck('drop_boundary_polymers_rejected',without_cross!=coef,True)
# Root counting threshold checked in rationals. Written proof handles all orders.
A0=624**2; rq=F(1,1000*A0); dq=81*rq/(1-A0*rq)
ck('explicit_root_threshold_nonempty',A0*rq<1 and dq<F(1,4))
ck('geometric_animal_majorant_matches_partial_sum',sum(81*A0**(m-1)*rq**m for m in range(1,8))==dq*(1-(A0*rq)**7))

out={'schema':'source-history-author-exact-v1','claim_scope':'Finite rational fixture and formal graph checks; not a proof of YM sea averaging or physical mass gap',
     'checks':checks,'negative_controls':controls,'counts':{'checks':len(checks),'negative_controls':len(controls)},
     'states':len(states),'sea_states':len(sea),'compatible_collections':len(collections),
     'raw_integral_exact_digest':digestq(Z),'history_integral_exact_digest':digestq(Zxi),
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'elapsed_seconds':time.monotonic()-started,'all_pass':True}
print(json.dumps(out,indent=2))
