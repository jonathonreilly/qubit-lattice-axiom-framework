"""Independent saved-array cross-check; never executes author source."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,time,json,datetime,hashlib,itertools
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
resource.setrlimit(resource.RLIMIT_CPU,(30,30)); start=time.process_time()
d=Path(__file__).resolve().parent; a=d.parent/'native-threshold-certification-route'
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not any((rt/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
 assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
guard()
import numpy as np
p=np.load(d/'PRE_ARRAYS.npz'); states=p['states']; core=p['core']; F=p['F12']; B=p['B12']; G2=p['G2']; ar=p['A_rows']; ac=p['A_cols']; av=p['A12']
idx={s.tobytes():i for i,s in enumerate(states)}; ci=np.array([idx[s.tobytes()] for s in core]); invcore={int(i):j for j,i in enumerate(ci)}
c=np.load(a/'CORE_TRIAL.npz'); assert np.array_equal(core,c['core']); assert np.array_equal(F[ci],c['F12'])
ad={(i,j):int(v) for i,j,v in zip(c['rows'],c['cols'],c['vals'])}
idc={(invcore[int(i)],int(j)):int(v) for i,j,v in zip(ar,ac,av) if int(i) in invcore}; assert ad==idc
src=np.load(a/'COMPLETE_SOURCE.npz'); si=np.array([idx[s.tobytes()] for s in src['shapes']]); assert np.array_equal(F[si],src['mu_source12']+src['tau_source12']); assert np.array_equal(np.flatnonzero(np.any(F,axis=1)),np.sort(si))
Xi=c['X_numerator']; scale=int(c['scale']); HX=np.zeros_like(F)
for k in range(0,len(av),2048):np.add.at(HX,ar[k:k+2048],av[k:k+2048,None]*Xi[ac[k:k+2048]])
# Bound every integer dot product before using fixed-width evaluation.
rownorm=max(sum(abs(v) for (i,j),v in idc.items() if i==z) for z in range(len(core)))
mx=int(abs(Xi).max()); bound=len(core)*rownorm*mx*mx; assert bound<2**63
assert len(core)*mx*int(abs(F[ci]).max())*scale<2**61
Q=B*scale**2+Xi.T@HX[ci]+scale*(F[ci].T@Xi+Xi.T@F[ci]); qden=12*scale**2
cr=json.loads((a/'CORE_RESULTS.json').read_text()); assert np.array_equal(Q,np.array(cr['upper_pulse_matrix_numerator'],dtype=np.int64)); assert qden==cr['upper_pulse_matrix_denominator']
R=F*scale+HX; rden=12*scale
res=np.load(a/'RESIDUAL.npz'); ri=np.array([idx[s.tobytes()] for s in res['shapes']]); assert int(res['denominator'])==rden; assert np.array_equal(R[ri],res['numerator']); assert np.array_equal(np.flatnonzero(np.any(R,axis=1)),np.sort(ri))
gram=np.zeros((15,15),dtype=object)
for k in range(0,len(R),512):
 z=R[k:k+512].astype(object);gram+=z.T@z
rr=json.loads((a/'RESIDUAL_RESULTS.json').read_text()); assert np.array_equal(gram,np.array(rr['residual_gram_numerator'],dtype=object).astype(object).astype(str).astype(object).astype(object)) if False else True
assert [[str(x) for x in row] for row in gram]==rr['residual_gram_numerator']
new=1920*Q.astype(object)-gram; nd=160*144*scale**2
assert [[str(x) for x in row] for row in new]==rr['improved_upper_pulse_matrix_numerator']; assert nd==rr['improved_upper_pulse_matrix_denominator']
mon=list(itertools.combinations_with_replacement(range(5),2)); E=np.zeros(15,dtype=np.int64); E[mon.index((0,0))]=1;E[mon.index((0,1))]=-1;E[mon.index((1,1))]=1;T=np.zeros(15,dtype=np.int64);T[mon.index((2,2))]=1
fractions={'E1':str(Fraction(int(E@new@E),2*nd)),'T12':str(Fraction(int(T@new@T),2*nd))};assert fractions==rr['exact_normalized_coherent_threshold_upper']
# Metric check without irrational frame arithmetic: these raw vectors have norm4.
assert int(E@G2@E)==4 and int(T@G2@T)==4
# Physical geometry and ordered removal, independently reconstructed.
sub=lambda x,y:tuple(int(i)-int(j) for i,j in zip(x,y))
def isedge(x,y):
 ds=sorted(abs(v) for v in sub(x,y));return ds in ([0,0,2],[0,1,1])
ptypes=[(i,j,s) for i,j in itertools.combinations(range(3),2) for s in (-1,1)]
def identify(edge):
 x,y=sorted(edge);diff=sub(y,x);ii=[i for i,v in enumerate(diff) if v]
 if len(ii)==1:return ii[0],tuple((x[k]+y[k])//2 for k in range(3))
 i,j=ii;assert diff[i]==1
 return 3+ptypes.index((i,j,diff[j])),x
lift=json.loads((a/'DUAL_LIFT.json').read_text());dc=json.loads((a/'DUAL_RESULTS.json').read_text());ds={}
for name,v in [('E1',E),('T12',T)]:
 qcost=Fraction(); g={}; pc=qc=0
 for row,s in zip(R,states):
  val=int(row@v)
  if not val:continue
  S=tuple(tuple(int(t) for t in x) for x in s);aa,bb,cc,dd=S
  pm=[(e,f) for e,f in [((aa,bb),(cc,dd)),((aa,cc),(bb,dd)),((aa,dd),(bb,cc))] if isedge(*e) and isedge(*f)]
  if not pm:
   degrees=[sum(isedge(x,y) for y in S if x!=y) for x in S];D=sum((t-1)*(t-2)//2 for t in degrees);assert D>=1;qcost+=Fraction(val*val,D);qc+=1;continue
  pc+=1;m=len(pm);gn=(6//m)*val;assert m in (1,2,3);keys=[]
  for e,f in pm:
   for residual,removed in [(e,f),(f,e)]:
    alpha,y=identify(residual);beta,x=identify(removed);key=(alpha,beta,sub(x,y));assert key not in g;g[key]=gn;keys.append(key)
  assert sum(g[k] for k in keys)==12*val
 expected={ (int(aa),int(bb),tuple(pos)):Fraction(int(n),int(q)) for (aa,bb,pos),n,q in zip(lift[name]['keys'],lift[name]['numerators'],lift[name]['denominators'])}
 assert len(expected)==len(g);assert all(Fraction(n,12)==expected[k] for k,n in g.items())
 l1=defaultdict(int)
 for (alpha,beta,pos),num in g.items():l1[alpha,beta]+=abs(num)
 lcost=Fraction(sum(x*x for x in l1.values()),144*2*rden*rden);qcost/=2*rden*rden
 assert str(qcost)==dc[name]['exact_q_cost'];assert str(lcost)==dc[name]['exact_sum_channel_l1_squared'];assert pc==dc[name]['perfect_rows'] and qc==dc[name]['nonmatching_rows'];assert len(g)==dc[name]['lift_coordinates']
 ds[name]={'P_rows':pc,'Q_rows':qc,'ordered_coordinates':len(g),'q_cost':str(qcost),'channel_l1_squared':str(lcost)}
 guard()
result={'source_all_coefficients_matched':int(len(si)*15),'core_all_coefficients_matched':len(ad),'residual_all_coefficients_matched':int(len(ri)*15),'rational_upper_all_entries_matched':225,'exact_residual_gram_entries_matched':225,'improved_upper_all_entries_matched':225,'normalized_coherent_upper':fractions,'overflow_bound':bound,'dual':ds,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'primary_arrays_sha256':hashlib.sha256((d/'PRE_ARRAYS.npz').read_bytes()).hexdigest(),'author_report_sha256':hashlib.sha256((a/'REPORT.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2));assert result['cpu_seconds']<30 and result['peak_rss_bytes']<=150*1024**2;guard();(d/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
