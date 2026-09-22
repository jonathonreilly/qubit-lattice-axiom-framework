import numpy as np, math, json
from pathlib import Path
rng=np.random.default_rng(8160)
res={}
# Independent rank-two square root via Cayley-Hamilton on the range; random
# non-curl rank-two matrices probe anisotropic/noncommuting algebra.
errors=[];wrong=[]
for _ in range(30):
 X=rng.normal(size=(2,3)); H=X.T@X
 ev,U=np.linalg.eigh(H); ev[0]=0
 root=(U*np.sqrt(np.maximum(ev,0)))@U.T
 proj=U[:,1:]@U[:,1:].T
 q=np.linalg.det(X@X.T); tr=np.trace(H)
 candidate=(H+np.sqrt(q)*proj)/np.sqrt(tr+2*np.sqrt(q))
 errors.append(float(np.linalg.norm(candidate@candidate-H)))
 wrong.append(float(np.linalg.norm((H+np.sqrt(q)*np.eye(3))/np.sqrt(tr+2*np.sqrt(q))-root)))
assert max(errors)<1e-11 and min(wrong)>1e-3
res['rank_two_square']={'samples':30,'max_square_residual':max(errors),'min_missing_projection_discrepancy':min(wrong)}
# Spectral inequality computed from independent matrix elements, ground
# rank three, arbitrary Hermitian probes, including positive lower bounds.
slack=[]; positive=0
for _ in range(40):
 energies=np.r_[np.zeros(3), rng.uniform(.05,3,5)]
 X=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));F=X+X.conj().T
 X=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));B=X+X.conj().T
 c=abs(np.trace((F@B-B@F)[:3,:3])/3)
 a=np.sum(abs(F[3:,:3])**2,axis=1)/3; b=np.sum(abs(B[3:,:3])**2,axis=1)/3
 mf=energies[3:]@a;mb=energies[3:]@b
 for lam in [.1,.5,1,3,100]:
  lower=c-2*np.sqrt(mf*mb)/lam; actual=sum((a+b)[energies[3:]<=lam]); slack.append(float(actual-lower));positive+=lower>0
assert min(slack)>=-1e-10 and positive
res['degenerate_spectral']={'samples':200,'positive_lower_bound_cases':int(positive),'minimum_slack':min(slack)}
# Rank-one integer Gaussian direct/dual parity identity, independent scalar
# implementation, including non-small coupling.
rows=[]
for g in [.21,.53,1.1]:
 K=1.7; n=range(-100,101); norm=sum(math.exp(-g*g*K*j*j) for j in n)
 overlap=sum(math.exp(-g*g*K*(j*j+(j-1)**2)/2) for j in n)/norm
 weights=[math.exp(-math.pi**2*j*j/(g*g*K)) for j in n]
 dual=math.exp(-g*g*K/4)*sum(w*((-1)**j) for j,w in zip(n,weights))/sum(weights)
 assert abs(overlap-dual)<1e-13
 rows.append({'g':g,'error':abs(overlap-dual)})
res['parity_overlap']=rows
# Explicit wavepacket corollary extremal analytic estimates, not a model run.
g=.1; smin=.99*math.pi*math.sqrt(8/3)/(2+g); smax=math.pi*math.sqrt(8/3)/2; tmax=math.pi*math.sqrt(20/3)/2
Dmax=math.sqrt(smax*smax+2)*(tmax+math.sqrt(240))/(smin*.9)
assert Dmax<27 and smin*.9/2>1
res['soft_corollary']={'D_over_g_upper':Dmax,'weight_over_g_lower':smin*.9/2}
# Root electric commutator by basis action; wrong omission of path square
# is explicitly distinguishable. Charged flux basis choice is unnecessary.
g=.27; e=np.array([.7,1.9,1.2]);p=np.array([1,-1,0]);n=np.array([2,-3,1])
direct=g*g/2*(sum(e*(n+p)**2)-sum(e*n*n));pred=g*g*(e*p)@n+g*g/2*sum(e*p*p)
assert abs(direct-pred)<1e-13 and abs(direct-g*g*(e*p)@n)>.01
res['root_electric']={'identity_error':abs(direct-pred),'omitted_scalar_discrepancy':abs(direct-g*g*(e*p)@n)}
Path('/private/tmp/review-drain-20260915/drain8160-independent-controls.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
