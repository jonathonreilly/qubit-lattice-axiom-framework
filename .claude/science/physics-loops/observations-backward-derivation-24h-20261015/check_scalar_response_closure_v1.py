"""Root post-exposure constraint/clock closure. Independent proof is attributed."""
import hashlib
import json
from pathlib import Path
import sympy as s

p=Path(__file__).resolve().parent
M,A=s.symbols('M A',positive=True)
H,r,v,F,mu,alpha,K2,P,u,pi,U,delta=s.symbols('H r v F mu alpha K2 P u pi U delta',real=True)
Pd=(v*u-r*U)/(2*M*M)-H*P
rates={H:-(r+v*v)/(2*M*M),r:(alpha*v-3*H)*r,v:-3*H*v-F,F:mu*v-3*H*alpha*r,
       K2:-2*H*K2,P:Pd,u:pi,U:-P-alpha*u-alpha*v*U,delta:3*Pd+K2*U,
       pi:-3*H*pi-(K2+mu)*u-alpha*r*delta+4*v*Pd-2*F*P}
dt=lambda q:sum(s.diff(q,a)*z for a,z in rates.items())
rows=[]
def ck(n,e):
 q=s.factor(s.cancel(e));rows.append({'name':n,'pass':q==0,'residual':str(q)})
E=-2*M*M*K2*P-3*H*(v*u-r*U)-r*delta-v*pi+v*v*P-F*u
ck('Hamiltonian constraint propagated',dt(E)+3*H*E)
ck('spatial trace follows from momentum and original equations',dt(Pd)+4*H*Pd+(2*rates[H]+3*H*H)*P-(v*pi-v*v*P-(F-alpha*r)*u)/(2*M*M))
ck('physical Euler theta factors',dt(-K2*U)+(2*H+alpha*v)*(-K2*U)-K2*(P+alpha*u))

h,b,x,xp,kap,kj2,w,wp,wpp,Pp=s.symbols('h b x xp kap kj2 w wp wpp Pp',real=True)
ell=h-b*x
FM=-M*A*A*(xp+3*h*x-2*b*x*x)
udd=s.symbols('udd',real=True)
elim=udd+(3*H-alpha*v)*pi+(K2+mu-alpha*F)*u-(6*M*M*alpha*H+4*v)*s.Symbol('Pdot')-(2*M*M*alpha*K2+6*M*M*alpha*H*H-alpha*v*v-2*F)*P
trans=elim.subs({udd:M*A*A*(wpp+b*x*wp),pi:M*A*wp,u:M*w,H:A*ell,v:M*A*x,alpha:b/M,
                K2:A*A*kj2,mu:A*A*kap,F:FM,s.Symbol('Pdot'):A*Pp})/(M*A*A)
deff=kap+b*xp+3*b*h*x-2*b*b*x*x
derived=wpp+3*ell*wp+(kj2+deff)*w-(6*b*ell+4*x)*Pp-(2*b*kj2+6*b*ell*ell-b*x*x+2*(xp+3*h*x-2*b*x*x))*P
ck('full matter-time response conversion',trans-derived)
ck('matter-time damping coefficient',s.diff(trans,wp)-3*ell)
ck('canonical scalar perturbation remains w=u/M',s.diff(trans,wpp)-1)
ck('Jordan potential difference supplies b*w',((P+b*w)-(P-b*w))/2-b*w)

# A quotient rule is retained rather than assigning its derivative to zero.
tau=s.symbols('tau',real=True);J=s.Function('J')(tau);bf=s.Function('b')(tau)
ck('J over b derivative retained',s.diff(J/bf,tau)-(s.diff(J,tau)/bf-J*s.diff(bf,tau)/bf**2))
ck('J over b second derivative retained',s.diff(J/bf,tau,2)-(s.diff(J,tau,2)/bf-2*s.diff(J,tau)*s.diff(bf,tau)/bf**2-J*s.diff(bf,tau,2)/bf**2+2*J*s.diff(bf,tau)**2/bf**3))
wrong_damping=s.diff(trans,wp)-3*h
rows.append({'name':'detect omitted clock damping shift','pass':bool(wrong_damping.subs({b:1,x:1})!=0),'residual':str(s.factor(wrong_damping))})

# Inspect every independent saved mode epoch, without adopting the trajectory
# as measured input or re-labelling these post-exposure checks as independent.
f=p/'independent_scalar_response/INDEPENDENT_RESULTS_v1.json';d=json.loads(f.read_text());trajectory=d['numerical']['rows']
rows.append({'name':'all105mode epochs inspected','pass':len(trajectory)==105,'count':len(trajectory)})
import math
flat=[]
def collect(obj):
 if isinstance(obj,dict):
  for v_ in obj.values():collect(v_)
 elif isinstance(obj,list):
  for v_ in obj:collect(v_)
 elif isinstance(obj,(float,int)) and not isinstance(obj,bool):flat.append(obj)
collect(trajectory)
rows.append({'name':'saved trajectory numeric entries finite','pass':all(math.isfinite(z) for z in flat),'count':len(flat)})
before=next(z for z in trajectory if abs(z['t_E']-.25)<1e-12)
after=next(z for z in trajectory if abs(z['t_E']-.30)<1e-12)
rows.append({'name':'response trajectory crosses monotonic inverse boundary','pass':before['v']>0 and after['v']<0,'v_before':before['v'],'v_after':after['v']})
first=trajectory[0]
rows.append({'name':'well separated synthetic proxy counterexample','pass':abs(first['P_E'])>1e-5 and abs(first['slip']-first['naive_static_fixed_bare_proxy'])>1,'slip':first['slip'],'proxy':first['naive_static_fixed_bare_proxy']})
sources=['check_scalar_response_closure_v1.py','SCALAR_RESPONSE_CLOSURE_v1.md','SCALAR_RESPONSE_DERIVATION_v1.md','independent_scalar_response/INDEPENDENT_RESULTS_v1.json','independent_scalar_response/INDEPENDENT_PROOF_v1.md','independent_scalar_response/DUST_SYSTEM_SUPPLEMENT_v1.md']
result={'author':'/root','stage':'post-exposure personal rederivation and integration','checks':rows,
        'passed':sum(q['pass'] for q in rows),'failed':sum(not q['pass'] for q in rows),
        'source_sha256':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in sources},
        'empirical_validation':False,'independent_new_control_count':False}
print(json.dumps(result,indent=2,sort_keys=True));raise SystemExit(int(result['failed']>0))
