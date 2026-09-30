#!/usr/bin/env python3
"""Exact finite graded algebra control; not a physical lattice simulation."""
import os, time, resource, json, hashlib
from pathlib import Path
from fractions import Fraction as F
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
t0=time.perf_counter();c0=time.process_time()
# Gaussian rationals, dense dimension three; Laurent support [-4,8].
def z(a=0,b=0):return (F(a),F(b))
def za(a,b):return (a[0]+b[0],a[1]+b[1])
def zn(a):return (-a[0],-a[1])
def zm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zc(a):return (a[0],-a[1])
def zs(a,f):return (a[0]*f,a[1]*f)
Z=z();ONE=z(1);I=z(0,1);d=3
zero=lambda:tuple(Z for _ in range(d*d))
def mat(rows):return tuple(z(v) if not isinstance(v,tuple) else z(*v) for row in rows for v in row)
def add(a,b):return tuple(za(x,y) for x,y in zip(a,b))
def neg(a):return tuple(zn(x) for x in a)
def scale(a,f):return tuple(zm(x,f) for x in a)
def mul(a,b):
    out=[]
    for i in range(d):
        for j in range(d):
            v=Z
            for k in range(d):v=za(v,zm(a[i*d+k],b[k*d+j]))
            out.append(v)
    return tuple(out)
