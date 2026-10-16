import pickle, sympy as sp, sys
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
char=sys.argv[1]; out=sys.argv[2]
names=",".join(str(p) for p in params)
L=[]
for e in eqs:
    e=sp.expand(e*sp.lcm([sp.fraction(c)[1] for c in sp.Poly(e,*params).coeffs()]))
    L.append(str(e).replace('**','^'))
with open(out,'w') as f:
    f.write("ring r=%s,(%s),dp;\noption(redSB);\nideal I=\n%s;\n"%(char,names,",\n".join(L)))
    f.write('int t=timer; ideal G=std(I); "time",timer-t; "dim",dim(G); "vdim",vdim(G); "size",size(G);\n')
    f.write('if(size(G)<60){G;}\n')
    f.write('write(":w %s.gb",G);\nquit;\n'%out)
