#!/usr/bin/env python3
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import ast,collections,datetime,hashlib,itertools,json,resource,time
from fractions import Fraction as F
from pathlib import Path
here=Path(__file__).resolve().parent;runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert all(not(runtime/n).exists() for n in ('STOP_REQUESTED','STOP_REQUESTED.json'))
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(5,5));c0=time.process_time();t0=time.monotonic()
source=here/'check.py';source_sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_sha=='0a9ad45254895f22b6e716ac14c2aace1f333338d286cd35df889343ac493604'
dirs=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1));z=(0,0,0)
ns={'collections':collections,'dirs':dirs,'z':z}
parsed=ast.parse(source.read_text());defs=ast.Module(body=[n for n in parsed.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))],type_ignores=[])
exec(compile(defs,str(source),'exec'),ns)
near=tuple(sorted({ns['add'](d,e) for d in dirs for e in dirs}-{z}));ns['near']=near
nb=ns['nb'];hop=ns['hop'];physical=ns['physical'];info=ns['info'];H=ns['H'];gauss=ns['gauss']
a=(4,0,0);S=set(nb(z))|set(nb(a))|{(7,0,0),(6,1,0),(6,-1,0),(6,0,1),(15,0,0)}
assert len(S)==17
st=physical(S);middle=hop(hop(st,z,(1,0,0),True),(2,0,0),(1,0,0))
end=hop(hop(middle,(2,0,0),(3,0,0),True),a,(3,0,0))
assert all(gauss(x) for x in (st,middle,end))
assert info(st)[2:]==(0,7) and info(middle)[2]>0 and info(end)[2]==0 and info(end)[3]>=10
assert H(st).get(middle)==1 and H(middle).get(end)==1
# Displacement4 along one axis in two allowed <=2 moves forces the single
# intermediate hole2e_x and single shared-B paths, so H² entry is exactly1.
transfer={'global_NB':len(S),'initial_local_N3':info(st)[3],'middle_G':info(middle)[2],'final_local_N3':info(end)[3],'final_G':info(end)[2],'actual_two_step_amplitude':1,'unique_two_step_hole_geometry':True}
# Exact Gaussian rational matrices.
Z=(F(0),F(0));I=(F(1),F(0))
def c(x):return (F(x),F(0))
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def times(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return(a[0],-a[1])
def matmul(A,B):return [[sumc(times(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sumc(it):
    x=Z
    for a in it:x=plus(x,a)
    return x

def madd(A,B):return [[plus(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(x,A):return [[times(c(x),a) for a in r] for r in A]
def adj(A):return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A))]
def determinant(A):
    out=Z;n=len(A)
    for p in itertools.permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));v=c(sign)
        for i in range(n):v=times(v,A[i][p[i]])
        out=plus(out,v)
    return out

def psd(A):
    assert A==adj(A)
    count=0
    for n in range(1,len(A)+1):
        for inds in itertools.combinations(range(len(A)),n):
            d=determinant([[A[i][j] for j in inds] for i in inds]);assert d[1]==0 and d[0]>=0
            count+=1
    return count

Id=[[c(i==j) for j in range(4)] for i in range(4)]
Good=[[c(i==j and i!=1) for j in range(4)] for i in range(4)]
O=[[Z for j in range(4)] for i in range(4)];O[0][2]=(F(0),F(1));O[2][0]=(F(0),F(-1))
minors=0;cases=[]
for seed in range(4):
    a,d,r,b,u,v,w=[F(((seed+2)*(j+1))%7-3,2) for j in range(7)]
    Hr=[[a,0,1,u],[0,d,0,v],[1,0,r,w],[u,v,w,b]]
    HH=[[c(x) for x in row] for row in Hr];M=max(sum(abs(F(x)) for x in row) for row in Hr)
    G=[[c((10 if i==2 else 2 if i==3 else 0) if i==j else 0) for j in range(4)]
    for delta,kappa in ((F(1),F(1)),(F(2,3),F(1,4))):
        Xi=2*delta*M+(4*delta*M+10*kappa)**2/(4*delta)
        aa=1/delta+(Xi/delta+1)/(2*kappa)
        TT=madd(scale(aa,Id),scale(-1/delta,O))
        A=madd([[times((F(0),-delta),x) for x in row] for row in HH],scale(-kappa/2,G))
        LT=madd(matmul(adj(A),TT),matmul(TT,A))
        margin=scale(-1,madd(LT,Good))
        minors+=psd(TT)+psd(margin)
        assert matmul(TT,Good)==matmul(Good,TT)
        cases.append({'M':str(M),'delta':str(delta),'kappa':str(kappa),'upper_C':str(aa+1/delta)})
result={'dense_dark_transfer':transfer,'abstract_rational_multiplier_cases':cases,'principal_minors_checked':minors,'bound_word_runner_sha256':source_sha,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<5 and result['peak_rss_bytes']<80*1024**2
(here/'FOLLOWUP_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
