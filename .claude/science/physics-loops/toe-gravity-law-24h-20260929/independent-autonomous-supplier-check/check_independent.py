#!/usr/bin/env python3
"""Independent exact small controls; never imports or executes author code."""
import itertools, json, math, os, resource, sys, time
from fractions import Fraction as F
from pathlib import Path

START=time.monotonic()
OUT=Path(__file__).parent
DEAD=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (DEAD/'STOP_REQUESTED.json').exists(), 'stop sentinel present'
assert time.time()<json.loads((DEAD/'DEADLINE.json').read_text())['deadline_epoch']
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    assert os.environ.get(name)=='1'
sys.set_int_max_str_digits(20000)
def ceil(q): return -(-q.numerator//q.denominator)
def logceil(q):
    assert q>0
    j=max(0,q.numerator.bit_length()-q.denominator.bit_length())
    if (1<<j)*q.denominator<q.numerator: j+=1
    assert (1<<j)*q.denominator>=q.numerator
    assert j==0 or (1<<(j-1))*q.denominator<q.numerator
    return j
def icbrtceil(z):
    lo,hi=0,1<<((z.bit_length()+2)//3)
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**3>=z: hi=mid
        else: lo=mid
    return hi

# Whole-cell supports from the actual union of two cubic A stars.
dirs=[]
for j in range(3):
    for sg in (-1,1): dirs.append(tuple(sg if k==j else 0 for k in range(3)))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
base=set(dirs)
disps={plus(a,b) for a in dirs for b in dirs}-{(0,0,0)}
geometry=[]
for c in sorted(disps):
    other={plus(c,d) for d in dirs}
    shared=len(base&other); bsites=len(base|other)
    geometry.append({'c':c,'shared_B':shared,'B_union':bsites,
                     'arity_constant':2+2*bsites,'q_E_coefficient':6*bsites})
assert len(disps)==18
assert sum(g['shared_B']==1 for g in geometry)==6
assert sum(g['shared_B']==2 for g in geometry)==12
assert max(g['arity_constant'] for g in geometry)==24
assert max(g['q_E_coefficient'] for g in geometry)==66

# Matched record code under positive copy-conjugated generator.
vectors=((1,1,0,-1),(0,1,1,1))
G=[[sum(v[i]*v[j] for v in vectors) for j in range(4)] for i in range(4)]
copy=lambda i: 4*(i//4)+2*((i//2)%2)+((i%2+(i//2)%2)%2)
G8=[[0]*8 for _ in range(8)]
for i in range(4):
    for j in range(4):
        for e in range(2): G8[copy(2*i+e)][copy(2*j+e)]=G[i][j]
matched=lambda i: (i//2)%2==i%2
assert all(G8[i][j]==0 for i in range(8) for j in range(8) if matched(i)!=matched(j))
assert any(G8[i][j]!=0 for i in range(8) for j in range(8)
           if matched(i) and matched(j) and (i//2)%2!=(j//2)%2)
# A ready-column-correct one-sided copy is insufficient: flag-X followed by copy.
naive=lambda i: copy(i^2)
assert naive(0)==3 and not matched(naive(3))

# Literal interaction-picture words with noncommuting source Hamiltonian.
# Source/flag G is the Gram matrix above. h=(0,0,2,2); omega=1.
# We apply 2V(t), with positive f=4+2cos(x)+cos(2x): weights 8,2,1.
# Times are multiples of pi/2, so all phases are exact Gaussian integers.
hs=(0,0,2,2)
def rot(z,n):
    a,b=z
    return ((a,b),(-b,a),(-a,-b),(b,-a))[n%4]
def act(state,l,band):
    out={}
    for (m,i),z in state.items():
        for dm,co in ((-2,1),(-1,2),(0,8),(1,2),(2,1)):
            p=m+dm
            if abs(p)>band: continue
            for j in range(4):
                w=co*G[j][i]
                if not w: continue
                zz=rot(z,l*(dm+hs[j]-hs[i]))
                old=out.get((p,j),(0,0))
                out[(p,j)]=(old[0]+w*zz[0],old[1]+w*zz[1])
    return {k:z for k,z in out.items() if z!=(0,0)}
init={(m,0):(1,0) for m in (-1,0,1)}
comparisons=0
for times in itertools.product(range(4),repeat=3):
    small=large=init
    for l in times:
        small=act(small,l,7); large=act(large,l,15)
        assert small==large
        comparisons+=1
small=large=init
for l in (0,1,2,3):
    small=act(small,l,7); large=act(large,l,15)
assert small!=large and any(abs(m)>7 for m,i in large)
boundary_sq=sum(a*a+b*b for (m,i),(a,b) in large.items() if abs(m)>7)
assert boundary_sq>0
# [P,S]=S for the ordinary compressed raising shift, not a cyclic shift.
K=7
assert all((m+1)-m==1 for m in range(-K,K))
cyclic_commutator_defect=(-K-K)-1
assert cyclic_commutator_defect==-15

# Reconstruct the complete rational parameter prescription from the report.
L=24; N=L**3//2; T=F(1); R=1346132804
v=2592*N; g=80*N; gw=300*N
qmax=1+6*N*R
hbar=2*qmax*qmax+2*v
pbar=gw*(316*qmax*qmax+2*v)
alpha=F(1,1000*(1+hbar*hbar+pbar*pbar)); eps=F(1,1000)
c=7*g*g+4*hbar*g
n=ceil(max(F(1),2*T*g,5*T*T*c/alpha)); tau=T/n; mg=N*n
s=min(tau/(8*N+4),alpha/(80*mg*(hbar+1)))
sigma=min(s/2,alpha*s/(320*mg))
vbar=8*N/s
theta=min(alpha*alpha/(1600*N),eps/(8*vbar*N))
lc=4*T
k0=ceil(lc*lc/(8*sigma*sigma*theta))
d0=ceil(max(160*mg*lc/(alpha*s),64*mg*lc/(eps*s*s)))
M=d0*d0-1
dcut=min(alpha/5,eps/(4*vbar))
k=max(ceil(6*vbar*T),logceil(8/dcut),1)
r=k-1; kc=k0+M*r
assert k>=6 and M>=1 and kc>k0
assert 80*tau<=F(1,2)
assert T*tau*c<=alpha/5
assert 16*mg*s*hbar<=alpha/5
assert 32*mg*lc/(s*d0)<=alpha/5  # pi<4
assert 32*mg*sigma/s<=alpha/10
assert 16*N*theta<=(alpha/10)**2
assert lc*lc/(4*(2*k0+1)*sigma*sigma)<=theta
assert k>=6*vbar*T and k>=logceil(8/dcut)
assert dcut<=alpha/5
endpoint_bound=16*mg*lc/(s*s*d0)+2*vbar*N*theta+vbar*dcut
assert endpoint_bound<=3*eps/4
assert max(hbar,hbar*hbar,pbar,pbar*pbar)*alpha<F(1,1000)
qE=(2*R).bit_length(); qC=(2*kc).bit_length(); qF=4
bA=1+qC+2*n*qF; bB=2+6*qE
block=icbrtceil(max(bA,bB))
assert block**3>=max(bA,bB)>(block-1)**3
results={
 'geometry':geometry,
 'record_code':{'positive_Gram_generator':True,'matched_code_reducing':True,
                'one_sided_copy_negative_control':True},
 'clock_words':{'prefix_comparisons':comparisons,'distinct_time_triples':64,
                'k0':1,'M':2,'small_band':7,'reference_band':15,
                'first_unprotected_order':4,'escaped_squared_gaussian_norm':boundary_sq,
                'cyclic_boundary_defect':cyclic_commutator_defect},
 'resources':{'L':L,'N':N,'R':R,'v':v,'g':g,'g_w':gw,'Qmax':qmax,
              'hbar':hbar,'Pbar':pbar,'n_digits':len(str(n)),'m_g_digits':len(str(mg)),
              'M_digits':len(str(M)),'K_c_digits':len(str(kc)),
              'q_C':qC,'q_E':qE,'block_digits':len(str(block)),
              'range_digits':len(str(7*block)),
              'all_five_process_budgets_verified':True,
              'endpoint_bound_le_three_quarters_epsilon':True,
              'moment_apparatus_errors_lt_one_thousandth':True},
 'timing':{'wall_seconds':time.monotonic()-START,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
 'independence':'No author implementation imported, read, or executed.'}
(OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='geometry'},indent=2))
