import sympy as sp, itertools
x=sp.symbols('x1:4'); y=sp.symbols('y1:4')
f=sum(x[i]**2*y[i]**2 for i in range(3))-2*sum(x[i]*x[(i+1)%3]*y[i]*y[(i+1)%3] for i in range(3))+sum(x[i]**2*y[(i+1)%3]**2 for i in range(3))
Mx=sp.hessian(f,x)/2
print(Mx)
for r in range(1,4):
    for S in itertools.combinations(range(3),r):
        m=sp.expand(Mx.extract(list(S),list(S)).det())
        P=sp.Poly(m,*y)
        print(S, m, all(c>=0 for c in P.coeffs()), all(all(e%2==0 for e in mon) for mon in P.monoms()))
