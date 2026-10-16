"""Finite local-energy extension: exact path controls and bounded recursion."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,math
import numpy as np

P=Path(__file__).resolve().parent;checks=[]
def check(name,ok,**data):
    assert bool(ok),name
    checks.append({'name':name,'passed':True,**data})

def path_law(bits,B):
    state=0;prob=F(1)
    for bit in bits:
        inc=2*bit-1
        if state==B and inc==1:return F(0)
        if state==-B and inc==-1:return F(0)
        prob*=1 if abs(state)==B else F(1,2)
        state+=inc
    return prob

rows=[]
for B in [1,2,3]:
    for N in range(1,13):
        target=F(1,2**N);surv=F(0);mass=F(0);tv=F(0)
        for word in product([0,1],repeat=N):
            q=path_law(word,B);mass+=q;tv+=abs(q-target)/2
            if q:
                surv+=target;assert q>=target
                e0=F(B,2)
                for c in word:e0+=F(1,2)-c;assert 0<=e0<=B
        assert mass==1 and tv==1-surv
        if B==1:assert surv==F(1,2**(N//2))
        if N>B:assert surv<1
    rows.append({'B':B,'N':N,'target_survival':str(surv),'optimal_TV':str(tv)})
check('exact energy-conserving paths attain the support TV bound',True,rows=rows,max_depth=12)

def matrices(B):
    K=np.zeros((2*B+1,2*B+1));R=K.copy()
    for i in range(2*B+1):
        if i>0:K[i,i-1]=.5
        if i<2*B:K[i,i+1]=.5
    R[:]=K;R[0,1]=1;R[-1,-2]=1
    return K,R

for B in range(1,9):
    K,R=matrices(B);vals=np.linalg.eigvalsh(K)
    exact=sorted(math.cos(j*math.pi/(2*B+2)) for j in range(1,2*B+2))
    assert np.max(np.abs(vals-exact))<2e-15
    pi=np.full(2*B+1,1/(2*B));pi[0]=pi[-1]=1/(4*B)
    assert abs(pi.sum()-1)<1e-15 and np.max(np.abs(pi@R-pi))<1e-15
    assert np.max(np.abs(pi[:,None]*R-(pi[:,None]*R).T))<1e-15
    corr=sum(pi[i]*R[i,j]*R[j,k]*(j-i)*(k-j) for i in range(len(pi)) for j in range(len(pi)) for k in range(len(pi)))
    assert abs(corr+1/(2*B))<1e-15
check('absorbing spectrum and reflecting invariant lag correlation',True,buffers=8,periodicity='two; no convergence from each state asserted')

examples=[]
for B in [1,2,4,8,16,32,64]:
    K,R=matrices(B);absorb=np.zeros(2*B+1);reflect=absorb.copy();absorb[B]=reflect[B]=1
    states=np.arange(-B,B+1)
    for N in range(1,1001):
        # Vector stencil avoids unnecessary dense matrix multiplications.
        na=np.zeros_like(absorb);na[1:]+=.5*absorb[:-1];na[:-1]+=.5*absorb[1:];absorb=na
        nr=np.zeros_like(reflect);nr[1:]+=.5*reflect[:-1];nr[:-1]+=.5*reflect[1:];nr[1]+=.5*reflect[0];nr[-2]+=.5*reflect[-1];reflect=nr
        if N in [10,100,1000]:
            surv=float(absorb.sum());bound=min(1.,math.sqrt(2*B+1)*math.cos(math.pi/(2*B+2))**N)
            var=float((reflect*states**2).sum()-(reflect*states).sum()**2)/4
            assert surv<=bound+1e-12 and var<=B*B/4+1e-12 and abs(reflect.sum()-1)<1e-12
            examples.append({'B_in_energy_quanta':B,'trials':N,'iid_path_survival':surv,'minimum_TV':1-surv,'survival_norm_bound':bound,'reflecting_count_variance':var,'iid_count_variance':N/4})
check('finite horizon survival and variance controls',True,rows=examples)

# General time-dependent fractions: conservation telescopes pathwise; this
# check does not presume every chosen path fits the declared finite capacity.
ps=[F(1,4),F(2,3),F(3,5),F(1,2)];eps=F(7,3);einit=F(5,2)
for bits in product([0,1],repeat=len(ps)):
    cumulative=F(0);energy=einit*eps
    for p,c in zip(ps,bits):
        cumulative+=c-p;energy+=eps*(p-c)
        assert energy==eps*(einit-cumulative)
        work=eps*cumulative
        assert energy+work==eps*einit
check('closed and externally compensated energy accounting',True,paths=16)

for N in range(1,11):
    works=[sum(word)-F(N,2) for word in product([0,1],repeat=N)]
    mean=sum(works)/len(works);variance=sum((x-mean)**2 for x in works)/len(works)
    assert mean==0 and variance==F(N,4)
check('balanced iid exchange fluctuation requirement',True,max_depth=10)

result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK07_v1.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Conditional finite-storage extension of mathematical flux to actual energy; excludes neither powered detectors nor general network dynamics.'}
text=json.dumps(result,indent=2)+'\n';(P/'ENERGY_RECORD_CONTROLS_v1.json').write_text(text);print(text,end='')
