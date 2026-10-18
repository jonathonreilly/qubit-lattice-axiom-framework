"""B17: does an anisotropic (uniaxial) Weyl cone close against an isotropic structure function?
Continuum, leading order.

Smeared Weyl operator: h_N = (1/2) sum_j v_j {N, sigma^j (-i d_j)}.
Compute [h_N, h_M] acting on a test spinor and extract the derivative part. The isotropic
case reproduces B15's -v^2 L_w (Kosmann). Then test whether the anisotropic bracket equals
kappa * (isotropic relabelling along w) for any kappa.
"""
import sympy as sp
x,y,z=sp.symbols('x y z',real=True); X=(x,y,z)
N=sp.Function('N')(*X); M=sp.Function('M')(*X)
f1=sp.Function('f1')(*X); f2=sp.Function('f2')(*X)
s=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
def h(L,v,psi):
    out=sp.zeros(2,1)
    for j in range(3):
        d=lambda u: sp.diff(u,X[j])
        out+= v[j]*sp.Rational(1,2)*(L*(s[j]*(-sp.I)*psi.applyfunc(d)) + s[j]*(-sp.I)*(L*psi).applyfunc(d))
    return out
psi=sp.Matrix([f1,f2])
def comm(v): return (h(N,v,h(M,v,psi))-h(M,v,h(N,v,psi))).applyfunc(sp.expand)
def kosmann(xi,psi):
    # L_xi psi = xi.grad psi + (1/2) div xi psi + (i/4) (curl xi).sigma psi
    div=sum(sp.diff(xi[j],X[j]) for j in range(3))
    curl=[sp.diff(xi[2],y)-sp.diff(xi[1],z), sp.diff(xi[0],z)-sp.diff(xi[2],x), sp.diff(xi[1],x)-sp.diff(xi[0],y)]
    out=sum((xi[j]*psi.applyfunc(lambda u: sp.diff(u,X[j])) for j in range(3)),sp.zeros(2,1))
    out+=sp.Rational(1,2)*div*psi + sp.I/4*sum((curl[j]*s[j] for j in range(3)),sp.zeros(2,2))*psi
    return out
w=[N*sp.diff(M,X[j])-M*sp.diff(N,X[j]) for j in range(3)]
npass=0; nfail=0
def check(name,cond):
    global npass,nfail
    print(("PASS " if cond else "FAIL ")+name); npass+=bool(cond); nfail+=(not cond)
v=sp.symbols('v',positive=True)
r=(comm([v,v,v])+v**2*kosmann(w,psi)).applyfunc(sp.simplify)
check("isotropic: [h_N,h_M] = -v^2 L_w (Kosmann), reproduces B15 C2", r==sp.zeros(2,1))
va,vt,kap=sp.symbols('v_a v_t kappa',positive=True)
C=comm([vt,vt,va])
# first-derivative content of C along each direction: coefficient of d_j f1 in component 0
coef=[sp.simplify(sp.expand(C[0]).coeff(sp.diff(f1,X[j]))) for j in range(3)]
print("anisotropic derivative coefficients (comp 0, d_j f1):",coef)
check("anisotropic: derivative part is -v_j^2 w_j d_j (direction-dependent shift)",
      all(sp.simplify(coef[j]+[vt,vt,va][j]**2*w[j])==0 for j in range(3)))
# can it equal -kappa L_w for any kappa? Solve on the derivative part.
eqs=[sp.simplify(coef[j]+kap*w[j]) for j in range(3)]
sol=sp.solve([sp.expand(e).coeff(sp.diff(M,X[j])*N) for j,e in enumerate(eqs)],[kap,va],dict=True)
print("solutions for kappa, v_a:",sol)
check("closure against an isotropic relabelling forces v_a = v_t (=sqrt kappa)",
      all(s_.get(va)==vt for s_ in sol) and len(sol)>0)
# corner-step numbers
import math
vk=math.sqrt(2)/3; vax,vtr=0.2467,0.5838
check("the corner step's doubler cone (0.2467, 0.5838) is not the +-k* cone sqrt2/3: closure fails for the eight-node step",
      abs(vax-vk)>0.05 and abs(vtr-vk)>0.05)
print(f"TOTAL: PASS={npass} FAIL={nfail}")
