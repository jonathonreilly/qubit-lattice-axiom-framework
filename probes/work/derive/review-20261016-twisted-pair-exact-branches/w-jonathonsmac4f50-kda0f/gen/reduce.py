import pickle, itertools
from fractions import Fraction as F
from branches import *
def padd_inplace(r,m,v):
    nv=r.get(m,F(0))+v
    if nv==0: r.pop(m,None)
    else: r[m]=nv
def pmul(p,q):
    r={}
    for m1,v1 in p.items():
        for m2,v2 in q.items():
            padd_inplace(r,tuple(sorted(m1+m2)),v1*v2)
    return r
def branch_reduction(m):
    A,piv,cons=rref(rows_for(m))
    assert cons
    free=[c for c in range(NV) if c not in piv]
    fidx={c:i for i,c in enumerate(free)}
    # var c -> linear poly in new vars (dict mon->coef)
    sub={}
    for c in free: sub[c]={(fidx[c],):F(1)}
    for row,pc in zip(A,piv):
        p={}
        if row[NV]!=0: p[()]=row[NV]
        for c in free:
            if row[c]!=0: padd_inplace(p,(fidx[c],),-row[c])
        sub[pc]=p
    red=set()
    for eq in eqs:
        out={}
        for mon,cf in eq:
            term={():cf}
            for v in mon: term=pmul(term,sub[v])
            for mo,c in term.items(): padd_inplace(out,mo,c)
        if out: red.add(tuple(sorted(out.items())))
    return free,sub,sorted(red)
if __name__=='__main__':
    import collections
    ok=[(-1,1,-1,1),(-1,1,0,0),(-1,1,1,-1),(0,0,-1,1),(0,0,0,0),(0,0,1,-1),(1,-1,-1,1),(1,-1,0,0),(1,-1,1,-1)]
    out={}
    for m in ok:
        free,sub,red=branch_reduction(m)
        degs=collections.Counter(max(len(mo) for mo,_ in e) for e in red)
        consts=sum(1 for e in red if any(len(mo)==0 for mo,_ in e))
        print(m,len(free),len(red),dict(degs),'with const',consts)
        out[m]=(free,sub,red)
    pickle.dump(out,open('red.pkl','wb'))
