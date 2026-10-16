# Unique Gram matrix Q with phi^T Q phi = 1-|g|^2, phi=(1,e1,e2,e3) in c_a=cos k_a
import sympy as sp
c1,c2,c3,b0,b1,b2,u=sp.symbols('c1 c2 c3 b0 b1 b2 u',real=True)
c=[c1,c2,c3]
g2=0
for a in range(3):
    b_,cc=[c[j] for j in range(3) if j!=a]
    g2+= (1-c[a]**2)*(b0+b1*(b_+cc)+b2*b_*cc)**2
T=sp.expand(1-g2)
e1=c1+c2+c3; e2=c1*c2+c1*c3+c2*c3; e3=c1*c2*c3
phi=[1,e1,e2,e3]
q=sp.symbols('q0:10'); Qs=sp.zeros(4,4); k=0
for i in range(4):
    for j in range(i,4):
        Qs[i,j]=Qs[j,i]=q[k]; k+=1
expr=sp.expand(sum(Qs[i,j]*phi[i]*phi[j] for i in range(4) for j in range(4))-T)
eqs=sp.Poly(expr,c1,c2,c3).coeffs()
sol=sp.solve(eqs,q,dict=True); assert len(sol)==1
Q=sp.simplify(Qs.subs(sol[0])); sp.pprint(Q)
D=sp.factor(Q.det()); print("det Q =",D)
import pickle; pickle.dump(Q,open('Q.pkl','wb'))
# specialization
Qp=Q.subs({b0:sp.Rational(11,30),b2:sp.Rational(3,20)})
Dp=sp.factor(sp.expand(Qp.det().subs(b1,sp.sqrt(u))))
print("det at b0=11/30,b2=3/20 as poly in u=b1^2:",Dp)
P=sp.Poly(sp.numer(sp.together(Dp)),u)
for r in sp.real_roots(P): print(r, sp.N(r,15))
