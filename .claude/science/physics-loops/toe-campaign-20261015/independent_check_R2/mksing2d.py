import pickle, sympy as sp
d=pickle.load(open('slice2d.pkl','rb')); P=d['params']; eqs=d['eqs']
L=[str(sp.expand(e*sp.lcm([sp.fraction(c)[1] for c in sp.Poly(e,*P).coeffs()]))).replace('**','^') for e in eqs]
names=",".join(map(str,P))
open('slice2d.sing','w').write("""ring r=0,(%s),dp;
option(redSB);
ideal I=%s;
int t=timer; ideal G=std(I); "time",timer-t; "dim",dim(G); "vdim",vdim(G); "size",size(G);
LIB "primdec.lib";
list L=minAssGTZ(I); "ncomponents",size(L);
for(int i=1;i<=size(L);i++){"--- component",i, "dim", dim(std(L[i])); L[i];}
quit;
"""%(names,",\n".join(L)))
