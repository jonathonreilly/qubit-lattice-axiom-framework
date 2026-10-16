"""Synthetic/symbolic checks only; never opens raw experiment records."""
import hashlib,json
from pathlib import Path
import numpy as np
import sympy as s
from fuchs_weak_math_v1 import integrals,fit,design

HERE=Path(__file__).resolve().parent
checks=[]
def ck(name,passed,**kw):checks.append(dict(name=name,passed=bool(passed),**kw))
def zero(name,expr):
    residual=s.simplify(expr);ck(name,residual==0,residual=str(residual))
m,M,k,c,K,C,w,gt,gp,fp,f=s.symbols("m M k c K C w gt gp fp f")
Z=k+s.I*w*c;D=Z-m*w**2;P=K-M*w**2+s.I*w*C
Delta=D*P-m*w**2*Z
q=(m*P*gt+m*w**2*(M*gp+fp)+(P-m*w**2)*f)/Delta
X=((M*gp+fp-f)*D+Z*(m*gt+f))/Delta
zero("test-body equation",D*q-m*w**2*X-m*gt-f)
zero("support equation",P*X-Z*q-M*gp-fp+f)
zero("internal calibration numerator",s.diff(q,f)-(P-m*w**2)/Delta)
zero("uniform free-support source cancellation",q.subs({K:0,C:0,fp:0,f:0,gp:gt}))
zero("external force reaction differs",P/Delta-(P-m*w**2)/Delta-m*w**2/Delta)
a,nu,Om,lam=s.symbols("a nu Om lam",real=True)
operator=lam**2+(-2*a+2*s.I*Om)*lam+2*Om*nu-2*s.I*Om*a
weak=lam-s.I*lam**2/(2*Om)-a*(1-s.I*lam/Om)-s.I*nu
zero("exact carrier/adjoint normalization",2*s.I*Om*weak-operator)
ss=s.symbols("ss",real=True);poly=140*ss**3*(1-ss)**3
zero("window unit integral",s.integrate(poly,(ss,0,1))-1)
for endpoint in (0,1):
    zero("window zero "+str(endpoint),poly.subs(ss,endpoint))
    zero("window derivative zero "+str(endpoint),s.diff(poly,ss).subs(ss,endpoint))
# Distinct arbitrary homogeneous histories with a persistent tone.
Omega=20.;gamma=.004;omega0=20.017;sigma=.031
root=-gamma/2+1j*(np.sqrt(omega0**2-gamma**2/4)-Omega)
tone=.37-.21j
b=((1j*sigma)**2+(gamma+2j*Omega)*(1j*sigma)
   +(omega0**2-Omega**2+1j*gamma*Omega))*tone/(2j*Omega)
expected=np.array([-gamma/2,(omega0**2-Omega**2)/(2*Omega),b.real,b.imag])
records=[]
for H in (.8+.2j,-1.1+.4j,.25-1.5j):
    t=np.linspace(0,1200,24001);u=np.exp(1j*sigma*t)
    z=H*np.exp(root*t)+tone*u
    rows=integrals(t,z,u,100.)
    fitout=fit(rows,Omega)
    error=float(np.max(np.abs(np.array(fitout["parameters"])-expected)))
    ck("independent homogeneous history "+str(H),fitout["real_rank"]==4 and error<1e-9,
       parameter_max_abs_error=error)
    ck("manufactured weak residual "+str(H),fitout["train_residual_rms"]<1e-10,
       residual_rms=fitout["train_residual_rms"])
    coarse=fit(integrals(t,z,u,100.,4),Omega)
    coarseerr=float(np.max(np.abs(np.array(coarse["parameters"])-expected)))
    ck("quadrature refinement "+str(H),coarseerr<1e-7,
       coarse_error=coarseerr,fine_error=error)
    records.append(dict(H=[H.real,H.imag],fine=fitout,coarse=coarse))
# A single steady tone carries only one complex equation.
z=tone*u;rows=integrals(t,z,u,100.)
XX,yy,ZZ,RR=design(rows,Omega)
sing=np.linalg.svd(XX/np.linalg.norm(XX,axis=0),compute_uv=False)
ck("monochromatic practical rank loss",sing[2]<1e-8,
   normalized_singular_values=sing.tolist(),numerical_quadrature_prevents_symbolic_rank_claim=True)
zero("analytic monochromatic weak identity",weak.subs(lam,s.I*sigma)-operator.subs(lam,s.I*sigma)/(2*s.I*Om))
# A common filter acts on each exponential by the same multiplier on both sides.
# Different channel filters multiply b by their ratio, so b is not registered.
p,hq,hu,beta=s.symbols("p hq hu beta",nonzero=True)
zero("common-filter commutation",p*hq-beta*hq*(p/beta))
ck("different-filter ambiguity",complex((hq/hu).subs({hq:2,hu:3}))!=1,
   meaning="Unknown receiver/source filter ratio changes inferred forcing coefficient")
ck("source square magnitude positive",abs(b)>0)
out=dict(passed=sum(x["passed"] for x in checks),failed=sum(not x["passed"] for x in checks),
         checks=checks,expected_parameters=expected.tolist(),manufactured=records,
         sources={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in
          ("FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v1.md","fuchs_weak_math_v1.py",Path(__file__).name)},
         raw_data_opened=False,empirical_validation=False)
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
if out["failed"]:raise SystemExit(1)
