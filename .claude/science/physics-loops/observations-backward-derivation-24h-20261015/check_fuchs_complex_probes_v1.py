"""Synthetic controls for modulated probes; no experiment record opened."""
import hashlib,json
from pathlib import Path
import numpy as np
import sympy as s
from fuchs_weak_math_v1 import integrals,fit,design
from fuchs_weak_modulated_v1 import modulated_integrals,phase_slope
HERE=Path(__file__).resolve().parent
checks=[]
def ck(name,passed,**extra):checks.append(dict(name=name,passed=bool(passed),**extra))
x,kap=s.symbols('x kap',real=True);p=s.Function('p')(x)
w=p*s.exp(-s.I*kap*x)
ck('first complex derivative',s.simplify(s.diff(w,x)-(s.diff(p,x)-s.I*kap*p)*s.exp(-s.I*kap*x))==0)
ck('second complex derivative',s.simplify(s.diff(w,x,2)-(s.diff(p,x,2)-2*s.I*kap*s.diff(p,x)-kap**2*p)*s.exp(-s.I*kap*x))==0)
Omega=20.;gamma=.004;omega0=20.017;sigma=.031
root=-gamma/2+1j*(np.sqrt(omega0**2-gamma**2/4)-Omega)
tone=.37-.21j
b=((1j*sigma)**2+(gamma+2j*Omega)*(1j*sigma)+(omega0**2-Omega**2+1j*gamma*Omega))*tone/(2j*Omega)
expected=np.array([-gamma/2,(omega0**2-Omega**2)/(2*Omega),b.real,b.imag])
t=np.linspace(0,1200,24001);u=np.exp(1j*sigma*t)
slope,meta=phase_slope(t,u)
ck('affine phase slope',abs(slope-sigma)<1e-14,metadata=meta)
histories=[]
for H in (.8+.2j,-1.1+.4j,.25-1.5j):
    z=H*np.exp(root*t)+tone*u
    rows=modulated_integrals(t,z,u,100.,[0.,slope])
    one=modulated_integrals(t,z,u,100.,[0.])
    old=integrals(t,z,u,100.)
    ck('zero modulation recovers original '+str(H),np.array_equal(np.array([r['moments'] for r in one]),np.array([r['moments'] for r in old])))
    X,y,Z,R=design(rows,Omega)
    residual=float(np.max(abs(R-Z@expected)))
    ck('exact bilinear weak identity '+str(H),residual<1e-10,residual=residual)
    f=fit(rows,Omega);error=float(np.max(abs(np.array(f['parameters'])-expected)))
    ck('two probe parameter recovery '+str(H),f['real_rank']==4 and error<1e-8,error=error)
    ft=fit(rows,Omega,train_count=2*(2*(len(rows)//2)//3))
    ck('chronological prediction '+str(H),ft['validation_residual_rms']<1e-10,residual=ft['validation_residual_rms'])
    fine=fit(modulated_integrals(t,z,u,100.,[0.,slope],4),Omega)
    ck('thinned quadrature '+str(H),max(abs(np.array(fine['parameters'])-expected))<1e-7)
    histories.append(dict(H=[H.real,H.imag],fit=f,chronological=ft))
long=modulated_integrals(t,z,u,600.,[0.,slope])
zero_input=np.linalg.norm([r['moments'][3] for r in long[::2]])
mod_input=np.linalg.norm([r['moments'][3] for r in long[1::2]])
ck('matched tone probe preserves input moment',mod_input>10*zero_input,zero_norm=float(zero_input),modulated_norm=float(mod_input))
ck('window first ordering',all(r['window_index']==j//2 and np.isclose(r['kappa_per_s'],[0.,slope][j%2]) for j,r in enumerate(long)))
out=dict(passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks),checks=checks,histories=histories,
    sources={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('FUCHS_COMPLEX_PROBE_EXTENSION_v1.md','fuchs_weak_math_v1.py','fuchs_weak_modulated_v1.py',Path(__file__).name)},
    raw_data_opened=False,empirical_validation=False)
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
if out['failed']:raise SystemExit(1)
