"""Exact complement/CAR support. Neither fixture evaluates native alpha."""
from itertools import combinations,product
from pathlib import Path
import json,time
import sympy as s
start=time.perf_counter(); checks=[]; data={}
def req(name,p):
    if not p: raise AssertionError(name)
    checks.append(name)
def same(A,B):
    if isinstance(A,s.MatrixBase):return all(s.expand(x)==0 for x in A-B)
    return A==B
def eq(name,A,B): req(name,same(A,B))
I=s.I; X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-I],[I,0]])
Z=s.diag(1,-1); one=s.eye(2)
gamma=[]
for j in range(4):
    for a in (X,Y): gamma.append(s.kronecker_product(*([Z]*j+[a]+[one]*(3-j))))
eye=s.eye(16); g=gamma[0]
legs=[I*g*gamma[j] for j in range(1,7)]
bs=sum(legs,s.zeros(16)); cavity=10*eye+I*gamma[7]*(gamma[1]+2*gamma[2]+3*gamma[4])
H=cavity-bs/2
eq('toy_cavity_commutes_center',cavity*g,g*cavity)
eq('toy_star_square',bs*bs,6*eye)
eq('toy_center_conjugation',g*H*g,H+bs)
eq('toy_center_commutator_sign',g*H-H*g,bs*g)
req('wrong_center_commutator_sign_rejected',not same(g*H-H*g,-bs*g))
# Norm of cavity perturbation sqrt14 and that of any signed half-star sqrt(3/2).
# Both are below4 and2 respectively, so every D in this fixture is >4I.
eq('toy_cavity_perturbation_square',(cavity-10*eye)**2,14*eye)
pairs=list(combinations(range(6),2)); B={}; R={}; Rbar={}; J={}; noncommuting=[]
for A in pairs:
    b=legs[A[0]]+legs[A[1]]; B[A]=b
    d=H+b; db=H+bs-b
    R[A]=-d.inv(); Rbar[A]=-db.inv(); J[A]=g*b-b*g
    eq('toy_gJ_2B_'+str(A),g*J[A],2*b)
    eq('toy_complement_inverse_'+str(A),Rbar[A],g*R[A]*g)
    eq('toy_negative_inverse_identity_'+str(A),Rbar[A]-R[A],Rbar[A]*(bs-2*b)*R[A])
    eq('toy_full_complement_vector_operator_'+str(A),
       R[A]-g*R[A]*J[A]*R[A],Rbar[A]*(eye-bs*R[A]))
    if not same(cavity*b,b*cavity):noncommuting.append(A)
req('toy_some_cavity_pairs_noncommuting',0<len(noncommuting)<15)
wrong=Rbar[pairs[0]]*(eye+bs*R[pairs[0]])
req('wrong_complement_boundary_sign_rejected',not same(wrong,R[pairs[0]]-g*R[pairs[0]]*J[pairs[0]]*R[pairs[0]]))
req('ordered_inverse_commutation_rejected',not same(R[pairs[0]]*R[pairs[-1]],R[pairs[-1]]*R[pairs[0]]))
matching_count=0
for A,C,D in combinations(pairs,3):
    if len(set(A+C+D))!=6: continue
    matching_count+=1
    for U,V in ((A,C),(A,D),(C,D)):
        if not same(B[U]*B[V]+B[V]*B[U],s.zeros(16)): raise AssertionError('matching anticomm')
    eq('toy_matching_cavity_sum_'+str((A,C,D)),3*H+B[A]+B[C]+B[D],2*H+g*H*g)
req('fifteen_perfect_matchings',matching_count==15)
data['toy']={'Majoranas':8,'Fock_dimension':16,'pairs':15,'matchings':matching_count,
             'strict_D_lower_bound':4,'reference_vacuum_used':False,
             'scope':'synthetic shared-center quadratic matrices; no native scalar'}