def adj(a):return tuple(zc(a[j*d+i]) for i in range(d) for j in range(d))
def clean(a):return {k:v for k,v in a.items() if any(x!=Z for x in v)}
def padd(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=add(out.get(k,zero()),v)
    return clean(out)
def pscale(a,f):return clean({k:scale(v,f) for k,v in a.items()})
def pmul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            if -4<=k+l<=8:out[k+l]=add(out.get(k+l,zero()),mul(v,w))
    return clean(out)
def padj(a):return clean({k:adj(v) for k,v in a.items()})
Id=mat([[1,0,0],[0,1,0],[0,0,1]])
W=mat([[0,0,0],[0,1,0],[0,0,2]])
def off(a):return tuple(v if i//d!=i%d else Z for i,v in enumerate(a))
def invW(a):return tuple(zs(v,F(1,i//d-i%d)) if i//d!=i%d else Z for i,v in enumerate(a))
def expgen(p,g,sgn=1):
    out={0:Id};power=Id;fact=1
    for r in range(1,8//p+1):
        power=mul(power,g);fact*=r
        out[r*p]=scale(power,z(F(sgn**r,fact)))
    return clean(out)
def transform(A,J,p,g):
    X=expgen(p,g);Xi=expgen(p,g,-1)
    return pmul(pmul(X,A),Xi),pmul(pmul(X,J),Xi)
def getH(A):return pscale(padd(A,pscale(padj(A),z(-1))),z(0,F(1,2)))
def getB(A,J):return padd(padd(A,padj(A)),pmul(padj(J),J))
H={-4:W,-2:mat([[2,0,0],[0,-1,0],[0,0,3]]),
   -1:mat([[1,(2,1),-1],[(2,-1),2,(0,1)],[-1,(0,-1),-2]]),
   0:mat([[3,-2,(1,1)],[-2,1,4],[(1,-1),4,0]]),
   1:mat([[0,1,2],[1,2,-1],[2,-1,3]]),
   2:mat([[2,(0,1),1],[(0,-1),-3,2],[1,2,1]])}
J={-1:mat([[0,1,0],[0,0,2],[0,0,0]]),
   0:mat([[1,0,3],[0,-2,0],[0,0,2]]),
   1:mat([[1,2,0],[3,-1,1],[2,4,2]])}
B={0:mat([[2,1,(2,1)],[1,-3,-2],[(2,-1),-2,1]]),
   1:mat([[1,(1,2),-1],[(1,-2),2,3],[-1,3,-2]]),
   2:mat([[0,1,1],[1,1,-1],[1,-1,2]])}
A=padd(pscale(H,z(0,-1)),padd(pscale(pmul(padj(J),J),z(F(-1,2))),pscale(B,z(F(1,2)))))
checks=[]
def check(name,test):
    assert test,name
    checks.append(name)
check('initial potential coefficients exact',all(getB(A,J).get(k,zero())==v for k,v in B.items()))
for p in range(3,7):
    hp=getH(A).get(p-4,zero());g=invW(off(hp))
    check('unitary generator anti-Hermitian order'+str(p),adj(g)==neg(g))
    A,J=transform(A,J,p,g)
    check('offgrade H canceled order'+str(p-4),off(getH(A).get(p-4,zero()))==zero())
pre_A=dict(A);pre_J=dict(J)
for p in (4,5):
    bp=getB(A,J).get(p-4,zero());g=scale(invW(off(bp)),z(0,F(1,2)))
    check('positive generator Hermitian order'+str(p),adj(g)==g)
    wrongA,wrongJ=transform(A,J,p,neg(g))
    check('wrong sign doubles offgrade potential order'+str(p-4),off(getB(wrongA,wrongJ).get(p-4,zero()))==scale(off(bp),z(2)))
    A,J=transform(A,J,p,g)
    check('offgrade potential canceled order'+str(p-4),off(getB(A,J).get(p-4,zero()))==zero())
induced=off(getH(A).get(2,zero()))
check('positive congruence induces genuine H order2 correction',induced!=zero())
g=invW(induced);A,J=transform(A,J,6,g)
for k in range(-4,3):
    check('final Hamiltonian coefficient grade zero '+str(k),off(getH(A).get(k,zero()))==zero())
for k in (0,1):check('final potential coefficient grade zero '+str(k),off(getB(A,J).get(k,zero()))==zero())
for k in (-4,-3,-2,-1):check('no negative-order potential '+str(k),getB(A,J).get(k,zero())==zero())
# Unscaled jump J has positive grade only at epsilon² or later.
for k in (-1,0):
    check('positive jump grade absent at scaled order '+str(k),all(v==Z for i,v in enumerate(J.get(k,zero())) if i//d-i%d>0))
check('final jump leading coefficient unchanged',J[-1]==pre_J[-1])
check('final jump next coefficient unchanged',J[0]==pre_J[0])
# Universal variation identity: dB= -2i[D,H] + 2 D_J^*(D).
D=mat([[1,2,(1,1)],[2,-1,3],[(1,-1),3,0]])
Hs=H[0];Js=J[-1];Bs=B[0]
As=add(scale(Hs,z(0,-1)),add(scale(mul(adj(Js),Js),z(F(-1,2))),scale(Bs,z(F(1,2)))))
comm=lambda x,y:add(mul(x,y),neg(mul(y,x)))
dA=comm(D,As);dJ=comm(D,Js)
lhs=add(add(dA,adj(dA)),add(mul(adj(dJ),Js),mul(adj(Js),dJ)))
DJ=add(mul(mul(adj(Js),D),Js),scale(add(mul(mul(adj(Js),Js),D),mul(D,mul(adj(Js),Js))),z(F(-1,2))))
rhs=add(scale(comm(D,Hs),z(0,-2)),scale(DJ,z(2)))
check('full positive-congruence potential derivative includes recycling',lhs==rhs)
# Exact grade drift algebra for a finite jump matrix, all grades retained coherently.
JJ=mat([[1,2,3],[4,-1,2],[1,3,2]])
drift=add(mul(mul(adj(JJ),W),JJ),scale(add(mul(mul(adj(JJ),JJ),W),mul(W,mul(adj(JJ),JJ))),z(F(-1,2))))
diag=lambda m:tuple(v if i//d==i%d else Z for i,v in enumerate(m))
rhs=zero()
for r in range(-2,3):
    jr=tuple(v if i//d-i%d==r else Z for i,v in enumerate(JJ))
    rhs=add(rhs,scale(mul(adj(jr),jr),z(r)))
check('phase-diagonal drift sum r Jr*Jr exact',diag(drift)==rhs)
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
res={'status':'all exact checks passed','checks':checks,'count':len(checks),'scope':'dimension3 Gaussian-rational graded algebra, not a physical Gauss carrier or proof of volume uniformity','laurent_range':[-4,8],'cpu_seconds':time.process_time()-c0,'wall_seconds':time.perf_counter()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('SERIES_RESULTS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
