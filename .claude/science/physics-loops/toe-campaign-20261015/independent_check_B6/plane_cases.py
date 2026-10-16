import sympy as sp, pickle, time, sys
from polysys import *
rb=pickle.load(open('plane_real_r3.pkl','rb')); nb=len(rb)
X=sp.symbols('x1:%d'%(nb+1))
W=combine(rb,X)
L0=( (0,0,0),(1,0,0) ); Lpi=((0,1,0),(1,0,0)); Ld=((0,0,0),(1,1,0))
c0f=line_coeffs(W,*L0,0); c0g=line_coeffs(W,*L0,1)
cpf=line_coeffs(W,*Lpi,0); cpg=line_coeffs(W,*Lpi,1)
cdf=line_coeffs(W,*Ld,0)
out=open('plane_cases.sing','w')
out.write('option(redSB);\n')
ncase=0; t0=time.time()
for m1 in range(-3,4):
  e2=(-1)**(m1%2)
  for m2 in range(-3,4):
    for m3 in range(0,7):
      if (-1)**(m3%2)!=e2*(-1)**(m2%2): continue
      eqs=lin_eqs_from(c0f,target_cos(1,m1,3))+lin_eqs_from(c0g,target_sin(1,m1,3))
      eqs+=lin_eqs_from(cpf,target_cos(e2,m2,3))+lin_eqs_from(cpg,target_sin(e2,m2,3))
      eqs+=lin_eqs_from(cdf,target_cos(1,m3,6))
      sol=sp.linsolve(eqs,X)
      tag='m1=%d m2=%d m3=%d'%(m1,m2,m3)
      if sol==sp.EmptySet:
          out.write('"%s : linear inconsistent";\n'%tag); continue
      sol=list(sol)[0]
      free=sorted(set().union(*[s.free_symbols for s in sol]),key=str)
      sub=dict(zip(X,sol))
      W2={n:[sp.expand(e.subs(sub)) for e in v] for n,v in W.items()}
      ue=[e for e in unit_eqs(W2) if e!=0]
      ncase+=1
      if not free:
          ok=all(e==0 for e in ue)
          out.write('"%s : no free vars, unitary=%s";\n'%(tag,ok)); continue
      out.write('ring r%d=0,(%s),dp;\n'%(ncase,','.join(map(str,free))))
      out.write('ideal I=%s;\n'%(',\n'.join(to_sing(e) for e in ue) if ue else '0'))
      out.write('ideal J=std(I); "%s nfree=%d dim=",dim(J); if(dim(J)>=0){J;}\nkill r%d;\n'%(tag,len(free),ncase))
out.write('quit;\n'); out.close()
print('cases',ncase,time.time()-t0)
