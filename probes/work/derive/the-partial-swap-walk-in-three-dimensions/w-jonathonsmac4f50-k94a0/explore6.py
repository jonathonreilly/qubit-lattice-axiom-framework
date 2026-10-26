import sympy as sp, pickle
c1,c2,c3,s1,s2,s3,C,Sn=sp.symbols('c1 c2 c3 s1 s2 s3 C Sn')
e=sp.symbols('e')
q0,qv=pickle.load(open('S_pal.pkl','rb'))
def ser(x,n):
    return sp.expand(sp.series(x.subs({C:sp.cos(e/2),Sn:sp.sin(e/2)}),e,0,n).removeO())
Q=[ser(x,5) for x in qv]
q1=[x.coeff(e,1) for x in Q]; q3=[x.coeff(e,3) for x in Q]
P=sum(x**2 for x in [c1,c2,c3])
cq3=sum(a*b for a,b in zip([c1,c2,c3],q3))
# omega = eps*w1 + eps^3 w3 ; w1=2|c| ; w3/w1 = c.q3/(2P) + 2P/3
rho=sp.simplify(cq3/(2*P)+2*P/3)   # = w3/w1
# node variables: k = pi/2 + q  ->  c_j=-sin(q_j), s_j=cos(q_j)
t=sp.symbols('t',positive=True)
n1,n2,n3=sp.symbols('n1 n2 n3',real=True)
sub={c1:-sp.sin(t*n1),c2:-sp.sin(t*n2),c3:-sp.sin(t*n3),s1:sp.cos(t*n1),s2:sp.cos(t*n2),s3:sp.cos(t*n3)}
rn=sp.series(rho.subs(sub),t,0,2).removeO()
print('rho at node, series in t (n unit):',sp.simplify(rn))
print('cq3 raw', sp.factor(sp.expand(cq3)))
