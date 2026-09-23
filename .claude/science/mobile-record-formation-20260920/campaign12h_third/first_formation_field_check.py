"""First-event field dynamics from the complete microscopic two-record ring sector."""
from pathlib import Path
from itertools import combinations
from datetime import datetime,timezone
import numpy as np
from scipy.linalg import schur,expm,eigh
import json,hashlib,math
HERE=Path(__file__).resolve().parent
OUT=HERE/'FIRST_FORMATION_FIELD_RESULTS.json';assert not OUT.exists()
delta=1.3;kappa=.7;K=1.;J=2*delta;rate=8*kappa
times=[0,.05,.1,.25,.5]
def rotor(cut):
 E=np.arange(-cut,cut+1);H=np.diag(4*K*E*E).astype(float)
 H+=np.diag(np.full(2*cut,-J),1)+np.diag(np.full(2*cut,-J),-1)
 val,V=eigh(H,driver='evd');g=np.zeros(len(E));g[cut]=g[cut+1]=1/math.sqrt(2)
 return E,np.array([math.exp(-rate*t/2)*(V@(np.exp(-1j*val*t)*(V.T@g))) for t in times])
fields,targets=rotor(32);largefields,largetargets=rotor(64)
cuterr=max(np.linalg.norm(np.pad(v,(32,32))-w) for v,w in zip(targets,largetargets))
assert cuterr<1e-12
rows=[]
for S in [2,4,8,16,32]:
 C=S*(S+1);epsilon=math.sqrt(delta/(K*C));bg=(1,0,1,0);states=[]
 for occupied in combinations(range(4),2):
  q=tuple(int(i in occupied) for i in range(4))
  for first in range(-S,S+1):
   E=[first]
   for x in [1,2,3]:E.append(E[-1]+q[x]-bg[x])
   if E[0]-E[-1]+bg[0]-q[0] or max(abs(v) for v in E)>S:continue
   states.append((q,tuple(E)))
 ix={v:i for i,v in enumerate(states)};d=len(states);T=np.zeros((d,d));W=np.zeros(d);loss=np.zeros(d)
 for col,(q,E) in enumerate(states):
  W[col]=sum(q[a]==0 for a in [0,2])
  for e in range(4):
   x,y=e,(e+1)%4
   if not q[x] and not q[y]:loss[col]+=2*(1-E[e]*E[e]/C)
   for a,b,sgn in [(x,y,1),(y,x,-1)]:
    if q[a] and not q[b] and abs(E[e]-sgn)<=S:
     qq=list(q);ff=list(E);qq[a]=0;qq[b]=1;ff[e]-=sgn
     T[ix[(tuple(qq),tuple(ff))],col]-=math.sqrt(1-(E[e]*E[e]-sgn*E[e])/C)
 assert np.max(abs(T-T.T))<1e-14
 H=delta*np.diag(W)/epsilon**4+delta*T/epsilon**3
 NH=H-.5j*kappa*np.diag(loss)/epsilon**2
 tri,V=schur(NH,output='complex')
 residual=float(np.linalg.norm(NH@V-V@tri,2)/max(1,np.linalg.norm(NH,2)))
 orthogonality=float(np.linalg.norm(V.conj().T@V-np.eye(d),2))
 assert residual<1e-12 and orthogonality<1e-12
 g=np.zeros(d);g[ix[bg,(0,0,0,0)]]=g[ix[bg,(1,1,1,1)]]=1/math.sqrt(2)
 coeff=V.conj().T@g;data=[]
 for index,t in enumerate(times):
  actual=V@(expm(-1j*t*tri)@coeff)
  if t==0:assert np.linalg.norm(actual-g)<1e-12
  target=np.zeros(d,complex)
  for i,(q,E) in enumerate(states):
   if q==bg and abs(E[0])<=32:target[i]=targets[index,fields.tolist().index(E[0])]
  # Missing rotor support lies in electric modes absent from the microscopic box.
  tail=float(sum(abs(targets[index,j])**2 for j,e in enumerate(fields) if abs(e)>S))
  na=float(np.vdot(actual,actual).real);nb=math.exp(-rate*t)
  overlap=np.vdot(actual,target)
  nb_numeric=float(np.vdot(target,target).real)+tail
  perpendicular=float(np.linalg.norm(target-actual*overlap/na)**2)+tail
  trace_error=math.sqrt((na-nb_numeric)**2+4*na*perpendicular)
  conditional_error=2*math.sqrt(perpendicular/nb_numeric)
  # The extended exact target includes its omitted spin-box tail, already
  # included in nb; it is orthogonal to actual. This is a full-space comparison.
  assert na>=0 and na<=1+1e-9
  data.append({'time':t,'microscopic_no_event_probability':na,'rotor_no_event_probability':nb,
    'unnormalized_density_trace_error':trace_error,'conditional_field_trace_error':conditional_error,
    'target_electric_tail_probability':tail,'numerical_rotor_norm_defect':abs(nb_numeric-nb),'trace_error_divided_by_epsilon':trace_error/epsilon})
 rows.append({'spin':S,'epsilon':epsilon,'N2_sector_dimension':d,
   'Schur_basis_orthogonality':orthogonality,'relative_Schur_residual':residual,'times':data})
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'delta':delta,'kappa':kappa,'K':K,'J':J,'first_rate':rate,
 'rotor_cutoff':32,'rotor_refinement_cutoff':64,'rotor_state_refinement_norm':float(cuterr),
 'rows':rows,'scope':'Complete microscopic pre-first-event two-record sector on a genuine four-edge cycle, compared to finite-rate killed rotor field dynamics. Full electric-tail contribution retained. No post-formation field approximation or volume limit.'}
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'source_sha256':out['source_sha256'],'result_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
 'largest_refinement_error':float(cuterr),'largest_spin_last_time':rows[-1]['times'][-1]},indent=2))
