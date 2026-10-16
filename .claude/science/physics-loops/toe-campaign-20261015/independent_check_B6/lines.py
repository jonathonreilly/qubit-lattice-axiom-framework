import sympy as sp, pickle, sys
LINES={'L1':((0,0,0),(1,0,0)),'L2':((0,0,1),(1,0,0)),'L3':((0,1,1),(1,0,0)),
       'L4':((0,0,0),(1,1,0)),'L5':((0,0,1),(1,1,0)),'L6':((0,0,0),(1,1,1))}  # p in units of pi
def restrict(b,p,a):
    out={}
    for n,v in b.items():
        s=(-1)**(sum(pi*ni for pi,ni in zip(p,n))%2)
        j=sum(ai*ni for ai,ni in zip(a,n))
        o=out.setdefault(j,[0]*4)
        for c in range(4): o[c]+=s*v[c]
    return out
def line_matrix(rb,names):
    rows=[]
    for nm in names:
        p,a=LINES[nm]
        R=[restrict(b,p,a) for b in rb]
        js=sorted({j for r in R for j in r})
        for j in js:
            for c in range(4):
                rows.append([sp.expand(r.get(j,[0]*4)[c]) for r in R])
    return sp.Matrix(rows)
if __name__=="__main__":
    rb=pickle.load(open(sys.argv[1],'rb'))
    M=line_matrix(rb,list(LINES))
    print('vars',len(rb),'rank of all-lines restriction',M.rank())
    for nm in LINES: print(nm, line_matrix(rb,[nm]).rank())
def line_matrix_comp(rb,spec):
    """spec: list of (linename, components list)"""
    rows=[]
    for nm,comps in spec:
        p,a=LINES[nm]
        R=[restrict(b,p,a) for b in rb]
        js=sorted({j for r in R for j in r})
        for j in js:
            for c in comps:
                rows.append([sp.expand(r.get(j,[0]*4)[c]) for r in R])
    return sp.Matrix(rows)
