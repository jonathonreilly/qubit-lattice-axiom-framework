# Impose V(k1,k2,0)=e1*I and V(k1,k2,pi)=e2*I (consequence of the 2D slice theorem) as exact linear constraints
import pickle, sympy as sp, itertools
d=pickle.load(open('param.pkl','rb')); params=d['params']; c0=d['c0']; cu=d['cu']
eqs=pickle.load(open('eqs.pkl','rb'))
names=",".join(map(str,params))
for e1,e2 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    lin=[]
    for n1 in range(-2,3):
        for n2 in range(-2,3):
            for sgn,eps in [(1,e1),(-1,e2)]:
                s0=sum(c0[(n1,n2,n3)]*sp.Integer(sgn)**n3 for n3 in range(-2,3))
                sv=[sum(cu[(n1,n2,n3)][j]*sp.Integer(sgn)**n3 for n3 in range(-2,3)) for j in range(3)]
                if (n1,n2)==(0,0): s0=s0-eps
                for x in [s0]+sv:
                    x=sp.expand(x)
                    for y in (sp.re(x),sp.im(x)):
                        y=sp.expand(y)
                        if y!=0: lin.append(y)
    A,b=sp.linear_eq_to_matrix(lin,params)
    sol=sp.linsolve((A,b),params)
    if not list(sol):
        print('signs',e1,e2,': linear constraints INCONSISTENT (rank A',A.rank(),', rank [A|b]',A.row_join(b).rank(),')'); continue
    sol=list(sol)[0]
    free=sorted(set().union(*[sp.sympify(s).free_symbols for s in sol]),key=str)
    sub=dict(zip(params,sol))
    red=set()
    for e in eqs:
        r=sp.expand(e.subs(sub))
        if r!=0: red.add(r)
    red=sorted(red,key=str)
    print("signs",e1,e2,"rank lin",A.rank(),"free vars",free,"n eqs",len(red))
    tag=("p" if e1==1 else "m")+("p" if e2==1 else "m")
    pickle.dump(dict(sub=sub,free=free,eqs=red),open('red3d_%s.pkl'%tag,'wb'))
    L=[]
    for e in red:
        e=sp.expand(e*sp.lcm([sp.fraction(c)[1] for c in sp.Poly(e,*free).coeffs()]))
        L.append(str(e).replace('**','^'))
    if not free: print("no free vars; eqs:",red); continue
    for ch in ["0","32003"]:
        open('red3d_%s_%s.sing'%(tag,ch),'w').write("""ring r=%s,(%s),dp;
option(redSB);
ideal I=%s;
int t=timer; ideal G=std(I); "time",timer-t; "dim",dim(G); "vdim",vdim(G); "size",size(G);
if(size(G)<40){G;}
LIB "primdec.lib";
list L=minAssGTZ(I); "ncomponents",size(L);
for(int i=1;i<=size(L);i++){"--- component",i, "dim", dim(std(L[i])); L[i];}
quit;
"""%(ch,",".join(map(str,free)),",\n".join(L)))
# exact GB (sympy, over Q) for the surviving sign cases
import os
for tag in ["pp","pm","mp","mm"]:
    f='red3d_%s.pkl'%tag
    if not os.path.exists(f): continue
    r=pickle.load(open(f,'rb'))
    G=sp.groebner(r['eqs'],*r['free'],order='lex')
    sols=sp.solve(G.exprs,r['free'],dict=True)
    full=[{p:sp.sympify(r['sub'][p]).subs(s) for p in params} for s in sols]
    nz=[{str(p):v for p,v in fs.items() if v!=0} for fs in full]
    print(tag,"GB:",G.exprs,"-> solutions (nonzero params only):",nz)
