import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,signal,time,json
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(20,21));signal.alarm(60)
t0,c0=time.monotonic(),time.process_time();out=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929');assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
import numpy as np
from fractions import Fraction
raw=json.loads((out/'DUAL_LIFT.json').read_text());prior=json.loads((out/'DUAL_RESULTS.json').read_text());rows=[]
for n in (32,64):
 q=[np.reshape(2*np.pi*np.arange(n)/n,tuple(n if i==j else 1 for j in range(3))) for i in range(3)]
 ell=6-2*sum(np.cos(x) for x in q);safe=np.where(ell>1e-12,ell,1.)
 for name,data in raw.items():
  total=0.;sectors=[]
  for alpha in range(9):
   field=np.zeros((9,n,n,n),dtype=complex)
   for (a,b,pos),num,den in zip(data['keys'],data['numerators'],data['denominators']):
    if a==alpha:field[(b,)+tuple(x%n for x in pos)]+=int(num)/den/data['raw_common_denominator']
   f=np.fft.fftn(field,axes=(1,2,3));del field
   axnorm=np.sum(abs(f[:3])**2,axis=0);high=abs(np.sum(f[:3],axis=0))**2/3
   energy=(axnorm-high)/safe+high/2
   energy[0,0,0]=high[0,0,0]/2
   index=3
   for i,j in ((0,1),(0,2),(1,2)):
    vv=[-sg/2*(np.exp(1j*sg*q[j])+np.exp(1j*q[i])) for sg in (-1,1)]
    S=1+np.cos(q[i])*np.cos(q[j]);Sn=np.where(S>1e-12,S,1.)
    proj=abs(np.conj(vv[0])*f[index]+np.conj(vv[1])*f[index+1])**2/Sn
    proj=np.where(S>1e-12,proj,0.)
    norm=abs(f[index])**2+abs(f[index+1])**2
    lam=2-S+ell*S;ln=np.where(lam>1e-12,lam,1.)
    part=proj/ln+(norm-proj)/2
    part[0,0,0]=(norm[0,0,0]-proj[0,0,0])/2
    energy+=part;index+=2
   val=float(np.mean(energy).real)/2;sectors.append(val);total+=val
   del f,energy
  qcost=float(Fraction(prior[name]['exact_q_cost']));rows.append({'grid':n,'channel':name,'diagnostic_K2_green_cost':total,'exact_q_cost_display':qcost,'diagnostic_total_dual_cost':qcost+total,'per_residual_type':sectors})
  assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
result={'scope':'Uncertified Riemann sums with singular soft q=0 omitted. No numerical upper/lower bound or convergence rate asserted.','rows':rows,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['peak_rss_bytes']<200000000
(out/'GREEN_DIAGNOSTIC.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
