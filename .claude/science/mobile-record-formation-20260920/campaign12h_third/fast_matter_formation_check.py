"""Finite fast-matter/fourth-order Hamiltonian with finite formation controls."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import sys,json,hashlib,math
sys.dont_write_bytecode=True
import numpy as np
from scipy.linalg import eigh,eigvalsh
from scipy.sparse.linalg import expm_multiply
from repeated_formation_check import tree_model,superop

HERE=Path(__file__).resolve().parent
OUT=HERE/'FAST_MATTER_FORMATION_RESULTS.json';assert not OUT.exists()
delta=1.3;kappa=.7

def ring(S):
 C=S*(S+1);bg=(1,0,1,0);states=[]
 for q in product((-1,0,1),repeat=4):
  if sum(q)!=2:continue
  for first in range(-S,S+1):
   E=[first]
   for x in [1,2,3]:E.append(E[-1]+q[x]-bg[x])
   if E[0]-E[-1]+bg[0]-q[0] or max(abs(e) for e in E)>S:continue
   states.append((q,tuple(E)))
 ix={v:i for i,v in enumerate(states)};D=len(states);T=np.zeros((D,D));rs=[];cs=[]
 for e in range(4):
  x,y=e,(e+1)%4;js=[]
  for charge in [-1,1]:
   j=np.zeros((D,D))
   for col,(q,E) in enumerate(states):
    if q[x]==q[y]==0 and abs(E[e]+charge)<=S:
     qq=list(q);ee=list(E);qq[x]=charge;qq[y]=-charge;ee[e]+=charge
     j[ix[tuple(qq),tuple(ee)],col]=math.sqrt(1-(E[e]**2+charge*E[e])/C)
   js.append(j);rs.append(j)
  cs.append(js[0]+js[1])
  for col,(q,E) in enumerate(states):
   for a,b,sg in [(x,y,1),(y,x,-1)]:
    if q[a] and not q[b] and abs(E[e]-sg*q[a])<=S:
     qq=list(q);ee=list(E);charge=q[a];qq[a]=0;qq[b]=charge;shift=-sg*charge;ee[e]+=shift
     T[ix[tuple(qq),tuple(ee)],col]-=math.sqrt(1-(E[e]**2+shift*E[e])/C)
 N=np.diag([sum(c!=0 for c in q) for q,E in states])
 W=np.diag([sum(q[a]==0 for a in [0,2]) for q,E in states])
 w=np.diag(W);p=np.where(w==0)[0];q1=np.where(w==1)[0];q2=np.where(w==2)[0]
 assert np.max(abs(T-T.T))<1e-14 and np.max(abs(N@T-T@N))<1e-14
 for js in [rs,cs]:
  for j in js:
   assert np.max(abs(W@j-j@W+j))<1e-14 and np.max(abs(N@j-j@N-2*j))<1e-14
   assert np.max(abs(j[:,p]))<1e-14
 g=np.zeros(D);g[ix[(bg,(0,0,0,0))]]=1/math.sqrt(2)
 g[ix[(bg,(1,1,1,1))]]=1/math.sqrt(2)
 return dict(label=f'ring_S{S}',states=states,T=T,N=N,W=W,p=p,q1=q1,q2=q2,resolved=rs,coherent=cs,g=g,spin=S)

def target(m,eps,kind):
 T=m['T'];p=m['p'];q=m['q1'];q2=m['q2'];A=T[np.ix_(q,p)]
 M=A.T@A;Z=T[np.ix_(q2,q)]@A
 H2=-M;H4=M@M-.5*Z.T@Z
 js=[-math.sqrt(kappa)*j[np.ix_(p,q)]@A for j in m[kind]]
 return delta*H2/eps**2+delta*H4,js,H2,H4

models=[tree_model(4),tree_model(None),ring(1),ring(2)]
coeffs=[];dynamics=[]
for m in models:
 p=m['p'];w=np.diag(m['W']);D=len(w)
 _,_,H2,H4=target(m,1,'coherent')
 rr=[]
 for eps in [.04,.02,.01]:
  h=m['W']+eps*m['T'];ev,V=eigh(h,driver="evd")
  S=np.zeros((D,D));cluster_errors=[]
  for grade in sorted(set(w)):
   indices=np.where(w==grade)[0];selected=np.where(abs(ev-grade)<.4)[0]
   assert len(indices)==len(selected),(m['label'],eps,grade)
   Pj=V[:,selected]@V[:,selected].T
   S[:,indices]=Pj[:,indices]
  se,sv=eigh(S.T@S,driver="evd");assert min(se)>.5
  U=S@(sv@np.diag(se**(-.5))@sv.T)
  ht=U.T@h@U
  assert np.max(abs(U.T@U-np.eye(D)))<2e-13
  assert max(abs(ht[i,j]) for i in range(D) for j in range(D) if w[i]!=w[j])<2e-13
  coeff=(ht[np.ix_(p,p)]-eps**2*H2)/eps**4
  error=float(np.linalg.norm(coeff-H4,2))
  rr.append({'epsilon':eps,'fourth_coefficient_operator_error':error,'error_divided_by_epsilon_squared':error/eps**2})
 # Error ratios corroborate a fixed coefficient rather than a sign or factor miss.
 assert rr[-1]['fourth_coefficient_operator_error']<rr[0]['fourth_coefficient_operator_error']/10
 coeffs.append({'model':m['label'],'dimension':D,'P_dimension':len(p),
  'two_hole_dimension':len(m['q2']),'H2':H2.tolist(),'H4':H4.tolist(),'canonical_polar_controls':rr})
 for eps in [.2,.1,.075]:
  for kind in ['coherent','resolved']:
   Hp,js,_,_=target(m,eps,kind)
   L=superop(delta*m['W']/eps**4+delta*m['T']/eps**3,
             [math.sqrt(kappa)*j/eps for j in m[kind]])
   E=superop(Hp,js)
   rho0=np.outer(m['g'],m['g']);small=rho0[np.ix_(p,p)]
   real=expm_multiply(L,rho0.reshape(-1,order='F'),start=0,stop=.1,num=3,traceA=L.diagonal().sum())
   eff=expm_multiply(E,small.reshape(-1,order='F'),start=0,stop=.1,num=3,traceA=E.diagonal().sum())
   for tau,a,b in zip([0,.05,.1],real,eff):
    rho=a.reshape((D,D),order='F');sig=np.zeros((D,D),complex);sig[np.ix_(p,p)]=b.reshape((len(p),len(p)),order='F')
    assert abs(np.trace(rho)-1)<1e-9 and abs(np.trace(sig)-1)<1e-9
    assert np.max(abs(rho-rho.conj().T))<1e-9 and np.max(abs(sig-sig.conj().T))<1e-9
    assert min(eigvalsh((rho+rho.conj().T)/2))>-1e-9
    diff=rho-sig;err=float(sum(abs(eigvalsh((diff+diff.conj().T)/2))))
    ns=np.diag(m['N']);n0=int(np.dot(m['g'],m['N']@m['g'])+.5)
    counts={}
    for number in sorted(set(ns)):
     sub=np.ix_(ns==number,ns==number)
     counts[str((int(number)-n0)//2)]={'microscopic':float(np.trace(rho[sub]).real),'target':float(np.trace(sig[sub]).real)}
    dynamics.append({'model':m['label'],'epsilon':eps,'instrument':kind,'time':tau,
                     'trace_norm_error':err,'error_divided_by_epsilon':err/eps,'counts':counts})
# Nontrivial first-event field controls on two genuine cyclic Gauss sectors.
first=[]
for m in models[2:]:
 p=m['p'];ns=np.diag(m['N']);vac=[i for i,k in enumerate(p) if ns[k]==2]
 h,j,H2,H4=target(m,1,'coherent');fields=[m['states'][p[i]][1][0] for i in vac]
 C=m['spin']*(m['spin']+1)
 want=np.diag([-4+4*f*f/C for f in fields])
 assert np.max(abs(H2[np.ix_(vac,vac)]-want))<1e-13
 loss=sum(x.T@x for x in j)[np.ix_(vac,vac)]
 assert np.max(abs(loss-np.diag(np.diag(loss))))<1e-13
 assert abs(loss[fields.index(0),fields.index(0)]-8*kappa)<1e-13
 assert np.max(abs(H4[np.ix_(vac,vac)]-np.diag(np.diag(H4[np.ix_(vac,vac)]))))>0
 first.append({'model':m['label'],'loop_fields':fields,'initial_sector_H2':H2[np.ix_(vac,vac)].tolist(),
  'initial_sector_H4':H4[np.ix_(vac,vac)].tolist(),'initial_sector_birth_loss':loss.tolist(),
  'unit_rotor_total_first_rate':8*kappa,'nonzero_fourth_order_loop_terms':True})
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'tree_builder_sha256':hashlib.sha256((HERE/'repeated_formation_check.py').read_bytes()).hexdigest(),
 'coefficients':coeffs,'full_density_comparisons':dynamics,'first_event_loop_controls':first,
 'scope':'Author controls for canonical H2/H4 and finite positive formation, with actual cyclic Gauss sectors. Numeric rates corroborate, rather than prove, the separate residual/finite-volume argument.'}
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'models':[m['label'] for m in models],'full_density_rows':len(dynamics),
 'largest_error_divided_by_epsilon':max(r['error_divided_by_epsilon'] for r in dynamics),
 'source_sha256':out['source_sha256'],'result_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},indent=2))
