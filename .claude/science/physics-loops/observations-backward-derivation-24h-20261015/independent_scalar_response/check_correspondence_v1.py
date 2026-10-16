"""Post-exposure Eq8 checks on independently frozen trajectory; no ODE rerun."""
import hashlib,json,importlib.util,sys
from pathlib import Path
import numpy as np
O=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent_original',O/'check_independent_v1.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
data=json.loads((O/'INDEPENDENT_RESULTS_v1.json').read_text());rows=data['numerical']['rows'];M=old.M
maxima={x:0. for x in ['deff','seff','damping','response_numerator','error_bound_excess']}
min_den=float('inf');turnings=[];background=rows[::3]
for aa,bb in zip(background[:-1],background[1:]):
 if aa['v']*bb['v']<0:turnings.append([aa['t_E'],bb['t_E']])
for row in rows:
 A=row['A'];al=row['alpha'];H=row['H_E'];v=row['v'];f=row['Fforce'];mu=row['mu_fixed_bare'];b=M*al
 hJ=(H+al*v)/A;x=v/(M*A);xp=(-3*H*v-f-al*v*v)/(M*A*A);kap=mu/(A*A);kJ2=(row['K_E']/A)**2
 deff=kap+b*xp+3*b*hJ*x-2*b*b*x*x
 seff=2*b*xp+6*b*hJ*x+6*b*b*hJ*hJ-12*b**3*hJ*x+(6*b**4-5*b*b)*x*x
 B=6*M*M*al*al*H*H-al*al*v*v-2*al*f
 maxima['deff']=max(maxima['deff'],abs(deff-(mu-al*f)/(A*A)))
 maxima['seff']=max(maxima['seff'],abs(seff-B/(A*A)))
 maxima['damping']=max(maxima['damping'],abs(3*H/A-3*(hJ-b*x)))
 chi=row['chi'];Pi=row['chi_dot'];P=row['P_E'];r=A*row['rho_bare'];U=row['U'];delta=row['delta_bare'];K2=row['K_E']**2
 Pd=(v*chi-r*U)/(2*M*M)-H*P
 Pid=-3*H*Pi-(K2+mu)*chi-al*r*delta+4*v*Pd-2*f*P
 T=(6*M*M*al*al*H+4*al*v)*Pd/P-al/P*(Pid+(3*H-al*v)*Pi)
 c=al*chi/P
 lhs=(K2+mu-al*f)*c;rhs=2*M*M*al*al*K2+B+T
 maxima['response_numerator']=max(maxima['response_numerator'],abs(lhs-rhs))
 den=abs(K2+mu);min_den=min(min_den,den)
 actual=abs(c-2*M*M*al*al*K2/(K2+mu));bound=(abs(al*f*c)+abs(B)+abs(T))/den
 maxima['error_bound_excess']=max(maxima['error_bound_excess'],actual-bound)
checks=[{'name':key,'pass':val<2e-9,'residual':val} for key,val in maxima.items()]
checks += [{'name':'positive naive denominator on finite fixture','pass':min_den>0,'minimum':min_den},{'name':'velocity turning preserved; not one monotonic inverse chart','pass':turnings==[[.24999999999999997,.3]],'brackets':turnings}]
# The exact time samples are emitted as floating values by np.linspace; compare
# the intended bracket numerically, not an accidental decimal display identity.
checks[-1]['pass']=len(turnings)==1 and np.allclose(turnings[0],[.25,.30],rtol=0,atol=1e-14)
r={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'preexposure_results_sha256':hashlib.sha256((O/'INDEPENDENT_RESULTS_v1.json').read_bytes()).hexdigest(),'scope':'Post-exposure correspondence only: Eq8 and exact ratio/error identity on pre-existing independent rows; no new trajectory or empirical input','checks':checks,'passed':sum(bool(q['pass']) for q in checks),'failed':sum(not q['pass'] for q in checks),'maxima':maxima,'minimum_denominator':min_den,'turning_brackets':turnings,'stable_initial_counterexample':rows[0]}
for q in r['checks']:q['pass']=bool(q['pass'])
(O/'CORRESPONDENCE_RESULTS_v1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':r['passed'],'failed':r['failed'],'maxima':maxima,'turning_brackets':turnings},indent=2));assert r['failed']==0
