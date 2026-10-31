#!/usr/bin/env python3
"""Independent controls; written before opening the author runner. No author imports."""
from fractions import Fraction as F
from itertools import product, combinations, permutations
from collections import Counter, deque
import hashlib, json, math, platform, sys
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 70
checks = []
observations = {}

def check(label, ok, evidence=None):
    checks.append({'label':label, 'passed':bool(ok), 'evidence':evidence})

def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def transpose(a):
    return list(map(list, zip(*a)))

def mm(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]

def madd(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def det(a):
    """Direct rational elimination with row pivots; no Schur formula."""
    a=[list(map(F,row)) for row in a]
    answer=F(1)
    for c in range(len(a)):
        pivot=next((i for i in range(c,len(a)) if a[i][c]),None)
        if pivot is None: return F(0)
        if pivot!=c:
            a[c],a[pivot]=a[pivot],a[c]
            answer=-answer
        q=a[c][c]
        answer*=q
        for i in range(c+1,len(a)):
            ratio=a[i][c]/q
            for j in range(c+1,len(a)):
                a[i][j]-=ratio*a[c][j]
    return answer

def mpx(x):
    return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(x)

def block_precision(b):
    p,q=len(b),len(b[0])
    out=ident(p+q)
    for i in range(p):
        for j in range(q): out[i][p+j]=out[p+j][i]=F(b[i][j])
    return out

# Rational elimination versus Wick moments and actual Gaussian quadrature.
t=F(1,64)
for d in (1,2,3,7,12):
    b=[[t*int(i==j) for j in range(d)] for i in range(d)]
    determinant=det(block_precision(b))
    check(f'direct_det_rank_{d}', determinant==(1-t*t)**d, str(determinant))
    trace2=sum(x*x for row in b for x in row)*2
    check(f'trace_rank_{d}', trace2==2*d*t*t, str(trace2))
check('missing_rank_mutation_rejected', (1-t*t)**7 != (1-t*t))

# Conditional integration E_y exp(-t*x*y)=exp(t^2*x^2/2), then a scalar integral.
for x in (mp.mpf(0),mp.mpf('0.7'),mp.mpf('-2.3')):
    z=mp.quad(lambda y: mp.exp(-y*y/2-mpx(t)*x*y)/mp.sqrt(2*mp.pi),[-mp.inf,0,mp.inf])
    check(f'conditional_gaussian_integral_{x}', mp.almosteq(z,mp.exp(mpx(t)**2*x*x/2)))
for s in (mp.mpf('0'),mp.mpf('0.125'),mp.mpf('0.6')):
    integral=mp.quad(lambda x:mp.exp(-(1-s*s)*x*x/2)/mp.sqrt(2*mp.pi),[-mp.inf,0,mp.inf])
    check(f'normalized_gaussian_integral_{s}',mp.almosteq(mp.sqrt(1-s*s)*integral,1))
    if s:
        check(f'omitted_prefactor_mutation_{s}',abs(integral-1)>mp.mpf('0.001'))
        check(f'wrong_schur_sign_mutation_{s}',abs(mp.sqrt(1+s*s)*integral-1)>mp.mpf('0.001'))
        check(f'lost_half_power_mutation_{s}',abs((1-s*s)*integral-1)>mp.mpf('0.001'))

# Fixed-rank and fixed-HS passing controls, without forming huge matrices.
observations['rank_growth']=[{'d':d,'minus_log_at_zero':str(-d*mp.log1p(-mpx(t)**2)/2)} for d in (1,17,4096,1048576)]
for d in (1,4,16,64):
    c=mp.mpf('0.5')
    nrm=-d*mp.log1p(-c*c/d)/2
    check(f'fixed_hs_budget_{d}',c*c/2<=nrm<=c*c/(2*(1-c*c)))
    check(f'fixed_rank_budget_{d}',det(block_precision([[F(1,5)]+[F(0)]*(d-1)]))==F(24,25))

rectangles=[[[F(1,4),F(1,6),F(-1,8)]],[[F(1,7),F(-1,8),F(1,9)],[F(1,10),F(1,11),F(-1,12)]],[[F(0),F(0)],[F(0),F(0)],[F(0),F(0)]],[[F(3,5)],[F(1,5)],[F(-1,10)]]]
for i,b in enumerate(rectangles):
    p,q=len(b),len(b[0])
    btb=mm(transpose(b),b); bbt=mm(b,transpose(b))
    schur1=[[F(j==k)-btb[j][k] for k in range(q)] for j in range(q)]
    schur2=[[F(j==k)-bbt[j][k] for k in range(p)] for j in range(p)]
    determinant=det(block_precision(b))
    check(f'rectangular_schur_{i}',determinant==det(schur1)==det(schur2))
    hs2=sum((x*x for row in b for x in row),F(0))
    # Frobenius is an independently valid upper bound on the operator norm.
    k2=hs2
    lhs=-mp.log(mpx(determinant))/2
    check(f'rectangular_logdet_bounds_{i}',mpx(hs2)/2-mp.mpf('1e-65')<=lhs<=mpx(hs2/(2*(1-k2)))+mp.mpf('1e-65'))
check('lower_logdet_factor_two_mutation', -mp.log(mp.mpf('0.99'))/2 < mp.mpf('0.01'))
check('upper_logdet_lost_denominator_mutation',-mp.log(mp.mpf('0.75'))/2 > mp.mpf('0.25')/2)

# Trace-zero nonbipartite example, evaluated by determinant elimination, not eigenvalue sum.
ks=[[[F(-1,5),0,0],[0,F(1,10),0],[0,0,F(1,10)]],[[0,F(1,10),F(1,20)],[F(1,10),0,F(-1,15)],[F(1,20),F(-1,15),0]]]
for i,k in enumerate(ks):
    k=[list(map(F,row)) for row in k]
    rho=max(sum(map(abs,row),F(0)) for row in k)
    hs2=sum((x*x for row in k for x in row),F(0))
    val=abs(mp.log(mpx(det(madd(ident(len(k)),k))))/2)
    check(f'general_trace_zero_{i}',val<=mpx(hs2/(4*(1-rho))),'bound uses a symmetric Schur operator majorant')
    if i==0: check('general_lost_denominator_mutation',val>mpx(hs2/4))
no_trace=abs(mp.log(mp.mpf('1.01')))/2
check('trace_zero_hypothesis_is_necessary',no_trace>mp.mpf('0.0001')/(4*(1-mp.mpf('0.01'))))

# Marks computed from an exact determinant polynomial rather than the author's formulas.
z=sp.Symbol('z',real=True)
d0=11
ld=sp.log((1-z*z)**d0)/2
check('source_first_derivative',sp.simplify(sp.diff(ld,z)+d0*z/(1-z*z))==0)
check('source_second_derivative',sp.simplify(sp.diff(ld,z,2)+d0*(1+z*z)/(1-z*z)**2)==0)
check('vacuum_subtraction_does_not_remove_mark',sp.simplify(sp.diff(ld-ld.subs(z,sp.Rational(1,64)),z)-sp.diff(ld,z))==0)

# Noncommuting 2x2 cell blocks. Exact path sum independently compared with full-matrix powers.
r=2; ncell=3
v=F(1,50)
blocks={(0,1):[[v,v],[0,0]],(0,2):[[0,v],[v,0]],(1,2):[[v,0],[v,0]]}
for (i,j),b in list(blocks.items()): blocks[j,i]=transpose(b)
for i in range(ncell): blocks[i,i]=[[F(0)]*r for _ in range(r)]
big=[[F(0)]*(r*ncell) for _ in range(r*ncell)]
for (i,j),b in blocks.items():
    for a in range(r):
        for c in range(r):big[r*i+a][r*j+c]=F(b[a][c])
kappa=max(sum(np.linalg.norm(np.array(blocks[i,j],float),2) for j in range(ncell)) for i in range(ncell))
power=np.eye(r*ncell)
local_sums=np.zeros(ncell)
for order in range(1,29):
    power=power@np.array(big,float)
    for root in range(ncell):
        trace=float(np.trace(power[r*root:r*(root+1),r*root:r*(root+1)]))
        if 2<=order<=6:
            paths=F(0)
            for inner in product(range(ncell),repeat=order-1):
                walk=(root,)+inner+(root,)
                word=ident(r)
                for a,b in zip(walk,walk[1:]):word=mm(word,blocks[a,b])
                paths+=sum(word[i][i] for i in range(r))
            check(f'local_path_trace_{root}_{order}',abs(float(paths)-trace)<1e-15)
        if order>=2:local_sums[root]+=((-1)**(order+1))*trace/(2*order)
check('local_series_global_logdet',abs(sum(local_sums)-float(mp.log(mpx(det(madd(ident(r*ncell),big))))/2))<1e-15)
check('local_cell_budget',all(abs(g)<=r*kappa*kappa/(4*(1-kappa)) for g in local_sums))
check('local_lost_rank_mutation',-8*mp.log1p(-mp.mpf('0.1')**2)/4>mp.mpf('0.1')**2/(4*(1-mp.mpf('0.1'))))

# Exact l1 diameter from all signed projections, and a nearest-neighbor spanning tree.
geometry=[]
for q in (2,3,4,7):
    R=6
    points=list(product(range(0,q*R,R),repeat=4))
    diameter=max(max(sum(a*b for a,b in zip(sign,p)) for p in points)-min(sum(a*b for a,b in zip(sign,p)) for p in points) for sign in product((-1,1),repeat=4))
    seen={points[0]}; queue=deque([points[0]]); tree_edges=[]
    pointset=set(points)
    while queue:
        p=queue.popleft()
        for axis in range(4):
            for step in (-R,R):
                v1=list(p);v1[axis]+=step;v1=tuple(v1)
                if v1 in pointset and v1 not in seen:seen.add(v1);queue.append(v1);tree_edges.append((p,v1))
    tree_length=sum(sum(abs(a-b) for a,b in zip(p,q1)) for p,q1 in tree_edges)
    check(f'grid_diameter_{q}',diameter==4*R*(q-1))
    check(f'grid_tree_length_{q}',tree_length==R*(len(points)-1))
    check(f'grid_diameter_linear_mutation_{q}',diameter<R*(len(points)-1))
    geometry.append({'q':q,'n':len(points),'diameter':diameter,'tree_length':tree_length,'ratio':str(F(diameter,tree_length))})
check('straight_path_passing_control',max(5*i for i in range(17))-min(5*i for i in range(17))==5*(17-1))
observations['geometry']=geometry

# Original-edge plaquette incidence on nondegenerate periodic and open 4D boxes.
def lattice(ell,periodic):
    faces=[]
    def step(x,axis):
        y=list(x);y[axis]+=1
        if periodic:y[axis]%=ell
        elif y[axis]>=ell:return None
        return tuple(y)
    for x in product(range(ell),repeat=4):
        for a,b in combinations(range(4),2):
            xa,xb=step(x,a),step(x,b)
            if xa is not None and xb is not None:faces.append(frozenset(((x,a),(xa,b),(xb,a),(x,b))))
    incidence=Counter(e for f in faces for e in f)
    conflicts={e:set() for e in incidence}
    for face in faces:
        for e in face:conflicts[e].update(face-{e})
    return faces,incidence,conflicts
for ell,periodic in ((3,True),(4,True),(3,False)):
    faces,incidence,conflicts=lattice(ell,periodic)
    check(f'four_distinct_edges_{ell}_{periodic}',all(len(f)==4 for f in faces))
    check(f'six_plaquette_incidence_{ell}_{periodic}',max(incidence.values())==6)
    check(f'conflict_degree_18_{ell}_{periodic}',max(map(len,conflicts.values()))==18)
    selected=[]; remaining=set(conflicts)
    while remaining:
        e=min(remaining);selected.append(e);remaining-=conflicts[e]|{e}
    check(f'greedy_pivot_lower_bound_{ell}_{periodic}',len(selected)>=math.ceil(len(conflicts)/19))

# Exact Z2 Wilson weights: beta=log(2)/2, each positive plaquette contributes 2.
faces=[(0,1,2,3),(3,4,5,6)]
def joint(pivots,exterior):
    raw={}
    for signs in product((-1,1),repeat=len(pivots)):
        state=dict(exterior);state.update(zip(pivots,signs))
        raw[signs]=2**sum(math.prod(state[e] for e in face)==1 for face in faces)
    norm=sum(raw.values())
    return {k:F(v,norm) for k,v in raw.items()}
def factorization_gap(prob):
    m0={s:sum(p for v,p in prob.items() if v[0]==s) for s in (-1,1)}
    m1={s:sum(p for v,p in prob.items() if v[1]==s) for s in (-1,1)}
    return max(abs(p-m0[v[0]]*m1[v[1]]) for v,p in prob.items())
for pivots in ((0,4),(0,1)):
    rest=[e for e in range(7) if e not in pivots]
    gaps=[];expectations=[]
    for ext in product((-1,1),repeat=len(rest)):
        prob=joint(pivots,dict(zip(rest,ext)))
        gaps.append(factorization_gap(prob))
        expectations.append(abs(sum(p*math.prod(v) for v,p in prob.items())))
        check(f'conditional_normalization_{pivots}_{ext}',sum(prob.values())==1)
        for idx in range(2):
            marginal={s:sum(p for v,p in prob.items() if v[idx]==s) for s in (-1,1)}
            check(f'haar_density_minorization_{pivots}_{ext}_{idx}',min(2*p for p in marginal.values())>=F(1,64))
    if pivots==(0,4):
        check('nonsharing_exact_product_all_exteriors',max(gaps)==0)
        check('separately_centered_product_bound',max(expectations)<=(1-F(1,64))**2)
    else:check('shared_plaquette_product_mutation_rejected',max(gaps)>0)
# Conditional product may be lost by integrating the shared nonpivot edge.
pminus=joint((0,4),{1:1,2:1,3:-1,5:1,6:1})
pplus=joint((0,4),{1:1,2:1,3:1,5:1,6:1})
mixture={v:(pminus[v]+pplus[v])/2 for v in pminus}
check('premature_nonpivot_marginalization_mutation',factorization_gap(mixture)>0)
check('beta_zero_endpoint_centered_expectation',sum(F(math.prod(v),4) for v in product((-1,1),repeat=2))==0)

# SU(2) one-link check with six aligned staples and normalized Haar class integral.
for beta in (mp.mpf('0'),mp.mpf('0.3'),mp.mpf('1.1')):
    partition=mp.quad(lambda theta:2/mp.pi*mp.sin(theta)**2*mp.exp(6*beta*mp.cos(theta)),[0,mp.pi])
    mindensity=mp.exp(-6*beta)/partition
    check(f'su2_six_staples_minorization_{beta}',mindensity+mp.mpf('1e-65')>=mp.exp(-12*beta))
    if beta:check(f'oscillation_factor_six_mutation_{beta}',mindensity<mp.exp(-6*beta))

# Exact finite BKAR two-level polynomial identity, integrating ordered edge sectors.
edges=((0,1),(0,2),(1,2)); xx=sp.symbols('x0:6')
def connected_path(forest,i,j):
    stack=[(i,[])];seen={i}
    while stack:
        a,path=stack.pop()
        if a==j:return path
        for e in forest:
            if a in e:
                b=e[0] if e[1]==a else e[1]
                if b not in seen:seen.add(b);stack.append((b,path+[e]))
    return None
forests=[tuple(s) for n in range(3) for s in combinations(edges,n)]
def jungle_value(poly):
    answer=sp.S(0)
    for f2 in forests:
        for n1 in range(len(f2)+1):
            for f1 in combinations(f2,n1):
                derivative=poly
                for e in f1:derivative=sp.diff(derivative,xx[edges.index(e)])
                for e in f2:
                    if e not in f1:derivative=sp.diff(derivative,xx[3+edges.index(e)])
                if derivative==0:continue
                for ordered in permutations(f2):
                    params=sp.symbols('h0:'+str(len(ordered)))
                    ranks={e:j for j,e in enumerate(ordered)}
                    subs={}
                    for level,fprev,fcur in ((0,(),f1),(1,f1,f2)):
                        for j,e in enumerate(edges):
                            if connected_path(fprev,*e) is not None:val=sp.S(1)
                            else:
                                path=connected_path(fcur,*e)
                                if path is None:val=sp.S(0)
                                else:val=params[min(ranks[b] for b in path if b not in fprev)]
                            subs[xx[3*level+j]]=val
                    integrand=derivative.subs(subs)
                    for j,h in enumerate(params):integrand=sp.integrate(integrand,(h,0,params[j+1] if j+1<len(params) else 1))
                    answer+=integrand
    return sp.simplify(answer)
for i,poly in enumerate((xx[0]*xx[2]*xx[4]**2,xx[0]*xx[1]*xx[2]*xx[3],(1+xx[0]*xx[4])*(2+xx[2]*xx[3]+xx[5]**2),xx[0]**2*xx[3]**3)):
    check(f'two_level_jungle_polynomial_{i}',jungle_value(poly)==poly.subs({x:1 for x in xx}))

# Convex block restrictions prove positivity; check a nontrivial exact Gram matrix.
gram=sp.Matrix([[1,0,1],[0,2,1],[1,1,0],[1,-1,2]])
cov=gram*gram.T+sp.eye(4)
forest=((0,1),(1,2),(1,3));weights={forest[0]:sp.Rational(1,5),forest[1]:sp.Rational(4,5),forest[2]:sp.Rational(2,5)}
interpolated=sp.zeros(4)
for i in range(4):
    for j in range(4):interpolated[i,j]=cov[i,j]*(1 if i==j else min(weights[e] for e in connected_path(forest,i,j)))
levels=sorted(set([sp.S(0),sp.S(1)]+list(weights.values())))
convex=sp.zeros(4)
for a,b in zip(levels,levels[1:]):
    threshold=(a+b)/2
    active=tuple(e for e in forest if weights[e]>=threshold)
    convex+=(b-a)*sp.Matrix(4,4,lambda i,j:cov[i,j] if connected_path(active,i,j) is not None else 0)
check('bkar_convex_block_identity',convex==interpolated)
check('bkar_positivity_principal_minors',all(interpolated.extract(s,s).det()>0 for k in range(1,5) for s in combinations(range(4),k)))
bad=sp.Matrix([[1,1,0],[1,1,1],[0,1,1]])
check('positivity_lost_transitive_links_mutation',bad.det()<0)

failed=[c for c in checks if not c['passed']]
out={'scope':'Independent finite controls plus primary-text proof review; no Yang-Mills continuum theorem','author_runner_read_before_implementation':False,'runtime':{'python':sys.version,'platform':platform.platform(),'sympy':sp.__version__,'numpy':np.__version__,'mpmath':mp.__version__},'checks':checks,'checks_total':len(checks),'checks_passed':len(checks)-len(failed),'failed':failed,'observations':observations,'limits':['No actual Karcher optical matrix instantiated','No actual many-pivot Wilson reference activity instantiated','No full marked polymer or continuum estimate','No whole-paper audit','Finite forest identities do not verify model-specific amplitudes']}
print(json.dumps(out,indent=2))
sys.exit(bool(failed))
