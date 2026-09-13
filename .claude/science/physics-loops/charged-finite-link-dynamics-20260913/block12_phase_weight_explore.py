from pathlib import Path
import json,numpy as np
from scipy.linalg import expm
P=Path(__file__).resolve().parent
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)];I=np.eye(2)
def hops(b=.4,zeta=.7,mu=.2):
 S=[np.kron(I,s) for s in sig]
 onsite=(2+zeta)*S[2]+mu*np.kron(sig[0],np.sin(b)*sig[0]+np.cos(b)*sig[2])
 C=[-np.sin(b)*S[0]-np.cos(b)*S[2],-S[2],-S[2]]
 A=[np.kron(sig[2],np.cos(b)*sig[0]-np.sin(b)*sig[2]),S[1],np.zeros((4,4))]
 return onsite,[(c-1j*a)/2 for c,a in zip(C,A)]
on,hop=hops();edges=[(0,1,0),(0,2,1),(1,3,1),(2,3,0)]
def h(phases):
 H=np.kron(np.eye(4),on)
 for phase,(a,b,i) in zip(phases,edges):
  val=hop[i]*np.exp(1j*phase);H[4*a:4*a+4,4*b:4*b+4]+=val;H[4*b:4*b+4,4*a:4*a+4]+=val.conj().T
 return H
rng=np.random.default_rng(2026091312);rows=[]
for nsteps in [1,2,3,4,6]:
 for trial in range(6):
  phases=rng.uniform(-np.pi,np.pi,(nsteps,4));M=np.eye(16,dtype=complex);Mtr=M.copy()
  for pp in phases:M=expm(-.4*h(pp))@M;Mtr=expm(-.4*h(-pp))@Mtr
  sign,logabs=np.linalg.slogdet(np.eye(16)+M);sgn2,la2=np.linalg.slogdet(np.eye(16)+Mtr)
  rows.append(dict(nsteps=nsteps,trial=trial,phase=float(np.angle(sign)),logabs=float(logabs),time_reversed_conjugation=float(abs(sign.conjugate()-sgn2)),phases=phases.tolist()))
heat=[]
for S in [1,2,3,5]:
 N=2*S+1;m=np.arange(-S,S+1);tau=.02
 values=[float(np.sum(np.exp(-tau*m*m/2)*np.cos(2*np.pi*d*m/N))/N) for d in range(N)]
 heat.append(dict(S=S,step=tau,discrete_phase_kernel=values))
result=dict(fermion_determinants=rows,finite_electric_heat_kernels=heat)
(P/'BLOCK12_PHASE_WEIGHT_EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(max_phase_by_steps={n:max(abs(r['phase']) for r in rows if r['nsteps']==n) for n in [1,2,3,4,6]},max_TR_error=max(r['time_reversed_conjugation'] for r in rows),heat=heat),indent=2))
