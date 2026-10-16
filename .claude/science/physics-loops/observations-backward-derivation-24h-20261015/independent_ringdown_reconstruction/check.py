"""Independent inverse, branch, covariance, and error checks; no author imports."""
AUDIT_TIMEOUT_SEC=120
import numpy as np
import sympy as s
import json
from scipy.integrate import quad
rows=[]
def ck(n,c,d=None):rows.append({'name':n,'passed':bool(c),'detail':d})
x,w=s.symbols('x w',real=True)
tau=s.exp(x/5+x*x/20); O=2+x/3+x*x/10; Ga=s.Rational(2,5)+x/30
C=tau*O; gamma=tau*Ga; w0=x*x/7-x/3; E=x*x/2+x**4/30
G=-C*s.diff(w0,x); nu=s.Rational(1,10)+x/40; M=3+x*x/8; d=s.Rational(4,5)
V=E+C*(w-w0)**2/2
ck('constructed_cross',s.simplify(s.diff(V,w,x).subs(w,w0)-G)==0)
ck('constructed_curvature',s.simplify(s.diff(V,x,2).subs(w,w0)-s.diff(E,x,2)-G*G/C)==0)
f=s.lambdify(x,[tau,O,Ga,C,gamma,G,nu,M,d,s.diff(tau,x),s.diff(O,x),s.diff(C,x),s.diff(E,x),s.diff(E,x,2)],'numpy')
for i,xx in enumerate(np.linspace(-.7,.8,17)):
    ta,oo,ga,cc,gm,gg,nn,mm,dd,tp,op,cp,R0,R0p=map(float,f(xx))
    la=-ga/2+1j*np.sqrt(oo-ga*ga/4); aa=2*la+ga; n=gg+nn*la
    rho=-n*n/(ta*aa); prep=.21+(.09+.02*i)*1j
    ff=n*prep; hh=ta*op*abs(prep)**2; g2=(cp-tp*la*la)*prep*prep/2
    K=abs(aa*rho); Q=K*hh/abs(ff)**2; S=-2*aa*rho*g2/(ff*ff); rr=(S-Q)/(oo-la*la)
    ck('inertia_gradient_'+str(i),abs(rr-tp/ta)<2e-14 and abs(Q-op)<2e-14)
    # Reconstruct under a distinct arbitrary unit and reflection.
    tr=2.7*ta; nr=-np.sqrt(2.7)*n; nur=nr.imag/la.imag; gr=nr.real-nur*la.real
    cr=tr*oo; gammar=tr*ga
    for sv in [0,.3j,1.7j,2+.4j]:
        Z=mm*sv**2+dd*sv+R0p+gg*gg/cc-(gg+nn*sv)**2/(ta*(sv*sv+ga*sv+oo))
        P=Z+(gr+nur*sv)**2/(tr*(sv*sv+ga*sv+oo))
        ck('full_response_'+str((i,sv)),abs(P-(mm*sv*sv+dd*sv+R0p+gr*gr/cr))<2e-13)
    cnew=ff/nr
    ck('all_ringdown_coefficients_'+str(i),abs(tr*Q*abs(cnew)**2-hh)<2e-14 and abs(tr*(Q+rr*(oo-la*la))*cnew*cnew/2-g2)<2e-14)
    ck('positive_representative_'+str(i),tr>0 and cr>0 and mm>0 and dd*gammar-nur*nur>0)
    # Nonaffine work-conjugate transform, both orientations.
    for sign in [-1,1]:
        jp=sign*(1+3*xx*xx); jpp=sign*6*xx
        rhoy=rho/jp**2; fy=ff/jp; hy=hh/jp; gy=g2/jp
        Qy=abs(aa*rhoy)*hy/abs(fy)**2; Sy=-2*aa*rhoy*gy/fy**2
        ck('nonaffine_'+str((i,sign)),abs(Qy-Q/jp)<1e-14 and abs((Sy-Qy)/(oo-la*la)-rr/jp)<1e-14)
        # Static derivative chain rule, including connection term.
        Zy0=R0p/jp**2-R0*jpp/jp**3
        Ryder=(R0p/jp-R0*jpp/jp**2)/jp
        ck('static_covariance_'+str((i,sign)),abs(Zy0-Ryder)<1e-14)
# Cross-coordinate congruence: arbitrary nonzero k, and its retained dissipation.
for i in range(25):
    ta=1+.1*i;k=.2-.01*i;ma=2.;ga=.3;nu=.07;da=.8
    T=np.array([[1,0],[-k/ta,1]])
    kinetic=T.T@np.array([[ma,k],[k,ta]])@T
    ray=T.T@np.array([[da,nu],[nu,ga]])@T
    ck('congruence_'+str(i),abs(kinetic[0,1])<1e-14 and abs(kinetic[0,0]-ma+k*k/ta)<1e-14 and abs(ray[0,1]-(nu-ga*k/ta))<1e-14 and np.min(np.linalg.eigvalsh(ray))>0)
# Exact continuum integration, both directions relative to normalization point.
for end in [-.7,.8]:
    integ=quad(lambda xx:.2+.1*xx,.1,end)[0]
    ck('relative_inertia_'+str(end),abs(np.exp(integ)-float(tau.subs(x,end)/tau.subs(x,.1)))<1e-14)
# Smooth winding square root exists, while principal pointwise roots jump.
theta=np.linspace(0,4*np.pi,161); squared=np.exp(1j*theta); branch=np.exp(.5j*theta)
ck('continuous_branch_winding',np.max(abs(branch**2-squared))<1e-14 and np.max(abs(np.diff(branch)))<.05)
ck('principal_branch_not_certificate',np.max(abs(np.diff(np.sqrt(squared))))>1.9)
rng=np.random.default_rng(744)
for i in range(200):
    la=-.3+1.2j;ga=.6;oo=abs(la)**2;rh=.4+.2j;ff=.7-.2j;gg=.08+.11j;qq=.17
    el=.001;egamma=.002;erho=.003;ef=.002;eg=.001;eoo=.004;eq=.003
    dl=el*np.exp(1j*rng.uniform(0,7));dr=erho*np.exp(1j*rng.uniform(0,7));df=ef*np.exp(1j*rng.uniform(0,7));dg=eg*np.exp(1j*rng.uniform(0,7));dga=rng.choice([-1,1])*egamma;do=rng.choice([-1,1])*eoo;dq=rng.choice([-1,1])*eq
    aa=2*la+ga;ah=aa+2*dl+dga;ea=2*el+egamma
    S=-2*aa*rh*gg/ff**2;Sh=-2*ah*(rh+dr)*(gg+dg)/(ff+df)**2
    D=abs(ff)**2;ed=2*abs(ff)*ef+ef**2
    en=2*((abs(aa)+ea)*(abs(rh)+erho)*(abs(gg)+eg)-abs(aa)*abs(rh)*abs(gg))
    es=en/(D-ed)+2*abs(aa)*abs(rh)*abs(gg)*ed/(D*(D-ed))
    L=oo-la*la;Lh=oo+do-(la+dl)**2;el2=eoo+2*abs(la)*el+el**2
    er=(es+eq)/(abs(L)-el2)+abs(S-qq)*el2/(abs(L)*(abs(L)-el2))
    ck('deterministic_errors_'+str(i),abs(Sh-S)<=es and abs((Sh-qq-dq)/Lh-(S-qq)/L)<=er)
result={'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows,'empirical_validation':False}
print(json.dumps(result,indent=2));assert not result['summary']['failed']
