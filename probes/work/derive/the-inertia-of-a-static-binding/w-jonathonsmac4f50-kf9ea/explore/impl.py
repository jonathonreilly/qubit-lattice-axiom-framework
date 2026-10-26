import sympy as sp, time
t0=time.time()
z,E,t,m,s=sp.symbols('z E t m s',positive=True)
c=-(1+z)/E
Np=(1+z)/E**2+(1+c**2)/(1-z)+4*m**2*((1+z)/t**2+z**2/(E**2*(1-z)))
S1=-1/E+c/(1-z)
Qp=(1+z)*((2*m/t)**2+(2*m)**2*(z/E-1/t)**2)+(2*m/E)**2*z**2*(1-z)
W=(E*(1+z)*S1+Qp)/(2*Np)
F1=(1+z)**2-z*(E**2-4*m**2)
F2=E*t**2-(2+z)*t-4*m**2*E
# implicit derivatives dE/dz, dt/dz
dEdz=-sp.diff(F1,z)/sp.diff(F1,E)
dtdz=-(sp.diff(F2,z)+sp.diff(F2,E)*dEdz)/sp.diff(F2,t)
dW=sp.diff(W,z)+sp.diff(W,E)*dEdz+sp.diff(W,t)*dtdz
tc=(1+s)/(4*m)
pt={z:-1,E:2*m,t:tc}
def red(e):
    e=sp.together(e); num,den=sp.fraction(e)
    def r(p):
        P=sp.Poly(sp.expand(p),s); out=0
        for (k,),co in P.terms(): out+=co*(64*m**4+1)**(k//2)*s**(k%2)
        return sp.expand(out)
    num=r(num);den=r(den)
    Pd=sp.Poly(den,s);B=Pd.coeff_monomial(s);A=Pd.coeff_monomial(1)
    if B==0: return sp.factor(num/den)
    n2=r(sp.expand(num*(A-B*s)));d2=sp.expand(A**2-B**2*(64*m**4+1))
    return sp.factor(sp.simplify(n2/d2))
print('W(-1)',sp.simplify(W.subs(pt)))
alpha=red(-dW.subs(pt))
print('alpha',alpha, time.time()-t0)
Vc=2*m-tc
u1=red(Vc*(1+4*m**2/tc**2))
print('u1',u1)
dV=red((dEdz-dtdz).subs(pt))
print('dV/dz',dV)

# second order
Ep=dEdz; tp=dtdz
def D(f): return sp.diff(f,z)+sp.diff(f,E)*Ep+sp.diff(f,t)*tp
wr2=1+(2*m/t)**2
V_=E-t
U=V_*wr2*(1+z)/Np          # U(z) (note delta=1+z)
d2W=D(D(W)); d1U=D(U); d2U=D(D(U))
print('building second derivatives', time.time()-t0)
# U is 0 at z=-1 ; need limit: U = (1+z) * G(z) with G finite
G=V_*wr2/Np
d1G=D(G)
U1=red(G.subs(pt))            # U = U1 delta + (dG/dz) delta^2
U2=red(d1G.subs(pt))
W2=red((d2W/2).subs(pt))
print('U1',U1); print('U2',U2); print('W2',W2, time.time()-t0)
lam0=red(alpha/(2*m*U1))
c2=red(W2+lam0*2*m*U2)
print('c2(m)=',c2)
import mpmath as mp
for mv in [4,0.8,0.1]:
    print(mv, sp.N(c2.subs(s,sp.sqrt(64*m**4+1)).subs(m,mv),12), 'lam0',sp.N(lam0.subs(s,sp.sqrt(64*m**4+1)).subs(m,mv),12))

print('---- p4/p2')
p2=(1+(2*m/t)**2)
p4=z**2*(1+(2*m/E)**2)
ratio=p4/p2
r0=red(ratio.subs(pt)); r1=red(D(ratio).subs(pt))
print('ratio at thr',r0,' d/dz',r1)
import sympy
print(sp.N(r1.subs(s,sp.sqrt(64*m**4+1)).subs(m,4)),sp.N(r1.subs(s,sp.sqrt(64*m**4+1)).subs(m,0.1)))
