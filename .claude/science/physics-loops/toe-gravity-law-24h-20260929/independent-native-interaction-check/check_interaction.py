"""Connected infinite-lattice N=4 calculation, independently implemented.

Coordinates are unrestricted integers. Variables are a,b,t12,t13,t23;
opposite coefficients are a,b,-a-b. Each t is the coefficient of the
UNNORMALIZED uniform T state sum_x Q_T(x)^dagger Omega (Gram density 2).
No author implementation or output is imported.
"""
from collections import defaultdict
from itertools import product, combinations, permutations
from pathlib import Path
from fractions import Fraction as F
import json
import resource
import sys
import time

ZERO=(0,0,0)
E=[(1,0,0),(0,1,0),(0,0,1)]
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def pair(x,y): return tuple(sorted((x,y)))
lin={}
axis=[(1,0,0,0,0),(0,1,0,0,0),(-1,-1,0,0,0)]
for i in range(3):
    for sign in [-1,1]:lin[scale(2*sign,E[i])]=axis[i]
for j,(u,v) in enumerate(combinations(range(3),2)):
    for p,q in product([-1,1],repeat=2):
        z=[0]*5;z[j+2]=-p*q
        lin[add(scale(p,E[u]),scale(q,E[v]))]=tuple(z)
D=tuple(lin)
MON=list(combinations(range(5),2))
MON=sorted([(i,j) for i in range(5) for j in range(i,5)])
INDEX={p:j for j,p in enumerate(MON)}
SP={v:tuple((i,x) for i,x in enumerate(v) if x) for v in set(lin.values())}

def coeff(x,y): return lin.get(sub(y,x))
def mul(a,b):
    if a is None or b is None:return {}
    out=defaultdict(int)
    for i,x in SP[a]:
        for j,y in SP[b]:out[INDEX[tuple(sorted((i,j)))]]+=x*y
    return {i:x for i,x in out.items() if x}
def acc(dst,src,factor=1):
    for i,v in src.items():dst[i]+=factor*v
def gram_add(G,p,factor):
    p={i:v for i,v in p.items() if v}
    for i,x in p.items():
        for j,y in p.items():G[i][j]+=factor*x*y
def zero_gram():return [[0]*15 for _ in range(15)]

def channels(x):
    d=[pair(add(x,e),sub(x,e)) for e in E]
    ch=[({d[0]:1,d[1]:-1},2),({d[0]:1,d[1]:1,d[2]:-2},6)]
    for i,j in combinations(range(3),2):
        ch.append(({pair(add(x,scale(a,E[i])),add(x,scale(b,E[j]))):a*b
                    for a,b in product([-1,1],repeat=2)},4))
    return ch

rows=[]
rows.append(('mu_singlet',{pair(e,scale(-1,e)):1 for e in E},8,'mu'))
for i,j in combinations(range(3),2):
    v=[(pair(scale(a,E[i]),scale(b,E[j])),a*b) for a,b in product([-1,1],repeat=2)]
    for (p,a),(q,b) in combinations(v,2):rows.append(('mu_plane',{p:a,q:-b},3,'mu'))
