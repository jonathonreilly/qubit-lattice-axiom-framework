"""Independent exact Fubini/history and actual-collar cluster diagnostics."""
from fractions import Fraction as F
from itertools import product, combinations, combinations_with_replacement
from math import factorial
from functools import lru_cache
from dataclasses import dataclass
import json,time

start=time.monotonic();checks={};controls={};data={}
def req(n,p): checks[n]=bool(p);assert p,n
def neg(n,p): controls[n]=bool(p);assert p,n

@dataclass(frozen=True)
class C:
    r:F=F(0)
    i:F=F(0)
    def __add__(self,o):
        o=cc(o);return C(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.i)
    def __sub__(self,o):return self+-cc(o)
    def __rsub__(self,o):return cc(o)+-self
    def __mul__(self,o):
        o=cc(o);return C(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=cc(o);d=o.r*o.r+o.i*o.i;return self*C(o.r/d,-o.i/d)
    def __rtruediv__(self,o):return cc(o)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        z=C(F(1))
        for _ in range(n):z=z*self
        return z
    def out(self):return [str(self.r),str(self.i)]
def cc(x):return x if isinstance(x,C) else C(F(x))
def prod(xs):
    z=cc(1)
    for x in xs:z=z*x
    return z

polys=(frozenset([0]),frozenset([1]),frozenset([0,1]),frozenset([2]))
fsupport=(frozenset([0]),frozenset([1]),frozenset([2]),frozenset([0,1]),frozenset())
sources=(C(F(5,6),F(1,7)),C(F(8,9),F(-1,11)),C(F(7,8),F(1,13)),C(F(11,12),F(1,17)),C(F(13,14),F(-1,19)))

def weight(j,x,b,no_norm=False):
    if j<3:
        # A conditional coarse kernel normalized under uniform b=0,1.
        k=F(2*(2+b+x[j]),1 if no_norm else 5+2*x[j])
        return k*F(1,j+2)**x[j]
    if j==3:return F(3+x[0]+2*x[1]+b,7+x[0]+x[1])
    return F(1,2+b)
def energy(j,x,b):return x[j] if j<3 else x[0]*x[1]+x[0] if j==3 else b+1
def sf(j,x,b,src=sources):return src[j]**energy(j,x,b)
def allw(x,b,src=sources):return prod(weight(j,x,b)*sf(j,x,b,src) for j in range(5))
def baseline(x,b):return prod(weight(j,x,b) for j in range(5))
def factors(Y):return [j for j,S in enumerate(fsupport) if S&Y]
def replaced(x,Y,vals):
    q=list(x)
    for i,v in zip(sorted(Y),vals):q[i]=v
    return tuple(q)

@lru_cache(None)
def local(Y,x,b,kind,src=sources,no_norm=False):
    ans=cc(0)
    for vals in product([0,1] if kind=='D' else [2],repeat=len(Y)):
        q=replaced(x,Y,vals)
        ans+=prod(weight(j,q,b,no_norm)*(1 if kind=='D' else sf(j,q,b,src)) for j in factors(Y))
    return ans/(3**len(Y))
def comp(B):
    ans=[]
    q=B&{0,1}
    if q:ans.append(frozenset(q))
    if 2 in B:ans.append(frozenset([2]))
    return tuple(ans)
def h(Y,x,b,broken=False):
    if len(Y)>1:return 0
    if Y==frozenset([2]):v=(b==0)
    else:
        other=next(iter({0,1}-Y));v=(b+x[other]<=1)
    if broken:v=v and all(x[i]==0 for i in Y)
    return int(v)
def activity(Y,x,b,src=sources,mutation=''):
    Fs=prod(sf(j,x,b,src) for j in factors(Y))
    numerator=local(Y,x,b,'N',src,mutation=='normalizer')
    denominator=local(Y,x,b,'D',sources,False)
    dress=1 if mutation=='omit' else Fs if mutation=='sign' else 1/Fs
    return dress*numerator/denominator

allB=[frozenset(j for j in range(3) if mask>>j&1) for mask in range(8)]
states=list(product(range(3),repeat=3));sea=list(product([0,1],repeat=3))
Z0=sum((baseline(x,b)/54 for b in range(2) for x in sea),cc(0))
req('positive_common_zero_source_reference',Z0.i==0 and Z0.r>0)
req('normalized_coarse_kernel',all(sum(weight(j,x,b)/F(1,j+2)**x[j] for b in [0,1])/2==1 for x in states for j in range(3)))

def raw(Xi):return sum((allw(x,b)*Xi(x,b)/54 for b in range(2) for x in states),cc(0))
def repl(B,x,b,Xi,mutation=''):
    cs=comp(B)
    pre=prod((1 if mutation=='omit' else prod(sf(j,x,b) for j in factors(Y)) if mutation=='sign' else 1/prod(sf(j,x,b) for j in factors(Y)))/local(Y,x,b,'D') for Y in cs)
    ans=cc(0)
    for vals in product([2],repeat=len(B)):
        q=replaced(x,B,vals)
        ans+=prod(weight(j,q,b,mutation=='normalizer')*sf(j,q,b) for Y in cs for j in factors(Y))*Xi(x if mutation=='sea_history' else q,b)
    return pre*ans/(3**len(B))
def returned(Xi,mutation=''):
    return sum((baseline(x,b)*prod(sf(j,x,b) for j in range(5))*sum((repl(B,x,b,Xi,mutation) for B in allB),cc(0))/54 for b in range(2) for x in sea),cc(0))

Xis=[lambda x,b:1,lambda x,b:(2+b)*int((x[0]+x[2])%3==x[1]),lambda x,b:int(x[0]==3),lambda x,b:C(F(x[0]+2*x[2]),F(b-x[1]))]
for i,Xi in enumerate(Xis):req(f'joint_replacement_Xi{i}',raw(Xi)==returned(Xi))
req('zero_mass_history_retained',raw(Xis[2])==cc(0))
for mutation in ['omit','sign','normalizer','sea_history']:
    neg('replacement_mutation_'+mutation,raw(Xis[1])!=returned(Xis[1],mutation))
neg('product_history_substitution',raw(Xis[1])!=raw(lambda x,b:(2+b)*int(x[0]==x[1])*int(x[2]==x[1])))
neg('omit_common_reference',raw(Xis[0])!=returned(Xis[0])/Z0)

def compatible(A,B):return not (A&B) and not (bool(A&{0,1}) and bool(B&{0,1}))
collections=[tuple(polys[j] for j in range(4) if mask>>j&1) for mask in range(16)
             if all(compatible(polys[i],polys[j]) for i,j in combinations([k for k in range(4) if mask>>k&1],2))]
def gas(Fail,x,b,broken=False):
    return sum((prod(h(Y,x,b,broken)*activity(Y,x,b) for Y in G) for G in collections if all(compatible(Y,Z) for Y in G for Z in Fail)),cc(0))
def hist(x,b,broken=False):
    B=frozenset(i for i in range(3) if x[i]==2)
    return tuple(Y for Y in comp(B) if not h(Y,x,b,broken))
histvalues={}
for k,Fail in enumerate(collections):
    left=raw(lambda x,b:int(hist(x,b)==Fail))
    right=sum((baseline(x,b)*prod(sf(j,x,b) for j in range(5))*prod((1-h(Y,x,b))*activity(Y,x,b) for Y in Fail)*gas(Fail,x,b)/54 for b in range(2) for x in sea),cc(0))
    req(f'individual_failure_history_{k}',left==right);histvalues[str(k)]=left.out()
req('histories_partition_full_raw',sum((raw(lambda x,b,F_=Fail:int(hist(x,b)==F_)) for Fail in collections),cc(0))==raw(Xis[0]))
wrong_hist=sum((baseline(x,b)*prod(sf(j,x,b) for j in range(5))*gas((),x,b,True)/54 for b in range(2) for x in sea),cc(0))
neg('selector_depends_on_replaced_interior',wrong_hist!=raw(lambda x,b:int(hist(x,b,True)==())))
for B in allB:
    for x in states:
        for b in range(2):
            cs=comp(B)
            req('selector_invariant_for_all_replaced_interiors',all(h(Y,x,b)==h(Y,replaced(x,B,(2,)*len(B)),b) for Y in cs))
remote=list(sources);remote[2]=C(F(2,3),F(2,11));near=list(sources);near[0]=C(F(3,4),F(1,5))
req('remote_original_source_absent',activity(polys[0],(0,1,0),0,tuple(remote))==activity(polys[0],(0,1,0),0))
neg('local_original_source_present',activity(polys[0],(0,1,0),0,tuple(near))!=activity(polys[0],(0,1,0),0))
data['raw_joint_value']=raw(Xis[1]).out();data['common_reference']=Z0.out();data['histories']=histvalues

# Finite connected expansion on actual four-dimensional periodic collars.
T=9
cores=[frozenset([p]) for p in [(0,0,0,0),(2,0,0,0),(4,0,0,0),(6,0,0,0)]]+[frozenset([(1,2,0,0),(3,2,0,0)])]
def collar(Y):return frozenset(tuple((x+s)%T for x,s in zip(p,shift)) for p in Y for shift in product([-1,0,1],repeat=4))
supports=[collar(Y) for Y in cores]
z=[F(1,101),F(-2,103),F(3,107),F(-1,109),F(2,113)]
O=frozenset(p for p in product(range(T),repeat=4) if p[0]<=3)
AF=supports[1];degree=6
def indep_poly(ids):
    out=[F(0)]*(degree+1);out[0]=1
    for k in range(1,len(ids)+1):
        for S in combinations(ids,k):
            if all(not supports[i]&supports[j] for i,j in combinations(S,2)):
                v=F(1)
                for i in S:v*=z[i]
                out[k]+=v
    return out
def polylog(p):
    out=[F(0)]*len(p)
    for n in range(1,len(p)):out[n]=p[n]-sum(F(k,n)*out[k]*p[n-k] for k in range(1,n))
    return out
@lru_cache(None)
def connected(ids,positive=False):
    n=len(ids);adj=[sum(1<<j for j in range(n) if j!=i and supports[ids[i]]&supports[ids[j]]) for i in range(n)]
    total={0:F(1)};conn={}
    for mask in range(1,1<<n):
        ec=sum((adj[i]&mask).bit_count() for i in range(n) if mask>>i&1)//2
        total[mask]=F(2**ec) if positive else F(ec==0)
        root=mask&-mask;c=total[mask];sub=(mask-1)&mask
        while sub:
            if sub&root:c-=conn[sub]*total[mask^sub]
            sub=(sub-1)&mask
        conn[mask]=c
    return conn[(1<<n)-1]
terms=[]
for n in range(1,degree+1):
    for ids in combinations_with_replacement(range(5),n):
        c=connected(ids)
        for i in range(5):c*=z[i]**ids.count(i)/factorial(ids.count(i))
        terms.append((n,ids,c,frozenset().union(*(supports[i] for i in ids)),frozenset().union(*(cores[i] for i in ids))))
def series(pred):return [sum((c for n,ids,c,X,Y in terms if n==d and pred(ids,X,Y)),F(0)) for d in range(degree+1)]
alllog=polylog(indep_poly(range(5)))
req('all_order_mechanism_finite_coefficients_through6',series(lambda ids,X,Y:True)==alllog)
allowed=[i for i in range(5) if not supports[i]&AF]
excludedlog=polylog(indep_poly(allowed))
req('exact_full_collar_exclusion',excludedlog==series(lambda ids,X,Y:not X&AF))
req('excluded_history_log_difference',[a-b for a,b in zip(excludedlog,alllog)]==[-a for a in series(lambda ids,X,Y:bool(X&AF))])
inside=[i for i in range(5) if supports[i]<=O];outside=[i for i in range(5) if not supports[i]&O]
boundary=[a-b-c for a,b,c in zip(alllog,polylog(indep_poly(inside)),polylog(indep_poly(outside)))]
req('two_sided_boundary_cancellation',boundary==series(lambda ids,X,Y:bool(X&O) and not X<=O))
innerboundary={x for x in O if any(tuple((a+(s if j==mu else 0))%T for j,a in enumerate(x)) not in O for mu in range(4) for s in [-1,1])}
req('boundary_crossing_union_hits_inner_boundary',all(bool(X&innerboundary) for n,ids,c,X,Y in terms if c and X&O and not X<=O))
neg('omit_repeated_polymers',series(lambda ids,X,Y:len(set(ids))==len(ids))!=alllog)
neg('use_core_support_in_boundary',series(lambda ids,X,Y:bool(Y&O) and not Y<=O)!=boundary)
neg('use_core_support_in_exclusion',polylog(indep_poly([i for i in range(5) if not cores[i]&cores[1]]))!=excludedlog)
positive_second=sum((connected(ids,True)*z[ids[0]]*z[ids[1]]/(2 if ids[0]==ids[1] else 1) for ids in combinations_with_replacement(range(5),2)),F(0))
neg('wrong_Mayer_edge_sign',positive_second!=alllog[2])
data['cluster_coefficients']=[str(v) for v in alllog];data['full_collar_sizes']=list(map(len,supports));data['cluster_multisets']=len(terms)

# Exact source price and threshold budget, with both independent source legs.
for N,L,rho_factor,lam in product([2,3],[3,5],[F(0),F(1,2)],[0,2]):
    cut=F(1,2);a=cut*cut/(4*N);nP=24*L**3*(L-1);rho=rho_factor*a/(4*nP)
    ae=a-4*rho*nP
    for u in [1,17,10000]:
        combined=-a*u+2*(2*(u*rho+lam)*nP)
        req('two_source_legs_exact_cost',combined==-ae*u+4*lam*nP)
    req('fixed_radius_positive_remainder',ae==a*(1-rho_factor))
neg('drop_compensator_source_cost',(-F(1,8)+4*F(1,1024)*16)!=(-F(1,8)+2*F(1,1024)*16))
Delta=624;A0=Delta*Delta;s0=81;rq=F(1,2*A0+8*s0);dq=s0*rq/(1-A0*rq)
req('explicit_threshold_rooted_budget',A0*rq<1 and dq<=F(1,4))
data['threshold_dq_at_ceiling']=str(dq)

print(json.dumps({'schema':'independent-source-history-identity-cluster-v1','checks':checks,'negative_controls':controls,'data':data,'elapsed_seconds':time.monotonic()-start},indent=2))