# Independent polynomial CAR multiplication on the actual native L4 AP torus.
# This flat small torus is an identity check, outside the large-L spectral theorem.
L=4; vertices=list(product(range(L),repeat=3)); ix={v:j for j,v in enumerate(vertices)}
K=s.zeros(64)
for r in vertices:
    for a in range(3):
        q=list(r); q[a]=(q[a]+1)%L; q=tuple(q)
        sign=(-1)**sum(r[:a]) * (-1 if r[a]==L-1 else 1)
        K[ix[r],ix[q]]=sign; K[ix[q],ix[r]]=-sign
eq('literal_L4_AP_square',K*K,-6*s.eye(64))
def multiply(a,b):
    out={}
    for m,x in a.items():
        for n,y in b.items():
            parity=sum((n&((1<<j)-1)).bit_count() for j in range(64) if m>>j&1)%2
            key=m^n; out[key]=out.get(key,0)+(-1 if parity else 1)*x*y
    out={k:s.expand(v) for k,v in out.items()}
    return {k:v for k,v in out.items() if v!=0}
def add(a,b,scale=1):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,0)+scale*v
    out={k:s.expand(v) for k,v in out.items()}
    return {k:v for k,v in out.items() if v!=0}
def comm(a,b):return add(multiply(a,b),multiply(b,a),-1)
def field(v):return {1<<j:v[j] for j in range(64) if v[j]!=0}
hpoly={(1<<i)|(1<<j):I*K[i,j]/2 for i in range(64) for j in range(i+1,64) if K[i,j]}
gpoly={1:1}; neigh=[j for j in range(64) if K[0,j]]
actualpairs=list(combinations(neigh,2)); fields={}; currents={}; defects={}
for A in actualpairs:
    d=s.zeros(64,1)
    for j in A:d[j]=-K[0,j]
    w=-K*d/6
    eq('native_w_center_'+str(A),w[0],s.Rational(1,3))
    eq('native_inverse_source_'+str(A),K*w,d)
    wp=field(6*w); jp=field(2*I*d); vp=add(wp,gpoly,-2)
    bp=multiply(gpoly,field(I*d)); fields[A]=vp; currents[A]=jp; defects[A]=bp
    eq('native_W_H_commutator_'+str(A),comm(wp,hpoly),{k:-3*v for k,v in jp.items()})
    eq('native_W_B_commutator_'+str(A),comm(wp,bp),{k:2*v for k,v in jp.items()})
    eq('native_W_D_Ward_'+str(A),comm(wp,add(hpoly,bp)),{k:-v for k,v in jp.items()})
    for C in actualpairs:
        dc=s.zeros(64,1)
        for j in C:dc[j]=-K[0,j]
        if comm(vp,multiply(gpoly,field(I*dc)))!={}:raise AssertionError('cross defect commutator')
req('native_all_225_cross_defect_commutators',True)
jstar={}
for j in neigh:
    jstar=add(jstar,{1<<j:-2*I*K[0,j]})
for A in actualpairs:
    eq('native_incidence_current_'+str(A),comm(fields[A],hpoly),add(jstar,currents[A],-3))
    tv={}
    for C in actualpairs:
        if not set(A)&set(C):tv=add(tv,fields[C])
    eq('native_Kneser_V_eigenvalue_'+str(A),tv,{k:-3*v for k,v in fields[A].items()})
eq('native_current_star_sign',jstar,{k:-2*v for k,v in comm(gpoly,hpoly).items()})
data['native_identity_fixture']={'L':4,'one_particle_sites':64,'Fock_space_constructed':False,
    'arithmetic':'exact polynomial CAR and rational one-particle matrix',
    'native_alpha_evaluated':False,'uniform_spectral_gap_checked':False}
out={'scope':'same-agent algebra support, no native alpha or sign certificate',
     'check_groups':len(checks),'checks':checks,'data':data,'seconds':time.perf_counter()-start}
Path(__file__).with_name('BLOCK06_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('scope','check_groups','data','seconds')},indent=2))
