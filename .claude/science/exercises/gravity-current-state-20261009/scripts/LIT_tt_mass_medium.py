# Check: TT graviton mass term from a medium L = sqrt(g) F(Y), Y^{ij} = g^{ij} (static, comoving labels phi^i = x^i),
# expanded to 2nd order in a spatial TT perturbation h. Solid: F(I1,I2,I3) generic isotropic. Fluid: F(I3) only.
# Impose Minkowski background (zero stress: F=0 and dF/dY^{ij}=0 at Y=delta). Report coefficient of h_ij h_ij.
import sympy as sp
e=sp.symbols('e')
a,b=sp.symbols('a b')
# a TT h: traceless, symmetric, transverse to k=z: h = [[a,b,0],[b,-a,0],[0,0,0]]
h=sp.Matrix([[a,b,0],[b,-a,0],[0,0,0]])*e
g=sp.eye(3)+h
ginv=(sp.eye(3)-h+h*h)  # to O(e^2)
sqrtg=sp.sqrt(g.det())
I1,I2,I3=sp.symbols('I1 I2 I3')
F=sp.Function('F')
Y=ginv
inv={I1:Y.trace(), I2:(Y*Y).trace(), I3:Y.det()}
# generic isotropic F(I1,I2,I3): Taylor to 2nd order around (3,3,1)
d1,d2,d3=sp.symbols('F1 F2 F3'); F0=sp.Symbol('F0')
H=sp.Matrix(3,3,lambda i,j: sp.Symbol('F%d%d'%tuple(sorted((i+1,j+1)))))
dI=sp.Matrix([inv[I1]-3,inv[I2]-3,inv[I3]-1])
Fexp=F0+ (sp.Matrix([d1,d2,d3]).T*dI)[0] + sp.Rational(1,2)*(dI.T*H*dI)[0]
L=sp.series(sp.expand(sqrtg*Fexp),e,0,3).removeO()
L2=sp.simplify(L.coeff(e,2)); L1=sp.simplify(L.coeff(e,1))
print("O(h) term:",L1)
print("O(h^2) term, solid:",sp.factor(L2))
# zero background stress: T_ij ~ dL/dg at flat: compute with a general (not TT) uniform perturbation
s=sp.symbols('s0:6'); hg=sp.Matrix([[s[0],s[3],s[4]],[s[3],s[1],s[5]],[s[4],s[5],s[2]]])*e
gg=sp.eye(3)+hg; Yg=sp.eye(3)-hg
Lg=sp.series(sp.sqrt(gg.det())*(F0+d1*(Yg.trace()-3)+d2*((Yg*Yg).trace()-3)+d3*(Yg.det()-1)),e,0,2).removeO().coeff(e,1)
print("stress (linear in general h):",sp.factor(sp.expand(Lg)))
sol=sp.solve([sp.expand(Lg).coeff(s[0]), sp.expand(Lg).coeff(s[3])],[F0,d1],dict=True)
print("zero-stress conditions:",sol)
L2z=sp.factor(L2.subs(sol[0]))
print("O(h^2) at zero stress, solid:",L2z)
print("fluid (F depends on I3 only: F1=F2=F11=F12=F22=F13=F23=0):",sp.factor(L2z.subs({d2:0,'F11':0,'F12':0,'F22':0,'F13':0,'F23':0})))
print("fluid, corrected (F1=F2=0):", sp.factor(L2z.subs({d1:0,d2:0})))
# Shear modulus of the solid: second-order energy for a static spatial strain of the MEDIUM (phi^i = x^i + u^i) at flat metric
# equals the same quadratic form with h -> 2 sym grad u (Stueckelberg), so TT mass^2 coefficient = shear-modulus combination.
