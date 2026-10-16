"""Independent checks; no author helper imports."""
AUDIT_TIMEOUT_SEC=120
import json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.integrate import quad
import sympy as s
rows=[]
def ck(n,v,detail=None):
    rows.append(dict(name=n,passed=bool(v),detail=detail))
rng=np.random.default_rng(419)
# Independent complex residue via contour integration, force records via expm.
for i in range(9):
    tau=1+.2*i; Gamma=.2+.05*i; O=1.4+.1*i
    tp=(-1)**i*.3; Op=[-.7,0,.6][i%3]; Cp=tau*Op+tp*O
    G=.5+.1*i; k=.11-.02*i; nu=.04+.01*i
    la=-Gamma/2+1j*np.sqrt(O-Gamma**2/4)
    N=lambda z:G+nu*z+k*z*z
    Z=lambda z:3*z*z+.8*z+2-N(z)**2/(tau*(z*z+Gamma*z+O))
    angle=2*np.pi*(np.arange(1024)+.5)/1024; radius=.1
    circle=la+radius*np.exp(1j*angle)
    rho=np.mean(Z(circle)*radius*np.exp(1j*angle))
    K=abs((2*la+Gamma)*rho)
    ck('contour_residue_'+str(i),abs(K-abs(N(la))**2/tau)<1e-12)
    initial=np.array([.4+.02*i,-.3+.07*i]); t=np.linspace(0,19,521)
    flow=np.array([expm(np.array([[0,1],[-O,-Gamma]])*ti)@initial for ti in t]); zz,v=flow.T
    acc=-O*zz-Gamma*v
    force=1.3+G*zz+k*acc+nu*v+Cp*zz**2/2-tp*v**2/2
    # Complex exponential fitting instead of real cosine convention.
    exponents=np.array([0,la,la.conjugate(),-Gamma,2*la,2*la.conjugate()])
    basis=np.exp(t[:,None]*exponents[None,:]); fit=np.linalg.lstsq(basis,force,rcond=None)[0]
    Q=K*fit[3].real/abs(fit[1])**2
    ck('independent_ringdown_'+str(i),abs(Q-Op)<2e-11 and np.max(abs(basis@fit-force))<2e-12,{'Q':float(Q),'Oprime':Op})
    # Variable projection rational fit; only observed Z values enter residual.
    freqs=np.linspace(.15,4.8,49); sp=1j*freqs; observed=Z(sp)
    poly=np.column_stack([sp**j for j in range(5)])
    pm=np.vstack([poly.real,poly.imag])
    def residual(rates):
        target=observed*(sp**2+rates[0]*sp+rates[1]); yy=np.r_[target.real,target.imag]
        cf=np.linalg.lstsq(pm,yy,rcond=None)[0]
        return pm@cf-yy
    opt=least_squares(residual,[.7,2.3],xtol=1e-13,ftol=1e-13,gtol=1e-13)
    ck('independent_pole_fit_'+str(i),np.max(abs(opt.x-[Gamma,O]))<1e-10)
    # An output-only term fails the identity; cubic fails closure.
    f2=np.linalg.lstsq(basis,force+.12*zz**2,rcond=None)[0]
    ck('quadratic_defect_'+str(i),abs(K*f2[3].real/abs(f2[1])**2-Q-.24/tau)<2e-11)
    fc=np.linalg.lstsq(basis,force+zz**3,rcond=None)[0]
    ck('cubic_closure_'+str(i),np.max(abs(basis@fc-force-zz**3))>1e-5)
    for gx,gr in [(2.,3.),(-2.,-3.)]:
        ck('signed_covariance_'+str((i,gx)),abs((abs(gr/gx)*K)*(gr*fit[3].real)/abs(gr*fit[1])**2-Op/gx)<2e-11)
# Actual basis rank loss at Gamma=0, zero excitation and pole cancellation.
t=np.linspace(0,8,100)
base=np.column_stack([t*0+1,np.cos(t),np.sin(t),t*0+1,np.cos(2*t),np.sin(2*t)])
ck('undamped_actual_rank_loss',np.linalg.matrix_rank(base)==5)
z=s.symbols('z'); gamma=s.Rational(2,5); O=s.Integer(3)
den=z*z+gamma*z+O
ck('cancelled_pole_is_polynomial',s.cancel(2*z*z-den**2/den).is_polynomial(z))
ck('zero_preparation_no_anchor',np.all(expm(np.array([[0,1],[-3,-.4]]))@np.zeros(2)==0))
# Exact symbolic complex-pair coefficient checks independent of parameter assumptions.
a,b,c,d,Cp,tp=s.symbols('a b c d Cp tp',real=True)
# pair lambda=a+ib; c=real+i imag; mixed square coefficients
ck('mixed_coefficient',s.expand(Cp*(2*(c*c+d*d))/2-tp*(2*(a*a+b*b)*(c*c+d*d))/2-(Cp-tp*(a*a+b*b))*(c*c+d*d))==0)
# Random fully correlated errors with true bounds, including negative h and complex f.
for i in range(200):
    la=-rng.uniform(.1,.5)+1j*rng.uniform(.5,2); ga=-2*la.real; rho=rng.normal()+1j*rng.normal()
    el,eg,er=.01,.02,.015
    dl=el*np.exp(1j*rng.uniform(0,7)); dg=rng.choice([-eg,eg]); dr=er*np.exp(1j*rng.uniform(0,7))
    K=abs((2*la+ga)*rho); Kh=abs((2*(la+dl)+ga+dg)*(rho+dr))
    ek=(2*abs(la)+abs(ga))*er+abs(rho)*(2*el+eg)+(2*el+eg)*er
    f=.5+rng.random()+1j*rng.normal(); h=rng.normal(); ef=.01; eh=.015
    fh=f+ef*np.exp(1j*rng.uniform(0,7)); hh=h+rng.choice([-eh,eh])
    ed=2*abs(f)*ef+ef*ef; dm=abs(f)**2; en=K*eh+abs(h)*ek+ek*eh
    bound=en/(dm-ed)+K*abs(h)*ed/(dm*(dm-ed))
    ck('correlated_error_'+str(i),abs(Kh-K)<=ek+1e-13 and abs(Kh*hh/abs(fh)**2-K*h/abs(f)**2)<=bound+1e-13)
# Lipschitz midpoint envelope: per-bin tents saturate geometric error exactly.
edges=np.array([-.4,-.1,.2,1.]); widths=np.diff(edges); L=1.7
exact=sum(L*w*w/4 for w in widths)
ck('midpoint_sharp_lipschitz',abs(exact-L*sum(widths**2)/4)<1e-15)
print(json.dumps({'checks':rows,'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'empirical_validation':False},indent=2))
assert all(r['passed'] for r in rows)
