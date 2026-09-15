"""Exact symbolic controls, no candidate runner or coefficient helper imports."""
import sympy as s,json,time
start=time.monotonic();checks=[]
def ck(n,x):
 assert x,n
 checks.append(n)
# Linear coframe coefficient directly Taylor-expanded in parameter integral.
t,x=s.symbols('t x',real=True);c=s.symbols('c0:4',real=True);es=[1+t*z for z in c];A=[x+(1-x)*e**2 for e in es]
for j in range(4):
 integrand=-x*(2*es[j]**2-sum(e**2 for e in es))*es[j]/A[j]/s.sqrt(s.prod(A))
 derivative=s.integrate(s.diff(integrand,t).subs(t,0),(x,0,1));ck('coframe_linear_'+str(j),s.simplify(derivative+5*c[j]/3-2*sum(c)/3)==0)
# Symmetric tensor covariance extends the diagonal calculation to offdiagonal components.
r=s.symbols('r',positive=True);I0=2/(1+r)**2;Is=2*(2+r)/(3*r*(1+r)**2)
f=s.factor(r*((1+r*r)*Is+(1-3*r*r)*I0)/8);g=(r-1/r)/12;beta=s.factor(f-r*g)
ck('scalar_attraction',s.factor(beta+(r-1)*(r**3+11*r*r+9*r+3)/(12*(r+1)**2))==0)
ck('relative_eigenvalue',s.diff(beta,r).subs(r,1)==-s.Rational(1,2))
# Trace-free W kernel: verify every coefficient rather than sampled directions.
w1,w2,w3,w4,w5=s.symbols('w1:6');W=s.Matrix([[w1,w3,w4],[w3,w2,w5],[w4,w5,-w1-w2]])
n0,k1,k2,k3=s.symbols('n0 k1 k2 k3');k=s.Matrix([k1,k2,k3]);C=s.Matrix([[0,-k3,k2],[k3,0,-k1],[-k2,k1,0]])
K=s.zeros(4);K[0,0]=(k.T*W*k)[0];K[0,1:4]=-n0*(W*k).T;K[1:4,0]=-n0*W*k;K[1:4,1:4]=n0**2*W+C.T*W*C
ck('W_transversality',s.simplify(K*s.Matrix([n0,k1,k2,k3]))==s.zeros(4,1));ck('W_trace',s.expand(s.trace(K))==0)
mean=s.zeros(4)
for j,n in enumerate([n0,k1,k2,k3]):mean+=K.subs({v:int(v==n) for v in [n0,k1,k2,k3]})/4
ck('W_no_linear_fermion_source',mean==s.zeros(4))
# Solve accumulated Maxwell tensor variance without using proposed ODE solution.
z,u=s.symbols('z u',positive=True);f=(1+2*u**-3)/3;m1=s.integrate(f,(u,1,z))/z;m2=s.integrate(f*f,(u,1,z))/z
ck('second_order_variance',s.simplify(2*(m2-m1*m1)-s.Rational(2,5)*(z**-1-z**-6))==0)
# Constitutive mixture coefficient and exact scalar/rank-one exceptions.
a=s.symbols('a',positive=True);weight=s.symbols('weight',positive=True)
for i,V in enumerate([s.diag(a,a,a),s.diag(1,1,a)]):
 ef=V**2/V.det();bf=ef.inv();P=(s.eye(3)+weight*ef)*(s.eye(3)+weight*bf);ck('mixture_exception_'+str(i),s.simplify(P-P[0,0]*s.eye(3))==s.zeros(3))
sh=s.symbols('sh');V=s.diag(1+sh,1-sh,1);ef=V**2/V.det();bf=ef.inv();difference=(1+weight*bf[2,2])/(1+weight*ef[1,1])-(1+weight*bf[1,1])/(1+weight*ef[2,2]);ck('shear_split',s.factor(s.diff(difference,weight).subs(weight,0)+sh**2*(4-sh**2)/(1-sh**2))==0)
# Hall degree from each positive north-pole mass; endpoint regimes exact rational.
for mass,target in [(s.Rational(7,10),1),(s.Rational(9,5),1),(s.Rational(11,5),0),(s.Rational(37,10),0)]:
 degree=sum(sign for value,sign in zip([mass-2,mass,mass,mass+2],[1,-1,-1,1]) if value>0);ck('north_pole_degree_'+str(mass),-degree==target)
# The factor relating determinant to physical polynomial is checked at generic symbolic k.
omega,H=s.symbols('omega H',real=True);q2=(k.T*k)[0];Cz=s.Matrix([[0,-1,0],[1,0,0],[0,0,0]]);wave=(omega**2-q2)*s.eye(3)+k*k.T+s.I*omega*H*Cz
ck('Hall_dispersion_polynomial',s.factor(wave.det()-omega**2*((omega**2-q2)**2-H**2*(omega**2-k1*k1-k2*k2)))==0)
h,q=s.symbols('h q',positive=True);soft=2*q*q/(s.sqrt(h*h+4*q*q)+h);ck('Hall_quadratic_axis',s.limit(soft/q**2,q,0)==1/h)
# Integrating occupied slices: width in physical momentum, not dimensionless k.
kappa,vel,e2,spacing=s.symbols('kappa vel e2 spacing',positive=True);ck('Hall_slice_jacobian',s.simplify(e2*(2*kappa*vel/spacing)/(2*s.pi)**2-e2*kappa*vel/(2*s.pi**2*spacing))==0)
print(json.dumps(dict(status='ok',count=len(checks),checks=checks,elapsed_seconds=time.monotonic()-start,scope='Independent exact algebra and degree count; no primary execution or native quadrature reused.'),indent=2))