for e in E:
    for (pos,norm),(base,norm0) in zip(channels(e),channels(ZERO)):
        assert norm==norm0
        r=defaultdict(int)
        for p,c in pos.items():r[p]+=c
        for p,c in base.items():r[p]-=c
        rows.append(('tau_gradient',{p:c for p,c in r.items() if c},12//norm,'tau'))

price=[]
for name,R,weight,kind in rows:
    S={x for e in R for x in e}
    U={add(x,d) for x in S for d in D}|S
    price.append({'kind':name,'endpoints':len(S),'residual_sites':len(U),
                  'candidate_pairs':len(U)*(len(U)-1)//2,'annihilator_words':len(R)})
if '--price' in sys.argv:
    print(json.dumps({'rows':len(rows),'candidate_pairs':sum(p['candidate_pairs'] for p in price),
                      'pair_word_iterations':sum(p['candidate_pairs']*p['annihilator_words'] for p in price),
                      'max_residual_sites':max(p['residual_sites'] for p in price),
                      'star_triples':816},indent=2));sys.exit()

t0=time.perf_counter()
def abs2(z):return (z*z.conjugate()).real
# Check the hard-core connected number identity on a completely separate,
# nontranslation-invariant seven-site graph by explicit four-site words.
n=7
testC=[[0j]*n for _ in range(n)]
for i,j in combinations(range(n),2):
    testC[i][j]=testC[j][i]=complex((i+2*j)%5-2,(2*i+j)%3-1)
snorm=sum(abs2(testC[i][j]) for i,j in combinations(range(n),2))
wnorm=0
for a,b,c,d in combinations(range(n),4):
    amp=2*(testC[a][b]*testC[c][d]+testC[a][c]*testC[b][d]+testC[a][d]*testC[b][c])
    wnorm+=abs2(amp)
MM=[[sum(testC[i][k]*testC[j][k].conjugate() for k in range(n))
     for j in range(n)] for i in range(n)]
closed=sum(abs2(v) for row in MM for v in row)
rownorm=sum(sum(abs2(v) for v in row)**2 for row in testC)
edge4=sum(abs2(testC[i][j])**2 for i,j in combinations(range(n),2))
assert wnorm-2*snorm**2==closed-4*rownorm+4*edge4
GM,GT=zero_gram(),zero_gram()
nonzero_counts=[]
for name,R,weight,kind in rows:
    # Every energy square kills the chosen entire uniform pair family.
    null=[0]*5
    for (u,v),r in R.items():
        for i,c in enumerate(coeff(u,v)):null[i]+=r*c
    assert null==[0]*5
    S={x for e in R for x in e}
    U=sorted({add(x,d) for x in S for d in D}|S)
    nz=0
    for a,b in combinations(U,2):
        eta={a,b};cab=coeff(a,b)
        out=defaultdict(int)
        for (u,v),r in R.items():
            if u in eta or v in eta:
                acc(out,mul(coeff(u,v),cab),-r)
            else:
                acc(out,mul(coeff(u,a),coeff(v,b)),r)
                acc(out,mul(coeff(u,b),coeff(v,a)),r)
        if any(out.values()):
            nz+=1;gram_add(GM if kind=='mu' else GT,out,weight)
    nonzero_counts.append({'kind':name,'nonzero_residual_pair_polynomials':nz})

# At N=4 every nonzero C^2 occupation word already has a graph partner
# for each particle. The D diagonal therefore contributes only m_0=3.
for x,y,z in combinations(D,3):
    p=defaultdict(int)
    acc(p,mul(coeff(ZERO,x),coeff(y,z)))
    acc(p,mul(coeff(ZERO,y),coeff(x,z)))
    acc(p,mul(coeff(ZERO,z),coeff(x,y)))
    gram_add(GM,p,12)

# Number fourth coefficient from an independent closed-walk identity:
# (||C^2 Omega||^2-2||C Omega||^4)/V = tr[(c c*)^2]/V-16g^2+4u4.
def biform_square(G,M,factor):
    terms=[(i,j,M[i][j]) for i in range(5) for j in range(5) if M[i][j]]
    for i,j,v in terms:
        for k,l,w in terms:
            left=INDEX[tuple(sorted((j,k)))];right=INDEX[tuple(sorted((i,l)))]
            G[left][right]+=factor*v*w
gmat=[[0]*5 for _ in range(5)]
for d,v in lin.items():
    if d<scale(-1,d):
        for i,x in enumerate(v):
            for j,y in enumerate(v):gmat[i][j]+=x*y
GN=zero_gram()
cor=defaultdict(lambda:[[0]*5 for _ in range(5)])
for d,v in lin.items():
    for e,w in lin.items():
        M=cor[sub(d,e)]
        for i,x in enumerate(v):
            for j,y in enumerate(w):M[i][j]+=x*y
for M in cor.values():biform_square(GN,M,1)
biform_square(GN,gmat,-16)
for d,v in lin.items():
    if d<scale(-1,d):gram_add(GN,mul(v,v),4)
assert all(G[i][j]==G[j][i] for G in [GM,GT,GN] for i in range(15) for j in range(15))

def evaluate(G,z,den=1):
    m=[z[i]*z[j] for i,j in MON]
    return sum(m[i].conjugate()*G[i][j]*m[j] for i in range(15) for j in range(15))/den
def frac_evaluate(G,z,den=1):
    z=list(map(F,z));m=[z[i]*z[j] for i,j in MON]
    return sum(m[i]*G[i][j]*m[j] for i in range(15) for j in range(15))/den
directions={
 'diag_1_minus1_0':(1,-1,0,0,0),
 'offdiag_12':(0,0,1,0,0),
 'diag_1_1_minus2':(1,1,0,0,0),
 'offdiag_all_equal':(0,0,1,1,1),
 'generic_real':(1,2,3,4,5)}
direction_results={name:{'mu_energy_t4':str(frac_evaluate(GM,z,12)),
                         'tau_energy_t4':str(frac_evaluate(GT,z,12)),
                         'number_t4':str(frac_evaluate(GN,z,3))}
                   for name,z in directions.items()}

# Exact cubic covariance on general complex direction; Gaussian integers
# represented by Python complex remain exact here (all values well below 2^53).
base=[1+2j,2-1j,3+1j,-1+2j,2+3j]
assert max(abs(v) for G in [GM,GT,GN] for row in G for v in row)*225*max(abs(z.real)+abs(z.imag) for z in base)**4 < 2**53
scalarC={d:sum(v[i]*base[i] for i in range(5)) for d,v in lin.items()}
scalarCor=defaultdict(complex)
for d,v in scalarC.items():
    for e,w in scalarC.items():scalarCor[sub(d,e)]+=v*w.conjugate()
g=sum(abs2(v) for d,v in scalarC.items())/2
u4=sum(abs2(v)**2 for d,v in scalarC.items())/2
directN=sum(abs2(v) for v in scalarCor.values())-16*g*g+4*u4
assert evaluate(GN,base)==directN
T=[[base[0],base[2],base[3]],[base[2],base[1],base[4]],
   [base[3],base[4],-base[0]-base[1]]]
def parity(p):return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
rotation_count=0
for perm in permutations(range(3)):
    for signs in product([-1,1],repeat=3):
        if parity(perm)*signs[0]*signs[1]*signs[2]!=1:continue
        R=[[signs[i]*signs[j]*T[perm[i]][perm[j]] for j in range(3)] for i in range(3)]
        z=[R[0][0],R[1][1],R[0][1],R[0][2],R[1][2]]
        for G in [GM,GT,GN]:assert evaluate(G,z)==evaluate(G,base)
        rotation_count+=1
assert rotation_count==24

out=Path(__file__).parent
data={'variable_order':['a','b','t12','t13','t23'],
      'monomial_order':MON,'mu_energy_gram_numerator_denominator_12':GM,
      'tau_energy_gram_numerator_denominator_12':GT,
      'number_t4_gram_numerator_denominator_3':GN,'pair_norm_density_matrix':gmat,
      'coefficient_domain':'Complex variables, conjugated monomial on left; real symmetric matrices.',
      'safe_finite_torus_scope':'L>=10 by the conservative connected-coordinate bound; see independent report.'}
(out/'quartic_matrices.json').write_text(json.dumps(data,indent=2)+'\n')
result={'rows':len(rows),'row_nonzero_counts':nonzero_counts,'direction_results':direction_results,
        'exact_cubic_rotations':rotation_count,'seven_site_literal_number_identity':True,
        'complex_convolution_number_identity':True,'author_code_imported':False,
        'elapsed_seconds':time.perf_counter()-t0,
        'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
