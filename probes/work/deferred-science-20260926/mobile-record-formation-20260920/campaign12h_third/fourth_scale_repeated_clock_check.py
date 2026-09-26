"""Exact successive formation clocks at a nonvanishing fourth-order scale."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,cmath,math,sys
sys.dont_write_bytecode=True
import numpy as np
import sympy as s
from scipy.sparse.linalg import expm_multiply
from repeated_formation_check import tree_model,superop

HERE=Path(__file__).resolve().parent
OUT=HERE/'FOURTH_SCALE_REPEATED_CLOCK_RESULTS.json'
assert not OUT.exists()
delta=1.3;kappa=.7
model=tree_model(4);T=model['T'];N=np.diag(model['N']);W=np.diag(model['W'])
pn=np.where((N==3)&(W==0))[0];qn=np.where((N==3)&(W==1))[0]
A=s.Matrix(T[np.ix_(qn,pn)]);M=A.T*A
ev=M.eigenvals();assert ev=={s.Integer(0):6,s.Integer(1):3,s.Integer(2):3,s.Integer(3):2,s.Integer(5):3,s.Integer(6):1}
projectors={}
for lam in ev:
 P=s.eye(len(pn))
 for mu in ev:
  if mu!=lam:P=P*(M-mu*s.eye(len(pn)))/(lam-mu)
 assert P*P==P and M*P==lam*P
 projectors[int(lam)]=P
assert sum(projectors.values(),s.zeros(len(pn)))==s.eye(len(pn))
g=model['g'];bright=T@g
assert np.array_equal(bright,np.rint(bright))
bright=bright.astype(int)
weights={}
for kind in ['coherent','resolved']:
 sigma=s.zeros(len(pn))
 for j in model[kind]:
  v=s.Matrix((j@bright)[pn]);sigma+=v*v.T/24
 assert s.trace(sigma)==1
 weights[kind]={lam:s.factor(s.trace(P*sigma)) for lam,P in projectors.items()}
assert weights['coherent']=={0:s.Rational(4,15),1:0,2:s.Rational(1,3),3:0,5:s.Rational(1,15),6:s.Rational(1,3)}
assert weights['resolved']=={0:s.Rational(1,3),1:0,2:s.Rational(1,6),3:0,5:s.Rational(1,3),6:s.Rational(1,6)}

def clock(eps,lam,gap):
 Delta=delta/eps**4;t=delta/eps**3;beta=kappa/eps**2;b=gap*beta
 z=Delta-1j*b;D=cmath.sqrt(z*z+4*lam*t*t)
 assert D.real>0
 slow=-2*lam*t*t/(z+D);gamma=-2*slow.imag;eta=2*b-gamma
 pref=2*b*lam*t*t/abs(D)**2;rate=2*gap*kappa*lam
 assert gamma>0 and eta>0
 terms=[(pref,complex(gamma)),(pref,complex(eta)),
        (-pref,b-1j*D.real),(-pref,b+1j*D.real)]
 integral=sum(c/a for c,a in terms)
 mean=sum(c/(a*a) for c,a in terms)
 exactmean=1/rate+eps**2/(gap*kappa)+gap*kappa*eps**4/(2*lam*delta**2)
 assert abs(integral-1)<2e-12
 assert abs(mean-exactmean)<2e-12
 bound=(abs(pref-rate)+abs(gamma-rate))/gamma+pref/eta+2*pref/b
 return terms,{'lambda':lam,'empty_neighbors_after_hop':gap,'slow_decay':gamma,
  'fast_decay':eta,'prefactor':pref,'limit_rate':rate,'all_time_density_L1_bound':bound,
  'bound_divided_by_epsilon_squared':bound/eps**2,
  'normalization_error':float(abs(integral-1)),'mean':float(mean.real),
  'exact_mean':exactmean,'fourth_order_scale':t**4/Delta**3}

def integral_exp(a,t):
 return -np.expm1(-a*t)/a
def convolution_exp(a,b,t):
 if abs(a-b)<1e-12*max(1,abs(a),abs(b)):return t*np.exp(-a*t)
 return (np.exp(-b*t)-np.exp(-a*t))/(a-b)
def cdf(terms,t):
 z=sum(c*integral_exp(a,t) for c,a in terms)
 assert abs(z.imag)<1e-11
 return float(z.real)
def second_cdf(first,second,t):
 z=sum(c*d/b*(integral_exp(a,t)-convolution_exp(a,b,t)) for c,a in first for d,b in second)
 assert abs(z.imag)<1e-11
 return float(z.real)
def probabilities(first,sub,kind,t):
 p0=1-cdf(first,t)
 p2=sum(float(w)*second_cdf(first,sub[lam],t) for lam,w in weights[kind].items() if lam and w)
 return np.array([p0,1-p0-p2,p2])

rows=[];firstterms={};secondterms={}
for eps in [.2,.1,.05,.025,.0125]:
 first,fr=clock(eps,4,3);firstterms[eps]=first
 sub={};cr=[]
 for lam in [1,2,3,5,6]:
  sub[lam],row=clock(eps,lam,1);cr.append(row)
 secondterms[eps]=sub
 instruments={}
 for kind in weights:
  jointbound=fr['all_time_density_L1_bound']+sum(float(weights[kind][r['lambda']])*r['all_time_density_L1_bound'] for r in cr)
  times=[]
  for tau in [0,.0001,.001,.005,.02,.1,.5,2,5]:
   exact=probabilities(first,sub,kind,tau)
   target=probabilities([(24*kappa,complex(24*kappa))],
     {lam:[(2*kappa*lam,complex(2*kappa*lam))] for lam in sub},kind,tau)
   assert min(exact)>-1e-12 and max(exact)<1+1e-12
   error=float(np.sum(np.abs(exact-target)))
   assert error<=jointbound+1e-11
   times.append({'time':tau,'exact_counts':exact.tolist(),'limiting_counts':target.tolist(),
                'count_L1_error':error})
  instruments[kind]={'joint_waiting_measure_L1_bound':jointbound,
   'counting_path_TV_bound':jointbound/2,'eventual_second_probability':str(1-weights[kind][0]),'times':times}
 rows.append({'epsilon':eps,'first_clock':fr,'later_clocks':cr,'instruments':instruments})

# Direct full 45-state Lindblad control. This is the microscopic generator,
# not a propagation of the reduced waiting-time model.
controls=[]
for eps in [.2,.1]:
 for kind in ['coherent','resolved']:
  L=superop(delta*model['W']/eps**4+delta*model['T']/eps**3,
            [math.sqrt(kappa)*j/eps for j in model[kind]])
  rho0=np.outer(g,g).reshape(-1,order='F')
  actual=expm_multiply(L,rho0,start=0,stop=.1,num=3,traceA=L.diagonal().sum())
  for tau,v in zip([0,.05,.1],actual):
   rho=v.reshape((len(g),len(g)),order='F')
   counts=np.array([np.trace(rho[np.ix_(N==n,N==n)]).real for n in [1,3,5]])
   exact=probabilities(firstterms[eps],secondterms[eps],kind,tau)
   err=float(max(abs(counts-exact)));traceerr=float(abs(np.trace(rho)-1))
   assert err<2e-10 and traceerr<2e-10
   assert np.max(abs(rho-rho.conj().T))<2e-10
   controls.append({'epsilon':eps,'instrument':kind,'time':tau,'microscopic_counts':counts.tolist(),
                    'exact_clock_counts':exact.tolist(),'max_count_difference':err,'trace_error':traceerr})
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'model_builder_sha256':hashlib.sha256((HERE/'repeated_formation_check.py').read_bytes()).hexdigest(),
 'sector_dimension':len(g),'spectral_weights':{kind:{str(lam):str(w) for lam,w in ww.items()} for kind,ww in weights.items()},
 'rows':rows,'full_microscopic_controls':controls,
 'scope':'Exact four-leaf count/waiting laws and analytic all-time L1 bounds; fourth-order scale stays delta. No field loops exist on this star, so this is not a joint photon/formation theorem. Charge marks and quantum output are discarded in the path-law assertion.'}
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'full_microscopic_controls':len(controls),
 'largest_micro_count_difference':max(r['max_count_difference'] for r in controls),
 'smallest_epsilon_joint_L1_bounds':{k:v['joint_waiting_measure_L1_bound'] for k,v in rows[-1]['instruments'].items()},
 'source_sha256':out['source_sha256'],'result_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},indent=2))

