"""Direct first-order metric curvature and primitive tidal identities."""
import json
import time
import sympy as s

start=time.monotonic()
checks=[]
def check(name,residual):
    v=s.simplify(residual)
    checks.append({'name':name,'pass':bool(v==0),'residual':str(v)})
def truth(name,value):
    checks.append({'name':name,'pass':bool(value)})
t,x,y,z=s.symbols('t x y z',real=True)
coords=[t,x,y,z]
a=s.Function('a')(t)
P=s.Function('Psi')(t,z)
F=s.Function('Phi')(t,z)
g=s.diag(-1,a*a,a*a,a*a)
h=s.diag(-2*P,-2*a*a*F,-2*a*a*F,-2*a*a*F)
gi=g.inv(); hi=-gi*h*gi
G0={};G1={}
for r in range(4):
    for i in range(4):
        for j in range(4):
            G0[r,i,j]=s.simplify(sum(gi[r,d]*(s.diff(g[d,j],coords[i])+s.diff(g[d,i],coords[j])-s.diff(g[i,j],coords[d])) for d in range(4))/2)
            G1[r,i,j]=s.simplify(sum(gi[r,d]*(s.diff(h[d,j],coords[i])+s.diff(h[d,i],coords[j])-s.diff(h[i,j],coords[d]))+hi[r,d]*(s.diff(g[d,j],coords[i])+s.diff(g[d,i],coords[j])-s.diff(g[i,j],coords[d])) for d in range(4))/2)
def riemann(order,i,j):
    G=G0 if order==0 else G1
    v=s.diff(G[0,j,i],t)-s.diff(G[0,0,i],coords[j])
    for l in range(4):
        if order==0:
            v+=G0[0,0,l]*G0[l,j,i]-G0[0,j,l]*G0[l,0,i]
        else:
            v+=G1[0,0,l]*G0[l,j,i]+G0[0,0,l]*G1[l,j,i]-G1[0,j,l]*G0[l,0,i]-G0[0,j,l]*G1[l,0,i]
    return s.simplify(v)
H=s.diff(a,t)/a;Q=s.diff(H,t)+H**2
iso=s.diff(F,t,2)+2*H*s.diff(F,t)+H*s.diff(P,t)+2*Q*P
for i in range(1,4):
    for j in range(1,4):
        R0=riemann(0,i,j);R1=riemann(1,i,j)
        lower0=-R0;lower1=-R1-2*P*R0
        tetrad1=s.simplify((lower1+(-2*P+2*F)*lower0)/a**2)
        expected=s.diff(P,coords[i],coords[j])/a**2+(iso if i==j else 0)
        check(f'direct_tetrad_curvature_{i}{j}',tetrad1-expected)
        check(f'background_tetrad_curvature_{i}{j}',lower0/a**2+(Q if i==j else 0))

k=s.symbols('k',positive=True)
J=s.Function('J')(t);U=s.Function('U')(t)
Psi=U+J;Phi=U-J
Mop=lambda f:s.diff(f,t,2)+2*H*s.diff(f,t)
Aop=lambda f:s.diff(f,t,2)+3*H*s.diff(f,t)+2*Q*f
T=Mop(Phi)+H*s.diff(Psi,t)+2*Q*Psi
L=T-k*k*Psi/a**2
check('lapse_readout',a*a*(T-L)/k**2-Psi)
check('scalar_derivative_readout',(Aop(Psi)-T)/2-Mop(J))
check('constant_kernel',Mop(s.Integer(1)))
kernel=s.Integral(1/a**2,t)
check('second_kernel',Mop(kernel))

# A polynomial fixture supports exact integration without supplied field eqs.
af=1+t;hf=s.diff(af,t)/af;qf=s.diff(hf,t)+hf**2
pf=2+t+3*t*t;ff=1-t+t**3;jf=(pf-ff)/2;kf=s.Integer(2)
tf=s.diff(ff,t,2)+2*hf*s.diff(ff,t)+hf*s.diff(pf,t)+2*qf*pf
lf=tf-kf*kf*pf/af**2
lam=t**3*(1-t)**3
md=s.diff(lam,t,2)-2*s.diff(hf*lam,t)
ad=s.diff(lam,t,2)-3*s.diff(hf*lam,t)+2*qf*lam
wt=af**2*ad/(2*kf*kf)-lam/2;wl=-af**2*ad/(2*kf*kf)
check('weak_exact_polynomial_fixture',s.integrate(s.cancel(md*jf-wt*tf-wl*lf),(t,0,1)))
for point in [0,1]:
    check(f'test_value_endpoint{point}',lam.subs(t,point))
    check(f'test_derivative_endpoint{point}',s.diff(lam,t).subs(t,point))

omega=s.symbols('omega',positive=True)
Fe=s.Function('Fe')(t);Ge=s.Function('Ge')(t)
phase=s.exp(-s.I*omega*t)
ph=Fe*phase;ps=Ge*phase;j=(ps-ph)/2
tt=Mop(ph)+H*s.diff(ps,t)+2*Q*ps
ll=tt-k*k*ps/a**2
jfr=((1+k*k/(a*a*omega**2))*tt-ll)/(2*k*k/a**2)
rem=(s.diff(Fe,t,2)-2*s.I*omega*s.diff(Fe,t)+2*H*(s.diff(Fe,t)-s.I*omega*Fe)+H*(s.diff(Ge,t)-s.I*omega*Ge)+2*Q*Ge)/(2*omega**2)
check('exact_frozen_remainder',(jfr-j)/phase-rem)
# Constant envelopes with nonzero expansion: an exact failure of the frozen map.
rv=s.simplify(rem.subs({Fe:2,Ge:5,a:s.exp(t)}).doit().subs(omega,3))
truth('frozen_map_expansion_error_nonzero',rv!=0)
check('flat_constant_envelope_remainder',s.simplify(rem.subs({Fe:2,Ge:5,a:1}).doit()))
# Metric observation kernel only: not advertised as an Einstein/scalar solution.
fker=-2/(1+t)
check('kernel_zero_transverse',s.diff(fker,t,2)+2*hf*s.diff(fker,t))
truth('kernel_spatial_curvature_can_be_nonzero',-kf*kf*fker != 0)
print(json.dumps({'scope':'First-order supplied FLRW metric observation identities; no empirical or action-solution claim', 'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks),'checks':checks,'frozen_error_witness':str(rv),'weak_moment':str(s.integrate(s.cancel(md*jf),(t,0,1))),'elapsed_seconds':time.monotonic()-start},indent=2))
raise SystemExit(any(not c['pass'] for c in checks))
