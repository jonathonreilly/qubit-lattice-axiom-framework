import pickle, sys, time
from fractions import Fraction as F
from poly import *
red=pickle.load(open('red.pkl','rb'))
def key(m): return (len(m),m)
P=2147483629
def inv(a): return pow(a,P-2,P)
def modf(f): return f.numerator%P*inv(f.denominator%P)%P
def independent_subset(eqs):
    piv={};keep=[]
    for idx,e in enumerate(eqs):
        v={mo:modf(c) for mo,c in e}
        while v:
            lead=max(v,key=key)
            if lead in piv:
                c=v[lead]
                for m,x in piv[lead].items():
                    nv=(v.get(m,0)-c*x)%P
                    if nv: v[m]=nv
                    else: v.pop(m,None)
            else:
                ic=inv(v[lead]); piv[lead]={m:x*ic%P for m,x in v.items()}; keep.append(idx); break
    return keep
# item = [poly, cof]  cof: dict gen_index -> poly
def cof_add(c1,c2,s=F(1)):
    r=dict(c1)
    for k,v in c2.items():
        nv=padd(r.get(k,{}),v,s)
        if nv: r[k]=nv
        else: r.pop(k,None)
    return r
def cof_mulpoly(c,q):
    r={}
    for k,v in c.items():
        nv=pmul(v,q)
        if nv: r[k]=nv
    return r
def combine(items,coefs):
    poly={};cof={}
    for it,a in zip(items,coefs):
        poly=padd(poly,it[0],a); cof=cof_add(cof,it[1],a)
    return [poly,cof]
def tracked_echelon(items):
    """degree-ordered echelon with constant coefficients; returns list of (lead, item) with item normalised"""
    piv={}
    for it in items:
        poly,cof=it[0],it[1]
        poly=dict(poly)
        while poly:
            lead=max(poly,key=key)
            if lead in piv:
                c=poly[lead]
                pit=piv[lead]
                poly=padd(poly,pit[0],-c); cof=cof_add(cof,pit[1],-c)
            else:
                ic=1/poly[lead]
                poly=pscale(poly,ic); cof={k:pscale(v,ic) for k,v in cof.items()}
                piv[lead]=[poly,cof]; break
    return piv
def verify_item(it,gens):
    s={}
    for k,c in it[1].items(): s=padd(s,pmul(c,gens[k]))
    return s==it[0]
def cascade(m,verbose=True):
    free,sub,r=red[m]
    keep=independent_subset(r)
    gens={i:{mo:c for mo,c in r[i]} for i in keep}
    items=[[dict(gens[i]),{i:{():F(1)}}] for i in keep]
    elim=[]   # (var, sigma, cof of (x_k - sigma))
    stage=0
    while True:
        piv=tracked_echelon(items)
        if () in piv:
            it=piv[()]
            assert len(it[0])==1
            return ('unit',items,elim,gens,it,keep)
        lin=[(lead,it) for lead,it in piv.items() if len(lead)==1]
        if not lin:
            return ('stuck',[it for it in piv.values()],elim,gens,None,keep)
        # eliminate each linear item: choose highest var lead; process sequentially
        stage+=1
        items=[it for it in piv.values()]
        done=set()
        # repeatedly: pick a deg-1 item
        while True:
            cand=[it for it in items if degp(it[0])==1]
            if not cand: break
            it=cand[0]
            vars_=[mo[0] for mo in it[0] if len(mo)==1]
            k=max(vars_); c=it[0][(k,)]
            sigma={mo:-v/c for mo,v in it[0].items() if mo!=(k,)}
            # cof of (x_k - sigma) = it.cof / c
            cofe={kk:pscale(v,1/c) for kk,v in it[1].items()}
            new=[]
            for jt in items:
                if jt is it: continue
                if any(k in mo for mo in jt[0]):
                    q,rem=divide_linear(jt[0],k,sigma)
                    cof=cof_add(jt[1],cof_mulpoly(cofe,q),F(-1))
                    if rem or cof: new.append([rem,cof])
                else: new.append(jt)
            elim.append((k,sigma,cofe))
            items=new
            if any(degp(x[0])==0 and x[0] for x in items): break
        if verbose: print(m,'stage',stage,'eliminated total',len(elim),'items',len(items),flush=True)
        # constant check happens in next echelon
if __name__=='__main__':
    for m in red:
        t=time.time()
        res=cascade(m)
        print(m,res[0],len(res[2]),'elims',round(time.time()-t,1))
        if res[0]=='unit':
            it=res[4]; gens=res[3]
            print('  verify flat:',verify_item(it,gens),'cof deg',max(degp(v) for v in it[1].values()),'terms',sum(len(v) for v in it[1].values()))
