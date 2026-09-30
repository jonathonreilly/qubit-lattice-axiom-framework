import numpy as np
from solve2d_matched import *
R=1
cols=[(('G2',u),None) for u in enum_G2(R)]
# per (type) residual analysis
bytype=defaultdict(lambda: defaultdict(list))
for j,(lab,_) in enumerate(cols):
    fun=lattice_fun2(lab)
    for mono,c in fun.items():
        sl=slots_of2(mono); typ=tuple(t[0] for t in sl)
        bytype[typ][j].append((c,sl))
tgt=defaultdict(list)
for coef,slots in REF2['G2']:
    sl=sorted(slots,key=lambda t:t[0]); typ=tuple(t[0] for t in sl)
    tgt[typ].append((coef,sl))
print("types in lattice:",len(bytype)," types in target:",len(tgt))
for typ in sorted(set(bytype)|set(tgt),key=str):
    m=len(typ); rows=[]; rhs_l=[]
    for D in (0,1):
        for ks in hyperplane_points2(m,npts_for(m,D),seed=7+D):
            row={}
            for j,lst in bytype.get(typ,{}).items():
                v=sum((c*sym_lattice2(sl,ks,D) for c,sl in lst),F(0))
                if v!=0: row[j]=float(v)
            rhs=F(0)
            for coef,sl in tgt.get(typ,[]):
                if sum(n[0]+n[1] for _,n in sl)==D: rhs+=sym_cont2(coef,sl,ks)
            rows.append(row); rhs_l.append(float(rhs))
    js=sorted({j for r in rows for j in r})
    A=np.zeros((len(rows),max(1,len(js)))); 
    idx={j:i for i,j in enumerate(js)}
    for i,r in enumerate(rows):
        for j,v in r.items(): A[i,idx[j]]=v
    bb=np.array(rhs_l)
    sol=np.linalg.lstsq(A,bb,rcond=None)[0] if js else np.zeros(1)
    res=np.linalg.norm(A@sol-bb)
    print(typ, "cols",len(js),"rows",len(rows),"|b|=%.3f"%np.linalg.norm(bb),"resid=%.3e"%res)
