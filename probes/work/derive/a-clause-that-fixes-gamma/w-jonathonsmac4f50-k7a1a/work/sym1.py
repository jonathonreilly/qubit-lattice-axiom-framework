import sympy as sp
t=sp.symbols('t',real=True)
k1,k2,k3=sp.symbols('k1 k2 k3',real=True)
s=[sp.sin(k1),sp.sin(k2),sp.sin(k3)]
d1=sp.Matrix(s)
d2=sp.Matrix([sp.sin(k1+t),s[1],s[2]])
r1=sp.sqrt(sum(x**2 for x in d1)); r2=sp.sqrt(sum(x**2 for x in d2))
a=(d1+d2)/2
n1=d1/r1; n2=d2/r2
dot=lambda x,y:(x.T*y)[0]
t1=sp.Rational(1,4)*(-dot(n1,d2)-r1)
num=sp.Rational(1,2)*(dot(a,a)*(1+dot(n1,n2))-2*dot(a,n1)*dot(a,n2))
t2=-num/(r1+r2)
f=t1+t2
ftt=sp.diff(f,t,2).subs(t,0)
ftt=sp.simplify(ftt)
print(ftt)
import pickle
open('ftt.txt','w').write(sp.srepr(ftt))
# also f0, f_t
print(sp.simplify(sp.diff(f,t).subs(t,0)))
print(sp.simplify(f.subs(t,0)))
