#!/usr/bin/env python3
"""Independent exact local algebra controls; no author implementation imported."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import itertools,json,time,resource,hashlib
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(29,30))
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic()
from sympy.polys.domains import QQ, QQ_I
Z=QQ_I.zero; ONE=QQ_I.one; I=QQ_I.dtype(QQ.zero,QQ.one)
def rat(p,q=1): return QQ_I.dtype(QQ(p,q),QQ.zero)
def add(a,b):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,Z)+v
        if not c[k]: del c[k]
    return c
def scale(a,s): return {k:v*s for k,v in a.items() if v*s}
def mul(a,b):
    rows={}
    for (k,j),v in b.items(): rows.setdefault(k,[]).append((j,v))
    c={}
    for (i,k),v in a.items():
        for j,w in rows.get(k,[]): c[i,j]=c.get((i,j),Z)+v*w
    return {k:v for k,v in c.items() if v}
def adj(a): return {(j,i):QQ_I.dtype(v.x,-v.y) for (i,j),v in a.items()}
def comm(a,b): return add(mul(a,b),scale(mul(b,a),-ONE))
MAX=10
def padd(a,b):
    c={k:v.copy() for k,v in a.items()}
    for k,v in b.items():
        if k>MAX: continue
        c[k]=add(c.get(k,{}),v)
        if not c[k]: del c[k]
    return c
def pscale(a,s): return {k:scale(v,s) for k,v in a.items() if v and s}
def shift(a,r): return {k+r:v for k,v in a.items() if k+r<=MAX}
def pmul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items():
            if k+l<=MAX: c[k+l]=add(c.get(k+l,{}),mul(v,w))
    return {k:v for k,v in c.items() if v}
def padj(a): return {k:adj(v) for k,v in a.items()}
def pcomm(a,b): return padd(pmul(a,b),pscale(pmul(b,a),-ONE))
def conjugate(a,g,r,order=6):
    out={k:v for k,v in a.items() if k<=order}; term=out
    for count in range(1,order//r+1):
        term={k+r:scale(comm(g,v),rat(1,count)) for k,v in term.items() if k+r<=order}
        term={k:v for k,v in term.items() if v}
        out=padd(out,term)
    return out
# Literal four-site physical tree, oriented from A to B; S=1 normalized shifts.
edges=[(0,1),(2,1),(2,3)]; A=[0,2]
states=[]
for q in itertools.product((0,1,-1),repeat=4):
    if sum(q)!=2: continue
    fields=(q[0]-1,q[2]-1+q[3],-q[3])
    if all(abs(m)<=1 for m in fields): states.append((q,fields))
index={s:k for k,s in enumerate(states)}; n=len(states)
w=[sum(q[a]==0 for a in A) for q,e in states]
W={(k,k):rat(x) for k,x in enumerate(w) if x}
Fedges=[]; resolved=[]; coherent=[]
for edge,(a,b) in enumerate(edges):
    f={}; js=[]
    for sign in (1,-1):
        j={}
        for col,(q,e) in enumerate(states):
            if q[a]==sign and q[b]==0:
                qq=list(q); ee=list(e); qq[a]=0; qq[b]=sign; ee[edge]-=sign
                if abs(ee[edge])<=1:
                    out=(tuple(qq),tuple(ee)); assert out in index
                    f[index[out],col]=ONE
            if q[a]==q[b]==0:
                qq=list(q); ee=list(e); qq[a]=sign; qq[b]=-sign; ee[edge]+=sign
                if abs(ee[edge])<=1:
                    out=(tuple(qq),tuple(ee)); assert out in index
                    j[index[out],col]=ONE
        js.append(j); resolved.append(j)
    Fedges.append(f); coherent.append(add(*js))
    assert not mul(adj(js[0]),js[1]) and not mul(adj(js[1]),js[0])
    assert add(mul(adj(coherent[-1]),coherent[-1]),scale(add(mul(adj(js[0]),js[0]),mul(adj(js[1]),js[1])),-ONE))=={}
F={}
for f in Fedges:
    assert comm(W,f)==f
    F=add(F,f)
for j in resolved+coherent: assert comm(W,j)==scale(j,-ONE)
Cterms=[]
for a in A:
    fa={}
    for edge,(aa,b) in enumerate(edges):
        if aa==a: fa=add(fa,Fedges[edge])
    diag={}; gate={}
    for k,(q,e) in enumerate(states):
        if all(q[c]!=0 for c in A if c!=a): gate[k,k]=ONE
        d=sum(e[edge]*(e[edge]-q[a]) for edge,(aa,b) in enumerate(edges) if aa==a and q[a]!=0 and q[b]==0)
        if d: diag[k,k]=rat(d,2)
    c=mul(add(mul(adj(fa),fa),diag),gate)
    assert c==adj(c) and not comm(W,c)
    Cterms.append(c)
# Preserve decomposition and sequential gate ordering; no global-generator shortcut.
terms=[]
for a in A: terms.append({0:{(k,k):ONE for k,(q,e) in enumerate(states) if q[a]==0}})
for f in Fedges: terms.append({1:scale(add(f,adj(f)),-ONE)})
for c in Cterms: terms.append({2:c})
def grade(a,r): return {k:v for k,v in a.items() if w[k[0]]-w[k[1]]==r}
def off(a): return {k:v for k,v in a.items() if w[k[0]]!=w[k[1]]}
def inv(a): return {k:v/rat(w[k[0]]-w[k[1]]) for k,v in a.items() if w[k[0]]!=w[k[1]]}
def pinv(a): return {k:inv(v) for k,v in a.items() if inv(v)}
def poff(a): return {k:off(v) for k,v in a.items() if off(v)}
gates=[]; stage=[]
for order in range(1,7):
    gs=[inv(term.get(order,{})) for term in terms]; gs=[g for g in gs if g]
    for g in gs:
        assert adj(g)==scale(g,-ONE)
        terms=[conjugate(t,g,order) for t in terms]
        gates.append((g,order))
    total={}
    for term in terms: total=padd(total,term)
    assert not off(total.get(order,{}))
    if order%2: assert not total.get(order,{})
    stage.append({'order':order,'gates':len(gs),'coefficient_entries':len(total.get(order,{}))})
first={}
for g,r in gates:
    if r==1: first=add(first,g)
assert first==add(adj(F),scale(F,-ONE))
H=shift(total,-4); delta=rat(2); kappa=rat(3)
checks=[]
for label,jumps in [('resolved',resolved),('coherent',coherent)]:
    rotated=[]
    for j in jumps:
        jp={0:j}
        for g,r in gates: jp=conjugate(jp,g,r)
        for r in range(1,3):
            assert not grade(jp.get(0,{}),r) and not grade(jp.get(1,{}),r)
        rotated.append(jp)
    def D(X):
        ans={}
        for jp in rotated:
            loss=pmul(padj(jp),jp)
            ans=padd(ans,padd(pmul(pmul(padj(jp),X),jp),pscale(padd(pmul(loss,X),pmul(X,loss)),rat(-1,2))))
        return ans
    def L(X): return padd(pscale(pcomm(H,X),I*delta),pscale(shift(D(X),-2),kappa))
    def B(X): return padd(L(X),pscale(shift(pcomm({0:W},X),-4),-I*delta))
    raw=pscale(shift(D({0:W}),-2),kappa)
    K1=pscale(shift(pinv(poff(raw)),4),I/delta)
    K2=pscale(shift(pinv(poff(B(K1))),4),I/delta)
    minus={}
    for jp in rotated:
        for r in (-1,-2):
            jr={k:grade(v,r) for k,v in jp.items() if grade(v,r)}
            minus=padd(minus,pscale(shift(pmul(padj(jr),jr),-2),kappa*rat(-r)))
    X=padd({0:W},padd(K1,K2)); residual=padd(L(X),minus)
    bad={k:len(v) for k,v in residual.items() if k<2 and v}
    assert not bad,bad
    without2=padd(L(padd({0:W},K1)),minus)
    wrong1=padd(L(padd({0:W},padd(pscale(K1,-ONE),K2))),minus)
    missing2={k:len(v) for k,v in without2.items() if k<2 and v}
    signbad={k:len(v) for k,v in wrong1.items() if k<2 and v}
    assert missing2 and signbad
    checks.append({'instrument':label,'K1_first_power':min(K1),'K2_first_power':min(K2),'residual_powers_below2':bad,'omitted_K2_detected':missing2,'wrong_K1_sign_detected':signbad})
# Cubic support count uses literal periodic vertex/link labels, L=6.
Lsize=6; sites=list(itertools.product(range(Lsize),repeat=3)); Avec=[x for x in sites if sum(x)%2==0]
def nbr(x):
    return [tuple((x[i]+(sg if i==j else 0))%Lsize for i in range(3)) for j in range(3) for sg in (-1,1)]
inc={}; sizes=[]
for a in Avec:
    bs=nbr(a); aas={c for b in bs for c in nbr(b)}
    factors={('v',x) for x in aas|set(bs)}|{('e',tuple(sorted((a,b)))) for b in bs}
    assert len(aas-{a})==18; sizes.append(len(factors))
    for x in factors: inc[x]=inc.get(x,0)+1
assert set(sizes)=={31} and max(inc.values())==19
report={'scope':'Independent exact algebra controls, not volume enumeration or theorem from samples','physical_tree_dimension':n,'physical_basis':[{'q':q,'E':e,'W':w[k]} for k,(q,e) in enumerate(states)],'normal_form_stages':stage,'instruments':checks,'cubic_L6_support_size':31,'cubic_maximum_incidence':19,'bare_leading_rotation_weight':str(mul(adj(F),F).get((index[((1,0,1,0),(0,0,0))],)*2,Z)),'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time(),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'author_code_imported':False,'model_limit':'Actual spin-one physical four-site tree algebra only; cubic uniform estimates are proved analytically. The tree is not a cubic counterexample or convergence test.'}
assert report['peak_rss_bytes']<150000000
Path(__file__).with_name('EXACT_RESULTS.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2,sort_keys=True))
