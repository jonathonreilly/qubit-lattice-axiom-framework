import pickle, itertools
from fractions import Fraction as F
d=pickle.load(open('cache.pkl','rb'))
NP,NV,eqs,Bent=d['NP'],d['NV'],d['eqs'],d['Bent']
h=F(1,2)
def proj(sx):  # 2x2 projector onto (1, sx)/sqrt2
    return [[h,h*sx],[h*sx,h]]
Pk=[]
for blk in (0,1):
    for sx in (1,-1):
        P=[[F(0)]*4 for _ in range(4)]
        p=proj(sx)
        for a in range(2):
            for b in range(2): P[2*blk+a][2*blk+b]=p[a][b]
        Pk.append(P)
def rows_for(m):
    rows=[]
    for r in (-1,0,1):
        tgt=[[sum((Pk[k][a][b] for k in range(4) if m[k]==r),F(0)) for b in range(4)] for a in range(4)]
        for a in range(4):
            for b in range(4):
                re,im=Bent[(r,a,b)]
                for part,t in ((re,tgt[a][b]),(im,F(0))):
                    row=[F(0)]*NV
                    for (v,),c in part.items(): row[v]+=c
                    rows.append((row,t))
    return rows
def rref(rows):
    """rows: list of (coeffs, rhs). returns (pivots dict col->(row), consistent)"""
    A=[r[:]+[t] for r,t in rows]
    piv=[];ri=0
    for c in range(NV):
        p=None
        for i in range(ri,len(A)):
            if A[i][c]!=0: p=i;break
        if p is None: continue
        A[ri],A[p]=A[p],A[ri]
        f=A[ri][c]; A[ri]=[x/f for x in A[ri]]
        for i in range(len(A)):
            if i!=ri and A[i][c]!=0:
                g=A[i][c]; A[i]=[x-g*y for x,y in zip(A[i],A[ri])]
        piv.append(c); ri+=1
    cons=all(A[i][NV]==0 for i in range(ri,len(A)))
    return A[:ri],piv,cons
if __name__=='__main__':
    res={}
    for m in itertools.product((-1,0,1),repeat=4):
        A,piv,cons=rref(rows_for(m))
        res[m]=(cons,len(piv))
    ok=[m for m,(c,_) in res.items() if c]
    print(len(ok),ok)
    print(set(r for c,r in res.values()))
