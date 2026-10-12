"""Independent bitstring/exact-matrix checks; no author imports."""
import json
from itertools import product
import sympy as s

I=s.I
rows=[]
def emit(name, ok, **data):
    row=dict(name=name,ok=bool(ok),**data);rows.append(row);print(json.dumps(row),flush=True)
def zero(M):
    return all(s.simplify(v)==0 for v in M.todok().values())
def op(N,j,kind):
    """Literal spin matrices, with site j the jth least-significant bit."""
    d={}
    for b in range(1<<N):
        bit=(b>>j)&1
        if kind=='Z': d[b,b]=1-2*bit
        elif kind=='X': d[b^(1<<j),b]=1
        elif kind=='Y': d[b^(1<<j),b]=I*(1-2*bit)
    return s.SparseMatrix(1<<N,1<<N,d)
def annih(N,j):
    d={}
    for b in range(1<<N):
        if (b>>j)&1: d[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
    return s.SparseMatrix(1<<N,1<<N,d)
def gammas(N):
    out=[]
    for j in range(N):
        a=annih(N,j);out.extend([a+a.H,-I*(a-a.H)])
    return out
def word(N,terms):
    M=s.SparseMatrix.eye(1<<N)
    for j,k in terms:M=M*op(N,j,k)
    return M
def coefficient(M,W):return s.simplify(s.trace(W.H*M)/M.rows)

for Nc in (2,3):
    N=2*Nc; ident=s.SparseMatrix.eye(1<<N);g=gammas(N)
    G=[(g[4*j+r]+g[4*j+2+r])/s.sqrt(2) for j in range(Nc) for r in (0,1)]
    car=[]
    for p in range(2*Nc):
        for q in range(p,2*Nc):car.append(zero(G[p]*G[q]+G[q]*G[p]-(2 if p==q else 0)*ident))
    emit('exact_retained_CAR',all(car),coarse_sites=Nc,pairs=len(car))
    for j in range(Nc):
        l=2*j;actual=-I*G[2*j]*G[2*j+1]
        explicit=(op(N,l,'Z')+op(N,l+1,'Z')-word(N,[(l,'X'),(l+1,'X')])-word(N,[(l,'Y'),(l+1,'Y')]))/2
        emit('D6',zero(actual-explicit),coarse_sites=Nc,site=j)
        bad=explicit+word(N,[(l,'Y'),(l+1,'Y')])/2
        emit('mutation_missing_YY_detected',not zero(actual-bad),coarse_sites=Nc,site=j)
    for j in range(Nc-1):
        l=2*j; actual=-I*G[2*j+1]*G[2*j+2]
        explicit=(word(N,[(l,'X'),(l+1,'Z'),(l+2,'X')])+word(N,[(l,'X'),(l+1,'Z'),(l+2,'Z'),(l+3,'X')])+word(N,[(l+1,'X'),(l+2,'X')])+word(N,[(l+1,'X'),(l+2,'Z'),(l+3,'X')]))/2
        emit('D7',zero(actual-explicit),coarse_sites=Nc,site=j)
    if Nc==3:
        gc,Jc,gf,Jf=s.symbols('gc Jc gf Jf',real=True)
        H=-gf*sum((op(N,j,'Z') for j in range(N)),s.zeros(1<<N))
        H-=Jf*sum((word(N,[(j,'X'),(j+1,'X')]) for j in range(N-1)),s.zeros(1<<N))
        Z=-I*G[2]*G[3]
        df=I*(H*Z-Z*H)
        rc=-2*Jc*((-I*G[1]*G[3])+(I*G[2]*G[4]))
        W=word(N,[(3,'Y'),(4,'Z'),(5,'X')])
        a=coefficient(df,W);b=coefficient(rc,W);c=coefficient(df-rc,W)
        emit('D30_exact_coefficients',a==0 and b==-Jc and c==Jc,fine=str(a),refined_coarse=str(b),difference=str(c))
        emit('mutation_reversed_commutator_detected',s.simplify(-c-Jc)!=0,wrong_coefficient=str(-c))

# JW extension by one site: old gamma pairs must agree, odd gamma must not.
g2=gammas(2);g3=gammas(3)
odd_old=s.kronecker_product(g2[0],s.eye(2))
even_old=s.kronecker_product(g2[0]*g2[3],s.eye(2))
emit('JW_left_endpoint_even_cancels',zero(g3[2]*g3[5]-even_old))
emit('JW_left_endpoint_odd_does_not_cancel',not zero(g3[2]-odd_old))

N=4
true=word(N,[(0,'X'),(1,'Z'),(2,'X')]);bad=word(N,[(0,'X'),(2,'X')]);delta=true-bad
ev=delta.eigenvals()
emit('ancillary_string_exact_norm',max(abs(x) for x in ev)==2,eigenvalues={str(k):int(v) for k,v in ev.items()})
emit('weak_unitarity_check_survives_string_mutation',zero(true*true-s.eye(1<<N)) and zero(bad*bad-s.eye(1<<N)),reason='Both separated XX candidates square to 1; this predicate does not test the string.')

# Direct finite one-particle maps, with integer physical labels including negatives.
indices=range(-2,2);fine=range(-4,4);finer=range(-8,8)
R=s.zeros(len(fine),len(indices));S=s.zeros(len(finer),len(fine));T=s.zeros(len(finer),len(indices))
for j in indices:
    for b in (0,1):R[2*j+b-fine.start,j-indices.start]=1/s.sqrt(2)
    for b in range(4):T[4*j+b-finer.start,j-indices.start]=s.Rational(1,2)
for j in fine:
    for b in (0,1):S[2*j+b-finer.start,j-fine.start]=1/s.sqrt(2)
emit('D5_two_step_negative_indices',zero(s.SparseMatrix(S*R-T)),coarse_labels=list(indices))
emit('one_particle_isometry',zero(s.SparseMatrix(R.T*R-s.eye(len(indices)))))
emit('mutation_wrong_normalization_detected',not zero(s.SparseMatrix((s.sqrt(2)*R).T*(s.sqrt(2)*R)-s.eye(len(indices)))))

r,c=s.symbols('r c',real=True)
h=(1-r*c)/s.sqrt(1-2*r*c+r*r)
derivative=s.simplify(s.diff(h,r)+r*(1-c*c)/(1-2*r*c+r*r)**s.Rational(3,2))
paired=s.factor((1-r*c)**2/(1-2*r*c+r*r)-(1+r*c)**2/(1+2*r*c+r*r))
emit('state_derivative_exact',derivative==0,residual=str(derivative))
emit('state_cosine_pair_difference',s.simplify(paired-4*c*r**3*(c*c-1)/((1+r*r)**2-4*r*r*c*c))==0,expression=str(paired),sign_domain='0<r<1 and 0<c<1: numerator negative, denominator positive')
emit('all_exact_predicates',all(x['ok'] for x in rows),predicate_count=len(rows))
raise SystemExit(0 if all(x['ok'] for x in rows) else 1)
