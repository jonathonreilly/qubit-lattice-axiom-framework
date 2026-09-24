"""Complete physical finite-spin cube, actual canonically prepared first birth.
Personal author consistency control; no imported campaign model or fiber.
The fixed-S epsilon refinement tests the fast-scale theorem, not a spin limit.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/complete_spin_one_cube_control.py',)
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import eigsh,expm_multiply
from scipy.linalg import eigh
HERE=Path(__file__).resolve().parent
A=(0,3,5,6);edges=tuple((a,b) for a in A for b in range(8) if (a^b).bit_count()==1)
inc=np.zeros((12,8),np.int8)
for k,(a,b) in enumerate(edges):inc[k,a]=1;inc[k,b]=-1
fields=np.asarray(list(product((-1,0,1),repeat=12)),np.int8)
charges=fields@inc+np.array([int(x in A) for x in range(8)],np.int8)
valid=np.all(abs(charges)<=1,axis=1);fields=fields[valid];charges=charges[valid]
number=np.sum(charges*charges,axis=1)

def build(N):
 mask=number==N;fs=fields[mask];qs=charges[mask];d=len(fs);index={tuple(f):i for i,f in enumerate(fs)}
 W=np.sum(qs[:,A]==0,axis=1).astype(float);D=np.zeros(d);rr=[];cc=[]
 for col,(q,f) in enumerate(zip(qs,fs)):
  for k,(a,b) in enumerate(edges):
   if q[a] and not q[b]:
    D[col]+=float(f[k]*(f[k]-q[a]));shift=-int(q[a])
    if abs(int(f[k])+shift)<=1:
     ff=f.copy();ff[k]+=shift;row=index[tuple(ff)]
     qq=q.copy();qq[b]=qq[a];qq[a]=0;assert np.array_equal(qq,qs[row])
     rr.append(row);cc.append(col)
 F=coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(d,d)).tocsr()
 Pidx=np.flatnonzero(W==0);P=diags((W==0).astype(float),format='csr')
 Cs=P@F.T@F@P+diags((W==0)*D/2,format='csr')
 return {'N':N,'fields':fs,'charges':qs,'index':index,'W':W,'D':D,'F':F,'Cs':Cs,'P':Pidx,'dim':d}

def jump(before,after,k,sign):
 rr=[];cc=[];a,b=edges[k]
 for col,(q,f) in enumerate(zip(before['charges'],before['fields'])):
  if q[a] or q[b]:continue
  for s in ((1,-1) if sign==0 else (sign,)):
   if abs(int(f[k])+s)>1:continue
   ff=f.copy();ff[k]+=s;row=after['index'][tuple(ff)]
   qq=q.copy();qq[a]=s;qq[b]=-s;assert np.array_equal(qq,after['charges'][row])
   rr.append(row);cc.append(col)
 return coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(after['dim'],before['dim'])).tocsr()

start=time.monotonic();pre=build(4);post=build(6);terminal=build(8)
assert (pre['dim'],post['dim'],terminal['dim'],len(pre['P']))==(3197,5604,672,69)
assert np.max(terminal['W'])==0 and terminal['F'].nnz==0 and terminal['Cs'].nnz==0
initial=np.zeros(pre['dim']);initial[pre['index'][(0,)*12]]=1
marks=[jump(pre,post,0,s) for s in (1,-1,0)]
resolved=[jump(post,terminal,k,s) for k in range(12) for s in (1,-1)]
coherent=[jump(post,terminal,k,0) for k in range(12)]
Gamma=sum(j.T@j for j in resolved);Gcoh=sum(j.T@j for j in coherent)
assert (Gamma-Gcoh).nnz==0
assert (Gamma-diags(Gamma.diagonal())).nnz==0
one=np.flatnonzero(post['W']==1);F=post['F'];G1=(F@F.T-F.T@F)[one,:][:,one].tocsr();Gamma1=Gamma[one,:][:,one].tocsr()
assert np.max(abs((G1-G1.T).data),initial=0)==0
Bcols=np.stack([j@(pre['F']@initial) for j in marks],axis=1)
# This local identity is evaluated from both global paths and the exact
# all-band expansion; no guessed high component is inserted into propagation.
Rcols=np.stack([j@(pre['F']@(pre['F']@initial))/2-F@Bcols[:,i] for i,j in enumerate(marks)],axis=1)
b=np.sum(Bcols*Bcols,axis=0);r=np.sum(Rcols*Rcols,axis=0)
assert np.array_equal(b,[2,2,4]) and np.array_equal(r,[4,2,6])
assert np.linalg.norm(Gamma@Rcols)==0 and np.linalg.norm(post['D'][:,None]*Bcols)==0
assert np.linalg.norm(Rcols*(post['W']-1)[:,None])==0
X=Rcols[one,:]/np.sqrt(b)[None,:]
lowrate=np.array([np.vdot(F@Bcols[:,i],Gamma@(F@Bcols[:,i])).real/b[i] for i in range(3)])
assert np.max(abs(lowrate-8))<1e-12
q=np.sum(X.conj()*(G1@(Gamma1@(G1@X))),axis=0).real
assert np.max(abs(q-np.array([36,18,27])))<1e-12
kappa=.7;delta=1.;T=.3;times=np.linspace(0,T,4)
fast=-1j*delta*G1-kappa*Gamma1/2
faststates=expm_multiply(fast,X,start=0,stop=T,num=4,endpoint=True)
fastnorm=np.sum(abs(faststates)**2,axis=1)
rows=[];spectral=[]
for eps in (.04,.02,.01):
 hpre=diags(pre['W'])-eps*(pre['F']+pre['F'].T)+eps**2*pre['Cs']
 count=len(pre['P']);v0=np.random.default_rng(20260924).normal(size=pre['dim'])
 ev,V=eigsh(hpre,k=count+1,which='SA',tol=1e-12,ncv=180,v0=v0)
 order=np.argsort(ev);ev=ev[order];V=V[:,order]
 assert max(abs(ev[:count]))<.2 and ev[count]>.5
 low=V[:,:count];overlap=low[pre['P'],:]@low[pre['P'],:].T
 gv,gq=eigh(overlap);assert min(gv)>.9
 invroot=(gq*(1/np.sqrt(gv)))@gq.T
 pcol=list(pre['P']).index(pre['index'][(0,)*12])
 dressed=low@low[pre['P'],:].T@invroot[:,pcol]
 assert abs(np.vdot(dressed,dressed)-1)<2e-12
 eig_res=float(np.max(np.linalg.norm(hpre@low-low*ev[:count][None,:],axis=0)))
 assert eig_res<1e-10
 spectral.append({'epsilon':eps,'low_rank':count,'dimension':pre['dim'],'minimum_overlap_eigenvalue':float(min(gv)),'first_excluded_eigenvalue':float(ev[count]),'max_low_eigenvector_residual':eig_res})
 actual=np.stack([j@dressed for j in marks],axis=1);actual/=np.sqrt(np.sum(abs(actual)**2,axis=0))[None,:]
 h=diags(post['W'])-eps*(F+F.T)+eps**2*post['Cs']
 gen=-1j*delta/eps**2*h-kappa*Gamma/2
 evolved=expm_multiply(gen,actual,start=0,stop=T,num=4,endpoint=True)
 for t,states,pred in zip(times,evolved,fastnorm):
  measured=np.sum(states.conj()*(h@states),axis=0).real/eps**2
  second=(1-np.sum(abs(states)**2,axis=0))/eps**2
  predicted_second=kappa*t*lowrate+r/b-pred
  for i,sign in enumerate((1,-1,0)):
   rows.append({'epsilon':eps,'tau':float(t),'physical_time':float(eps**2*t),'first_mark':sign,'scaled_ensemble_energy':float(measured[i]),'fast_survival_prediction':float(pred[i]),'energy_error':float(abs(measured[i]-pred[i])),'second_birth_probability_over_epsilon2':float(second[i]),'second_birth_prediction':float(predicted_second[i]),'second_birth_error':float(abs(second[i]-predicted_second[i]))})
# Convergence check on complete sets, allowing harmless time-zero roundoff.
errors=[]
for eps in (.04,.02,.01):
 rr=[v for v in rows if v['epsilon']==eps]
 errors.append({'epsilon':eps,'max_energy_error':max(v['energy_error'] for v in rr),'max_second_birth_error':max(v['second_birth_error'] for v in rr)})
assert errors[-1]['max_energy_error']<errors[0]['max_energy_error']/6
assert errors[-1]['max_second_birth_error']<errors[0]['max_second_birth_error']/6
result={'scope':'Complete physical spin-one cube; exact canonical low spectral preparation, actual original first mark, complete postbirth no-event evolution and exact terminal energy zero. Fixed-S epsilon refinement, not numerical S-to-infinity proof.','dimensions':{'N4':pre['dim'],'N6':post['dim'],'N8':terminal['dim'],'P_N4':len(pre['P']),'W1_N6':len(one)},'delta':delta,'kappa':kappa,'both_original_instruments_have_identical_Gamma':True,'initial_band_norms':r.tolist(),'initial_jump_norms':b.tolist(),'next_slow_rates':lowrate.tolist(),'spin_one_normalized_Gamma_G1R':q.tolist(),'spectral_checks':spectral,'rows':rows,'errors':errors,'all_assertions_passed':True,'wall_seconds':time.monotonic()-start}
(HERE/'COMPLETE_SPIN_ONE_CUBE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'dimensions':result['dimensions'],'errors':errors,'wall_seconds':result['wall_seconds']},indent=2))
