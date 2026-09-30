#!/usr/bin/env python3
"""Exact local-source controls, not a finite-density spectral calculation."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict
import json

zero=(0,0,0)
ei=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(s,a): return tuple(s*x for x in a)
def edge(a,b): return tuple(sorted((a,b)))
def accum(rows):
    z=defaultdict(F)
    for e,c in rows:z[e]+=c
    return {e:c for e,c in z.items() if c}
def ds(c):return [edge(add(c,e),add(c,mul(-1,e))) for e in ei]
def vs(c,i,j):return [(edge(add(c,mul(s,ei[i])),add(c,mul(t,ei[j]))),s*t) for s,t in product((1,-1),repeat=2)]
def qrows(c):
    d=ds(c)
    yield F(1,2),{d[0]:1,d[1]:-1}
    yield F(1,6),{d[0]:1,d[1]:1,d[2]:-2}
    for i,j in combinations(range(3),2):yield F(1,4),dict(vs(c,i,j))
def rows(c):
    yield 'mu',F(2,3),dict.fromkeys(ds(c),1)
    for i,j in combinations(range(3),2):
        for (e,a),(f,b) in combinations(vs(c,i,j),2):
            yield 'mu',F(1,4),accum([(e,a),(f,-b)])
    for v in ei:
        for (w,r),(w2,s) in zip(qrows(c),qrows(add(c,v))):
            assert w==w2
            yield 'tau',w,accum(list(s.items())+[(e,-a) for e,a in r.items()])

refs=ds(zero)
for i,j in combinations(range(3),2):
    for eta in (1,-1):refs.append(edge(zero,add(ei[i],mul(eta,ei[j]))))
refmap={e:i for i,e in enumerate(refs)}
G=set(mul(s*2,e) for e in ei for s in (1,-1))
for i,j in combinations(range(3),2):
    G.update(add(mul(s,ei[i]),mul(t,ei[j])) for s,t in product((1,-1),repeat=2))
pins=sorted(edge(zero,d) for d in G);pinmap={e:i for i,e in enumerate(pins)}
K={u:[defaultdict(F) for _ in refs] for u in ('mu','tau')}
P=[[F(0) for _ in pins] for _ in pins]
row_count=0
for c in product(range(-3,4),repeat=3):
    for unit,w,r in rows(c):
        row_count+=1
        for e,a in r.items():
            if e in refmap:
                k=K[unit][refmap[e]]
                for f,b in r.items():k[f]+=w*a*b
            if unit=='mu' and e in pinmap:
                for f,b in r.items():
                    if f in pinmap:P[pinmap[e]][pinmap[f]]+=w*a*b

# Expected pinned matrix from independent physical endpoint classification.
def pclass(e):
    d=e[1] if e[0]==zero else e[0]
    axes=tuple(i for i,x in enumerate(d) if x)
    return axes,d
for a,e in enumerate(pins):
    ca,da=pclass(e)
    for b,f in enumerate(pins):
        cb,db=pclass(f)
        want=F(0)
        if e==f:want=F(2,3) if len(ca)==1 else F(3,2)
        elif len(ca)==2 and ca==cb and sum(x!=y for x,y in zip(da,db))==1:want=F(1,4)
        assert P[a][b]==want,(e,f,P[a][b],want)

def midpoint(e):return tuple(F(x+y,2) for x,y in zip(*e))
def kind(e):
    d=tuple(y-x for x,y in zip(*e)); nz=[i for i,x in enumerate(d) if x]
    if len(nz)==1:return nz[0]
    i,j=nz
    # endpoint sorting makes the first nonzero coordinate positive
    eta=1 if d[i]*d[j]>0 else -1
    return 3+2*list(combinations(range(3),2)).index((i,j))+(0 if eta==1 else 1)

coeff={unit:[[defaultdict(F) for _ in refs] for _ in refs] for unit in K}
row_sums={}
for unit,table in K.items():
    row_sums[unit]=[]
    for a,(e,kr) in enumerate(zip(refs,table)):
        row_sums[unit].append(sum(abs(c) for c in kr.values()))
        assert row_sums[unit][-1] <= (3 if unit=='mu' else 24)
        for f,c in kr.items():
            if not c:continue
            r=tuple(y-x for x,y in zip(midpoint(e),midpoint(f)))
            assert sum(abs(x) for x in r)<=3
            coeff[unit][a][kind(f)][r]+=c
for table in coeff.values():
    for row in table:
        for cr in row:
            for r,c in list(cr.items()):assert cr.get(mul(-1,r),F(0))==c,(r,c,cr)

# h(0)=2 mu Q0 and exact second-order coefficients along six directions.
for unit,table in coeff.items():
    for i,row in enumerate(table):
        for j,cr in enumerate(row):
            want=F(0)
            if unit=='mu':
                if i<3 and j<3:want=F(2,3)
                elif i>=3 and j>=3 and (i-3)//2==(j-3)//2:want=F(1)
            assert sum(cr.values())==want,(unit,i,j,sum(cr.values()),want)
directions=ei+[add(ei[i],ei[j]) for i,j in combinations(range(3),2)]
for q in directions:
    q2=sum(x*x for x in q)
    for unit,table in coeff.items():
        for i,row in enumerate(table):
            for j,cr in enumerate(row):
                actual=-sum(c*sum(a*b for a,b in zip(r,q))**2 for r,c in cr.items())/2
                want=F(0)
                if i<3 and j<3 and unit=='tau':want=q2*((1 if i==j else 0)-F(1,3))
                if i>=3 and j>=3 and (i-3)//2==(j-3)//2:
                    u,v=list(combinations(range(3),2))[(i-3)//2]
                    sign=1 if (i-j)%2==0 else -1
                    if unit=='tau':want=sign*q2
                    else:
                        want=F(sign*(q[u]**2+q[v]**2),4)
                        if i==j:want+=F(q[u]*q[v],2)*(-1 if (i-3)%2==0 else 1)
                assert actual==want,(q,unit,i,j,actual,want)

# Independent full 4-site hard-core action of the actual plane S rows.
sites=[ei[0],mul(-1,ei[0]),ei[1],mul(-1,ei[1])]
siteidx={x:i for i,x in enumerate(sites)};dim=1<<len(sites)
all_edges=sorted(edge(a,b) for a,b in combinations(sites,2))
def zeros():return [[F(0) for _ in range(dim)] for _ in range(dim)]
def mm(A,B):
    C=zeros()
    for i in range(dim):
        for k in range(dim):
            if A[i][k]:
                for j in range(dim):
                    if B[k][j]:C[i][j]+=A[i][k]*B[k][j]
    return C
def plus(A,B,s=1):return [[a+s*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def adj(A):return list(map(list,zip(*A)))
def comm(A,B):return plus(mm(A,B),mm(B,A),-1)
def scale(A,s):return [[s*x for x in r] for r in A]
def annih(e):
    M=zeros(); mask=sum(1<<siteidx[x] for x in e)
    for n in range(dim):
        if n&mask==mask:M[n^mask][n]=1
    return M
B={e:annih(e) for e in all_edges}
H=zeros(); localK=defaultdict(F)
for (e,a),(f,b) in combinations(vs(zero,0,1),2):
    row={e:a,f:-b};L=zeros()
    for g,c in row.items():L=plus(L,scale(B[g],c))
    H=plus(H,scale(mm(adj(L),L),F(1,4)))
    for g,c in row.items():
        for h,d in row.items():localK[g,h]+=F(c*d,4)
N=[]
for x in range(4):
    n=zeros()
    for state in range(dim):n[state][state]=int(bool(state&(1<<x)))
    N.append(n)
A=zeros()
for x,n in enumerate(N):A=plus(A,scale(n,(1,2,4,8)[x]))
# Full carrier identity summed over all four physical endpoints.
left=zeros()
for n in N:left=plus(left,scale(comm(n,comm(H,n)),F(1,2)))
right=scale(H,-2)
for (e,f),c in localK.items():
    right=plus(right,scale(mm(adj(B[e]),B[f]),c*len(set(e)&set(f))))
assert left==right
J=comm(H,A);T=scale(comm(adj(J),comm(H,J)),F(1,2))
Qlift=zeros()
for e in all_edges:
    ie=sum(1<<siteidx[x] for x in e)
    for f in all_edges:
        jf=sum(1<<siteidx[x] for x in f)
        Qlift=plus(Qlift,scale(mm(adj(B[e]),B[f]),T[ie][jf]))
R=plus(T,Qlift,-1)
nonzero=[]
for i,j in product(range(dim),repeat=2):
    if i.bit_count()<=2 or j.bit_count()<=2:assert R[i][j]==0
    if R[i][j]:nonzero.append([i,j,str(R[i][j])])
assert nonzero, 'fixture must exhibit the hard-core higher-occupancy correction'
print(json.dumps({'source_rows':row_count,'pinned_edges':len(pins),
 'exact_row_sums':{k:[str(x) for x in v] for k,v in row_sums.items()},
 'hessian_directions':directions,'full_carrier_sites':sites,
 'nonzero_remainder_entries':nonzero},indent=2))
print('TOTAL PASS=7 FAIL=0')
