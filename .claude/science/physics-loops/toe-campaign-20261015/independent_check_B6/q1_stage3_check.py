# Machine check of the hand step: in the stage-2 family, write 1-f = S*p, S=prod sin^2; show p=0 at {0,pi}^3 forces p==0 (f==1).
import sympy as sp, pickle, itertools
from polysys import reim, ii
free,W=pickle.load(open('q1_stage2.pkl','rb'))
z=sp.symbols('z1:4')
F=sum(v[0]*z[0]**(n[0]+3)*z[1]**(n[1]+3)*z[2]**(n[2]+3) for n,v in W.items())
F=sp.expand(F.subs(ii,sp.I))
one=z[0]**3*z[1]**3*z[2]**3
num=sp.expand(one-F)
den=sp.expand(sp.prod([(zz**2-1)**2 for zz in z]))
q,r=sp.div(sp.Poly(num,*z),sp.Poly(den,*z))
print('remainder zero:',r.is_zero)
# 1-f = num/z^3.. ; S = prod sin^2 = prod (-(z^2-1)^2/(4 z^2)) => p = q * (-4)^3 / (z1 z2 z3)
vals=[sp.expand(q.as_expr().subs(dict(zip(z,pt)))) for pt in itertools.product([1,-1],repeat=3)]
lin=[]
for e in vals:
    re,im=reim(e.subs(sp.I,ii)); lin+=[re,im]
lin=[e for e in lin if e!=0]
sol=sp.linsolve(lin,free); sol=list(sol)[0]
q2=sp.expand(q.as_expr().subs(dict(zip(free,sol))))
print('p after 8-point conditions:',q2)
